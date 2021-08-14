import requests
from main import get_language_salary

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
        page += 1
        pages = response.json()['pages']
        response.raise_for_status()
        found_vacancies.extend(response.json()['items'])
        
        response.raise_for_status()
    return found_vacancies


def get_average_salaries_from_vacancies(language, vacancies):
    result = []

    for vacancy in vacancies:
        if vacancy['salary'] != None and vacancy['salary']['currency'] == 'RUR':
            result.append(vacancy['salary'])
    return result


def get_language_vacancies_for_hh(programming_languages):
    language_vacancies = {}
    url = "https://api.hh.ru/vacancies/"
    for language in programming_languages:
        params = {
            "text": f"Программист {language}",
            "area": "1",
            "period": "30",
        }
        response = requests.get(url, params=params)
        vacancies_average_salary = get_average_salaries_from_vacancies(language, get_found_vacancies(language))
        vacancies_found = response.json()['found']
        vacancies_processed = len(vacancies_average_salary)
        average_salary = get_language_salary(vacancies_average_salary)
        language_vacancies.update({language: {"vacancies_found": vacancies_found, "vacancies_processed": vacancies_processed, "average_salary": average_salary}})
        response.raise_for_status()

    return language_vacancies
