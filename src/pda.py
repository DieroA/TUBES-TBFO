# <---------- PUSH DOWN AUTOMATA ----------> 

class PDA:
    def __init__(self, total_states, 
                 input_symbols, stack_symbols, 
                 starting_state, starting_stack, 
                 accepting_states, accept_with,
                 production_rules, current_stack,
                 current_states):
        self.total_states = total_states            # ga kepake
        self.input_symbols = input_symbols          # ga kepake
        self.stack_symbols = stack_symbols          # ga kepake
        self.starting_state = starting_state          
        self.starting_stack = starting_stack
        self.accepting_states = accepting_states    # Final state(s)
        self.accept_with = accept_with              # E - empty stack, F - final state
        self.production_rules = production_rules
        self.current_stack = current_stack          # Stack top -> last element     
        self.current_states = current_states
    
    def baca_pda(self, file):
        # Membaca file pda.txt 
        try:
            lines = []
            filename = "../src/" + file
            for line in open(filename, "r"):
                lines.append(line.strip())
        except Exception as e:
            print(f"Gagal membuka file {file}.")
            print(e)
            return

        for state in lines[0].split():                  # States
            self.total_states.append(state)
        for symbol in lines[1].split():                 # Input symbols
            self.input_symbols.append(symbol)
        for symbol in lines[2].split():                 # Stack symbols
            self.stack_symbols.append(symbol)
        self.starting_state = lines[3]                  # Starting state
        self.current_states = self.starting_state       # Current state
        self.starting_stack = lines[4]                  # Starting stack symbol
        self.current_stack.append(self.starting_stack)  # Current stack symbol
        for state in lines[5].split():                  # Final state(s)
            self.accepting_states.append(state)
        self.accept_with = lines[6]                     # Accept with final state / empty stack
        for i in range(7, len(lines)):                  # Production rules
            char = lines[i].split()
            
            # δ(state, input_symbol, stack_pop) = (next_state, stack_push)
            state = char[0]
            input_symbol = char[1]
            stack_pop = char[2]
            next_state = char[3]
            stack_push = char[4]

            key = (state, input_symbol, stack_pop)
            value = (next_state, stack_push)

            self.production_rules[key] = value 

    def process_input(self, input_list):
        # Basis
        # Berhenti ketika input sudah diproses semua.
        if (len(input_list) < 1):     
            self.process_input_epsilon();                 
            return
        
        # Rekurens
        # note: input symbol dan pop stack 'e' belum (agak) bisa
        input = input_list[0]
        input_list = input_list[1:]

        next_states = []
        # new_stack = self.current_stack[:-1]         # Pop stack
        new_stack = []
        for current_state in self.current_states:
            key = (current_state, input, self.current_stack[-1])
            key_epsilon = (current_state, input, 'e');   
            # print(key)
            
            for i in range(3):
                if i == 0:                                          # δ(_, _, EPSILON) = (_, _)
                    if key_epsilon in self.production_rules:
                        new_stack = self.current_stack
                    else:
                        continue
                
                elif i == 1:                                        # δ(_, _, ~EPSILON) = (_, _)
                    if key in self.production_rules:
                        new_stack = self.current_stack[:-1]
                    else:
                        continue

                if i < 2:
                    next_state = self.production_rules[key][0]
                    stacks = self.production_rules[key][1].split(',')
                    stacks.reverse()

                    # Push to stack
                    for stack in stacks:
                        if stack != 'e':
                            new_stack.append(stack)
                    
                    # Lanjutkan dengan rekursi
                    next_states.append(next_state)
                    self.current_states = next_states
                    self.current_stack = new_stack
                             
                    self.process_input(input_list)   
                else:
                    self.process_input_epsilon()
    
    def process_input_epsilon(self):
        next_states = []
        new_stack = []
        for current_state in self.current_states:
            key = (current_state, 'e', self.current_stack[-1])
            key_epsilon = (current_state, 'e', 'e')  

            for i in range(2):
                if i == 0:                                          # δ(_, e, EPSILON) = (_, _)
                    if key_epsilon in self.production_rules:
                        new_stack = self.current_stack
                    else:
                        continue
                
                elif i == 1:                                        # δ(_, e, ~EPSILON) = (_, _)
                    if key in self.production_rules:
                        new_stack = self.current_stack[:-1]
                    else:
                        continue
                
                if key_epsilon in self.production_rules or key in self.production_rules:
                    next_state = self.production_rules[key][0]
                    stacks = self.production_rules[key][1].split(',')
                    stacks.reverse()

                    # Push to stack
                    for stack in stacks:
                        if stack != 'e':
                            new_stack.append(stack)
                    
                    # Lanjutkan dengan rekursi
                    next_states.append(next_state)
                    self.current_states = next_states
                    self.current_stack = new_stack

                    self.process_input_epsilon()                                

    def accept(self, input_list):
        self.process_input(input_list)

        Valid = False
        if self.accept_with == 'E' and len(self.current_stack) == 1 and self.current_stack[0] == 'E': # E adalah empty stack
            Valid = True
        elif self.accept_with == 'F':
            for current_state in self.current_states:
                if current_state in self.accepting_states:
                    Valid = True
                    break

        if Valid:
            print("Accepted")
        else:
            # print(self.current_stack)
            # print(self.current_states)
            print("Syntax Error")
