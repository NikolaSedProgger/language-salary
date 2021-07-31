import requests
import os
from terminaltables import AsciiTable
import hh
import sj

def get_average_salary(salaries):
    Sum = 0
    for i in salaries:
        Sum = Sum + i
    salary = Sum / len(salaries)
    return int(salary)

def table(languages_dict, table_name):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    
    for language in PROGRAMMING_LANGUAGES:        
        table_data.append([language, languages_dict[language]['vacancies_found'], languages_dict[language]['vacancies_processed'], languages_dict[language]['average_salary']])
    table = AsciiTable(table_data, table_name)
    print(table.table)

if __name__ == "__main__":
    PROGRAMMING_LANGUAGES = [
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

    table(hh.get_languages_vacancies_for_hh(PROGRAMMING_LANGUAGES), "HeadHunter Moscow")
    table(sj.get_languages_vacancies_for_sj(sj_token, PROGRAMMING_LANGUAGES), "SuperJob Moscow")