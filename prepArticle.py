def prep_article_dict(data):
    summary = data[0]
    text = data[1]
    title = data[2]
    first_keywords = data[3]
    link = data[4]
    image = data[5]
    published = data[6]
    polarity = data[7]
    subjectivity = data[8]
    channel = data[9]

    article = {
        'title': title,
        'keywords': first_keywords,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'link': link,
        'published': published,
        'summary': summary,
        'channel': channel,
        'text': text,
        'image': image,
        'news date': published
    }
    # print(article)

    return article
