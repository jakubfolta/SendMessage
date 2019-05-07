from selenium import webdriver
#! python3

"""email.py - A program that takes an email address and string of text on the command line and then,
using Selenium, logs into your email account and sends an email of the string to the provided address."""

# Import essential modules.
# import sys
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
# html_element = browser.find_element_by_tag_name('html')
# html_element.send_keys(Keys.END)
# html_element.send_keys(Keys.HOME)


# Set basic url to open and config login.
logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')
#logging.disable(logging.CRITICAL)
url = 'http://mail.yahoo.com'

logging.info('Opening .... ' + os.path.basename(url))

# Set variables with login, password and message to send using sys module.
# if len(sys.argv) < 2:
#     print('Please pass your login, password and a message to send.')
# elif len(sys.argv) < 4:
#     print('You forgot to pass your message.')

# TODO: Open url, enter login and password using selenium module.
# browser = webdriver.Firefox()
# browser.get('http://mail.yahoo.com')

# login = sys.argv[1]
# password = sys.argv[2]
# message = ' '.join(sys.argv[3:])

# TODO: Send message using selenium.
