from src.api_class import Vacancy
from src.get_save_json import GetVacancy, DataJson, HeadHunter


def main():
    user_input = input('Введите ключевое слово для получения вакансии с сервиса Head Hunter\n\n')
    head_hunt = HeadHunter('https://api.hh.ru/vacancies', user_input)
    data_head_hunt = head_hunt.get_response_head_hunt()
    response_from_head_hund = DataJson(data_head_hunt)
    response_from_head_hund.save_json()
    sorted_vacancies = GetVacancy('data.json')
    obj_class_vacancy = sorted_vacancies.get_vacancy_from_json()
    for vacancy in obj_class_vacancy:
        print(f'Вакансия: {vacancy.get_name()}\nТребования: {vacancy.get_requirement()}\n{vacancy.roles}\n'
              f'Опыт: {vacancy.get_experience()}'
              f'Зарплата: {vacancy.get_salary()}\nСсылка на вакансию: {vacancy.get_url()}\n\n\n')


if __name__ == '__main__':
    main()
