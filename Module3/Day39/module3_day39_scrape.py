"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day39_scrape.py
    Creation Date:  7/6/2019, 1:12 PM
    Description:    Python Automation Program 11: Web Scraping
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import os
import time


def check_price():
    """
    Utilize `requests` and `bs4` to load and scrape a specific Amazon product page. If the price falls below a specific
    value, then an email is sent with the specifics to prompt a purchase from the user. If an email is sent, the program
    sends an `exit(0)` command to quit from the infinite loop.
    :return: Execute the `send_mail()` function if conditions are met.
    """
    url = 'https://www.amazon.com/dp/B00OET2J7K'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    title = soup.title.string
    price = float(soup.find(id='priceblock_ourprice').get_text()[1:])

    if price <= 175:
        send_mail(title, price, url)
        exit(0)


def send_mail(title, price, url):
    """
    A simple function to connect to the email client and send a notification when the price drops below the provided
    level.
    :param title: The title from the Amazon page.
    :param price: The current price of the product.
    :param url: The URL link to the product page.
    :return: Email is sent with specifics about the product.
    """

    credentials = dict()
    with open("credentials.txt", "r") as cred:
        for line in cred:
            var, val = line.split(": ")
            credentials[var] = val.rstrip("\n")
            var = ""
            val = ""
            line = ""

    smtp_obj = smtplib.SMTP(f'smtp.{credentials["username"].split("@")[1]}', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    smtp_obj.login(credentials["username"], credentials["password"])
    subject = f"PRICE DROP: {title}"
    body = f"The price is now: ${price}\nLink: {url}"
    smtp_obj.sendmail(credentials["username"], credentials["username"],
                     f"Subject: {subject}\nDear {os.getlogin()},\n\n{body}.")
    credentials.clear()
    smtp_obj.quit()


if __name__ == '__main__':
    while True:
        check_price()
        time.sleep(86400)
