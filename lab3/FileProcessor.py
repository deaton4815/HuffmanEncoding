from typing import TextIO
from lab3.FrequencyTable import FrequencyTableQueue
class FileProcessor:

    def __init__(self, table_input: TextIO, clear_text_input: TextIO):
        self.huffman_queue = None
        self.process_frequency_table(table_input)

    def process_frequency_table(self, table_input):
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

        self.huffman_queue = FrequencyTableQueue(frequency_list)

    def process_clear_text(self, clear_text_input):

        clear_text = []

        while True:
            line = clear_text_input.readline()
            if not line:
                break
            clear_text.append()





