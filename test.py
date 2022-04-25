#!/usr/bin/python
# I believe we will return just the link, channel, and pub date
def grab_links(feeds):
    return_article_links = []

    for feed in feeds:
        # do we get a response? if no, just mo
        try:
            response = requests.get(feed)
        except:
            continue

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

        if feed in POLISH_SITES:
            if feed == 'https://tvn24.pl/tvn24-news-in-english':
                return_article_links.extend(tvn24())
            if feed == 'https://www.tvpworld.com':
                return_article_links.extend(tvpworld())
        else:
            soup = BeautifulSoup(webpage, features='xml')

            items = soup.find_all('item')
            with open('check_times.txt', 'w') as time_file:
                for a in items:
                    try:
                        link = a.find('link').text
                    except:
                        link = ''

                    try:
                        published = a.find('pubDate').text
                    except:
                        published = datetime.now().strftime("%a, %d %b %Y %X +0000")

                    time_file.write(link + ' : ' + published)
                    # check the date of the article, if older than two days (true), then do not append the article link
                    if check_time(published, feed):
                        pass
                    else:
                        return_article_links.append(link)

    return return_article_links