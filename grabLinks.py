#!/usr/bin/python
import concurrent.futures
import random
import time
from datetime import datetime

import mechanize
import nltk
import requests
from bs4 import BeautifulSoup
from checkTime import check_time

nltk.download('punkt')

POLISH_SITES = ['https://www.tvpworld.com', 'https://tvn24.pl/tvn24-news-in-english']


# return top 20 links with 'https://tvn24.pl/tvn24-news-in-english/' in it
def tvn24():
    return_links_tvn = []
    count = 0

    url = 'https://tvn24.pl/tvn24-news-in-english/'

    br = mechanize.Browser()
    br.set_handle_robots(False)
    user_agent = "Googlebot/2.1 (+http://www.google.com/bot.html)"
    br.addheaders = [('User-Agent', user_agent)]
    br.open(url)

    for link in br.links():
        if count >= 10:
            break
        if 'https://tvn24.pl/tvn24-news-in-english/' in link.url:
            return_links_tvn.append(link.url)
            count += 1

    br.close()

    return return_links_tvn


# link > 39 chars w/ no 'http' in it
def tvpworld():
    return_links_tvp = []

    url = 'https://tvpworld.com'

    br = mechanize.Browser()
    br.set_handle_robots(False)
    user_agent = "Googlebot/2.1 (+http://www.google.com/bot.html)"
    br.addheaders = [('User-Agent', user_agent)]
    br.open(url)

    # because there are two links for the same article, one after another, don't append duplicates
    prev_link = ''
    for link in br.links():
        if len(link.url) >= 40 and 'http' not in link.url:
            if link.url != prev_link:
                return_links_tvp.append('https://tvpworld.com' + link.url)
                prev_link = link.url

    br.close()

    return return_links_tvp


def link_getter(feed):
    time.sleep(random.uniform(0, 0.4))
    # do we get a response? if no, just move on
    article_links = []
    webpage = ''
    try:
        response = requests.get(feed, timeout=5)

        # if a normal 200 code w/out extras - throw the rss into a list
        if response.status_code == 200:
            webpage = response.content
        # if a 403 instead (blocked) - try with different headers and see what comes up...
        if response.status_code == 403:
            headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
            response = requests.get(feed, headers=headers)
            if response.status_code == 200:
                webpage = response.content
            else:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
                response = requests.get(feed, headers=headers)
                if response.status_code == 200:
                    webpage = response.content

        # need to do date check, at least for tvn
        if feed in POLISH_SITES:
            if feed == 'https://tvn24.pl/tvn24-news-in-english':
                article_links.extend(tvn24())
            if feed == 'https://www.tvpworld.com':
                article_links.extend(tvpworld())
        else:
            soup = BeautifulSoup(webpage, features='xml')

            items = soup.find_all('item')
            for a in items:
                try:
                    link = a.find('link').text
                except:
                    link = ''

                try:
                    published = a.find('pubDate').text
                except:
                    published = datetime.now().strftime("%a, %d %b %Y %X +0000")
                # check the date of the article, if older than two days (true), then do not append the article link
                if check_time(published):
                    pass
                else:
                    article_links.append(link)
    except:
        response = None

    return article_links


# I believe we will return just the link
def grab_links(feeds):
    return_article_links = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = [executor.submit(link_getter, j) for j in feeds]

        for f in concurrent.futures.as_completed(results):
            if f.result():
                return_article_links.extend(f.result())

    return return_article_links

