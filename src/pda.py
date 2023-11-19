# <---------- PUSH DOWN AUTOMATA ----------> 

class PDA:
    def __init__(self, total_states, 
                 input_symbols, stack_symbols, 
                 starting_state, starting_stack, 
                 accepting_states, accept_with,
                 production_rules, current_stack,
                 current_state):
        self.total_states = total_states            # ga kepake
        self.input_symbols = input_symbols          # ga kepake
        self.stack_symbols = stack_symbols          # ga kepake
        self.starting_state = starting_state          
        self.starting_stack = starting_stack
        self.accepting_states = accepting_states    # Final state(s)
        self.accept_with = accept_with              # E - empty stack, F - final state
        self.production_rules = production_rules
        self.current_stack = current_stack          # Stack top -> last element     
        self.current_state = current_state
    
    def baca_pda(self, file):
        try:
            lines = []
            for line in open(file, "r"):
                lines.append(line.strip())          # Baca file pda.txt, simpen di lines
        except Exception:
            print(f"Gagal membuka file {file}.")
            return

        for state in lines[0].split():
            self.total_states.append(state)
        for symbol in lines[1].split():
            self.input_symbols.append(symbol)
        for symbol in lines[2].split():
            self.stack_symbols.append(symbol)
        self.starting_state = lines[3]
        self.current_state = self.starting_state
        self.starting_stack = lines[4]
        self.current_stack.append(self.starting_stack)
        for state in lines[5].split():
            self.accepting_states.append(state)
        self.accept_with = lines[6]                      
        for i in range(7, len(lines)):             
            char = lines[i].split()
            
            state = char[0]
            input_symbol = char[1]
            stack_pop = char[2]
            next_state = char[3]
            stack_push = char[4]

            if state not in self.production_rules.keys():
                self.production_rules[state] = []
            self.production_rules[state].append((input_symbol, stack_pop, next_state, stack_push))

    def pda_input(self, input):
        isValid = False
        for rule in self.production_rules[self.current_state]:
            if input in rule:
                if rule[1] == self.current_stack[-1]:
                    isValid = True
                else:
                    isValid = False
                break
        
        if not isValid:        # Input tidak valid (gagal).
            return             # nunggu pda.txt
        
        # rule = (input, pop from stack, next state, push to stack)
        if rule[1] != 'e':
            self.current_stack.pop()
        self.current_state = rule[2]
        if rule[3] != 'e':
            symbols = [char for char in rule[3]]
            self.current_stack.extend(reversed(symbols))

    def stop(self):
        if self.accept_with == 'E' and len(self.current_stack) == 0:                          # Empty Stack
            return True
        elif self.accept_with == 'F' and self.current_state in self.accepting_states:              # Final State
            return True
        return False

    