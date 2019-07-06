"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day38_api.py
    Creation Date:  7/3/2019, 11:01 AM
    Description:    Python Automation Program 9: API Integration
"""

from twitter import Twitter, OAuth

credentials = dict()
with open("credentials.txt", "r") as cred:
    for line in cred:
        var, val = line.split(": ")
        credentials[var] = val.rstrip("\n")
        var = ""
        val = ""
        line = ""

access_token = credentials["access_token"]
access_secret = credentials["access_secret"]
consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
t = Twitter(auth=oauth)

access_token = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""
credentials.clear()

search_type = input("Choose an option\n1: User Search\n2: Hashtag Search\n")
if search_type == "1":
    user = input("What user do you want to search for?\n").lower()
    q = f"%40{user}"
elif search_type == "2":
    hashtag = input("What hashtag do you want to search for?\n").lower()
    q = f"%23{hashtag}"
else:
    print(f"{search_type} is not a valid entry. Enter either a 1 for user search or a 2 for hastag search.")

query = t.search.tweets(q=q)

for tweet in query["statuses"]:
    hashtags = []
    for hashtag in tweet["entities"]["hashtags"]:
        hashtags.append(hashtag["text"])

    print(f'''
    Tweet ID: {tweet["id"]}
    Created at: {tweet["created_at"]}
    Text: {tweet["text"]}
    
    User ID: {tweet["user"]["id"]}
    User: {tweet["user"]["name"]}
    Screen Name: {tweet["user"]["screen_name"]}
    Location: {tweet["user"]["location"]}
    Time Zone: {tweet["user"]["time_zone"]}
    Followers: {tweet["user"]["followers_count"]}
    Verified: {tweet["user"]["verified"]}
    Number of Tweets: {tweet["user"]["statuses_count"]}
    
    Hashtags: {hashtags}
    
    {"=" * 50}''')
