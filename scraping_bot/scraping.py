# import the request Library
import requests

# Import beautiful soup 4, make my text clean 
from bs4 import BeautifulSoup

# Get the response from the Hacker News website.
try:

  # Getting the response from the web page I want to scrape.
  # We will receive all the data from the Hacker News website.
  res = requests.get('https://news.ycombinator.com/news')

  # We will use beautiful soup to parse this data into an object.
  # This will convert the tax into HTML.
  parse_to_html = BeautifulSoup(res.text, 'html.parser')

  # Now you can manipulate the object like it's an html object. ie: print(parse_to_html.body)
  # grabbing links using css selector 
  links = parse_to_html.select('.titleline > a')

  # grabbing scores using css selector 
  subtext = parse_to_html.select('.subtext')

  # This will sort all of our information by the highest votes.
  def sort_stories_by_votes(unsorted_news_list):
     
     # I am sorting using a lambda function using the vote ski and reversing the sort to descending.
     return sorted(unsorted_news_list, key=lambda x: x['votes'], reverse=True)

  # Creates a custom feed for hacking news website.
  def custom_new_feed(links, subtext):

    # Creates a new empty news list
    news_list = []

    # Using the enumerate function for indexing.
    for index, item in enumerate(links):
      
      # Getting all of the titles and if the title is broken getting none
      title = item.getText()

      # Getting all of the link titles and if the title is broken getting none. ie: href = links[index].get('href', None)
      href = item.get('href', None)

      # Getting all of the scores
      vote = subtext[index].select('.score')

      # If the vote is 0 do nothing else continue
      if len(vote):

        # Turn scores from a string into integer replace the point string with an empty string.
        points = int(vote[0].getText().replace(' points', ''))

        # We only want items that are 50 votes or more 
        if points >= 100:

          # We will append both the titles and eight refs to a dictionary.
          news_list.append({'votes': points, 'title': title, 'link': href})

    return sort_stories_by_votes(news_list)

  # Validating I'm calling the right code on the correct script.
  if __name__ == '__main__':
    # Call the function and print the results.
    news_feed = custom_new_feed(links, subtext)
    print("Hacker News Titles:")
    for item in news_feed:
        print(item)

except requests.RequestException as e:
    print(f"An error occurred while fetching data: {e}")