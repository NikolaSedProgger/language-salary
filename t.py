import re
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
    vacancies_found = response.json()['objects']
    debugged_api = response.json()
    
    while debugged_api["more"]:
        page += 1
        params["page"] = page
        new_response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        debugged_api = new_response.json()
    return vacancies_found, debugged_api