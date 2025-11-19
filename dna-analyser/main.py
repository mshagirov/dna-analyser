#!/usr/bin/env python3

import sys
import os
# from pathlib import Path

from banner import display_banner
from dna_tools import *

TEXT_WIDTH = os.get_terminal_size().columns

def main(*input_files):
    display_banner()

    print('\nChecking input files:')    
    sequences = read_seq_files(input_files)

    print("\nAnalysing sequences:")
    for seq in sequences:
        print(f"\n🧬 Sequence: {seq}")
        
        print(f'  - length: {len(sequences[seq])} bp')

        bases = count_bases(sequences[seq])
        print(f'  - count : {bases}')

        print(f'  - weight: {calc_wight_ss(bases):.1f} Da (single strand)')

        print(f"  - GC content: {gc_content(bases):4.2f}%")

        print(f"  - AT:GC ratio: {at_to_gc_ratio(bases):5.2f}")

        print("")
        plasmid = sequences[seq][:TEXT_WIDTH]
        
        print(plasmid)
        print('|'*len(plasmid))
        print(complementary_strand(plasmid))

        print('\nRNA:')
        print(transcribe_to_rna(plasmid))

        print('-'*TEXT_WIDTH)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('DNA Analyser requires at least 1 input file\n')
        print(f'\t{sys.argv[0]} input_file1 [ input_file2 [ input_file3 ... ] ... ]\n')
        
        sys.exit(1)

    main(*sys.argv[1:])
