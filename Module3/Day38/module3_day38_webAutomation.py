"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day38_webAutomation.py
    Creation Date:  7/3/2019, 11:01 AM
    Description:    Python Automation Program 9: Web Automation
"""

from twitter import Twitter, OAuth

ACCESS_TOKEN = 'access_token'
ACCESS_SECRET = 'access_secret'
CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
t = Twitter(auth=oauth)

hashtag = input("What hashtag do you want to search for?\n").lower()

query = t.search.tweets(q=f'%23{hashtag}')

for s in query['statuses']:
    print(s['created_at'], s['text'], '\n')
