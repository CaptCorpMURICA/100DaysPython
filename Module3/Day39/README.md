# Day 39: Web Scraping
**Instructions:** 
1. Open a new python file.
2. The `requests` [package](https://2.python-requests.org//en/latest/) is used to open a webpage within python for later manipulations. These manipulations will be completed with the `bs4` [package](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Beautiful Soup 4 is used to read and parse the HTML code in order to scrape valuable information from the website.
    ```
    import requests
    from bs4 import BeautifulSoup
    import smtplib
    import os
    import time
    ```
3. Supply the URL of the Amazon item you wish to track. You might want to channel your inner Duke Silver, but aren't willing to pay full price; this app will help you with that.
    ```
    url = 'https://www.amazon.com/dp/B00OET2J7K'
    ```
4. In your browser, search for `What's my user agent`. This will provide the user agent string required for the `requests` package. Add this to a dictionary with `User-Agent` as the key and the user agent as the value. The user agent is valuable at bypassing "Robot Checks" since it helps python to simulate the actual browser.
    ```
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    ```
5. The `requests` package can now be used to retrieve the page of the Amazon item using the two variables above.
    ```
    r = requests.get(url, headers=headers)
    ```
6. The package `bs4` (BeautifulSoup4) is used to analyze and retrieve data from a website. As expected, the `lxml` option parses the XML code, which can then be used to identify specific elements for retrieval.
    ```
    soup = BeautifulSoup(r.content, 'lxml')
    ```
7. Beautiful Soup 4 contains simple methods of navigating the data structure. The title can easily be returned with the `soup.title.string` variable.
    ```
    title = soup.title.string
    ```
8. In order to quickly identify price in the HTML structure, right click on the price and select "Inspect Element." This will open the Developer Tools in the browser where the full HTML tag can be observed. From the string, the `id` of "priceblock_ourprice" can be used to immediately identify the price of the item. The `get_text()` method pulls just the text (i.e. the price) and ignores the HTML tags. Additionally, the price is converted into a float by removing the `$` sign and using the `float()` function.
    ```
    price = float(soup.find(id='priceblock_ourprice').get_text()[1:])
    ```
9. If the price is equal to or falls below the desired value, the `send_mail()` function is called and the `title`, `price`, and `url` are passed to the function for formatting the email. After the email is sent, the program receives an `exit(0)` command to quit the program with an exit code of 0.
    ```
    if price <= 175:
        send_mail(title, price, url)
        exit(0)
    ```
10. A simple function is used to generate the email connection and format the contents with pertinent information from the scraping actions.
    ```
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
    ```
11. An infinite loop is created to check the price once a day (86,400 seconds in a day). If an email is sent, the program exits due to the exit code passed in the `check_price()` function. This program can be added to the system boot sequence so it executes anytime the computer is turned on.
    ```
    if __name__ == '__main__':
        while True:
            check_price()
            time.sleep(86400)
    ```
12. Update the [log file](../../log.md) with what you have learned today.
