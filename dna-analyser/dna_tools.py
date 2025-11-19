def read_file(file_path):
    """Reads text file

    Returns an empty string when there's an error when reading files.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content

    except FileNotFoundError:
        print(f'⚠️ Error: "{file_path}" not found!')
        return ''

    except Exception as e:
        print(f'⚠️ Unexpected error: {e}')
        return ''

def clean_input(input_text):
    """Removes whitespace characters and converts to upper case letters"""
    lines = input_text.splitlines()

    no_comment = ''.join(filter(lambda l: l[:2] not in ['# ', '% ', '//'], lines))
    
    return no_comment.strip().upper().replace(' ', '')

def is_valid_dna(seq):
    """Check if sequence contains only A, T, G, C"""
    return set('ATGC') == set(seq)

def read_seq_files(file_paths):
    sequences = {}

    for fname in file_paths:
        contents = read_file(fname)
        # clean input if file exists
        seq = clean_input(contents)
        # check if it is DNA
        if not is_valid_dna(seq):
            print(f'❌ "{fname}"; NOT a valid DNA sequence!')
            continue
        else:
            print(f'✅ "{fname}"')
        
        # add a valid seq
        sequences[fname] = seq

    return sequences

def count_bases_withloop(seq):
    count = {'A':0, 'T':0, 'G':0, 'C':0}
    for base in seq:
        count[base] += 1
    return count

def count_bases(seq):
    return {base: seq.count(base) for base in 'ATGC'}

def gc_content(base_count):
    gc_count = base_count['G'] + base_count['C']
    total = base_count['A'] + base_count['T'] + base_count['G'] + base_count['C']
    return 100 * gc_count / total

def at_to_gc_ratio(base_count):
    return (base_count['A'] + base_count['T']) / (base_count['G'] + base_count['C'])

# https://www.thermofisher.com/sg/en/home/references/ambion-tech-support/rna-tools-and-calculators/dna-and-rna-molecular-weights-and-conversions.html
def calc_wight_ss(base_count):
    weight = 313.2*base_count['A'] + \
        304.2*base_count['T'] + \
        329.2*base_count['G'] + \
        289.2*base_count['C'] + 79.0
    return weight

# complementary strand
def complementary_strand(seq):
    convert = {'A': 'T', 'T':'A', 'G': 'C', 'C':'G'}
    return ''.join([convert[k] for k in seq])

# mRNA seq
def transcribe_to_rna(seq):
    convert = {'A': 'U', 'T':'A', 'G': 'C', 'C':'G'}
    return ''.join([convert[k] for k in seq])
