from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.pro-football-reference.com/boxscores/').text
print(html_text)
