def get_language_salary(salary_from, salary_to):
    average_salary = 0
    if salary_from == None:
        average_salary = salary_to * 0.8
    elif salary_to == None:
        average_salary = salary_from * 1.2
    elif salary_from and salary_to == None:
        average_salary = None
    return average_salary