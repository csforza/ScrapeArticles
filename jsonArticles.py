#!/usr/bin/python
import json


# so far I have decided to do each one individually despite some sections doing exactly the same thing
# this way in case an individual section needs modification I can modify without affecting the rest
def europe_all(ranked_articles):
    with open('resources/test_results/EuropeResults.txt', 'w') as file2:
        for i in ranked_articles[:30]:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    europe_topic_json = {}
    europe_main_headline_json = {}
    europe_sub_headline_json = {}

    europe_main_headline_to_json_list = [m for m in ranked_articles[0][:5]]

    europe_sub_headline_to_json_list = [m for group in ranked_articles[1:4] for m in group[:3]]
    europe_topic_to_json_list = [groups[0] for groups in ranked_articles[4:20]]

    for euta in europe_topic_to_json_list:
        europe_topic_json[euta['title']] = euta

    for euha in europe_main_headline_to_json_list:
        europe_main_headline_json[euha['title']] = euha

    for euha in europe_sub_headline_to_json_list:
        europe_sub_headline_json[euha['title']] = euha

    with open("resources/json_results/EuropeTopic1.json", "w") as outfile:
        json.dump(europe_topic_json, outfile, indent=4)

    with open("resources/json_results/EuropeMainHeadline.json", "w") as outfile:
        json.dump(europe_main_headline_json, outfile, indent=4)

    with open("resources/json_results/EuropeSubHeadline.json", "w") as outfile:
        json.dump(europe_sub_headline_json, outfile, indent=4)


def france(france_ranked):
    with open('resources/test_results/TestFranceResults.txt', 'w') as file2:
        for i in france_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    france_topic_json = {}
    france_headline_json = {}

    france_headline_to_json_list = [b for france_1 in france_ranked[:3] for b in france_1[:3]]
    france_topic_to_json_list = [france_2[0] for france_2 in france_ranked[3:17] if len(france_2) > 1]

    for fta in france_topic_to_json_list:
        france_topic_json[fta['title']] = fta

    for fha in france_headline_to_json_list:
        france_headline_json[fha['title']] = fha

    with open("resources/json_results/FranceTopic.json", "w") as outfile:
        json.dump(france_topic_json, outfile, indent=4)

    with open("resources/json_results/FranceHeadline.json","w") as outfile:
        json.dump(france_headline_json, outfile, indent=4)


def poland(poland_ranked):
    with open('resources/test_results/TestPolandResults.txt', 'w') as file2:
        for i in poland_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    poland_topic_json = {}
    poland_headline_json = {}

    poland_headline_to_json_list = [c for poland_1 in poland_ranked[:2] for c in poland_1[:3]]
    poland_topic_to_json_list = [poland_2[0] for poland_2 in poland_ranked[2:16] if len(poland_2) > 1]

    for pta in poland_topic_to_json_list:
        poland_topic_json[pta['title']] = pta

    for pha in poland_headline_to_json_list:
        poland_headline_json[pha['title']] = pha

    with open("resources/json_results/PolandTopic.json", "w") as outfile:
        json.dump(poland_topic_json, outfile, indent=4)

    with open("resources/json_results/PolandHeadline.json", "w") as outfile:
        json.dump(poland_headline_json, outfile, indent=4)


def germany(germany_ranked):
    with open('resources/test_results/TestGermanyResults.txt',
              'w') as file2:
        for i in germany_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    germany_topic_json = {}
    germany_headline_json = {}

    germany_headline_to_json_list = [d for germany_1 in germany_ranked[:3] for d in germany_1[:3]]
    germany_topic_to_json_list = [germany_2[0] for germany_2 in germany_ranked[3:17] if len(germany_2) > 1]

    for gta in germany_topic_to_json_list:
        germany_topic_json[gta['title']] = gta

    for gha in germany_headline_to_json_list:
        germany_headline_json[gha['title']] = gha

    with open("resources/json_results/GermanyTopic.json", "w") as outfile:
        json.dump(germany_topic_json, outfile, indent=4)

    with open( "resources/json_results/GermanyHeadline.json", "w") as outfile:
        json.dump(germany_headline_json, outfile, indent=4)


