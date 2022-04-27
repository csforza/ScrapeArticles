#!/usr/bin/python
from textblob import TextBlob
from statistics import mean


def sentiment_analysis(news_story):

    news = TextBlob(news_story)
    sentiments = []
    # does sentiment analysis on each sentence
    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiments.append(metric)

    polarity_data = []
    subjectivity_data = []
    # divide the polarity scores and subjectivity scores into separate lists
    for i in range(len(sentiments)):
        if i % 2 == 0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append((sentiments[i]))

    # calc the avg of each of those scores, round to 4 decimal points
    polarity = round(mean(polarity_data), 4)
    subjectivity = round(mean(subjectivity_data), 4)

    return [polarity, subjectivity]
