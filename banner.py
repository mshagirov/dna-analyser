import os

title = '▌ DNA Sequence Analyser ▐'

TERM_WIDTH = max(os.get_terminal_size().columns, len(title))
repeats = TERM_WIDTH // 10
pad = TERM_WIDTH % 10

template1 = '○       o '
template2 = '| ○   o | '
template3 = '| | ○ | | '
template4 = '| o   ○ | '
template5 = 'o       ○ '

banner1 = template1 * repeats + template1[:pad]
banner2 = template2 * repeats + template2[:pad]
banner3 = template3 * repeats + template3[:pad]
banner4 = template4 * repeats + template4[:pad]
banner5 = template5 * repeats + template5[:pad]

title_start = (TERM_WIDTH - len(title)) // 2
banner3 = banner3[:title_start] + title + banner3[title_start + len(title):]

banner = f"{banner1}\n{banner2}\n{banner3}\n{banner4}\n{banner5}"
