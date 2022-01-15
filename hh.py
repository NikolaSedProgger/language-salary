import json
import requests
from get_language_salary import get_language_salary


def get_found_vacancies(language):
    url = "https://api.hh.ru/vacancies/"
    town_id = 1
    days_period = 30
    params = {
        "text": f"Программист {language}",
        "area": town_id,
        "period": days_period,
    }
    found_vacancies = []
    page = 0
    pages = 100

    while page < pages:
        params["page"] = page

        response = requests.get(url, params=params)
        response.raise_for_status()
        page += 1
        response_content = response.json()
        pages = response_content["pages"]
        response.raise_for_status()
        found_vacancies.extend(response_content["items"])
    return found_vacancies


def get_vacancies_average_salaries(vacancies):
    vacancies_salaries = []

    for vacancy in vacancies:
        currency = vacancy["salary"]["currency"]
        if vacancy["salary"]:
            if currency == "RUR":
                vacancies_salaries.append(vacancy["salary"])
    return vacancies_salaries


def get_language_vacancies_hh(programming_languages):
    language_vacancies = {}
    url = "https://api.hh.ru/vacancies/"
    for language in programming_languages:
        params = {
            "text": f"Программист {language}",
            "area": "1",
            "period": "30",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        vacancies_found = get_found_vacancies(language)
        vacancies_average_salary = get_vacancies_average_salaries(vacancies_found)
        vacancies_processed = len(vacancies_average_salary)
        average_salary = get_language_salary(vacancies_average_salary)
        vacancies_description = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary
        }
        language_vacancies.update({language: vacancies_description})
        
    return language_vacancies
