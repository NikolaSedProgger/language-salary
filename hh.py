import requests
from get_language_salary import get_language_salary


def found_vacancies(language):
    url = "https://api.hh.ru/vacancies/"
    town_id = 1
    days_period = 30
    params = {
        "text": f"Программист {language}",
        "area": town_id,
        "period": days_period,
    }
    founded_vacancies = []
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
        founded_vacancies.extend(response_content["items"])
    return founded_vacancies


def get_language_vacancies_hh(programming_languages):
    language_vacancies = {}
    url = "https://api.hh.ru/vacancies/"
    for language in programming_languages:
        params = {
            "text": f"Программист {language}",
            "area": "1",
            "period": "30",
        }
        vacancies_found = found_vacancies(language)
        payments = []
        for vacancy in vacancies_found:
            try:
                payment_to = vacancy['salary']["to"]
                payment_from = vacancy['salary']["from"]
                average_salary_vacancy = get_language_salary(payment_from, payment_to)
                payments.append(average_salary_vacancy)
            except TypeError:
                None
        vacancies_processed = len(payments)
        try:
            average_salary = sum(payments) / vacancies_processed
        except ZeroDivisionError:
            average_salary = 0
        vacancies_description = {
            "vacancies_found": len(vacancies_found),
            "vacancies_processed": vacancies_processed,
            "average_salary": int(average_salary)
        }
        language_vacancies.update({language: vacancies_description})
    return language_vacancies
