import requests
from get_language_salary import get_language_salary


def get_vacancies_from_sj(language, sj_token):
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
    vacancies = []
    vacancies.append(response.json()['objects'])
    while response.json()["more"]:
        params["page"] = page + 1
        response = requests.get(url, params=params, headers=headers)
        objects = response.json()["objects"]
        response.raise_for_status()
        vacancies.extend(objects)
    return vacancies


def process_vacancies_from_sj(vacancies, total_vacancies):
    payments = []
    for vacancy in vacancies:
        payment_to = vacancy["payment_to"]
        payment_from = vacancy["payment_from"]
        average_salary_vacancy = get_language_salary(payment_from, payment_to)
        if average_salary_vacancy:
            payments.append(average_salary_vacancy)
    try:
        average_salary = sum(payments) / len(vacancies)
    except ZeroDivisionError:
        average_salary = 0
    process_vacancies = {
        "vacancies_found": total_vacancies["total"],
        "vacancies_processed": len(vacancies),
        "average_salary": int(average_salary)
    }
    return process_vacancies


def get_language_vacancies_sj(programming_languages, sj_token):
    language_vacancies = {}
    for language in programming_languages:
        sj_vacancies = get_vacancies_from_sj(language, sj_token)
        processed_vacancies = [process_vacancies_from_sj(vacancy) for vacancy in sj_vacancies]
        language_vacancies.update({language: processed_vacancies})
    return language_vacancies
