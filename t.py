import requests
import os

url = "https://api.superjob.ru/2.0/vacancies/"

params = {
    "town": "Москва",
    "keyword": f"Программист Python",
    "count": 1
}
headers = {
    "X-Api-App-Id": "v3.r.133318714.f70e6d4022872fb93a542e0aad893270e9bc0e95.2e9144ce232372ab5fb95b959f47528aa754271c"
}

response = requests.get(url, params=params, headers=headers)

a = {"pay_from":0, "pay_to":5}
b = {"paym_from":0, "paym_to":10}
def get_language_salary(average_salaries):
    salaries = []
    for salary in average_salaries:
        if "from" in salary == None:
            salaries.append(salary['to'] * 0.8)
        elif salary['to'] == None:
            salaries.append(salary['from'] * 1.2)
    return(int(sum(salaries) / len(salaries)))
print(get_language_salary(a))
print(get_language_salary(b))