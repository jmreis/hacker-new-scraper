#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Scraping hacker news using github API."""

import os
import requests
import pandas as pd
from datetime import datetime

# Clean the terminal
os.system('clear')

# Setting requests
url = 'https://hacker-news.firebaseio.com/v0'
top_stories = requests.get(url + '/topstories.json').json()


def scraper_header():
    """Provide header for script."""
    print("""\033[33m;
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ |
⣿⣿⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿ |
⣿⣿⣿⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⣿⣿⣿ |
⣿⣿⣿⠀⢸⣿⣿⣏⠹⣿⣿⠏⣹⣿⣿⡇⠀⣿⣿⣿ |
⣿⣿⣿⠀⢸⣿⣿⣿⣆⠹⠏⣰⣿⣿⣿⡇⠀⣿⣿⣿ |  Scraping Hacker News
⣿⣿⣿⠀⢸⣿⣿⣿⣿⡆⢰⣿⣿⣿⣿⡇⠀⣿⣿⣿ |  Site: https://news.ycombinator.com/news
⣿⣿⣿⠀⢸⣿⣿⣿⣿⣇⣸⣿⣿⣿⣿⡇⠀⣿⣿⣿ |  Autor: Jair Reis
⣿⣿⣿⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⣿⣿⣿ |  Using GitHub API
⣿⣿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣿⣿ |
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ |
____________________________________________________________________

  \033[0m""")


def scraper_api():
    """Scraping the data from the api."""
    # For store the data
    articles = []
    for story_id in top_stories:
        # Setting url by id stories
        story_url = url + f"/item/{story_id}.json"
        # Printin url
        print(f"Fetching: {story_url}")
        # Getting data from id stories
        req = requests.get(story_url)
        story_dict = req.json()
        # Storing data
        articles.append(story_dict)
    return articles


def create_dataframe():
    """Creating a dataframe from data and storing
    
    in .csv file."""
    data = scraper_api()
    data_frame = pd.DataFrame(data)
    print(data_frame.head())
    data_frame.to_csv(f"hacker_news_github_api{datetime.now().strftime('%d_%m_%Y_%H:%M')}.csv")


if __name__ == '__main__':
    scraper_header()
    data = scraper_api()    
    create_dataframe()