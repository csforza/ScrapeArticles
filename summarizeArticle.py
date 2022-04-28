#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from newspaper import Article, Config
from sentimentAnalysis import sentiment_analysis
import random
import re
from datetime import datetime
import time
from keepOrDump import keep_or_dump


def summarize_article(url, key):
    time.sleep(random.uniform(0, 0.4))

    new_list = []

    url = url.strip()
    # print(url)

    try:
        response = requests.get(url, timeout=5)
        # if a normal 200 code w/out extras - throw the rss into a list
        if response.status_code == 200:
            article = Article(url)
        # if a 403 instead (blocked) - try with different headers and see what comes up...
        if response.status_code == 403:
            headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                user_agent = "Googlebot/2.1 (+http://www.google.com/bot.html)"
                config = Config()
                config.browser_user_agent = user_agent
                article = Article(url, config=config)
            else:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
                    config = Config()
                    config.browser_user_agent = user_agent
                    article = Article(url, config=config)

        article.download()
        article.parse()

        article.download('punkt')
        article.nlp()

        article_meta_data = article.meta_data

        # in case no summary can be had
        summary = ''
        if len(article.summary) > 0:
            summary = article.summary
        elif len(article.summary) == 0:
            summary = [value for (key, value) in article_meta_data.items() if key == 'description'][0]
            if len(summary) == 0:
                summary = [value for (key, value) in article_meta_data.items() if key == 'dc:description'][0]
        new_list.append(summary)

        # if ekathermina news site, text must be gotten this way...
        if 'ekathimerini' in url:
            webpage = response.content
            soup = BeautifulSoup(webpage, features='lxml')
            text_list = soup.find_all('p')
            text = ''
            for p in text_list:
                text = text + ' ' + p.text
        else:
            text = article.text
        new_list.append(text)

        keywords = article.keywords
        new_list.append(keywords)

        title = article.title
        new_list.append(title)

        new_list.append(url)

        # what we have in the article data so far, we now check before moving on to filter out more garbage
        koc = keep_or_dump(new_list, key)
        if koc:
            new_list = koc
        else:
            return None

        try:
            image = article.top_image
        except:
            image = '/static/img/wln_alt.png'

        if 'securityweek' in url or 'abcnews' in url:
            image = '/static/img/wln_alt.png'
        if len(image) < 20:
            image = '/static/img/wln_alt.png'

        new_list.append(image)

        published = datetime.now().strftime("%a, %d %b %Y %X")

        new_list.append(published)

        # do sentiment analysis and return those values
        sa = sentiment_analysis(text)
        if sa[0] == 0.0 or sa[1] == 0.0:
            return None
        else:
            new_list.append(sa[0])  # polarity score
            new_list.append(sa[1])  # subjectivity score

        # input the channel here too - regex to snip the domain and nothing more
        try:
            channel = re.search("(http:\/\/|https:\/\/)+[^\s\/]+", url).group(0).split('//')[1]
        except:
            channel = url
        if 'www.' in channel:
            channel = channel.replace('www.', '')
        new_list.append(channel)

    except:
        return None

    return new_list

