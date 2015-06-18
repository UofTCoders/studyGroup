<<<<<<< HEAD
Mozilla Study Groups
============

Welcome to [Mozilla Science Lab](https://www.mozillascience.org/)'s Study Group project! From here, we'll set you up with everything you need to start your own study group.

### Wait What's a 'Mozilla Study Group'?

Mozilla Study Groups are fun, informal meetups of your friends and colleagues from around your local institution or town to share skills, stories and ideas on using code for research. The goal is to create a friendly, no-pressure environment where people can share their work, ask for help on a coding problem, and learn and work together with their peers.

## For Participants

Welcome to our Mozilla Study Group! A few things to do & know now that you're here:

 - **Watch this repo:** up in the top right, there's a button that says 'Watch'; click it, and set yourself to 'Watching'. This will send you email notifications of new discussions; if you don't want email, but would like an alert just on GitHub, change the setting in Settings -> Notification Center (Settings is the little cog in the top right).
 - **Check out the issue tracker:** click on 'issues' in the sidebar on the right; this is where all the conversations this study groups is having live. Use this space to ask questions, request events, make suggestions, or just say hi.
 - **Read the code of conduct:** this Study Group is for everyone - we abide by a [set of rules](https://www.mozillascience.org/code-of-conduct/) that require everyone be treated with respect. Help us make a space where everyone feels welcome, and we'll all have a better time!

## For Organizers

### It's Broken, I Need Help

If anything in these instructions doesn't work or doesn't make sense, open an issue [here](https://github.com/mozillascience/studyGroup/issues) or email bill@mozillafoundation.org.

### Check out the Handbook

The instructions below will help you set up the online tools for your Mozilla Study Group - but if you're looking for organziation strategies, event plans and lesson ideas, check out the [Mozilla Study Group Handbook](https://mozillascience.github.io/studyGroupHandbook/)!

## How to Set Up Your Own Mozilla Study Group Website

Everything you need to set up your own Mozilla Study Group website for organizing events is right here - follow the following steps and you'll be up and running soon, and if you have trouble, [open an issue](https://github.com/mozillascience/studyGroup/issues) and we'll help you out!

 1. **Make yourself an account on GitHub.** The free one is just fine.
 2. **Fork this repository.** Up in the top right corner of this page, there's a button that says 'Fork'; press it! This makes your very own copy of all this stuff in your space on GitHub; when the copy is done, GitHub will automatically take you there.
 3. **Turn on the Issue Tracker.** An issue tracker is a message board GitHub sets up for every repository; you'll use it to post information about your event and talk to your participants. To turn it on: 
   - click on 'Settings' in the right sidebar of your repo;
   - click the checkbox beside 'Issues'; 
   - head back to your repo by clicking on the big `studyGroup` at the top of the page.
 4. **Edit the `_config.yml` file** in your new repository:
   - click on `_config.yml`;
   - click on the little pencil near the top right;
   - follow the instructions in the file on how to edit it; 
   - when you're done, press the green 'Commit Changes' button at the bottom of the page.

That's it, you're done! You can see your new website at `https://yourUserName.github.io/studyGroup/`, where `yourUserName` is the user name you signed up for GitHub with. If this is your first time making a webpage on GitHub, it might take 30 minutes for things to percolate through their computers - don't worry, it's all good, check back later and your website should be up and running.

## How to Launch a New Event

When you're ready to list a new event for your Study Group, follow these steps, or [watch this video](https://youtu.be/abglQgEIccw) where we walk you through event listing.

 1. **Make a new Issue to describe your event.** 
   - Click on 'Issues' over on the right sidebar of your repo, 
   - click the green 'New Issue' button near the top right. 
   - You'll then see a form where you can give your event a title and a description - fill these out with all the relevant information:
     - Where will your event be? Include a link to a map.
     - When will it be? Date and time.
     - Should people do anything to prepare beforehand (install any dependencies, set something up?)
 2. **Go to the `_posts` directory**. It'll be at `https://github.com/yourUserName/studyGroup/tree/gh-pages/_posts` - or you can click on `_posts` in your repo.
 3. **Make a new file** by clicking on the `+` sign beside `_posts/` Name it like the following:

    ```
    YYYY-MM-DD-word.markdown
    ```

    where `YYYY-MM-DD` is the date of your event, and `word` is anything you want.
 4. **Cut and paste the following into your new file:**
    ```
    ---
    title: Study Group Meetup
    text: a one sentence description of your event
    location: Hacky Hour Stadium
    link: https://github.com/yourUserName/studyGroup/issues/1234
    date: 2016-01-04

    ---
    ```
    Change all the fields to describe your event; make sure the `link` is the address of the issue you created When you're done, click 'Commit Changes' at the bottom.

That's it! Your event is now listed on your webpage, and there's a discussion thread where people can ask questions and discuss the details. Events will be automatically removed from the schedule on the webpage when they're more than a week in the past - but the issue you created will always be there as a record of what you've done.

> **Event Listing Gotchas:** here are a few things to look out for when listing an event:
>  - Did you remember to include the `---` above and below? The website builder needs those.
>  - Can't find the issue tracker? Remember to turn it on under the 'Settings' menu on the right.
>  - Did your text editor insert linebreaks in long lines that aren't supposed to be there? You can tell by looking at the line numbers of the file in your repo; the five fields need to be on exactly one line each.

## How to Stay in Touch With Your Members

Now that you're all set up, GitHub provides several ways to stay in touch with the people involved in your Study Group.

  - **Ask users to Watch your repo.** Make sure all your users click 'Watch' at the top of your repository. This way, they'll be automatically notified of all the events you post in your issue tracker. 
  - **Use the Issue Tracker.** The Issue Tracker is your public message board to make announcements, ask questions and start conversations with your members. You can find yours at `https://github.com/yourUserName/studyGroup/issues`.
  - **Gitter** is a free chat room you can set up and share with your community to go with your website. To set it up, try the following:
   - Visit [their web site](https://gitter.im). You may have to sign in with your GitHub credentials.
   - Click 'create a room' in the bottom left;
   - Choose 'Channel' from the options presented;
   - Make the room name `studyGroup`, and select the 'public' option.
 
  That's it! Share the URL with your participants and you can chat live with them as they join the room.
  - **Use the Mozilla Science Forum** to chat with study groups worldwide. Find the [forum here](https://forum.mozillascience.org/category/events/study-groups); use this to share your stories, ask questions to the wider community, and find out who's out there.
=======
# sandbox
Sandbox for git tutorial

Please see the [lesson plan](./lesson.md)
>>>>>>> ffe36162811d23b844368c4c62e91347e6933a42
