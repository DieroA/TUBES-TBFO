import pda

# buat tes doang, hapus aja 

pda_var = pda.PDA(total_states = [], input_symbols = [], 
          stack_symbols = [], starting_state = "", 
          starting_stack = "", accepting_states = [],
          accept_with = "", production_rules = {},
          current_stack = [], current_state = "")

pda_var.baca_pda('src/pda.txt')

pda_var.pda_input('a')
pda_var.pda_input('e')
print(pda_var.current_state)
print(pda_var.current_stack)