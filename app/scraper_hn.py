#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Scraping hacker new site."""

import re
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
from time import sleep

# Clean the console
os.system('clear')

# Setting requests and bs4
url = 'https://news.ycombinator.com/news'
req = requests.get(url)
html_soup = BeautifulSoup(req.text, 'html.parser')


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
⣿⣿⣿⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⣿⣿⣿ |  Using Bs4 and Requests
⣿⣿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣿⣿ |
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ |
____________________________________________________________________

  \033[0m""")


def scraper():
    """Scraper of the site and return the extracted data."""
    # For store results in a list
    articles = []
    # Getting all data of tr tag
    for item in html_soup.find_all('tr', class_='athing'):
        # Getting tag a
        item_a = item.find('a', class_='storylink')
        item_link = item_a.get_text('href') if item_a else None
        item_text = item_a.get_text(strip=True) if item_a else None
        next_row = item.find_next_sibling('tr')
        # Getting tag spam
        item_score = next_row.find('span', class_='score')
        item_score = item_score.get_text(strip=True) if item_score else '0 points'
        # We use regex here to find the correct element
        item_comments = next_row.find('a', string=re.compile('\d+(&nbsp;|\s)comment(s?)'))
        item_comments = item_comments.get_text(strip=True).replace('\xa0', ' ') \
            if item_comments else '0 comments'
        # Storing results
        articles.append({
            'link' : item_link,
            'title' : item_text,
            'score' : item_score,
            'comments' : item_comments
        })
        pprint(articles)
        sleep(1)
    return articles


def create_dataframe():
    """Creating a dataframe from data and storing
    
    in .csv file."""
    data = scraper()
    data_frame = pd.DataFrame(data)
    print("Creating DataFrame........")
    print(data_frame.head())
    print("Creating CSV file.........")
    data_frame.to_csv(f"hacker_news_{datetime.now().strftime('%d_%m_%Y_%H:%M')}.csv")

if __name__ == '__main__':
    scraper_header() 
    data = scraper() 
    pprint(data)
    create_dataframe()
