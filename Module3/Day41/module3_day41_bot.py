"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day41_bot.py
    Creation Date:  7/6/2019, 8:40 PM
    Description:    Python Automation Program 13: Creating a Chatbot
"""

import slack
import random


def magic_8_ball():
    """
    Selects a random number between 1 and 20 and then returns the text output from the Magic 8 Ball.
    :return: Magic 8 Ball result
    """
    ball = {1: "It is certain.",
            2: "It is decidedly so.",
            3: "Without a doubt.",
            4: "Yes - definitely.",
            5: "You may rely on it.",
            6: "As I see it, yes.",
            7: "Most likely.",
            8: "Outlook good.",
            9: "Yes.",
            10: "Signs point to yes.",
            11: "Reply hazy, try again.",
            12: "Ask again later.",
            13: "Better not tell you now.",
            14: "Cannot predict now.",
            15: "Concentrate and ask again.",
            16: "Don't count on it.",
            17: "My reply is no.",
            18: "My sources say no.",
            19: "Outlook not so good.",
            20: "Very doubtful."}

    choice = random.randint(1, 20)
    return ball[choice]


@slack.RTMClient.run_on(event='message')
def roll_ball(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    rtm_client = payload["rtm_client"]
    try:
        if "roll" in data["text"].lower():
            channel_id = data["channel"]
            thread_ts = data["ts"]
            user = data["user"]

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user}>, the answer to your question is: '{magic_8_ball()}'",
                thread_ts=thread_ts
                )
        elif "shut down bot" in data["text"].lower():
            channel_id = data["channel"]
            thread_ts = data["ts"]
            user = data["user"]

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user}>, I will now go to sleep.",
                thread_ts=thread_ts
            )
            exit(0)
    except KeyError:
        pass


if __name__ == '__main__':
    credentials = dict()
    with open("credentials.txt", "r") as cred:
        for line in cred:
            var, val = line.split(": ")
            credentials[var] = val.rstrip("\n")
            var = ""
            val = ""
            line = ""

    slack_token = credentials["slack_bot_token"]
    credentials.clear()
    rtm_client = slack.RTMClient(token=slack_token)
    slack_token = ""
    rtm_client.start()
