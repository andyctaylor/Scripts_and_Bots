# This script will check your password to see if it's been hacked using password API
# the point in the request module so we can make requests without using a  browser.
import requests

# Importing the Python hash library
import hashlib

import sys

# Making a request to the API for data
def request_api_data(query_char):

  # Calling the API - url - using the SHA1 hash
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)

  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
  return res

# Look into all the hashes that we receive and checking the hash that is our password.
def get_pass_leaks_count(hashes, hash_to_check):

  # Spliting the hashe and the count And put them into a tuple.
  hashes = (line.split(':') for line in hashes.text.splitlines())

  # loop through the couple stand for hashes and count.
  for h, count in hashes:

    # Check the correc hash
    if h == hash_to_check:
      return count
  return 0



# Checking to see if the password if it exist in API response.
def pwned_api_check(password):

  # First we are going to hash the password for the API call using hastlib.
  # We want to then encode the password in UTF 8
  sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

  # Selecting only the first five characters. 
  first5_char, tall_char = sha1_password[:5], sha1_password[5:]

  # call the request_api_data function with the first 5 char and store it in a response.
  response = request_api_data(first5_char)

  return get_pass_leaks_count(response, tall_char)

# Execute the script, Provided with a password in the command line to check.
def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times.. I think it is time to change your password')
    else:
      print(f'{password} was not found. You are all good.')
    return 'Done'


# Here is where we will input the password this one accept any number of arguments.
main(sys.argv[1:])