def russia(russia_ranked):
    with open('resources/test_results/TestRussiaResults.txt',
              'w') as file2:
        for i in russia_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    russia_topic_json = {}
    russia_headline_json = {}

    russia_headline_to_json_list = [e for russia_1 in russia_ranked[:3] for e in russia_1[:3]]
    russia_topic_to_json_list = [russia_2[0] for russia_2 in russia_ranked[3:17] if len(russia_2) > 1]

    for rta in russia_topic_to_json_list:
        russia_topic_json[rta['title']] = rta

    for rha in russia_headline_to_json_list:
        russia_headline_json[rha['title']] = rha

    with open("resources/json_results/RussiaTopic.json", "w") as outfile:
        json.dump(russia_topic_json, outfile, indent=4)

    with open("resources/json_results/RussiaHeadline.json", "w") as outfile:
        json.dump(russia_headline_json, outfile, indent=4)


def gb(gb_ranked):
    with open('resources/test_results/TestGBResults.txt',
              'w') as file2:
        for i in gb_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    gb_topic_json = {}
    gb_headline_json = {}

    gb_headline_to_json_list = [f for gb_1 in gb_ranked[:3] for f in gb_1[:3]]
    gb_topic_to_json_list = [gb_2[0] for gb_2 in gb_ranked[3:17] if len(gb_2) > 1]

    for gbta in gb_topic_to_json_list:
        gb_topic_json[gbta['title']] = gbta

    for gbha in gb_headline_to_json_list:
        gb_headline_json[gbha['title']] = gbha

    with open("resources/json_results/GBTopic.json","w") as outfile:
        json.dump(gb_topic_json, outfile, indent=4)

    with open("resources/json_results/GBHeadline.json", "w") as outfile:
        json.dump(gb_headline_json, outfile, indent=4)


def eu(eu_ranked):
    with open('resources/test_results/TestEUResults.txt',
              'w') as file2:
        for i in eu_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    eu_topic_json = {}
    eu_headline_json = {}

    eu_headline_to_json_list = [g for eu_1 in eu_ranked[:3] for g in eu_1[:3]]
    eu_topic_to_json_list = [eu_2[0] for eu_2 in eu_ranked[3:17] if len(eu_2) > 1]

    for euta in eu_topic_to_json_list:
        eu_topic_json[euta['title']] = euta

    for euha in eu_headline_to_json_list:
        eu_headline_json[euha['title']] = euha

    with open("resources/json_results/EUTopic.json", "w") as outfile:
        json.dump(eu_topic_json, outfile, indent=4)

    with open("resources/json_results/EUHeadline.json", "w") as outfile:
        json.dump(eu_headline_json, outfile, indent=4)


def roe(r_of_europe_ranked):
    with open('resources/test_results/TestRestEuropeResults.txt',
              'w') as file2:
        for i in r_of_europe_ranked:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    r_of_europe_topic_json = {}
    r_of_europe_headline_json = {}

    r_of_europe_headline_to_json_list = [h for r_of_europe_1 in r_of_europe_ranked[:3] for h in r_of_europe_1[:3]]
    r_of_europe_topic_to_json_list = [r_of_europe_2[0] for r_of_europe_2 in r_of_europe_ranked[3:17] if len(r_of_europe_2) > 1]

    for roeta in r_of_europe_topic_to_json_list:
        r_of_europe_topic_json[roeta['title']] = roeta

    for roeha in r_of_europe_headline_to_json_list:
        r_of_europe_headline_json[roeha['title']] = roeha

    with open("resources/json_results/RestOfEuropeTopic.json", "w") as outfile:
        json.dump(r_of_europe_topic_json, outfile, indent=4)

    with open("resources/json_results/RestOfEuropeHeadline.json", "w") as outfile:
        json.dump(r_of_europe_headline_json, outfile, indent=4)


