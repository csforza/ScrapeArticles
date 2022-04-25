#!/usr/bin/python
from operator import itemgetter


# sorts all the groups of similar articles
# first by grabbing all articles that are similar to one another into a big group
# removing duplicates from the groups
# then ranking the entire list of groups by the length of each group
# then sorts the articles in each group by increasing subjectivity
def sort_and_rank(lists):
    for j in lists:
        if lists.count(j) > 1:
            lists.remove(j)

    # new_list = sorted(list_of_similar_groups, key=len, reverse=True)
    # finished_list = [sorted(item, key=itemgetter('subjectivity')) for item in new_list]

    lists2 = lists.copy()
    finished_list = []
    for i in lists:
        new_list = []
        for j in lists2:
            if i == j:
                pass
            else:
                if not new_list:
                    new_list = sort_list(i, j)
                else:
                    new_list = sort_list(new_list, j)
                    new_list = sorted(new_list, key=itemgetter('subjectivity'))  # must see which direction first
        # to filter out the same articles but might appear more than once from the same news source
        # reversed so that the more subjective articles get removed first
        for k in reversed(new_list):
            counter = 0
            if len([counter for elem in new_list if k['title'] in elem.values()]) > 1:
                new_list.remove(k)
        finished_list.append(new_list)

        for k in finished_list:
            if finished_list.count(k) > 1:
                finished_list.remove(k)

    # orders the list of article groups by the number of articles in each group
    # the group with the most articles will be first and therefore get the headline
    finished_list = sorted(finished_list, key=len, reverse=True)

    return finished_list


def sort_list(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3 = list1 + list2
            break
    if not list3:
        return list1
    else:
        list4 = sorted(list3, key=itemgetter('title'))
        for j in list4:
            if list4.count(j) > 1:
                list4.remove(j)
        return list4


if __name__ == '__main__':
    import json

    with open("1.json") as json_file1:
        data1 = json.load(json_file1)

    with open("2.json") as json_file2:
        data2 = json.load(json_file2)

    with open("3.json") as json_file3:
        data3 = json.load(json_file3)

    with open("4.json") as json_file4:
        data4 = json.load(json_file4)

    with open("5.json") as json_file5:
        data5 = json.load(json_file5)

    with open("6.json") as json_file6:
        data6 = json.load(json_file6)

    with open("7.json") as json_file7:
        data7 = json.load(json_file7)

    list_all = [data1, data2, data3, data4, data5, data6, data7]
    list_to_test = []
    for li in list_all:
        new_list = []
        for i, j in li.items():
            new_list.append(j)
        list_to_test.append(new_list)

    # print(list_to_test)

    x = sort_and_rank(list_to_test)

    count = 8
    for y in x:
        articles_dict = {}
        for b in y:
            try:
                articles_dict[b['title']] = b
            except:
                continue
        with open(f"{str(count)}.json",
                  "w") as outfile:
            json.dump(articles_dict, outfile, indent=4)
        count += 1
