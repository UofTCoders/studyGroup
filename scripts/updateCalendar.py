#######################################################################
# date: 2015-07-28
# author: Thea Van Rossum theavanrossum@gmail.com
# functionality:
#    1. Creates a Google Calendar API service object
#    2. Deletes all events in the calendar in case changes have been
#       made to existing events
#    3. Create events based on all the posts in
#       "_posts" (POSTS_DIRECTORY)
#    Commented out: 4. Print next 10 events
#
#    Will not add an event if it is missing one of the REQUIRED_FIELDS
#
# To modify and use:
#   1. See google docs to get setup with credentials:
#      https://developers.google.com/google-apps/calendar/quickstart/python
#   2. Update the variables indicated below (APPLICATION_NAME,
#      CALENDAR_ID, TIME_ZONE_SRT
#   3. run from scripts/ using:
#      python updateCalendar.py --noauth_local_webserver
########################################################################


import httplib2
import os
import glob

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime
import pytz

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# Modify these variables in step 2 above -------------------
# APPLICATION_NAME: app name you created in step one above:
APPLICATION_NAME = 'UofTCoders Calendar'
# CALENDAR_ID: google account name you created for your calendar:
CALENDAR_ID = 'utorontostudygroup@gmail.com'
# TIME_ZONE_STR: check here:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE_STR = 'America/Toronto'
# -----------------------------------------------------------

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
DEFAULT_START_TIME = "15:30"  # will be overridden by startTime in _posts
DEFAULT_END_TIME = "16:30"  # will be overridden by endTime in _posts
REQUIRED_FIELDS = ['title', 'location', 'text', 'link', 'date']
POSTS_DIRECTORY = "../_posts"


def main():
    """
    1. Creates a Google Calendar API service object
    2. Deletes all events in the calendar in case
       changes have been made to existing events
    3. Create events based on all the posts in "_posts" (POSTS_DIRECTORY)
    Commented out: 4. Print next 10 events

    Will not add an event if it is missing one of the REQUIRED_FIELDS
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    # clear the calendar
    service.calendars().clear(calendarId=CALENDAR_ID).execute()

    # create events
    for inputPath in glob.glob(os.path.join(POSTS_DIRECTORY, '*.markdown')):
        eventDict = parseEventPost(inputPath)
        events = getAllEvents(service)
        if not isEventComplete(eventDict, inputPath):
            print 'Event is incomplete'
        else:
            event = createEvent(eventDict)
            event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
            print 'Event created: %s' % (event.get('summary'))


def printNextEvents(service, numEvents):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print 'Getting the upcoming %d events' % numEvents
    eventsResult = service.events().list(
        calendarId=CALENDAR_ID, timeMin=now, maxResults=numEvents, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print start, event['summary']


def getAllEvents(service):
    eventsResult = service.events().list(
        calendarId=CALENDAR_ID, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events


def parseEventPost(inputPath):
    eventDict = {}
    eventDict['startTime'] = DEFAULT_START_TIME
    eventDict['endTime'] = DEFAULT_END_TIME
    f = open(inputPath, 'r')
    for line in f:
        listedline = line.strip().split(':', 1)  # split around the : sign
        if len(listedline) > 1:  # we have the = sign in there
            eventDict[listedline[0].strip()] = listedline[1].strip()
    return eventDict


def isEventComplete(eventDict, sourcePath):
    isComplete = 1
    for field in REQUIRED_FIELDS:
        if field not in eventDict:
            print "Error: event missing %s (%s)" % field, sourcePath
            isComplete -= 1
    return isComplete


def makeDateTime(dateStr, hourMinStr):
    # date like "2014-07-25"
    # hourMinStr like "15:30"
    timeStr = hourMinStr[1:-1]
    date = dateStr.split('-')
    TIME_ZONE_HR = ':00'+pytz.timezone(TIME_ZONE_STR).localize(datetime.datetime(int(date[0]), int(date[1]), int(date[2]))).strftime('%z')
    TIME_ZONE_HR = TIME_ZONE_HR[:-2] + ':' + TIME_ZONE_HR[-2:]
    return dateStr + "T" + timeStr + TIME_ZONE_HR


def createEvent(eventDict):
    event = {
        'summary': eventDict['title'],
        'location':  eventDict['location'],
        'description':  eventDict['text']+"\n"+eventDict['link'],
        'start': {
            'dateTime': makeDateTime(eventDict['date'], eventDict['startTime']),
            'timeZone': TIME_ZONE_STR
            },
        'end': {
            'dateTime':  makeDateTime(eventDict['date'], eventDict['endTime']),
            'timeZone': TIME_ZONE_STR
            },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 60 * 24 * 2},  # 2 days
                ],
            },
        }
    return event


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'google-sfuStudyGroupCalendar.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials


if __name__ == '__main__':
    main()
