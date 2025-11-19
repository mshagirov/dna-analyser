#!/usr/bin/env python3

import sys
# from pathlib import Path

from banner import display_dna_banner, display_ansi_art
from dna_tools import read_seq_files

def main(*input_files):
    display_dna_banner()
    display_ansi_art()

    print('\nRead and check DNA sequences:')    
    sequences = read_seq_files(input_files)

    for seq in sequences:
        print(seq)
        print(f'Length: {len(sequences[seq])}')

        # weight?
        # GC content
        # complementary strand
        # mRNA seq

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('DNA Analyser requires at least 1 input file\n')
        print(f'\t{sys.argv[0]} input_file1 [ input_file2 [ input_file3 ... ] ... ]\n')
        sys.exit(1)
    print(sys.argv[1:])
    main(*sys.argv[1:])
