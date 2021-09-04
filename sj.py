import requests
import os
from get_language_salary import get_language_salary


def get_vacancies_from_sj(language):
    url = "https://api.superjob.ru/2.0/vacancies/"
    page = 1

    params = {
        "town": "Москва",
        "keyword": f"Программист {language}",
        "count": 10,
        "page": page
    }
    headers = {
        "X-Api-App-Id": os.getenv("SJ_TOKEN")
    }

    response = requests.get(url, params=params, headers=headers)
    vacancies_found = response.json()['objects']
    debugged_api = response.json()
    response.raise_for_status()

    while debugged_api["more"]:
        page += 1
        params["page"] = page
        new_response = requests.get(url, params=params, headers=headers)
        debugged_api = new_response.json()
        response.raise_for_status()
    return vacancies_found, debugged_api


def process_vacancies_from_sj(vacancies, total_vacancies):
    vacancies_found = total_vacancies['total']
    vacancies_processed = len(vacancies)
    payments = []
    for vacancy in vacancies:
        payment_to = vacancy['payment_to']
        payment_from = vacancy['payment_from']
        average_salary_vacancy = get_language_salary([payment_to, payment_from])
        if average_salary_vacancy == 0:
            None
        else:
            payments.append(average_salary_vacancy)
    average_salary = get_language_salary(payments)
    process_vacancies = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": vacancies_processed,
        "average_salary": average_salary
    }
    return process_vacancies


def get_language_vacancies_sj(programming_languages):
    language_vacancies = {}
    for language in programming_languages:
        sj_vacancies = get_vacancies_from_sj(language)
        processed_vacancies = process_vacancies_from_sj(sj_vacancies[0], sj_vacancies[1])
        language_vacancies.update({language: processed_vacancies})
    return language_vacancies
