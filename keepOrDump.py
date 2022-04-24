def keep_or_dump(article):
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

    # print(text)
    # print(keywords)
    # print(title)
    # print(url)

    # we want regular news and not entertainment or politics
    for keys in keywords:
        if keys in bad_list:
            print("bad keys : ", keys)
            return None

    # checks if any of the bad words are in the article more than once
    for keyword in text.split(' '):
        if keyword.lower() in bad_list:
            if text.count(keyword.lower()) > 1:
                print("bad words : ", keyword)
                return None

    if url == '':
        print("no link")
        return None

    # for section in bad_sections:
    #     if section in url:
    #         if 'tvn24' in url and section == '/tv':
    #             pass
    #         else:
    #             print('tvn')
    #             return None

    if len(keywords) < 3:
        print('not enough keys')
        return None
    if "Morning Report" in title:
        print("bad title 1")
        return None
    # to get rid of useless covid numbers
    if "Covid-19 in Bulgaria" in title:
        print("bad title 2")
        return None
    if "Saudi Arabia records" in title or 'UAE reports' in title:
        print("bad title 3")
        return None
    if "Coronavirus in Russia: The Latest News" in title:
        print("bad title 4")
        return None
    # no false fact checks
    if "fact-check" in title or "Fact-check" in title:
        print("bad title 5")
        return None
    if "Photos:" in title:
        print("bad title 6")
        return None
    if "updates:" in title or "update:" in title:
        print("bad title 7")
        return None
    if 'Poll:' in title:
        print("bad title 8")
        return None
    if 'Become a certified AWS professional' in title:
        print("bad title 9")
        return None
    if 'COVID-19: ' in title:
        print("bad title 10")
        return None
    if 'COVID-19 in Bulgaria' in title:
        print("bad title 11")
        return None
    if 'PS5' in title or 'Xbox' in title or 'Nintendo' in title:
        print("bad title 12")
        return None
    if 'VPN bundle' in title:
        print("bad title 13")
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
    if '\u2013' in title or '\u2014' in title:
        title = title.replace('\u2013', '-')
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
    t0 = "Croatian PM says he will boycott president"
    t1 = "Croatian PM says he will boycott president"
    t2 = "Viral \u2018Ukraine Windows\u2019 Photo Didn\u2019t Show Whole Picture"
    t3 = [
        "photograph",
        "picture",
        "ukrainian",
        "russias",
        "snopes",
        "viral",
        "overturned",
        "russian",
        "cars",
        "ukraine",
        "windows",
        "claim",
        "bucha",
        "didnt"
    ]
    t4 = "https://www.snopes.com/news/2022/04/22/viral-ukraine-windows-photo-didnt-show-whole-picture/"
    print(keep_or_dump([t0, t1, t2, t3, t4]))
