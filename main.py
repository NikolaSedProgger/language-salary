import os
from pstats import Stats
from terminaltables import AsciiTable
import hh
import sj


def create_table(programming_languages, table_name):
    table_variables = [
        ["Язык программирования", "Вакансий найдено", "Вакансий обработано", "Средняя зарплата"],
    ]
    for language, stats in programming_languages.items():
        print(stats['vacancies_found'])
        table_variables.append([language, stats['vacancies_found'], stats['vacancies_processed'], stats['average_salary']])
    table = AsciiTable(table_variables, table_name)
    return table.table

if __name__ == "__main__":
    sj_token = os.getenv("SJ_TOKEN")
    programming_languages = [
        "JavaScript",
        "Java",
        "Python",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "C",
        "Go",
        "Objective-C",
        "Scala",
        "Swift",
        "Typescript"
    ]

    print(create_table(hh.get_language_vacancies_hh(programming_languages), "HeadHunter Moscow"))
    print(create_table(sj.get_language_vacancies_sj(programming_languages, sj_token), "SuperJob Moscow"))
