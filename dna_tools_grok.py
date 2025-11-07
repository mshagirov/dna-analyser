# dna_tools.py
# DNA Sequence Analysys Tools suggested by Grok

def is_valid_dna(seq):
    """Check if sequence contains only A, T, C, G"""
    return all(base in 'ATCG' for base in seq)

def count_nucleotides(seq):
    """Return dictionary with count of each base"""
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in seq:
        counts[base] += 1
    return counts

def gc_content(seq):
    """Calculate GC content as percentage"""
    if len(seq) == 0:
        return 0.0
    g = seq.count('G')
    c = seq.count('C')
    return (g + c) / len(seq) * 100

def find_start_codons(seq):
    """Find all positions of ATG (0-based index)"""
    positions = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            positions.append(i)
    return positions

def complementary_strand(seq):
    """Return complementary DNA strand (A→T, T→A, C→G, G→C)"""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in seq)

def print_analysis(seq):
    """Print full analysis of DNA sequence"""
    if not is_valid_dna(seq):
        print("\nInvalid DNA! Only A, T, C, G allowed.\n")
        return False
    
    print("\nValid DNA sequence!\n")
    
    # Nucleotide counts
    counts = count_nucleotides(seq)
    print("Nucleotide Count:")
    for base, count in counts.items():
        print(f"  {base}: {count}")
    
    # GC content
    print(f"\nGC Content: {gc_content(seq):.2f}%")
    
    # Start codons
    starts = find_start_codons(seq)
    if starts:
        print(f"Start Codons (ATG) found at positions: {', '.join(map(str, starts))}")
    else:
        print("No start codons (ATG) found.")
    
    # Complementary strand
    print(f"\nComplementary Strand: {complementary_strand(seq)}\n")
    return True

def main():
    print("=== DNA Sequence Analyzer ===\n")
    print("Enter DNA sequences to analyze. Type 'quit' to exit.\n")
    
    while True:
        seq = input("Enter DNA sequence: ").upper().strip()
        
        if seq.lower() == 'quit':
            print("Thanks for using DNA Analyzer! Goodbye.")
            break
        if not seq:
            print("Please enter a sequence.\n")
            continue
        
        print_analysis(seq)

if __name__ == "__main__":
    main()
