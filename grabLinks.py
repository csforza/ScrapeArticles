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
KEYS = ['europe', 'france', 'poland', 'russia', 'germany', 'gb', 'eu', 'rest_of_europe'
        # 'usa', 'world', 'middle_east', 'americas', 'tech'
        ]


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
        response = requests.get(feed)

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
                # print(link + ' : ' + published)
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


if __name__ == '__main__':
    start = time.perf_counter()
    from grabFeeds import append_google_feeds
    from prepArticle import prep_article_dict
    from checkEurope import Check_Europe_Section
    from checkArticle import check_article
    from jsonArticles import results_into_json
    from summarizeArticle import summarize_article

    with open('resources/feeds/EuropeNewsFeed.txt', 'r') as file1:
        europe_feeds = file1.read().splitlines()

    europe_countries = ['france', 'European Union', 'poland', 'germany', 'england', 'ireland', 'scotland', 'russia',
                        'Norway', 'Sweden', 'Finland', 'Belarus', 'Estonia', 'Latvia', 'Lithuania', 'Ukraine',
                        'Moldova', 'Iceland', 'georgia tbilisi', 'polish government'
                                              'Romania', 'Bulgaria', 'Greece', 'North Macedonia', 'Albania', 'Kosovo',
                        'Montenegro', 'Bosnia', 'london', 'great britain',
                        'Serbia', 'Croatia', 'Hungary', 'Austria', 'Slovenia', 'Slovakia', 'Czechia', 'Switzerland',
                        'Italy', 'Rome', 'Vatican', 'Spain', 'Portugal', 'Denmark', 'Netherlands', 'Belgium', 'Armenia',
                        ]

    europe_feeds.extend(append_google_feeds(europe_countries))

    # grab the links from each of the rss feeds
    europe_links = grab_links(europe_feeds)
    time.sleep(5)
    europe_links = list(set(europe_links))

    # begin getting the article data
    europe_articles_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
        articles_results = [e.submit(summarize_article, k, 'europe') for k in europe_links]

        for g in concurrent.futures.as_completed(articles_results):
            if g.result():
                europe_articles_list.append(prep_article_dict(g.result()))

    print("sleeping")
    time.sleep(5)

    # now we need to set europe countries lists
    france_list, poland_list, russia_list = [], [], []
    germany_list, gb_list, eu_list, r_o_e_list = [], [], [], []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ex:
        countries_results = [ex.submit(Check_Europe_Section, eal) for eal in europe_articles_list]

        for gg in concurrent.futures.as_completed(countries_results):
            if gg.result():
                article1 = gg.result()[0]
                countries = gg.result()[1]

                if len(countries) > 0:
                    for country in countries:
                        if country == 'france':
                            france_list.append(article1)
                        if country == 'poland':
                            poland_list.append(article1)
                        if country == 'germany':
                            germany_list.append(article1)
                        if country == 'gb':
                            gb_list.append(article1)
                        if country == 'russia':
                            russia_list.append(article1)
                        if country == 'eu':
                            eu_list.append(article1)
                        if country == 'rest of europe':
                            r_o_e_list.append(article1)

    all_eu_countries_list = [europe_articles_list, france_list, poland_list, russia_list,
                             germany_list, gb_list, eu_list, r_o_e_list]

    print("sleeping")
    time.sleep(5)

    groups_for_json = []
    count = 0
    for country in all_eu_countries_list:
        print(f'{KEYS[count]}: {len(country)}')
        results_into_json(check_article(country, KEYS[count]), KEYS[count])

    stop = time.perf_counter()
    print(f'Elapsed time: {round(start - stop, 2)} seconds')
