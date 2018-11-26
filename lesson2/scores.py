def mean(l):
    return int(sum(l)/len(l))


school_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
     {'school_class': '11a', 'scores': [2, 3, 2, 3, 3]},
     {'school_class': '10a', 'scores': [5, 5, 4, 4, 3]},
     {'school_class': '9a', 'scores': [2, 3, 4, 5, 3]}]

scores_list = []

for item in school_list:
    print('Класс: {} Среднее: {}'.format(item['school_class'], mean(item['scores'])))
    for score in item['scores']:
        scores_list.append(score)

print('Среднее по школе: {}'.format(mean(scores_list)))
