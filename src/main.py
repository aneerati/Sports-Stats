from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.pro-football-reference.com/boxscores/').text

soup = BeautifulSoup(html_text, "lxml")
week_title = soup.find("div", class_="section_heading")

week_title = str(week_title)
print(week_title)

game_dates = soup.find_all("tr", class_="date")
dates = []
for date in game_dates:
    dates.append(date.text)
print(dates)

game_winners = soup.find_all("tr", class_="winner")
winners = []
for winner in game_winners:
    winners.append(winner.a.text)
print(winners)

game_losers = soup.find_all("tr", class_="loser")
losers = []
for loser in game_losers:
    losers.append(loser.a.text)
print()
print(losers)
