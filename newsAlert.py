# This program scrapes the bbc world news website and extracts the top 5 headlines and their summaries
# It then organizes them and sends them on my phone as text message
import requests, bs4
import time
from twilio.rest import Client

'''
This function is used to scrape the bbc news website and fetch the top 5 world news headlines and their summaries 
'''


def newsCheck():
    url = 'https://www.bbc.com/news/world'  # the bbc url to scrape
    res = requests.get(url)  # use the get method to scrape the website
    res.raise_for_status()  # checking if the scraping was successful
    soup = bs4.BeautifulSoup(res.text, 'html.parser')  # parsing the html content

    link_elem = soup.select('.gs-c-promo-heading')  # getting the element using the heading id

    summary_elem = soup.select('.gs-c-promo-summary')  # getting the element using the summary id

    numOpen = min(6, len(link_elem))  # the minimum value between 5 and the total number of headlines

    for i in range(1, numOpen):  # looping through the headlines to send them as messages
        textmyself(link_elem[i].getText())  # texting the headlines
        time.sleep(1)  # pausing for 1 second

        if 'LIVE' in link_elem[i].getText():  # making sure any 'LIVE' news is not being included
            i = i - 1

        else:
            textmyself(summary_elem[i].getText())  # sending the summary of the headlines as a message
            time.sleep(1)  # pausing for 1 second

'''
This function is used to send messages to the recipient
It takes a string as a parameter that contains the message to be sent
'''


def textmyself(message):
    accountSID = 'AC18f96f58161d0d98e2d8a98771c8567f'  # account id to verify the recipient
    authToken = 'e76d74eb091c56431f368b9202f2bfb1'  # authentication token to verify the recipient
    myNumber = '+14753321424'  # recipients real number
    twilioNumber = '+19705095797'  # recipient's twilio number
    twilioCli = Client(accountSID, authToken)  # accessing the recipient using ID and token
    twilioCli.messages.create(body=message, from=twilioNumber, to=myNumber)  # sending the message to the recipient

newsCheck()
