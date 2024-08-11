from typing import TextIO
from PriorityQueue import PriorityQueue


def process_frequency_table(table_input: TextIO):
    freq_table = []

    while True:
        next_line = table_input.readline()

        if not next_line:
            break

    print("\nUnmodified line: " + next_line + "\nStripped line: " + next_line.strip())
