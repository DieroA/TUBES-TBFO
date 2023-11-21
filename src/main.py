import pda

# Initialize PDA
pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_states = [])
pda_var.baca_pda('src/pda.txt')

# Baca input dari file .html
input_pda = ["html", "html", "head", "/head", "body", "/body", "/html"]

pda_var.accept(input_pda)