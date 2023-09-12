from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.pro-football-reference.com/boxscores/').text

# Grab the year and week title
soup = BeautifulSoup(html_text, "lxml")
week_title = soup.find("div", class_="section_heading")
week_title = str(week_title)
week_title = week_title[33:-11]

# Scrape the game dataes
game_dates = soup.find_all("tr", class_="date")
dates = []
for date in game_dates:
    dates.append(date.text)
print(dates)

# Scrape the winners
game_winners = soup.find_all("tr", class_="winner")
winners = []
for winner in game_winners:
    winners.append(winner.a.text)
print(winners)

# Scrape the losers
game_losers = soup.find_all("tr", class_="loser")
losers = []
for loser in game_losers:
    losers.append(loser.a.text)
print()
print(losers)

# Scrape winner scores
""""
game_winner_scores = game_winners.find("td", class_="right")
winner_scores = []
for score in game_winner_scores:
    winner_scores.append(score.text)

print()
print()
print(winner_scores)

"""

# Present Info

print(f"Statistics for {week_title}:")
for i in range(len(dates)):
    print(f"\t{dates[i]} - {winners[i]} defeated {losers[i]}")
