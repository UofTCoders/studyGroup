# Setup and Usage ---------------------------------------------------------
#
# Will need to get a GitHub PAT to use some of these commands.
# See [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/). Once you have the GitHub PAT, you will need to save this PAT in your
# home directory ("~/") in a file called ".Renviron". Inside the file, type out:
#
#   GITHUB_PAT= # paste the PAT number after the equal sign
#
# NOTE: Keep this PAT **ONLY ON YOUR COMPUTER**. Don't save it to GitHub.
#
# This script can be used in a few ways. Either:
# 1.    Open the main.Rproj, open the scripts/announcements.R, and "Source" the file
#       using the button or the shortcut Ctrl-Shift-S.
# 2.    Open R console and run the command "source('announcements.R')" when in the
#       script folder.
# 3.    Open the main.Rproj, run "source('scripts/announcements.R')" in the console.

# Installation and Loading Packages ---------------------------------------
# Running these lines will install the necessary packages.

if (!require(devtools)) install.packages("devtools")
devtools::install_dev_deps()
library(stringr)
library(dplyr)
library(purrr)
library(lubridate)
library(glue)
library(assertr)
library(yaml)
library(readr)

# Importing and Filtering the Event Data ----------------------------------

session_details <-
    yaml.load_file(here::here("_data", "events.yml")) %>%
    map_dfr(as_tibble) %>%
    arrange(date) %>%
    # drop sessions that are not set (NA in date)
    filter(!is.na(date)) %>%
    mutate_at(vars(start_time, end_time), funs(
        as.POSIXct(., format = "%H:%M", tz = "GMT") %>%
            strftime(format = "%H:%M", tz = "GMT"))) %>%
    mutate(
        location_url = na_if(location_url, ""),
        location_string = case_when(
            # if both location and url are included!is.na(location) &
            !is.na(location_url) ~ glue("[{location}]({location_url})"),
            # if only location is included!is.na(location) &
            is.na(location_url) ~ location,
            # if neither location nor url are included
            TRUE ~ "TBD"
        ))

coffee_code_details <-
    yaml.load_file(here::here("_data", "coffee-code.yml")) %>%
    map_dfr(as_tibble) %>%
    arrange(date) %>%
    # drop sessions that are not set (NA in date)
    filter(!is.na(date)) %>%
    mutate_at(vars(start_time, end_time), funs(
        as.POSIXct(., format = "%H:%M", tz = "GMT") %>%
            strftime(format = "%H:%M", tz = "GMT"))) %>%
    mutate(
        location_url = na_if(location_url, ""),
        location_string = case_when(
            # if both location and url are included!is.na(location) &
            !is.na(location_url) ~ glue::glue("[{location}]({location_url})"),
            # if only location is included!is.na(location) &
            is.na(location_url) ~ location,
            # if neither location nor url are included
            TRUE ~ "TBD"
        ),
        title = "Coffee and Code",
        description = "A casual co-working session - bring your laptop and whatever you're working on!",
        key = "coffee-and-code")

# Find any existing posts, take the date, and filter out those sessions from the
# session_details dataframe.
keep_only_new <- function(events) {
    existing_post_dates <- fs::dir_ls(here::here("_posts"), regexp = ".md$|.markdown$") %>%
        str_extract("[0-9]{4}-[0-9]{2}-[0-9]{2}")

    events %>%
        filter(!as.character(date) %in% existing_post_dates)
}

new_sessions <- keep_only_new(session_details)
new_coffee_code <- keep_only_new(coffee_code_details)

# Create a GitHub Issue of the session ------------------------------------

# Format as eg August 23
day_month <- function(date_var, add_name = TRUE) {
    date_format <- "%B %e" # as August 23
    if (add_name) date_format <- "%A, %B %e" # as Monday, August 23
    trimws(format(as.Date(date_var), format = date_format))
}


post_gh_issue <- function(title, body, labels) {
    # Will need to set up a GitHub PAT via (I think) the function
    # usethis::browse_github_pat() in the console
    cat("\n\nPosting `", title, "`\n\n")
    if (ui_yeah("Are you sure you want to post this event as an Issue?")) {
        gh::gh(
            "POST /repos/:owner/:repo/issues",
            owner = "uoftcoders",
            repo = "Events",
            title = title,
            body = body,

            labels = array(c(labels))
        )
        usethis::ui_done("Event posted as an Issue to UofTCoders/Events.")
        return(invisible())
    } else {
        message("Event not posted to Issue.")
    }
}

