---
layout: page
title: 'Intro to Git'
visible: true
---

# (Brief) Introduction to Git + GitHub #

 - **Authors**: Luke Johnston
 - **Research field**: Nutritional and diabetes epidemiology
 - **Lesson topic**: Version control (Git)
 - **Lesson content URL**: <https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/git>

## Preface: ##

Version control is a system that manages changes to a file or files.
These changes are kept as logs in a history, with detailed information
on what file(s) was changed, what was changed within the file, who
changed it, and a message on why the change was made.  This is
extremely useful, especially when working in teams or for yourself 6
months in the future (because you *will* forget things)!

To understand how incredibly powerful version control is, think about
these questions: How many files of different versions of a manuscript
or thesis do you have laying around after getting feedback from your
supervisor or co-authors? Have you ever wanted to experiment with your
code or your manuscript and need to make a new file so that the
original is not touched? Have you ever deleted something and wish you
hadn't? Have you ever forgotten what you were doing on a project?  All
these problems are fixed by using version control (git)!

We are going to go over a typical workflow.  This could be either a
solo workflow or a collaborative workflow.

## Checklist: ##

* Configure your git
* Create a folder and create a git repository (`git init`; the saved
  history of the folder and files) in that folder
* Create a file and track it with git (`git add`), saving it to the
  history (`git commit`)
* Write a short bio in the file
* Check what's going on in the folder (`git status`)
* Compare the file with the one in the history (`git diff`)
* Add the tracked file to the 'staging' area (`git add`; this is an
  area *before* going into the history)
* Save the file in the history (`git commit`)
* Look into your history (`git log`)

(If we have time):

* Create a GitHub account and create a repository
* Set the URL of the new GitHub repository to your repository on your
  computer (`git remote`; the command is usually provided from GitHub)
* Upload your repository on your computer (called local repository)
  up to your GitHub repository (called the remote repository; use `git
  push`)
* Download from the remote to the local repository (`git pull`)

**Tips**:

* Make use of TAB-completion in the terminal!
* Up arrow on the terminal goes to the previous command you entered.

## Lesson topics and commands ##

For configuring your git, follow the "Initial setup" I've put
together:

* http://codeasmanuscript.org/lessons/git/cheatsheet/

Create a folder and create a git repository (which is the stored
history) in that folder. (Note: `##` is a comment, not a command).

    cd ~/Desktop ## Move to your desktop
    mkdir playing ## Create a folder (aka directory)
    cd playing
    git init ## Create the repository (init = initialize)

Now, create a file, get git to track it, and save it to the history.

    touch bio.txt ## Command to create a file called bio.txt
    ls ## Check that you created the file, ls = list files
    git add bio.txt ## Track the file
    ## Save the file to the history with a message (-m)
    git commit -m "Initial commit"

Now, open the `bio.txt` file and add:

* Your name
* Your program and year
* Your progamming language/statistical language of choice

Then:

    git status ## Check the activity
    git diff bio.txt ## Compare to the one in the history
    git add bio.txt ## This sends it to the staging area
    git commit -m "Added my bio" ## This sends it to the history

For a description on what the different stages are (working directory,
staging area, and committed history) see the below links:

* Description: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
* Image: https://git-scm.com/book/en/v2/book/01-introduction/images/areas.png

Then, to see what has happened in your history:

    git log ## View the log of your history

*If we have time*, we'll create a GitHub account, create a GitHub
repository (a remote repository), and upload the repository on your
computer (called the local repository) onto the remote repository
(GitHub):

    git remote add origin https://github.com/yourusername/playing.git
    git push origin master
    git pull

Now you know about a typical workflow!  There are **lots** of commands
and options in git, you really can do almost anything.  *However*,
these are the basic tools that are used most frequently.  If you have
any questions, please check out
[StackOverflow](http://stackoverflow.com/questions/tagged/git) for
*literally* any question on or about Git!!  Or just google it! Google
usually shows answers from StackOverflow.

# Resources: #

## Glossary: ##

* `cd` - change directory
* directory - the same thing as a folder
* `ls` - list the files and folders in a folder
* `touch` - create an empty file
* repository - the saved history of a folder and files, used by git.
* `init` - start or initialize a git repository
* `add` - put a file into the staging area, so that git starts
  tracking it
* staging/index area - where files are stored before going into the
  history
* `commit` - send files in the staging/index area into the history
  (the git repository)
* `status` - check the status of the folder and the git repository
* `diff` - compare a file to the a file in the history
* `log` - view the commit history in the git repository

## Links: ##

Here are a few great resources (excluding StackOverflow) to use if you
ever need help:

* [Hands-on tutorial, with web-based terminal](https://try.github.io/levels/1/challenges/1)
* [Official git documentation](https://git-scm.com/doc)
* [Simpler first-steps guide](http://rogerdudler.github.io/git-guide/)
* [Reference pages for all git commands](http://gitref.org/)
* [Interactive, visual tutorial on branching](http://pcottle.github.io/learnGitBranching/)

