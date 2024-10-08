# Required Inputs:
#   Input path to text file, Output path for text file

from pathlib import Path
import argparse

from lab3.FileProcessor import FileProcessor

# Argument Parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("frequency_table_input", type=str, help="Frequency Table Input Pathname")
arg_parser.add_argument("clear_text_input", type=str, help="Clear Text Input Pathname")
args = arg_parser.parse_args()

# Input and Output paths
frequency_table_path = Path(args.frequency_table_input)
clear_text_path = Path(args.clear_text_input)

# Process input file and write to output file
with frequency_table_path.open('r') as frequency_table, clear_text_path.open('r') as clear_text:
    file_processor = FileProcessor(frequency_table, clear_text)
