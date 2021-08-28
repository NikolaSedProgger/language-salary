import requests
import os
from terminaltables import AsciiTable
import hh
import sj

def сreate_table(languages_dict, table_name):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language in programming_languages:
        vacancies_found = languages_dict[language]['vacancies_found']
        vacancies_processed = languages_dict[language]['vacancies_processed']
        average_salary = languages_dict[language]['average_salary']
        table_data.append([language, vacancies_found, vacancies_processed, average_salary])
    table = AsciiTable(table_data, table_name)
    return table.table

if __name__ == "__main__":
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
    print(сreate_table(sj.get_language_vacancies_sj(programming_languages), "SuperJob Moscow"))
