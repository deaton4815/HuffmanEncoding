from typing import TextIO


def process_frequency_table(table_input: TextIO):
    freq_table = []

    while True:
        next_line = table_input.readline()
        if not next_line:
            break
        next_line = next_line.strip()

