import requests
import os
from main import get_average_salary


def get_vacancies_from_sj(language, token):
    url = "https://api.superjob.ru/2.0/vacancies/"
    count = 1

    params = {
        "town": "Москва",
        "keyword": f"Программист {language}",
        "count": count
    }
    headers = {
        "X-Api-App-Id": token
    }

    response = requests.get(url, params=params, headers=headers)
    vacancies_found = response.json()['objects']
    debugged_api = response.json()

    while debugged_api["more"]:
        count += 1
        params["count"] = count
        new_response = requests.get(url, params=params, headers=headers)
        debugged_api = new_response.json()

    return vacancies_found, debugged_api


def process_vacancies_from_sj(vacancies, vacancies_dict):
    vacancies_found = vacancies_dict['total']
    vacancies_processed = len(vacancies)
    payments = []
    for vacancy in vacancies:
        average_salary_vacancy = get_average_salary([vacancy['payment_to'], vacancy['payment_from']])
        if average_salary_vacancy == 0:
            None
        else:
            payments.append(average_salary_vacancy)
    average_salary = get_average_salary(payments)
    process_vacancies = {"vacancies_found": vacancies_found, "vacancies_processed": vacancies_processed, "average_salary": average_salary}
    return process_vacancies


def get_languages_vacancies_for_sj(token, programming_languages):
    language_vacancies = {}
    for language in programming_languages:
        language_vacancies.update({language: process_vacancies_from_sj(get_vacancies_from_sj(language, token)[0], get_vacancies_from_sj(language, token)[1])})
    return language_vacancies
