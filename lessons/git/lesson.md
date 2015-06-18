# (Brief) Introduction to Git + GitHub

 - **Authors**: Luke Johnston
 - **Research field**: Nutritional and diabetes epidemiology
 - **Lesson Topic**: Version control (Git)

## Preface: ##

* Make use of TAB-completion!
* Up arrow on the terminal goes to the previous command used.

We are going to go over a typical GitHub/collaborative workflow.  This
workflow doesn't have to be collaborative, it could also be a solo
workflow too!  Minus the Pull Requests, though.

## Checklist: ##

* Config your git
* Fork the Study Group (via @UofTCoders)
* Clone your fork down into your computer
* Check the log and status
* Create a new file (your bio)
* Add that file to the 'staging' area
* Commit the file in the 'staging' area into the history
* Push your changes up
* Submit a Pull Request (have it rejected/asked for clarification)
* Revise the file and check the differences
* Add + commit to the history
* Push, have pull request accepted
* Update your cloned and forked repo from the upstream (original)

## Lesson topics and commands ##

For configuring your git, follow the "Initial setup" I've put
together:

* http://codeasmanuscript.github.io/workshops/lessons/git/cheatsheet/

Then, fork @UofTCoders's repository into your own GitHub
account. Afterwards do these commands:

    cd ~/Desktop
    git clone https://github.com/your-account-name/studyGroup.git
    cd studyGroup
    ls
    git log
    git status
    cd lessons/git/bios
    touch your-name-bio.txt

Open the bio.txt file and add:

* Your name
* Your program and year
* Your progamming language/statistical language of choice

Then:

    git add your-name-bio.txt
    git commit -m "Added my bio"
    git push

Submit a "Pull request".  Pretend like I asked you to also include
types of analyses you do.  Revise your file to include:

* Main/predominate types of analyses you do

Then:

    ## <- this is a comment
    git status  ## See that the file has been modified
    git diff your-name-bio.txt ## View the differences
    git commit -am "Edited bio to include types of analyses"
    git log ## See your commits
    git push

The Pull Request should already be updated after pushing.  I'll accept
some of the Pull Requests, then you need to update your local and
forked versions to match the master version:

    git remote add upstream https://github.com/UofTCoders/studyGroup.git
    git pull upstream gh-pages
    git push

Now you know about a typical workflow!  There are **lots** of commands
and options in git, you really can do almost anything.  If you have
any questions, please check out
[StackOverflow](http://stackoverflow.com/questions/tagged/git) for
*literally* any question on or about Git!!