def usa(ranked_articles):
    with open('resources/test_results/USAResults.txt',
              'w') as file2:
        for i in ranked_articles:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    usa_topic_json = {}
    usa_headline_json = {}

    usa_headline_to_json_list = [n for group1 in ranked_articles[:4] for n in group1[:3]]
    usa_topic_to_json_list = [groups1[0] for groups1 in ranked_articles[4:20] if len(groups1) > 1]

    for usata in usa_topic_to_json_list:
        usa_topic_json[usata['title']] = usata

    for usaha in usa_headline_to_json_list:
        usa_headline_json[usaha['title']] = usaha

    with open("resources/json_results/USATopic.json", "w") as outfile:
        json.dump(usa_topic_json, outfile, indent=4)

    with open("resources/json_results/USAHeadline.json", "w") as outfile:
        json.dump(usa_headline_json, outfile, indent=4)


def world(ranked_articles):
    with open('resources/test_results/WorldResults.txt',
              'w') as file2:
        for i in ranked_articles:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    world_topic_json = {}
    world_headline_json = {}

    world_headline_to_json_list = [o for group4 in ranked_articles[:3] for o in group4[:3]]
    world_topic_to_json_list = [groups4[0] for groups4 in ranked_articles[3:19] if len(groups4) > 1]

    for wta in world_topic_to_json_list:
        world_topic_json[wta['title']] = wta

    for wha in world_headline_to_json_list:
        world_headline_json[wha['title']] = wha

    with open("resources/json_results/WorldTopic.json", "w") as outfile:
        json.dump(world_topic_json, outfile, indent=4)

    with open("resources/json_results/WorldHeadline.json", "w") as outfile:
        json.dump(world_headline_json, outfile, indent=4)


def me(ranked_articles):
    with open('resources/test_results/MEResults.txt',
              'w') as file2:
        for i in ranked_articles:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    me_topic_json = {}
    me_headline_json = {}

    me_headline_to_json_list = [o for group2 in ranked_articles[:3] for o in group2[:3]]
    me_topic_to_json_list = [groups2[0] for groups2 in ranked_articles[3:19] if len(groups2) > 1]

    for meta in me_topic_to_json_list:
        me_topic_json[meta['title']] = meta

    for meha in me_headline_to_json_list:
        me_headline_json[meha['title']] = meha

    with open("resources/json_results/MiddleEastTopic.json", "w") as outfile:
        json.dump(me_topic_json, outfile, indent=4)

    with open("resources/json_results/MiddleEastHeadline.json", "w") as outfile:
        json.dump(me_headline_json, outfile, indent=4)


def americas(ranked_articles):
    with open('resources/test_results/AmericaResults.txt',
              'w') as file2:
        for i in ranked_articles:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    americas_topic_json = {}
    americas_headline_json = {}

    americas_headline_to_json_list = [p for group3 in ranked_articles[:2] for p in group3[:3]]
    americas_topic_to_json_list = [groups3[0] for groups3 in ranked_articles[2:15] if len(groups3) > 1]

    for ata in americas_topic_to_json_list:
        americas_topic_json[ata['title']] = ata

    for aha in americas_headline_to_json_list:
        americas_headline_json[aha['title']] = aha

    with open("resources/json_results/AmericasTopic.json", "w") as outfile:
        json.dump(americas_topic_json, outfile, indent=4)

    with open("resources/json_results/AmericasHeadline.json", "w") as outfile:
        json.dump(americas_headline_json, outfile, indent=4)


def tech(ranked_articles):

    with open('resources/test_results/TechResults.txt',
              'w') as file2:
        for i in ranked_articles:
            for j in i:
                file2.write(str(j))
                file2.write('\n')
            file2.write('\n')
        file2.write('\n')
        file2.close()

    tech_json = {}

    tech_to_json_list = []
    for t in reversed(ranked_articles[:15]):
        # if the article is already in the database -> next one in the group
        y = 0
        while True:
            checked = True
            # this try block in case we go past the list index
            try:
                test = t[y]
            except:
                break
            if t[y] in tech_to_json_list:
                y += 1
                checked = False
            if checked:
                tech_to_json_list.append(t[y])
                break

    for ta in tech_to_json_list:
        tech_json[ta['title']] = ta

    with open("resources/json_results/Tech.json", "w") as outfile:
        json.dump(tech_json, outfile, indent=4)


# pulls all the article groupings and puts them into json files, ready to be delivered to my website
def results_into_json(groups_of_articles, key):
    print(f'Length of {key}: {len(groups_of_articles)}')

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

