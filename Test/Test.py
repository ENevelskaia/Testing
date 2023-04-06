from unittest import TestCase

import pytest

from _pytest import unittest

from main import Russian_tours, unique_ids, max_stats

@pytest.mark.parametrize("dict, expected",
                        [({'user1': [213, 213, 213, 15, 213],
                           'user2': [54, 54, 119, 119, 119],
                           'user3': [213, 98, 98, 35]}, [15, 35, 54, 98, 119, 213]),
                         ({'Kevin': [66,10,12],
                           'Leila': [66,12,17,17]}, [10,12,17,66])]
                        )
def test_unique_ids(dict,expected):
    result = unique_ids(dict)
    assert result == expected

@pytest.mark.parametrize("dict, expected",
                        [({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
                        ({'Parma': 15, 'Uventus': 19}, 'Uventus'),
                        ({'John': 15, 'Anna': 19, 'Glory': 25}, 'Glory')]
                        )
def test_with_params(dict, expected):
    result = max_stats(dict)
    assert result == expected

class Test_Rus_tour(TestCase):
    def test_1(self):
        List_ = [
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
        result = Russian_tours(List_)
        expected = [
                    {'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}
                  ]
        self.assertListEqual(result, expected)


# Задание 2

from main import create_folder, token, path

class Test_Create_folder(TestCase):
    def test_create_folder(self):
        result = create_folder(token, path)
        expected = 201
        self.assertEqual(result, expected)

    def test_folder_exists(self):
        result = create_folder(token, path)
        expected = 409
        self.assertEqual(result, expected)
