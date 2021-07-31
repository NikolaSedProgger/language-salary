import requests


def get_found_vacancies(language):
    url = "https://api.hh.ru/vacancies/"
    params = {
        "text": f"Программист {language}",
        "area": "1",
        "period": "30",
    }
    response = requests.get(url, params=params)
    found_vacancies = []
    page = 0
    pages = 100

    while page < pages:
        params = {
            "text": f"Программист {language}",
            "area": "1",
            "period": "30",
            "page": page
        }
        response = requests.get(url, params=params)
        page += 1
        pages = response.json()['pages']

        for vacancy in response.json()['items']:
            found_vacancies.extend([vacancy])
        response.raise_for_status()
    return found_vacancies


def get_average_salaries_from_vacancies(language, vacancies):
    result = []

    for vacancy in vacancies:
        if vacancy['salary'] != None and vacancy['salary']['currency'] == 'RUR':
            result.append(vacancy['salary'])
    return result


def get_language_salary(language, average_salaries):
    salaries = []
    for salary in average_salaries:
        if salary['from'] == None:
            salaries.append(salary['to'] * 0.8)
        elif salary['to'] == None:
            salaries.append(salary['from'] * 1.2)
    return(int(sum(salaries) / len(salaries)))


def get_languages_vacancies_for_hh(programming_languages):
    languages_vacancies = {}
    url = "https://api.hh.ru/vacancies/"
    for language in programming_languages:
        params = {
            "text": f"Программист {language}",
            "area": "1",
            "period": "30",
        }
        response = requests.get(url, params=params)
        vacancies_average_salaries = get_average_salaries_from_vacancies(language, get_found_vacancies(language))
        languages_vacancies.update({language: {"vacancies_found": response.json()['found'], "vacancies_processed": len(vacancies_average_salaries), "average_salary": get_language_salary(language, vacancies_average_salaries)}})
    return languages_vacancies
