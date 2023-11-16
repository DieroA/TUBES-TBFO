# <---------- PUSH DOWN AUTOMATA ----------> 

total_states = []
input_symbols = []
stack_symbols = []
starting_state = ""
starting_stack = ""
accepting_states = []                           # Final state
accept_with = ""                                # E - empty stack, F - final state
production_rules = {}                           # ieu kumaha cok

def baca_pda(file):
    global total_states, input_symbols, stack_symbols, starting_state, starting_stack, accepting_states, accept_with, production_rules

    try:
        lines = []
        for line in open(file, "r"):
            lines.append(line.strip())          # Baca file pda.txt, simpen di lines
    except:
        print(f"Gagal membuka file {file}.")
        return

    for state in lines[0].split():
        total_states.append(state)

    for symbol in lines[1].split():
        input_symbols.append(symbol)

    for symbol in lines[2].split():
        stack_symbols.append(symbol)

    starting_state = lines[3]

    starting_stack = lines[4]

    for state in lines[5].split():
        accepting_states.append(state)

    accept_with = lines[6]

    for i in range(7, len(lines)):              # Production rules 
        for char in lines[i].split():
            pass

baca_pda('pda.txt')
print(starting_state)