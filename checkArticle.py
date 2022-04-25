#!/usr/bin/python
import random
import concurrent.futures
from sortAndRank import sort_and_rank


# checks similarity based on the number of matching keywords
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
    if .4 <= similar_percent < 1:
        return True
    else:
        return False


def run_sim_check(article, article_list):
    is_similar = False
    article_list2 = article_list.copy()
    article_sims_list = [article]
    num1 = len(article['keywords'])
    for article2 in article_list2:
        is_similar = check_similarity(article['keywords'], num1, article2['keywords'])
        if is_similar:
            article_sims_list.append(article2)

    for ag in article_sims_list:
        if article_sims_list.count(ag) > 1:
            article_sims_list.remove(ag)

    return article_sims_list


def check_article(article_list):

    article_groups = []
    # so as not to favor articles that are pulled first
    random.shuffle(article_list)


    # grabs each article in the article list, and checks against the rest of the collected articles for any similars
    # and stores them
    # for article in article_list:
    # article_sims_list = []
    # num1 = len(article['keywords'])
    # for article2 in article_list2:
    #     is_similar = check_similarity(article['keywords'], num1, article2['keywords'])
    #     if is_similar:
    #         article_sims_list.append(article)

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
        results = [e.submit(run_sim_check, article, article_list) for article in article_list]

        # if more than one similar article found, add to the grouped articles
        for r in concurrent.futures.as_completed(results):
            if len(r.result()) > 1:
                article_groups.append(r.result())

        # if more than one similar article found, add to the grouped articles
        # if len(article_sims_list) > 1:
        #     article_groups.append(article_sims_list)

    article_groups = sort_and_rank(article_groups)

    return article_groups

