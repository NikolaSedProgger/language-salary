import requests
import os
from get_language_salary import get_language_salary

def get_vacancies_from_sj(language,sj_token):
    url = "https://api.superjob.ru/2.0/vacancies/"
    page = 1

    params = {
        "town": "Москва",
        "keyword": f"Программист {language}",
        "count": 10,
        "page": page
    }
    headers = {
        "X-Api-App-Id": sj_token
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    debugged_api = response.json()
    vacancies_found = debugged_api['objects']
    
    while debugged_api["more"]:
        page += 1
        params["page"] = page
        new_response = requests.get(url, params=params, headers=headers)
        new_response.raise_for_status()
        vacancies = []
        vacancies.extend(new_response.json()['objects'])
        debugged_api = new_response.json()

    return vacancies_found, vacancies


def process_vacancies_from_sj(vacancies, total_vacancies):
    vacancies_found = total_vacancies['total']
    vacancies_processed = len(vacancies)
    payments = []
    for vacancy in vacancies:
        payment_to = vacancy['payment_to']
        payment_from = vacancy['payment_from']
        average_salary_vacancy = get_language_salary(payment_from, payment_to)
        if average_salary_vacancy:
            payments.append(average_salary_vacancy)
    average_salary = get_language_salary(payments)
    process_vacancies = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return process_vacancies


def get_language_vacancies_sj(programming_languages, sj_token):
    language_vacancies = {}
    for language in programming_languages:
        vacancies_found = 0
        debugged_api = 1
        sj_vacancies = get_vacancies_from_sj(language, sj_token)
        processed_vacancies = process_vacancies_from_sj(sj_vacancies[vacancies_found], sj_vacancies[debugged_api])
        language_vacancies.update({language: processed_vacancies})
    return language_vacancies
