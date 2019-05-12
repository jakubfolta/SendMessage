#! python3

"""email.py - A program that takes an email address and string of text on the command line and then,
using Selenium, logs into your email account and sends an email of the string to the provided address.
"""

#Import essential modules.
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')
logging.info('Opening .... ' + os.path.basename(url))
#logging.disable(logging.CRITICAL)


# Set basic url to open.
url = 'http://mail.yahoo.com'

# Check if proper amount of arguments were passed in command line.
if len(sys.argv) < 2:
    print('Please pass your login, password, receiver\'s email and a message to send.')
elif len(sys.argv) < 4:
    print('You forgot to pass your message.')

# Set variables with login email, password, email of receiver and a message to send using sys module.
login = sys.argv[1]
password = sys.argv[2]
receiver_email = sys.argv[3]
message = ' '.join(sys.argv[4:])

# TODO: Open url, enter login and password using selenium module.
browser = webdriver.Firefox()
browser.get(url)


# TODO: Send message using selenium.
