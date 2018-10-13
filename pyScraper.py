import requests
from bs4 import BeautifulSoup

# Followed this guide: https://www.codementor.io/dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4
# Script grabs the names of all the US presidents from the Wikipedia page below. 
# First time using Requests or BeautifulSoup!

def main():
    url = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_='wikitable')

    for link in table.find_all('b'):
        name = link.find('a')
        print(name.get_text('title'))

if __name__ == "__main__":
    main()