import json
from abc import ABC, abstractmethod
from src.api_class import Vacancy
import requests


# class FileJson(ABC):
#
#     @abstractmethod
#     def get_json(self):
#         pass
#
#     @abstractmethod
#     def save_json(self):
#         pass
#
#     @abstractmethod
#     def repackaging(self):
#         pass


class DataJson:

    def __init__(self, file_json):
        self.file_json = file_json

    def save_json(self):
        list_vacancy = []
        for i in self.file_json['items']:
            repackaging = {'name': i['name'], 'salary': i['salary'], 'experience': i['experience']['name'],
                           'roles': i['snippet']['responsibility'],
                           'requirement': i['snippet']['requirement']}
            list_vacancy.append(repackaging)
        with open('data.json', 'w') as file:
            json.dump(list_vacancy, file)

    # def repackaging(self):
    #
    #         return list_vacancy


class GetVacancy:
    def __init__(self, file_name):
        self.file_json = file_name

    def get_vacancy(self):
        with open(self.file_json) as file:
            new_vacancy = json.load(file)
            return new_vacancy


class HeadHunter:

    def __init__(self, url, key_word):
        self.key_word = key_word
        self.url = url

    def vacancy(self):
        res = requests.get(self.url, params={'text': self.key_word})
        data = res.json()
        return data


def func(asd):
    for i in asd:
        return Vacancy(**i)


head_hunt = HeadHunter('https://api.hh.ru/vacancies', 'backend')
data_head_hunt = head_hunt.vacancy()
kuku = DataJson(data_head_hunt)
kuku.save_json()
loli = GetVacancy('data.json')
popi = loli.get_vacancy()

for i in popi:
    fafa = Vacancy(**i)
    print(fafa.get_requirement())
