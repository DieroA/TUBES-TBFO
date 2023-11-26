import pda
import html_parser_new as html_parser
import sys

# Input nama file dari terminal dengan format:
# python main.py pda.txt "file.html"
file_pda = sys.argv[1]
file_html = sys.argv[2]

# Initialize PDA
pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_states = [])
pda_var.baca_pda(file_pda)

# Parse html
hasil_parse = html_parser.parse_html(file_html)
print(hasil_parse)

# Proses menggunakan PDA
if hasil_parse[1]:
    token = hasil_parse[0]
    pda_var.accept(token)
else:
    print("Syntax Error")
