import requests
from bs4 import BeautifulSoup

#
# Basic web scraper
#

def scrape(url, *args):
  r = requests.get(url)
  if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all(args)
    num = 1
    for title in titles:
      print(f"({num}) Title: {title.text}\n")
      num = num+1

# MODIFY BELOW
# Arguments: target URL, tag1, tag2, tag3....
scrape("https://jeremiahtalamantes.com/", "h2", "li")