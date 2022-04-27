#!/usr/bin/python
import random
import concurrent.futures
from sortAndRank import sort_and_rank
import time


# checks similarity based on the number of matching keywords
def check_similarity_war(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .5 <= similar_percent < 1:
        return True
    else:
        return False


def check_similarity_higher(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .45 <= similar_percent < 1:
        return True
    else:
        return False


def check_similarity_high(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .4 <= similar_percent < 1:
        return True
    else:
        return False


def check_similarity(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .35 <= similar_percent < 1:
        return True
    else:
        return False


def check_similarity_low(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .33 <= similar_percent < 1:
        return True
    else:
        return False


def check_similarity_lowest(keywords1, num1, keywords2):
    count, similar_percent = 0, 0

    for i in keywords1:
        if i in keywords2:
            count += 1

    try:
        similar_percent = count / num1
    except ZeroDivisionError:
        pass

    # if the article is the exact same one then it will be = 1
    if .3 <= similar_percent < 1:
        return True
    else:
        return False


def run_sim_check(article, article_list, key):
    time.sleep(random.uniform(0, 0.4))
    is_similar = False
    article_list2 = article_list.copy()
    article_sims_list = [article]
    num1 = len(article['keywords'])
    for article2 in article_list2:
        # if key == 'poland':
        #     is_similar = check_similarity_lowest(article['keywords'], num1, article2['keywords'])
        if key == 'usa' or key == 'middle_east':
            is_similar = check_similarity_higher(article['keywords'], num1, article2['keywords'])
        if key == 'world':
            is_similar = check_similarity_high(article['keywords'], num1, article2['keywords'])
        if key == 'russia' or key == 'tech' or key == 'europe':
            is_similar = check_similarity_war(article['keywords'], num1, article2['keywords'])
        else:
            is_similar = check_similarity(article['keywords'], num1, article2['keywords'])

        if is_similar:
            article_sims_list.append(article2)

    for ag in article_sims_list:
        if article_sims_list.count(ag) > 1:
            article_sims_list.remove(ag)

    return article_sims_list


def check_article(article_list, key):
    article_groups = []
    # so as not to favor articles that are pulled first
    random.shuffle(article_list)

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
        results = [e.submit(run_sim_check, article, article_list, key) for article in article_list]

        # if more than one similar article found, add to the grouped articles
        for r in concurrent.futures.as_completed(results):
            if len(r.result()) > 1:
                article_groups.append(r.result())

    article_groups = sort_and_rank(article_groups)

    # just in case any groups are the same
    for ra in article_groups:
        if article_groups.count(ra) > 1:
            article_groups.remove(ra)

    return article_groups


