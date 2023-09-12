from bs4 import BeautifulSoup
import requests


def nfl_week():
    html_text = requests.get(
        'https://www.pro-football-reference.com/boxscores/').text
    soup = BeautifulSoup(html_text, "lxml")

    # Scrape year and week title
    week_title = soup.find("div", class_="section_heading")
    week_title = str(week_title)
    week_title = week_title[33:-11]


def nfl_dates():
    html_text = requests.get(
        'https://www.pro-football-reference.com/boxscores/').text
    soup = BeautifulSoup(html_text, "lxml")

    # Scrape the game dates
    game_dates = soup.find_all("tr", class_="date")
    dates = []
    for date in game_dates:
        dates.append(date.text)


def nfl_winners():
    html_text = requests.get(
        'https://www.pro-football-reference.com/boxscores/').text
    soup = BeautifulSoup(html_text, "lxml")

    # Scrape the winners
    game_winners = soup.find_all("tr", class_="winner")
    winners = []
    for winner in game_winners:
        winners.append(winner.a.text)


def nfl_losers():
    html_text = requests.get(
        'https://www.pro-football-reference.com/boxscores/').text
    soup = BeautifulSoup(html_text, "lxml")

    # Scrape the losers
    game_losers = soup.find_all("tr", class_="loser")
    losers = []
    for loser in game_losers:
        losers.append(loser.a.text)


"""""
# Present Info
print(f"Statistics for {week_title}:")
for i in range(len(dates)):
    print(f"\t{dates[i]} - {winners[i]} defeated {losers[i]}")
"""
