#!/usr/bin/python

FRANCE_KEYS = ['france ', 'french ', 'paris ', ' macron ', 'France ', 'French ', 'Paris ', 'Macron ']
EU_KEYS = [' european union ', ' brussels ', 'EU ', 'European Union ', 'Brussels ', 'EC ', ' eu ']
POLAND_KEYS = [' poland ', ' sejm ', ' polish ', ' warsaw ', ' duda ', 'Poland ', 'Polish ', 'Warsaw ', ' Duda ',
               'Morawiecki ']
GERMANY_KEYS = [' german ', ' germany ', ' berlin ', 'Merkel ', 'German ', 'Germany ', ' merkel ',
                'Berlin ', 'Scholz ', 'Bundestag ']
GB_KEYS = [' england ', ' english', ' gb ', ' ireland ', ' wales ', ' scotland ', ' british ', ' irish ',
           ' scottish ', ' welsh ', 'Great Britain', ' great britain ',
           ' london ', ' dublin ', 'England ', 'English ', 'GB ', 'Ireland ', 'Wales ', 'Scotland ', 'British ',
           'Irish ', ' tory ', ' commons ', 'Tory ', 'Tories ', ' tories ', 'Commons ', 'Westminster ',
           'Scottish ', 'Welsh ', 'London ', 'Dublin ']
# for the ukraine-russian war - we'll add ukraine stuff
RUSSIA_KEYS = [' moscow ', ' kremlin ', ' russia ', ' russian ', ' putin ', 'Moscow ', 'Kremlin ', 'Russia ',
               'Russian ', 'Putin ', 'Ukraine ', 'Ukrainian ', 'Kiev ', 'Crimea ', 'Donbas', 'Belarus ']
R_OF_EUROPE_KEYS = ['Norway', 'norway', 'Oslo', 'oslo', 'Norwegian', 'norwegian', ' Swedish ' ' swedish ', 'Sweden',
                    'sweden',
                    'Stockholm', 'Finland', ' Finnish ', ' Helsinki ', 'Belarus', 'Minsk', 'Estonia', 'Tallinn',
                    'Latvia',
                    ' Riga ', 'Lithuania', 'Vilnius', 'Moldova',
                    'Chisinau',
                    'Romania', 'Bucharest', 'Bulgaria', 'Greek', ' Greece ', ' Athens ', 'Macedonia', 'Skopje',
                    'Albania',
                    'Tirana', 'Kosovo', 'Montenegro', 'Bosnia', 'Herzegovina', 'Sarajevo', 'Serbia', 'Belgrade',
                    'Croatia', 'Zagreb', 'Hungary', 'Budapest', 'Hungarian', 'Austria', 'Vienna', 'Slovenia',
                    'Ljubljana', 'Slovakia', 'Bratislava', 'Czechia', 'Prague', 'Czech', 'Liechtenstein', 'Swiss',
                    'Switzerland', 'Zurich', ' Basel ', ' Bern ', ' Davos ', ' Italy ', ' Italian ', ' Rome ',
                    'Vatican',
                    ' Milan ',
                    ' Sicily ', ' Mafia ', ' Malta ', ' Maltese ', ' Spain ', ' Spanish ', ' Madrid ', 'Barcelona',
                    'Portugal',
                    'Portuguese', ' Lisbon ', 'Andorra', 'Monaco', ' Danish ', ' Denmark ', 'Copenhagen', 'Hague',
                    ' Dutch ', ' Holland ',
                    ' Netherlands', ' Belgium ', ' Amsterdam ', 'Armenia', 'Tbilisi', ' Iceland ', 'Rejkjavik']

def Check_Europe_Section(article):
    # note: the spaces here are deliberate

    countries = []

    for i in FRANCE_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('france')
            break
    for i in EU_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('eu')
            break
    for i in POLAND_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('poland')
            break
    for i in GERMANY_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('germany')
            break
    # i don't search the links here because some sites may have 'english' in the link
    # meaning the site language
    oops_pass = True
    for i in GB_KEYS:
        if i in article['title'] or i in article['text']:
            # unfortunately some hits may be articles that have nothing about the UK....
            # and LGBT articles as well since it has 'gb'
            oops_list = ['TVN24 News in English', 'English word', 'English language', 'LGBT', 'lgbt',
                         'English sentence', 'English phrase', 'tutored English', 'taught English', 'speak English',
                         'teach in English', 'English book', 'language is English', 'English word', 'English accent',
                         'News in English']
            for o in oops_list:
                if o in article['title'] or o in article['text']:
                    oops_pass = False
            if oops_pass:
                countries.append('gb')
                break

    for i in RUSSIA_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('russia')
            break
    for i in R_OF_EUROPE_KEYS:
        if i in article['title'] or i in article['text'] or i in article['link']:
            countries.append('rest of europe')
            break
        if i.lower() in article['title'] or i.lower() in article['text'] or i.lower() in article['link']:
            countries.append('rest of europe')
            break

    # because this stupid greek site keeps finding its way into sections it should not be in
    if 'ekathimerini' in article['link']:
        countries = ['rest of europe']

    # because of the threading, i need to return the article back as well
    for i in article['keywords']:
        i = i.lower()
        if len(i) < 3 and i != 'eu':
            article['keywords'].remove(i)

    return [article, countries]

