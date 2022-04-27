#!/usr/bin/python
from datetime import datetime, timedelta

TWO_DAYS_AGO_DATE = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")


def append_google_feeds(countries):
    return_list = []
    for country in countries:
        if ' ' in country:
            country = country.replace(' ', '+')
        return_list.append(
            f'https://news.google.com/rss/search?q={country}+-sports+-ripon+-themobility.club+after:{TWO_DAYS_AGO_DATE}&hl=en-US&gl=US&ceid=US:en'
        )
    return return_list


def grab_feeds():
    with open('resources/feeds/EuropeNewsFeed.txt', 'r') as file1:
        europe_feeds = file1.read().splitlines()

    with open('resources/feeds/USANewsFeeds.txt', 'r') as file2:
        usa_feeds = file2.read().splitlines()

    with open('resources/feeds/WorldNewsFeeds.txt', 'r') as file3:
        world_feeds = file3.read().splitlines()

    with open('resources/feeds/MiddleeastFeed.txt', 'r') as file4:
        me_feeds = file4.read().splitlines()

    with open('resources/feeds/AmericasFeeds.txt', 'r') as file5:
        americas_feeds = file5.read().splitlines()

    with open('resources/feeds/TechFeeds.txt', 'r') as file6:
        tech_feeds = file6.read().splitlines()

    # countries (or tech topics) list for Google rss feeds
    # updating these lists and shrinking because there might be over saturation
    # results from my old program we much better
    # first need to see if too much google rss is causing it

    # for europe, will just add italy, spain, and poland because I could never get enough results
    europe_countries = ['poland', 'italy', 'spain', 'warsaw', 'France', 'Germany', 'England']

    # this should be ok....had trouble getting data
    americas_countries = ['Mexico', 'Peru', 'Brazil', 'bogota colombia', 'Argentina', 'santiago Chile', 'Venezuela',
                          'Bolivia', 'guatemala', 'canada', 'Justin Trudeau', 'Jair Bolsonaro',
                          'Ecuador', 'Panama', 'Uruguay', 'Paraguay', 'Nicaragua', 'Honduras', 'el salvador', 'cuba',
                          'Andrés Manuel López Obrador', 'Nayib Bukele', 'Canada Trudeau', 'Mexico City',
                          'Mexican Government', 'Mexican Cartels', 'Canadian government', 'Brazilian Government'
                          ]
    # i don't think will be necessary
    # me_countries = ['Israel', 'iran', 'Saudi arabia', 'Egypt', 'Turkish government', 'Iraq', 'Syria', 'Jordan', 'Yemen',
    #                 'oman', 'united arab emirates', 'bahrain', 'kuwait', 'azerbaijan', 'lebanon', 'qatar',
    #                 'afghanistan', 'taliban', 'OPEC', 'Erdogan', 'Salman of Saudi Arabia', 'Israel Government',
    #                 'Iran Government', 'houthi', 'hezbollah']

    # overkill, but I didn't get enough china news prior
    world_countries = ['china', 'china government', 'japanese government', 'japan', 'india',
                       'indian government', 'korean government', 'australia', 'new zealand']
    # variable name not quite appropriate, but makes things easy
    tech_countries = ['cryptocurrency', 'cyber attack', 'ransomware', 'hacker group', 'vulnerability site:medium.com']
    # not at all necessary
    # usa_countries = ['white house', 'joe biden', 'donald trump', 'congress', 'usa defense', 'usa senate']

    # now add the Google News feeds to the feeds we have already
    to_append = [(europe_countries, europe_feeds), (world_countries, world_feeds),
                 (americas_countries, americas_feeds), (tech_countries, tech_feeds)]
    for x, y in to_append:
        y.extend(append_google_feeds(x))

    return [europe_feeds, usa_feeds, world_feeds, me_feeds, americas_feeds, tech_feeds]
