# Day 38: API Integration
**Instructions:** 
1. Open a new python file.
2. An Application Programming Interface (API) is a piece of software that allows two applications to talk to each other. In order to interface python with web applications like Twitter, the Twitter API needs to be used.
3. In order to get started, the [Twitter API](https://developer.twitter.com/en/docs) needs to be created. This process creates the four codes required to interface with Twitter through the API: consumer API keys (key and secret key) and access tokens (token and secret token). Once these codes have been generated, add them to the appropriate fields in the `credentials.txt` file.
4. Twitter uses `OAuth` to log into the service and requires the four codes created from the dev site. For simplicity, the same methodology as the email automation will be leveraged. After the codes are used, the variables are cleared to avoid additional risk. 
    ```
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
    ```
5. If a user is the subject of the search query, a `%40` (@) needs to be appended to the text. If a hashtag is the subject of the search query, a `%23` (#) needs to be appended to the text. Then the search term is used to query Twitter. With the free API app tier, only tweets from the past seven days can be returned.
    ```
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
    ```
6. With the query run, the tweets can be returned to the terminal, stored in a text file, or added to a dataset. The results are returned in a JSON format, so items can be extracted in the same manner as a nested dictionary.
    ```
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
    ```
7. Update the [log file](../../log.md) with what you have learned today.
