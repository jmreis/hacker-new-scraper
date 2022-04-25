#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Scraping hacker news using github API."""

import os
import requests
import logging
import timeit
#import pandas as pd
import http.client
#from datetime import datetime
from alive_progress import alive_bar

# Cleaning terminal
os.system("clear")
# Setting the logging configurations
httpclient_logger = logging.getLogger("http.client")
logging.basicConfig(format='%(asctime)s - hacker-new-scraper.py - %(message)s', level=logging.DEBUG)


def httpclient_logging(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))
        
    http.client.print = httpclient_log
    http.client.HTTPConnection.debuglevel = 1

# Get start time
starttime = timeit.default_timer()
logging.debug(f'Start time: {starttime}')

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
    with alive_bar(len(top_stories), dual_line=True, title='Hacker-News-Scraper') as bar:
        for story_id in top_stories:
            # Setting url by id stories
            story_url = url + f"/item/{story_id}.json"
            # Printin url
            logging.debug(f"Fetching: {story_url}")
            # Getting data from id stories
            req = requests.get(story_url)
            story_dict = req.json()
            # Storing data
            articles.append(story_dict)
            bar()
    return articles

"""
def create_dataframe():
    Creating a dataframe from data and storing
    
    in .csv file.
    data = scraper_api()
    data_frame = pd.DataFrame(data)
    logging.debug(data_frame.head())
    data_frame.to_csv(f"hacker_news_github_api{datetime.now().strftime('%d_%m_%Y_%H:%M')}.csv")
"""

if __name__ == '__main__':
    #httpclient_logging()
    scraper_header()
    news = scraper_api()
    with alive_bar(len(news), dual_line=True, title='Hacker-News-Scraper') as bar:
        for new in news: 
            logging.debug(new)
            bar()   
    #create_dataframe()
    logging.debug(f'End time: {timeit.default_timer() - starttime}')