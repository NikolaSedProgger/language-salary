
import requests

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

def get_found_vacancies(language):    
    url = "https://api.hh.ru/vacancies/"
    params = {
        "text":f"Программист {language}", 
        "area":"1",
        "period":"30",
    }
    response = requests.get(url, params=params)

    found_vacancies = []
    
    page = 0
    pages = 100


    #пока page < pages, в параметрах page = значение page на 14 строчке, запрос + raise_for_status, page += 1, pages обновляется в цикле
    while page < pages:
        params = {
            "text":f"Программист {language}", 
            "area":"1",
            "period":"30",
            "page":page         
        }
        response = requests.get(url, params=params)


        page += 1
        pages = response.json()['pages']

        for vacancy in response.json()['items']:
            found_vacancies.append(vacancy)
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

def get_languages_dict_for_hh():
    language_dict = {}
    url = "https://api.hh.ru/vacancies/"
    for language in PROGRAMMING_LANGUAGES:
        params = {
            "text":f"Программист {language}", 
            "area":"1",
            "period":"30",
        }
        response = requests.get(url, params=params)
        language_dict.update({language:{"vacancies_found":response.json()['found'], "vacancies_processed":len(get_average_salaries_from_vacancies(language, get_found_vacancies(language))), "average_salary":get_language_salary(language, get_average_salaries_from_vacancies(language, get_found_vacancies(language)))}})
    return language_dict
















  


