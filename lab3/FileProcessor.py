from typing import TextIO
from lab3.FrequencyTable import FrequencyTableQueue


def process_frequency_table(table_input: TextIO):
    frequency_list = []

    while True:
        line = table_input.readline()
        if not line:
            break
        line = line.strip()

        temp_letter = str()
        temp_freq = str()
        for char in line:

            if char.isalpha():
                temp_letter = char
            elif char.isdigit():
                temp_freq += char

        if temp_letter and temp_freq:
            frequency_list.append((temp_letter, int(temp_freq)))

    huffman_queue = FrequencyTableQueue(frequency_list)
