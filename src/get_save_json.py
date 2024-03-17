import json
from abc import ABC, abstractmethod
from src.api_class import Vacancy
import requests


class DataJson:

    def __init__(self, file_json):
        self.file_json = file_json

    def save_json(self):
        list_vacancy = []
        for i in self.file_json['items']:
            repackaging = {'name': i['name'], 'salary': i['salary'], 'experience': i['experience']['name'],
                           'roles': i['snippet']['responsibility'],
                           'requirement': i['snippet']['requirement'],
                           'url': i['alternate_url']}
            list_vacancy.append(repackaging)
        with open('data.json', 'w') as file:
            json.dump(list_vacancy, file)


class GetVacancy:
    def __init__(self, file_name):
        self.file_json = file_name

    def get_vacancy_from_json(self):
        with open(self.file_json) as file:
            new_vacancy = json.load(file)
            dict_new_vacancy = []
            for vacancy in new_vacancy:
                dict_new_vacancy.append(Vacancy(**vacancy))
        return dict_new_vacancy


class HeadHunter:

    def __init__(self, url, key_word):
        self.key_word = key_word
        self.url = url

    def get_response_head_hunt(self):
        res = requests.get(self.url, params={'text': self.key_word})
        data = res.json()
        if len(data['items']) == 0:
            print('По запросу не нашлось вакансий')
        return data


