from datetime import datetime, timedelta

TWO_DAYS_AGO_DATE = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")


def append_google_feeds(countries):
    return_list = []
    for country in countries:
        if ' ' in country:
            country = country.replace(' ', '+')
        return_list.append(
            f'https://news.google.com/rss/search?q={country}+-sports+after:{TWO_DAYS_AGO_DATE}&hl=en-US&gl=US&ceid=US:en'
        )
    return return_list


def grab_feeds():
    with open('resources/feeds/EuropeNewsFeed.txt', 'r') as file1:
        europe_feeds = file1.read().splitlines()

    with open('resources/feeds/USANewsFeeds.txt', 'r') as file2:
        usa_feeds = file2.read().splitlines()

    with open('resources/feeds/WorldNewsFeeds.txt', 'r') as file3:
        world_feeds = file3.read().splitlines()

    with open('resources/feeds/MiddleeastFeed.txt', 'r') as file4:
        me_feeds = file4.read().splitlines()

    with open('resources/feeds/AmericasFeeds.txt', 'r') as file5:
        americas_feeds = file5.read().splitlines()

    with open('resources/feeds/TechFeeds.txt', 'r') as file6:
        tech_feeds = file6.read().splitlines()

    # countries (or tech topics) list for Google rss feeds
    europe_countries = ['france', 'European Union', 'poland', 'germany', 'england', 'ireland', 'scotland', 'russia',
                        'Norway', 'Sweden', 'Finland', 'Belarus', 'Estonia', 'Latvia', 'Lithuania', 'Ukraine',
                        'Moldova',
                        'Romania', 'Bulgaria', 'Greece', 'North Macedonia', 'Albania', 'Kosovo', 'Montenegro', 'Bosnia',
                        'Serbia', 'Croatia', 'Hungary', 'Austria', 'Slovenia', 'Slovakia', 'Czechia', 'Switzerland',
                        'Italy', 'Rome', 'Vatican', 'Spain', 'Portugal', 'Denmark', 'Netherlands', 'Belgium', 'Armenia',
                        'Iceland', 'georgia tbilisi']
    americas_countries = ['Mexico', 'Peru', 'Brazil', 'Columbia', 'Argentina', 'Chile', 'Venezuela', 'Bolivia',
                          'Ecuador',
                          'Panama', 'Uruguay', 'Paraguay', 'Nicaragua', 'Honduras', 'el salvador', 'cuba', 'guatemala',
                          'canada']
    me_countries = ['Israel', 'iran', 'Saudi arabia', 'Egypt', 'Turkey', 'Iraq', 'Syria', 'Jordan', 'Yemen',
                    'oman', 'united arab emirates', 'bahrain', 'kuwait', 'azerbaijan', 'lebanon', 'qatar',
                    'afghanistan',
                    'OPEC']
    world_countries = ['china', 'japan', 'india', 'north korea', 'south korea', 'myanmar', 'cambodia', 'vietnam',
                       'thailand', 'indonesia', 'pakistan', 'kazakhstan', 'turkmenistan', 'mongolia', 'uzbekistan',
                       'bangladesh', 'sri lanka', 'malaysia', 'taiwan', 'hong kong', 'philippines', 'algeria',
                       'tunisia', 'nigeria', 'australia', 'new zealand', 'cameroon', 'ghana', 'ethiopia',
                       'sudan', 'libya', 'south africa', 'zimbabwe', 'angola', 'ivory coast', 'liberia', 'morocco',
                       'tanzania', 'kenya', 'central african republic', 'democratic republic of the congo', 'mali',
                       'niger', 'senegal']
    # variable name not quite appropriate, but makes things easy
    tech_countries = ['vulnerability remote code execution', 'windows critical flaw', 'russian hackers',
                      'poc vulnerability', 'cryptocurrency', 'crypto mining', 'bitcoin', 'ethereum', 'apple software',
                      'vulnerability security patch', 'hacker malware', 'microsoft vulnerability', 'cyber attack',
                      'ransomware', 'hacker group', 'ransomware group', 'blockchain', 'crypto currencies',
                      'cryptocurrency investing', 'linux security', 'windows security', 'vulnerability site:medium.com',
                      'windows exploit site:medium.com', 'malware site:medium.com', 'hacker site:medium.com']
    usa_countries = ['white house', 'joe biden', 'donald trump', 'congress', 'usa defense', 'usa senate']

    # now add the Google News feeds to the feeds we have already
    to_append = [(europe_countries, europe_feeds), (usa_countries, usa_feeds), (world_countries, world_feeds),
                 (me_countries, me_feeds), (americas_countries, americas_feeds), (tech_countries, tech_feeds)]
    for x, y in to_append:
        y.extend(append_google_feeds(x))

    return [europe_feeds, usa_feeds, world_feeds, me_feeds, americas_feeds, tech_feeds]
