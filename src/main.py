import pda

# buat tes doang, hapus aja 

pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_state = "")

pda_var.baca_pda('src/pda.txt')

print(pda_var.input_symbols)