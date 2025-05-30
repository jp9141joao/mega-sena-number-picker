# Mega Sena Number Picker

## Description

This program simulates the generation of random numbers for the **Mega Sena** lottery draw. The user can input the winning numbers, and the script will generate several random tickets. The program compares each generated ticket with the winning numbers and displays how many matches (3, 4, or 5) occurred. It also counts how many times you won (by matching all 6 numbers). The program will also display the number of **"Quinas"** (5 matches), **"Quadras"** (4 matches), and **Triples** (3 matches).

## Features

* **Random Number Generation**: Generates 6 random numbers between 1 and 60 for each ticket.
* **Winning Numbers Input**: The user can input the winning numbers.
* **Match Count**: The program compares each ticket with the winning numbers and counts how many numbers match.
* **Result Display**: Displays the number of wins (all 6 numbers), Quinas (5 matches), Quadras (4 matches), and Triples (3 matches).

## How to Use

1. **Start the Program**: Run the script.
2. **Enter the Number of Tickets**: The program will ask how many tickets you want to generate.
3. **Enter the Winning Numbers**: The program will ask you to input the 6 winning numbers (between 1 and 60), separated by spaces.
4. **View Results**: The program will generate the tickets, compare them, and display the number of matches and wins.

## Example Output

```text
How many tickets do you want to generate?
A: 5

Enter the winning numbers separated by spaces
Ex: "10 20 30 40 50 60"
A: 10 20 30 40 50 60

00001)  05  10  15  20  30  40 | Matches: 4  
00002)  01  08  13  14  22  60 | Matches: 3  
00003)  10  20  30  40  50  60 | Matches: 6 (Winner!)  
...
Number of winning tickets: 1  
Number of Quinas: 0  
Number of Quadras: 0  
Number of Triples: 1  
```

## Requirements

* Python 3.x

## How to Run the Script

1. **Install Python**: Make sure Python 3.x is installed on your computer.
2. **Run the Script**: Open the terminal and execute the Python file:

   ```bash
   python sorteio_mega_sena.py
   ```
