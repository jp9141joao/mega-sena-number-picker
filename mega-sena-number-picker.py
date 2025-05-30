import random  # Import to generate random numbers
import time    # Imported but not used in this code
import os      # Import for system commands like clearing the screen

os.system('cls')  # Clear the terminal screen on Windows

# Ask the user how many tickets to generate
quantity = int(input('How many tickets do you want to generate?\nA: '))

# Initialize counters for different match counts
wins = 0      # Tickets that match all numbers
fives = 0     # Tickets with 5 matches
fours = 0     # Tickets with 4 matches
triples = 0   # Tickets with 3 matches

# Ask the user to input the winning numbers separated by spaces
winner_input = input('Enter the winning numbers separated by spaces\nEx: "10 20 30 40 50 60"\nA: ')

# Split the input string into a list of strings
winner = winner_input.split()

# Convert each string to an integer
winner = [int(number) for number in winner]

# Sort the winning numbers to facilitate comparison
winner = sorted(winner)

# Validate that exactly 6 numbers were entered
if len(winner) != 6:
    print('Invalid winning ticket!')

# Validate that no number is repeated in the winning ticket
for i in range(6):
    count = 0
    for j in range(6):
        if winner[i] == winner[j]:
            count += 1

    # If any number appears twice, the ticket is invalid
    if count == 2:
        print('Invalid winning ticket!')
        break

sequence = []  # List to store generated tickets to avoid duplicates

# Loop to generate the requested number of tickets
for i in range(quantity):
    line = f'{(i + 1):05d}) '  # Format the ticket number with leading zeros (e.g., 00001)
    ticket = []  # List to hold the current ticket numbers
    matches = 0  # Counter for how many numbers match the winning numbers

    # Generate unique tickets (no duplicate tickets)
    while True:
        for i in range(6):  # Each ticket has 6 numbers
            while True:
                number = random.randint(1, 60)  # Generate a random number between 1 and 60
                if number not in ticket:       # Avoid duplicates within the same ticket
                    ticket.append(number)
                    break

        sorted_ticket = sorted(ticket)  # Sort ticket numbers for easier comparison

        # If this ticket hasn’t been generated before, accept it
        if ticket not in sequence:
            sequence.append(ticket)  # Add to the list of generated tickets
            break

    # Count how many numbers in the ticket match the winning numbers
    for i in range(6):
        if sorted_ticket[i] in winner:
            matches += 1

    # Update counters based on the number of matches
    if matches == 3:
        triples += 1
    elif matches == 4:
        fours += 1
    elif matches == 5:
        fives += 1

    # If all numbers match, increment the win counter
    if sorted_ticket == winner:
        wins += 1

    # Print the ticket if it has 3 or more matches
    if matches >= 3:
        for i in range(6):
            line += f' {sorted_ticket[i]:02d}'  # Add each ticket number formatted with leading zero

        line += f' | Matches: {matches}'  # Show how many matches

        print(line)  # Display the ticket

# After generating all tickets, print the summary of matches
print(f'\nNumber of winning tickets: {wins}')
print(f'Number of fives (5 matches): {fives}')
print(f'Number of fours (4 matches): {fours}')
print(f'Number of triples (3 matches): {triples}')
