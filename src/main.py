import pda

# Initialize PDA
pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_states = [])
pda_var.baca_pda('src/pda.txt')

# Baca input dari file .html
# input_pda = ["html","body","h1","/h1","p","/p","/body","head","title","/title","/head","/html"]
# input_pda = ["hmif","head","title","/title","/head","body","h1","/h1","p","/p","/body","/hmif"]
#input_pda = ["html","body","h1","/h1","p","/p","/body","/html"]
input_pda = ["html","head","/head","body","/body","/html"]
pda_var.accept(input_pda)