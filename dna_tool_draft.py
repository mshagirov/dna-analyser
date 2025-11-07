# https://www.101computing.net/dna-sequence-analysis-python-challenge/
#DNA Sequence Analysis - www.101computing.net/dna-sequence-analysis-python-challenge/
print("""
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O     DNA Sequence Analysis
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O      

""")

def count_nucleotides(dna_sequence):
   """Count the occurrences of each nucleotide in the DNA sequence."""
   counts = {}
   #...
   return counts

def complementary_strand(dna_sequence):
  """Return the complementary strand of the given DNA sequence."""
  strand = "" 
  #...
  return strand

def find_pattern(dna_sequence, pattern):
   """Find the starting indices of all occurrences of the pattern in the DNA sequence."""
   indices = []
   #...
   return indices

def transcribe_dna_to_rna(dna_sequence):
   """Transcribe the given DNA sequence to RNA."""
   rna_sequence = "" 
   return rna_sequence

def gc_content(dna_sequence):
   """Calculate the GC content of the given DNA sequence."""
   gc_count = 0
   #...
   return gc_count



dna_sequence = "ATAGCGATCGTAGTTCATAGCTACGTGCGATAGCTCAA"
print("DNA Sequence:", dna_sequence)
print("Count Nucleotides:", count_nucleotides(dna_sequence))
print("Complementary Strand:", complementary_strand(dna_sequence))
print("Find Pattern 'AGC':", find_pattern(dna_sequence, "AGC"))
print("Transcribe DNA to RNA:", transcribe_dna_to_rna(dna_sequence))
print("GC Content:", gc_content(dna_sequence))
