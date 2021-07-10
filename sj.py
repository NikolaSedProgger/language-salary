import requests
import os
from main import get_average_salary

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

def get_vacancies_from_sj(language):
    secret_key = os.getenv("KEY")
    url = "https://api.superjob.ru/2.0/vacancies/"

    params = {
        "town": "Москва",
        "keyword": f"Программист {language}",
        "count":100
    }
    headers = {
        "X-Api-App-Id": "v3.r.133318714.f70e6d4022872fb93a542e0aad893270e9bc0e95.2e9144ce232372ab5fb95b959f47528aa754271c"
    }

    response = requests.get(url, params=params, headers=headers)
    vacancies_found = response.json()['objects']
    debugged_api = response.json()

    return vacancies_found, debugged_api

def process_vacancies_from_sj(language_vacancies_list, vacancies_dict):
    #Вакансий найдено (всего)
    vacancies_found = vacancies_dict['total']
    
    #Вакансий обработано
    vacancies_processed = len(language_vacancies_list)
    
    #Приблизительная зарплата
    payments = [] 
    for vacancy in language_vacancies_list:
        average_salary_vacancy = get_average_salary([vacancy['payment_to'], vacancy['payment_from']]) 
        if average_salary_vacancy == 0:
            None
        else:
            payments.append(average_salary_vacancy)
    average_salary = get_average_salary(payments)
    
    #Итоговый результат (dict)
    process_vacancies = {"vacancies_found":vacancies_found, "vacancies_processed":vacancies_processed, "average_salary":average_salary}
    return process_vacancies

def get_languages_dict_for_sj():
    language_dict = {}
    for language in PROGRAMMING_LANGUAGES:
        language_dict.update({language:process_vacancies_from_sj(get_vacancies_from_sj(language)[0],get_vacancies_from_sj(language)[1])})
    return language_dict



