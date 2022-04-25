import json


# so far I have decided to do each one individually despite some sections doing exactly the same thing
# this way in case an individual section needs modification I can modify without affecting the rest

def europe_all(groups):
    pass


def france(groups):
    pass


def poland(groups):
    pass


def germany(groups):
    pass


def russia(groups):
    pass


def gb(groups):
    pass


def eu(groups):
    pass


def roe(groups):
    pass


def usa(groups):
    pass


def world(groups):
    pass


def me(groups):
    pass


def americas(groups):
    pass


def tech(groups):
    pass


# pulls all the article groupings and puts them into json files, ready to be delivered to my website
def results_into_json(groups_of_articles, key):
    if key == 'europe':
        europe_all(groups_of_articles)
    if key == 'france':
        france(groups_of_articles)
    if key == 'poland':
        poland(groups_of_articles)
    if key == 'russia':
        russia(groups_of_articles)
    if key == 'germany':
        germany(groups_of_articles)
    if key == 'gb':
        gb(groups_of_articles)
    if key == 'eu':
        eu(groups_of_articles)
    if key == 'rest_of_europe':
        roe(groups_of_articles)
    if key == 'usa':
        usa(groups_of_articles)
    if key == 'world':
        world(groups_of_articles)
    if key == 'middle_east':
        me(groups_of_articles)
    if key == 'americas':
        americas(groups_of_articles)
    if key == 'tech':
        tech(groups_of_articles)
