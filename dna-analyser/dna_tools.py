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
    """Check if sequence contains only A, T, C, G"""
    return set('ATGC') == set(seq)

def read_seq_files(file_paths):
    sequences = {}

    for fname in file_paths:
        contents = read_file(fname)
        # clean input if file exists
        seq = clean_input(contents)
        # check if it is DNA
        if not is_valid_dna(seq):
            print(f'❌ "{fname}" is NOT a valid DNA sequence')
            continue
        else:
            print(f'✅ "{fname}" is a valid DNA sequence.')
        
        # add a valid seq
        sequences[fname] = seq

    return sequences

