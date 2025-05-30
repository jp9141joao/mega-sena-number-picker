import random
import time
import os

os.system('cls')
quantity = int(input('How many tickets do you want to generate?\nA: '))

wins = 0
fives = 0
fours = 0
triples = 0

winner_input = input('Enter the winning numbers separated by spaces\nEx: "10 20 30 40 50 60"\nA: ')
winner = winner_input.split()
winner = [int(number) for number in winner]
winner = sorted(winner)

if len(winner) != 6:
    print('Invalid winning ticket!')

for i in range(6):
    count = 0
    for j in range(6):
        if winner[i] == winner[j]:
            count += 1

    if count == 2:
        print('Invalid winning ticket!')
        break

sequence = []

for i in range(quantity):
    line = f'{(i + 1):05d}) '
    ticket = []
    matches = 0

    while True:
        for i in range(6):
            while True:
                number = random.randint(1, 60)
                if number not in ticket:
                    ticket.append(number)
                    break

        sorted_ticket = sorted(ticket)

        if ticket not in sequence:
            sequence.append(ticket)
            break

    for i in range(6):
        if sorted_ticket[i] in winner:
            matches += 1

    if matches == 3:
        triples += 1
    elif matches == 4:
        fours += 1
    elif matches == 5:
        fives += 1

    if sorted_ticket == winner:
        wins += 1

    if matches >= 3:
        for i in range(6):
            line += f' {sorted_ticket[i]:02d}'

        line += f' | Matches: {matches}'

        print(line)

print(f'\nNumber of winning tickets: {wins}')
print(f'Number of fives (5 matches): {fives}')
print(f'Number of fours (4 matches): {fours}')
print(f'Number of triples (3 matches): {triples}')
