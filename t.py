import random
from time import sleep
logs = {
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
    random.randint(1, 100000000):"True",
}
b = 0
a = 0
objective_logs = []
while a != 100000000:
    a = a + 1
    try:
        print(logs[a])
        b = b + 1
        print(f"log adress: {a}. log adress working: True.")
        print(f"logs connected to server 'Objective logs': {b} / 70")
        objective_logs.append(a)
        sleep(25)
    except KeyError:
        print(f"log adress: {a}. log adress working: False.")

for log in objective_logs:
    print(f"connecting to {log} log...")