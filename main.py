#!/usr/bin/python
import time
from grabFeeds import grab_feeds
from grabLinks import grab_links
from summarizeArticle import summarize_article
from prepArticle import prep_article_dict
from checkEurope import Check_Europe_Section
import concurrent.futures
import json
from checkArticle import check_article
from jsonArticles import results_into_json

KEYS = ['europe', 'france', 'poland', 'russia', 'germany', 'gb', 'eu', 'rest_of_europe',
        'usa', 'world', 'middle_east', 'americas', 'tech']


# note order: europe_feeds, usa_feeds, world_feeds, me_feeds, americas_feeds, tech_feeds
def main():
    # gather all the feeds and collect them into separate lists
    big_list = grab_feeds()

    total_links = [grab_links(feeds) for feeds in big_list]

    time.sleep(5)

    # remove duplicates and set to respective list
    total_eu_links = list(set(total_links[0]))
    total_usa_links = list(set(total_links[1]))
    total_world_links = list(set(total_links[2]))
    total_me_links = list(set(total_links[3]))
    total_americas_links = list(set(total_links[4]))
    total_tech_links = list(set(total_links[5]))

    total_links_list = [total_eu_links, total_usa_links, total_world_links, total_me_links, total_americas_links,
                        total_tech_links]

    full_articles_list = []
    for tll in total_links_list:
        counted = 0
        articles_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
            articles_results = [e.submit(summarize_article, k) for k in tll]

            for g in concurrent.futures.as_completed(articles_results):
                if g.result():
                    articles_list.append(prep_article_dict(g.result()))
                    counted += 1

        full_articles_list.append(articles_list)

        print(f"length of list = {len(tll)}")
        print(f"length of counted = {counted}")
        time.sleep(5)

    europe_articles_list = full_articles_list[0]
    usa_articles_list = full_articles_list[1]
    world_articles_list = full_articles_list[2]
    me_articles_list = full_articles_list[3]
    americas_articles_list = full_articles_list[4]
    tech_articles_list = full_articles_list[5]

    # now we need to set europe countries lists
    france_list, poland_list, russia_list, germany_list, gb_list, eu_list, r_o_e_list = [], [], [], [], [], [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ex:
        countries_results = [ex.submit(Check_Europe_Section, eal) for eal in europe_articles_list]
        for gg in concurrent.futures.as_completed(countries_results):
            if gg.result():
                article1 = gg.result()[0]
                countries = gg.result()[1]
                if len(countries) > 0:
                    for country in countries:
                        if country == 'france':
                            france_list.append(article1)
                        if country == 'poland':
                            poland_list.append(article1)
                        if country == 'germany':
                            germany_list.append(article1)
                        if country == 'gb':
                            gb_list.append(article1)
                        if country == 'russia':
                            russia_list.append(article1)
                        if country == 'eu':
                            eu_list.append(article1)
                        if country == 'rest of europe':
                            r_o_e_list.append(article1)

    all_countries_list = [europe_articles_list, france_list, poland_list, russia_list, germany_list, gb_list, eu_list,
                          r_o_e_list, usa_articles_list, world_articles_list, me_articles_list, americas_articles_list,
                          tech_articles_list]

    print("sleeping")
    time.sleep(5)

    count = 0
    for country in all_countries_list:
        print(f'Country: {len(country)}')
        results_into_json(check_article(country, KEYS[count]), KEYS[count])


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    stop = time.perf_counter()

    print(f'Elapsed time: {round(stop - start, 2)} seconds')