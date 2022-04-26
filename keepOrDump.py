#!/usr/bin/python

AMERICAS = ['Mexico', 'Peru', 'Brazil', 'Colombia', 'Argentina', 'Chile', 'Venezuela', 'Bolivia',
            'Ecuador', 'Panama', 'Uruguay', 'Paraguay', 'Nicaragua', 'Honduras', 'El Salvador', 'Cuba',
            'Guatemala', 'Canada', 'Trudeau', 'Bolsonaro', 'Mexico City', 'Ottawa', 'Quebec', 'America']
MIDDLE_EAST = ['Israel', 'Iran', 'Saudi Arabia', 'Egypt', 'Turkey', 'Iraq', 'Syria', 'Jordan', 'Yemen',
               'Oman', 'United Arab Emirates', 'UAE', 'Bahrain', 'Kuwait', 'Azerbaijan', 'Lebanon', 'Qatar',
               'Afghanistan', 'Taliban', 'OPEC']
WORLD = ['China', 'Japan', 'India', 'Senegal', 'North Korea', 'South Korea', 'Myanmar', 'Cambodia', 'Vietnam',
         'Thailand', 'Indonesia', 'Pakistan', 'Kazakhstan', 'Turkmenistan', 'Mongolia', 'Uzbekistan',
         'Bangladesh', 'Sri Lanka', 'Malaysia', 'Taiwan', 'Hong Kong', 'Philippines', 'Algeria',
         'Tunisia', 'Nigeria', 'Australia', 'New zealand', 'Cameroon', 'Ghana', 'Ethiopia',
         'Sudan', 'Libya', 'South Africa', 'Zimbabwe', 'Angola', 'Ivory Coast', 'Liberia', 'Morocco',
         'Tanzania', 'Kenya', 'Central African Republic', 'Congo', 'Mali']


