#!/usr/bin/python


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
    summary = article[0]
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

    if url == '' or title == '' or text == '':
        return None

    for section in bad_sections:
        if section in url:
            if 'tvn24' in url and section == '/tv':
                pass
            else:
                return None

    bad_stuff = ["Morning Report", "Covid-19 in Bulgaria", 'COVID-19 in Bulgaria', "themobility", "ripon", "Ripon",
                 'irishemigrant', "Saudi Arabia records", "UAE Reports", "Coronavirus in Russia: The Latest News",
                 "fact-check", "Fact-check", "Photos:", 'bnamericas', "LIVE UPDATES", "Live Updates", "Live updates",
                 "updates:", "update:", "Poll:", 'Become a certified AWS professional', 'COVID-19: ', "PS5", 'Xbox',
                 'Nintendo', 'VPN bundle', 'Zoomer Radio', 'Desired Skills', 'Desired Work Experience',
                 'Peru: Coronavirus', 'Peru: Over', 'ad blocker', 'bloomberg', 'benzinga', 'We use cookies',
                 'Google Analytics', 'In review:', 'Earnings Call', 'Shareholders', 'shareholders', 'Earnings Report',
                 'earnings report', 'Earnings report', 'propertyeu.info', 'uses cookies', 'Early Edition:', 'WATCH:',
                 'Op-ed: ', 'Live: ']

    if len(keywords) < 3:
        return None
    for i in bad_stuff:
        if i in title or i in text or i in keywords or i in url or i in summary:
            return None

    # checking world articles to ensure relevance to the region
    # we don't want stories from asian newspapers that are about topics not relevant to the region the paper is from
    if key == 'world':
        country_count = 0
        for t in text.split(' '):
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

