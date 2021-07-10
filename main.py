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
    secret_key = os.getenv("KEY")
    headers = {
        "X-Api-App-Id": "v3.r.133318714.f70e6d4022872fb93a542e0aad893270e9bc0e95.2e9144ce232372ab5fb95b959f47528aa754271c"
    }
    params = {
        "town": "Москва",
        "keyword": "Программист Python"
    }    

    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=params)

    table(hh.get_languages_dict_for_hh(), "HeadHunter Moscow")
    table(sj.get_languages_dict_for_sj(), "SuperJob Moscow")