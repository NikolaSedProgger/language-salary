import requests
import os
from main import get_language_salary

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


def process_vacancies_from_sj(vacancies, vacancies_dict):
    vacancies_found = vacancies_dict['total']
    vacancies_processed = len(vacancies)
    payments = []
    for vacancy in vacancies:
        average_salary_vacancy = get_language_salary([vacancy['payment_to'], vacancy['payment_from']])
        if average_salary_vacancy == 0:
            None
        else:
            payments.append(average_salary_vacancy)
    average_salary = get_language_salary(payments)
    process_vacancies = {"vacancies_found": vacancies_found, "vacancies_processed": vacancies_processed, "average_salary": average_salary}
    return process_vacancies


def get_language_vacancies_for_sj(programming_languages):
    language_vacancies = {}
    for language in programming_languages:
        processed_vacancies = process_vacancies_from_sj(get_vacancies_from_sj(language)[0], get_vacancies_from_sj(language)[1])
        language_vacancies.update({language: processed_vacancies})
    return language_vacancies
