# <---------- PUSH DOWN AUTOMATA ----------> 

total_states = []
input_symbols = []
stack_symbols = []
starting_state = ""
starting_stack = ""
accepting_states = []                           # Final state(s)
accept_with = ""                                # E - empty stack, F - final state
production_rules = {}  
current_stack = []                              # Stack top -> last element                        
current_state = ""

def baca_pda(file):
    global total_states, input_symbols, stack_symbols, starting_state, starting_stack, accepting_states, accept_with, production_rules, current_stack, current_state

    try:
        lines = []
        for line in open(file, "r"):
            lines.append(line.strip())          # Baca file pda.txt, simpen di lines
    except Exception as e:
        print(f"Gagal membuka file {file}.")
        return

    for state in lines[0].split():
        total_states.append(state)
    for symbol in lines[1].split():
        input_symbols.append(symbol)
    for symbol in lines[2].split():
        stack_symbols.append(symbol)
    starting_state = lines[3]
    current_state = starting_state
    starting_stack = lines[4]
    current_stack.append(starting_stack)
    for state in lines[5].split():
        accepting_states.append(state)
    accept_with = lines[6]                      
    for i in range(7, len(lines)):             
        char = lines[i].split()
        
        state = char[0]
        input_symbol = char[1]
        stack_pop = char[2]
        next_state = char[3]
        stack_push = char[4]

        if state not in production_rules.keys():
            production_rules[state] = []
        production_rules[state].append((input_symbol, stack_pop, next_state, stack_push)) 

def pda_input(input):
    global production_rules, current_stack, current_state

    isValid = False
    for rule in production_rules[current_state]:
        if input in rule:
            if rule[1] == current_stack[-1]:
                isValid = True
            else:
                isValid = False
            break
    
    if not isValid:        # Input tidak valid, masuk ke dead state (gagal).
        return
    
    # rule = (input, pop from stack, next state, push to stack)
    if rule[1] != 'e':
        current_stack.pop()
    current_state = rule[2]
    if rule[3] != 'e':
        symbols = [char for char in rule[3]]
        current_stack.extend(reversed(symbols))

def stop():
    global current_stack, accept_with, accepting_states, current_state

    if accept_with == 'E' and len(current_stack) == 0:                          # Empty Stack
        return True
    elif accept_with == 'F' and current_state in accepting_states:              # Final State
        return True
    return False
    
baca_pda('src/pda.txt')