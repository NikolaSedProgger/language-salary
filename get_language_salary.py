def get_language_salary(average_salaries):
    salaries = []
    for salary in average_salaries:
        if salary['from'] or salary["payment_from"]:
            salaries.append(salary['to'] or salary["payment_to"] * 0.8)
        elif salary['to'] or salary["payment_to"] == None:
            salaries.append(salary['from'] or salary["payment_from"] * 1.2)
    return(int(sum(salaries) / len(salaries)))
