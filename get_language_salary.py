def get_language_salary(salary_from, salary_to):
    average_salary = 0
    if salary_to:
        average_salary = salary_to * 0.8
    elif salary_from:
        average_salary = salary_from * 1.2
    else:
        average_salary = 0
    return average_salary