gh_issue_info_event <- function(events) {
    content <- events %>%
        mutate(needs_packages = ifelse(
            !is.na(packages),
            str_c(
                "Please also install these packages: ",
                str_replace_all(packages, " ", ", "), "."
            ),
            ""
        )) %>%
        glue_data(
            "
            {description}

            - **Where**: {location_string}
            - **When**: {day_month(date)}, from {start_time}-{end_time} pm
            - **Instructor**: TBA
            - **Skill level**: {skill_level}

            *Installation instructions*: You will need to install the appropriate programs. See the {program_language} section of the [installation instructions page](https://github.com/UofTCoders/studyGroup/blob/gh-pages/lessons/install-git-python-r.md). {needs_packages}

            *Watch*: This event will be [streamed live]({youtube_link}). If you have questions during the live stream (or just want to chat with us), please ask in our [Gitter lobby](https://gitter.im/UofTCoders/Lobby) and we will forward your questions to the instructor! (Although we aim to live stream each event, there are sometimes technical difficulties so it's best to attend in person if you can.)

            **Directions:**  MADLab is located in [Gerstein Science Information Centre](https://goo.gl/maps/2916Y54jQkx), Room B112 at the south end of the first lower level. Once you go through the main entrance of Gerstein, take a right turn down a corridor (across from the admin desk or just past the reading room), then take the stairs down and follow the signs to MADLab, the door should be open 10-15 minutes before the lesson.
            "
        )

    events %>%
        mutate(content = content, title = str_c(title, " - ", day_month(date, add_name = FALSE))) %>%
        select(title, content, skill_level, gh_labels)
}

gh_issue_info_coffee_code <- function(events) {
    content <- events %>%
        glue_data(
            "
            Our bi-weekly 'Coffee and Code' meet-up:

            Show up anytime between the allotted hours for as long or short as you'd like (see below for details about when and where Coffee and Code will take place). You can even show up earlier or stay later if you're in a coding groove! Look for the UofT Coders posters to find where we're sitting.

            Bring something to work on whether it be data analysis, a Kaggle competition, making figures, setting up software or anything else you'd like to work on.

            Ask for help and discuss. This is friendly, welcoming environment for coders of all levels from absolute beginner to advanced, and of course we know coding is great, but it can be a lot more fun when you're not alone.

            - **Where**: {location_string}
            - **When**: {day_month(date)}, from {start_time}-{end_time}
            - **What to bring**: A laptop with something to work on
            "
        )

    events %>%
        mutate(content = content, title = str_c(title, " - ", day_month(date, add_name = FALSE))) %>%
        select(title, content, gh_labels)
}

create_gh_issues_coffee_code <- function(events) {
    events %>%
        gh_issue_info_coffee_code() %>%
        pmap( ~ post_gh_issue(..1, ..2, ..3))
}

create_gh_issues_events <- function(events) {
    events %>%
        gh_issue_info_event() %>%
        pmap( ~ post_gh_issue(..1, ..2, c(..3, ..4)))
}

create_gh_issues_coffee_code(new_coffee_code)
create_gh_issues_events(new_sessions)

# Create files in _posts/ -------------------------------------------------
# Adds the new sessions/events to the _posts folder.

create_new_posts_with_content <- function(events) {
    new_post_filenames <-
        glue_data(events, "{here::here('_posts')}/{date}-{key}.md")

    # Get the GitHub Issue URL for the event.
    gh_issue_number <- gh::gh("GET /repos/:owner/:repo/issues",
                              owner = "uoftcoders",
                              repo = "Events") %>%
        map_dfr(~ tibble(by_title = .x$title, url = .x$html_url))

    new_post_content <- events %>%
        mutate(by_title = str_c(title, " - ", day_month(date, add_name = FALSE))) %>%
        left_join(gh_issue_number, by = "by_title") %>%
        glue_data(
            '
            ---
            title: "{title}"
            text: "{description}"
            location: "{location}"
            link: "{location_url}"
            date: "{as.Date(date)}"
            startTime: "{start_time}"
            endTime: "{end_time}"
            ---
            '
        )

    # Save post content to file
    fs::dir_create(here::here("_posts"))
    map2(new_post_content, new_post_filenames, ~ readr::write_lines(x = .x, path = .y))
    usethis::ui_done("Markdown posts created in _posts/ folder.")
    return(invisible())
}

new_sessions <- new_sessions %>%
    add_row(
        key = 'co-working',
        title = 'Weekly co-working',
        description = 'An informal co-working session - come hang out with us while
        working on code or whatever else you want to get done.',
        date = 'Every Thursday from Jan 14 to Mar 18',
        start_time = '13:00',
        end_time = '14:00',
        location = 'Zoom',
        location_url = 'https://github.com/UofTCoders/Events/issues/302',
        packages = '',
        youtube_link = '',
        skill_level = '',
        program_language = 'Any',
        gh_labels = 'co-working',
        location_string = 'Zoom')

create_new_posts_with_content(new_sessions)
create_new_posts_with_content(new_coffee_code)
