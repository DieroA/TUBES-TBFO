import pda
import html_parser

file_pda = "pda.txt"
file_htmls = ['1reject', '2reject', '3reject', '4accept', '5accept', '6reject','7accept','8reject', '9accept','10reject','11accept'] 

# Initialize PDA
for i in file_htmls:
    pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_states = [])
    pda_var.baca_pda(file_pda)
    file_html = i + '.html'
    print("")
    print(file_html)

    # Parse html
    hasil_parse = html_parser.parse_html(file_html)

    # Proses menggunakan PDA
    if hasil_parse[1]:
        token = hasil_parse[0]
        print(token)
        pda_var.accept(token)
    else:
        print("Syntax Error")

    # HASIL TESTCASE: berhasil semua kecuali #7