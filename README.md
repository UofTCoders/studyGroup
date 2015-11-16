Mozilla Study Groups
============

Welcome to [Mozilla Science Lab](https://www.mozillascience.org/)'s Study Group project! From here, we'll set you up with everything you need to start your own study group.

### Wait What's a 'Mozilla Study Group'?

Mozilla Study Groups are fun, informal meetups of your friends and colleagues from around your local institution or town to share skills, stories and ideas on using code for research. The goal is to create a friendly, no-pressure environment where people can share their work, ask for help on a coding problem, and learn and work together with their peers.

## For Participants

Welcome to our Mozilla Study Group! A few things to do & know now that you're here:

 - **Watch the [Events](https://github.com/UofTCoders/Events) repo and/or this repo:** up in the top right, there's a button that says 'Watch'; click it, and set yourself to 'Watching'. This will send you email notifications of new discussions. If you only want to be notified about events (and not any other discussion topics), watch just the [Events](https://github.com/UofTCoders/Events) repo. If you want to stay updated on all group doings, watch this repo AND the Events repo. If you don't want email, but would like an alert just on GitHub, change the setting in Settings -> Notification Center (Settings is the little cog in the top right).
 - **Check out the issue tracker:** click on 'issues' in the sidebar on the right; this is where all the conversations this study groups is having live. Use this space to ask questions, request events, make suggestions, or just say hi.
 - **Read the code of conduct:** this Study Group is for everyone - we abide by a [set of rules](https://www.mozillascience.org/code-of-conduct/) that require everyone be treated with respect. Help us make a space where everyone feels welcome, and we'll all have a better time!
 - **Add yourself to the website:** If you'd like to appear on the website under the 'Who we Are' section, have a look at the `_data/members.yml`; send us a pull request with an entry for yourself, or open an issue and we'll do it for you.

## For Organizers

### It's Broken, I Need Help

If anything in these instructions doesn't work or doesn't make sense, open an issue [here](https://github.com/mozillascience/studyGroup/issues) or email sciencelab@mozillafoundation.org.

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

### Optional: Setting up a Google Calendar for your Study Group

If you'd like to offer your community a calendar of events they can import into their own calendars, try using a Google Calendar. To set up, make a new google account, and update the variables in `_config.yml` under the heading 'Setup Google Calendar'.

You can add events to your calendar by hand, but if you'd like to manage it automatically, there's a script to do so in `scripts/updateCalendar.py`; instructions for use are at the top of that file.

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
    startTime: '15:00'
    endTime: '16:00'
    ---
    ```

    Change all the fields to describe your event; make sure the `link` is the address of the issue you created When you're done, click 'Commit Changes' at the bottom.

That's it! Your event is now listed on your webpage, and there's a discussion thread where people can ask questions and discuss the details. Events will be automatically removed from the schedule on the webpage when they're more than a week in the past - but the issue you created will always be there as a record of what you've done.

> **Event Listing Gotchas:** here are a few things to look out for when listing an event:
>  - Did you remember to include the `---` above and below? The website builder needs those.
>  - Can't find the issue tracker? Remember to turn it on under the 'Settings' menu on the right.
>  - The seven fields need to be on exactly one line each; some text editors will insert line breaks into lines that are too long; remove these if so.

## How to Stay in Touch With Your Members

Now that you're all set up, GitHub provides several ways to stay in touch with the people involved in your Study Group.

  - **Ask users to Watch your repo.** Make sure all your users click 'Watch' at the top of your repository. This way, they'll be automatically notified of all the events you post in your issue tracker. 
  - **Use the Issue Tracker.** The Issue Tracker is your public message board to make announcements, ask questions and start conversations with your members. You can find yours at `https://github.com/yourUserName/studyGroup/issues`.
  - **Use the Mozilla Science Forum** to chat with study groups worldwide. Find the [forum here](https://forum.mozillascience.org/category/events/study-groups); use this to share your stories, ask questions to the wider community, and find out who's out there.

## Feature Your Community in the 'Who We Are' Section

Your website includes a gallery of participants in your Study Group; adding people here is a great way to show off your community and highlight your new friends and colleagues. To add someone to the list, edit the `_data/members.yml` file by adding the following section for them:

```
- name: their human name
  degree: school, lab, department, business....
  github: their GitHub handle
  interests:
    - list one to three
    - different interests
```
