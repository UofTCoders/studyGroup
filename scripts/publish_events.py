import hashlib
import json
import os
import pathlib
import re
import sys

import cmarkgfm
import dateparser
import frontmatter
import github


# The milestone used to determine which event issues are to be published.
MILESTONE = 'Publishable'


def main(event_dir: pathlib.Path, failure_path: pathlib.Path) -> None:
    """
    Convert publishable event issues into entries on the website.

    Publishable event issues are those that are in the UofTCoders/Events repo on the
    ``MILESTONE`` milestone. Published events are saved to *event_dir*. Parsing errors
    are saved in *failure_path*.
    """
    try:
        auth = github.Auth.Token(os.environ['GITHUB_TOKEN'])
    except KeyError:
        auth = None
        print('Connecting to GitHub without authentication')
    else:
        print('Connecting to GitHub with $GITHUB_TOKEN')
    gh = github.Github(auth=auth)

    repo = gh.get_repo('UofTCoders/Events')

    milestone = None
    for ms in repo.get_milestones():
        if ms.title == MILESTONE:
            milestone = ms
            break
    else:
        raise ValueError(f'Unable to find the {MILESTONE!r} milestone')
    print(f'Found {MILESTONE!r} milestone {milestone.number}')

    failures = {}
    event_summary = []
    for issue in repo.get_issues(milestone=milestone):
        try:
            event = parse_issue(issue)
        except Exception as e:
            print(f'::error title=Failed to parse event {issue.title}::{e}')
            failures[issue.number] = str(e)
        else:
            event_summary.append(
                f'- {event["title"]} on {event["date"]} at {event["startTime"]}')
            print(f'Parsed event: {issue.title}')
            with (event_dir / post_to_filename(event)).open('w', encoding='utf-8') as f:
                frontmatter.dump(event, f)

    summary = f'Parsed **{len(event_summary)}** issue(s) into event posts:'
    if 'GITHUB_STEP_SUMMARY' in os.environ:
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'w+') as f:
            f.write('# Event publishing\n')
            f.write(f'{summary}\n')
            f.write('\n'.join(event_summary))
    else:
        print(summary)

    with open(failure_path, 'w') as f:
        json.dump(failures, f)


def parse_issue(issue: github.Issue) -> frontmatter.Post:
    """
    Parse an event issue into information required to make a website entry.

    The issue title is used for the entry. If the title ends with something that looks
    like a date in parentheses, then that will be stripped.

    The issue body is parsed for description, date, time, and location. The issue body
    is expected to have the format::

        Some description of the event.

        The description may be multiple lines, but is terminated by the first "metadata"
        tag, which is anything bolded like below (i.e., something that looks like
        ``**key**:``).

        **Where**: Some location.
        **When**: A date and time acceptable to dateparser.
        **Instructor**: Unused.
        **Materials**: Unused.
    """
    body = issue.body
    end_of_description = None
    metadata = {}
    # Search for the boldened text + colon on a line by itself.
    for match in re.finditer(r'^\*\*(.+)\*\*: (.+)$', body, re.MULTILINE):
        if end_of_description is None:
            # Description ends at first match.
            end_of_description = match.start()
        key = match.group(1).lower()
        value = match.group(2).strip()
        metadata[key] = value

    title = issue.title.strip()
    if (ending := re.search(r' *\((.+)\)$', title)) is not None:
        if dateparser.parse(ending.group(1)) is not None:
            # Looks like a date, so strip it.
            title = title[:ending.start()]
    if end_of_description is None:
        raise ValueError(f'Could not find any metadata in {body!r}')
    description = markdownify(body[:end_of_description].strip())
    dt = dateparser.parse(metadata['when'], locales=['en-CA'])
    if dt is None:
        raise ValueError(f'Failed to parse date from {metadata["when"]!r}')
    if dt.hour == dt.minute == 0:
        print(
            f'::warning title={issue.title} may have no start time::'
            f'Trying to parse date and start time from {metadata["when"]!r}')
    location = markdownify(metadata['where'], inline=True)

    return frontmatter.Post(
        content='',
        title=title,
        text=description,
        location=location,
        link=issue.html_url,
        date=dt.date().isoformat(),
        startTime=dt.time().isoformat(timespec='minutes'),
    )


def post_to_filename(post: frontmatter.Post) -> str:
    """Convert a post from date and title to a safe filename."""
    safe_title = hashlib.sha256(post['title'].encode()).hexdigest()[:10]
    return f'{post["date"]}-{safe_title}.md'


def markdownify(content: str, inline: bool = False) -> str:
    markdown = cmarkgfm.github_flavored_markdown_to_html(content).strip()
    if inline:
        if markdown.startswith('<p>') and markdown.endswith('</p>'):
            markdown = markdown[len('<p>'):-len('</p>')]
    return markdown


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(f'usage: {__file__} EVENT_DIR FAILURE_FILE')
    event_dir = pathlib.Path(sys.argv[1])
    if not event_dir.is_dir():
        raise SystemExit(f'{event_dir} is not a directory')

    failure_path = pathlib.Path(sys.argv[2])
    main(event_dir, failure_path)
