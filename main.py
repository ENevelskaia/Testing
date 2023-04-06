geo_logs = [
   {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def Russian_tours(List_):
    n = 0
    for dict in geo_logs[:]:
        if 'Россия' not in list(dict.values())[0]:
            del geo_logs[n]
            n -= 1
        n += 1
    return geo_logs


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_ids (ids):
    ids_new = []
    for id in ids.values():
        ids_new += id
    ids_unique = sorted(list(set(ids_new)))
    return (ids_unique)


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def max_stats(dict):
    max_stat = max(dict, key=dict.get)
    return max_stat

#Задание 2

import requests


token = 'y0_'
path = '/my_folder'
def create_folder(token, path):
    host = 'https://cloud-api.yandex.net/'
    uri = 'v1/disk/resources/'
    url = host + uri
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code
