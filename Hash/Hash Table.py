# Birthday Problem
import random
TRIALS = 100000 # num of experiment
same_birthdays = 0 # count

for _ in range(TRIALS):
    birthdays = []

    # compare 23 people's birthdays
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

    # proportion
    print(f'{same_birthdays / TRIALS * 100}%')
