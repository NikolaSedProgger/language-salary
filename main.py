import requests
import os
from terminaltables import AsciiTable
import hh
import sj


def get_language_salary(average_salaries):
    salaries = []
    for salary in average_salaries:
        if salary['from'] or salary["payment_from"]:
            salaries.append(salary['to'] or salary["payment_to"] * 0.8)
        elif salary['to'] or salary["payment_to"] == None:
            salaries.append(salary['from'] or salary["payment_from"] * 1.2)
    return(int(sum(salaries) / len(salaries)))


def table(languages_dict, table_name):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language in programming_languages:
        vacancies_found = languages_dict[language]['vacancies_found']
        vacancies_processed = languages_dict[language]['vacancies_processed']
        average_salary = languages_dict[language]['average_salary']
        table_data.append([language, vacancies_found, vacancies_processed, average_salary])
    table = AsciiTable(table_data, table_name)
    print(table.table)

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

    table(hh.get_language_vacancies_hh(programming_languages), "HeadHunter Moscow")
    table(sj.get_language_vacancies_sj(programming_languages), "SuperJob Moscow")
