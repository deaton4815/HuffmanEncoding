# Required Inputs:
#   Input path to text file, Output path for text file

from pathlib import Path
import argparse

from FileProcessor import process_frequency_table

# Argument Parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("frequency_table_input", type=str, help="Frequency Table Input Pathname")
args = arg_parser.parse_args()

# Input and Output paths
in_path = Path(args.in_file)

# Process input file and write to output file
with in_path.open('r') as input_file:
    process_frequency_table(input_file)