def keep_or_dump(article, key):
    bad_list = [
        'hollywood', 'actor', 'actress', 'sport', 'sports', 'singer', 'music', 'song', 'entertainment', 'football',
        'basketball', 'soccer', 'baseball', 'hockey', 'tennis', 'superstar', 'movie', 'film', 'instagram', 'fan',
        'fans', 'mma', 'boxing', 'nfl', 'nba', 'mlb', 'nhl', 'olympics', 'ufc', 'golf', 'screen',
        'rugby', 'scores', 'vs.', 'midfielder', 'tv', 'episodes', 'crucial game'
    ]

    bad_sections = ['/sport', '/sports', '/film', '/entertainment', '/movies', '/gossip', '/tv', '/arts',
                    '/lifestyle', '/lifestyles', '/travel', '/dining', '/food', '/culture', '/rugby',
                    '/fashion', '/beauty', '/football', '/art/', '/recipes', '/weather', '.mp3', '.jpg', '.png']

    # new_list = [summary, text, title, keywords, url]
    text = article[1]
    keywords = article[2]
    title = article[3]
    url = article[4]

    # we want regular news and not entertainment or politics
    for keys in keywords:
        if keys in bad_list:
            return None

    # checks if any of the bad words are in the article more than once
    for keyword in text.split(' '):
        if keyword.lower() in bad_list:
            if text.count(keyword.lower()) > 1:
                return None

    if url == '':
        return None

    for section in bad_sections:
        if section in url:
            if 'tvn24' in url and section == '/tv':
                pass
            else:
                return None

    if len(keywords) < 3:
        return None
    if "Morning Report" in title:
        return None
    # to get rid of useless covid numbers
    if "Covid-19 in Bulgaria" in title:
        return None
    if "themobility" in url or "themobility" in title or "themobility" in keywords:
        return None
    if "ripon" in url or "ripon" in title or "ripon" in keywords:
        return None
    if "Ripon" in url or "Ripon" in title or "Ripon" in keywords:
        return None
    if 'irishemigrant' in url:
        return None
    if "Saudi Arabia records" in title or 'UAE reports' in title:
        return None
    if "Coronavirus in Russia: The Latest News" in title:
        return None
    # no false fact checks
    if "fact-check" in title or "Fact-check" in title:
        return None
    if "Photos:" in title:
        return None
    if 'bnamericas' in url or 'bnamericas' in title:
        return None
    if "LIVE UPDATES" in title or "Live Updates" in title or "Live updates" in title:
        return None
    if "updates:" in title or "update:" in title:
        return None
    if 'Poll:' in title:
        return None
    if 'Become a certified AWS professional' in title:
        return None
    if 'COVID-19: ' in title:
        return None
    if 'COVID-19 in Bulgaria' in title:
        return None
    if 'PS5' in title or 'Xbox' in title or 'Nintendo' in title:
        return None
    if 'VPN bundle' in title:
        return None
    if 'Zoomer Radio' in title:
        return None
    if 'Desired Skills' in text or 'Desired Work Experience' in text:
        return None

    # checking world, me, and americas articles to ensure relevance to the region
    # we don't want stories from asian newspapers that are about topics not relevant to the region the paper is from
    # can do europe too but it does not have this problem
    if key == 'world':
        country_count = 0
        for t in text.split(' '):
            #     if key == 'americas' and t in AMERICAS:
            #         country_count += 1
            #     if key == 'middle_east' and t in MIDDLE_EAST:
            #         country_count += 1
            if key == 'world' and t in WORLD:
                country_count += 1
        if country_count == 0:
            return None

    # if the article is worth using, check the title or html encoding
    if '&#8216;' in title:
        title = title.replace('&#8216;', "'")
    if '&#8217;' in title:
        title = title.replace('&#8217;', "'")
    if '&#039;' in title:
        title = title.replace('&#039;', "'")
    if '\u2019' in title:
        title = title.replace('\u2019', "'")
    if '\u2013' in title:
        title = title.replace('\u2013', '-')
    if '\u2014' in title:
        title = title.replace('\u2014', '-')
    if '\xa0' in title:
        title = title.replace('\xa0', "")
    if '\u200b' in title:
        title = title.replace('\u200b', "")
    if '&#039;' in title:
        title = title.replace('\u200b', "'")
    if '&quot;' in title:
        title = title.replace('&quot;', '"')
    if '[Ticker]' in title:
        title = title.replace('[Ticker]', '')

    for keyword in keywords:
        if keyword.lower() in url:
            keywords.remove(keyword)

    return [article[0], text, title, keywords, url]


if __name__ == '__main__':
    import time
    from grabFeeds import append_google_feeds
    from prepArticle import prep_article_dict
    import concurrent.futures
    from checkArticle import check_article
    from jsonArticles import results_into_json
    from summarizeArticle import summarize_article
    from grabLinks import grab_links

    start = time.perf_counter()

    with open('resources/feeds/AmericasFeeds.txt', 'r') as file1:
        americas_feeds = file1.read().splitlines()

    americas_countries = ['Israel', 'iran', 'Saudi arabia', 'Egypt', 'Turkish government', 'Iraq', 'Syria', 'Jordan', 'Yemen',
                    'oman', 'united arab emirates', 'bahrain', 'kuwait', 'azerbaijan', 'lebanon', 'qatar',
                    'afghanistan', 'taliban', 'OPEC', 'Erdogan', 'Salman of Saudi Arabia', 'Israel Government',
                    'Iran Government', 'houthi', 'hezbollah']

    americas_feeds.extend(append_google_feeds(americas_countries))

    # grab the links from each of the rss feeds
    americas_links = grab_links(americas_feeds)
    time.sleep(5)
    americas_links = list(set(americas_links))

    # begin getting the article data
    americas_articles_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
        articles_results = [e.submit(summarize_article, k, 'middle_east') for k in americas_links]

        for g in concurrent.futures.as_completed(articles_results):
            if g.result():
                americas_articles_list.append(prep_article_dict(g.result()))

    print("sleeping")
    time.sleep(5)

    print(f'{"middle_east"}: {len(americas_articles_list)}')
    results_into_json(check_article(americas_articles_list, 'middle_east'), 'middle_east')

    stop = time.perf_counter()
    print(f'Elapsed time: {round(start - stop, 2)} seconds')
