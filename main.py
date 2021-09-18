import requests
import os
from terminaltables import AsciiTable
import hh
import sj

def сreate_table(programming_language, table_name):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language in programming_languages:
        vacancies = programming_language[language].items()
        table_data.append([language, vacancies[0], vacancies[1], vacancies[2]])
    table = AsciiTable(table_data, table_name)
    return table.table

if __name__ == "__main__":
    sj_token = os.getenv("SJ_TOKEN")
    programming_languages = [
        'JavaScript',
        'Java',
        'Python',
        'Ruby',
        'PHP',
        'C++',
        'C#',
        'C',
        'Go',
        'Objective-C',
        'Scala',
        'Swift',
        'Typescript'
        ]
    sj_token = os.getenv("KEY")

    print(сreate_table(hh.get_language_vacancies_hh(programming_languages), "HeadHunter Moscow"))
    print(сreate_table(sj.get_language_vacancies_sj(programming_languages, sj_token), "SuperJob Moscow"))
