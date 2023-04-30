# Predictive parsing table
parsing_table = {
    ('E', 'a'): ['T', 'Q'],
    ('E', '('): ['T', 'Q'],
    ('Q', '+'): ['+', 'T', 'Q'],
    ('Q', '-'): ['-', 'T', 'Q'],
    ('Q', ')'): ['epsilon'],
    ('Q', '$'): ['epsilon'],
    ('T', 'a'): ['F', 'R'],
    ('T', '('): ['F', 'R'],
    ('R', '*'): ['*', 'F', 'R'],
    ('R', '/'): ['/', 'F', 'R'],
    ('R', '+'): ['epsilon'],
    ('R', '-'): ['epsilon'],
    ('R', ')'): ['epsilon'],
    ('R', '$'): ['epsilon'],
    ('F', 'a'): ['a'],
    ('F', '('): ['(', 'E', ')']
}

# Stack implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, symbol):
        self.stack.append(symbol)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


# Function to perform predictive parsing
def predictive_parse(input_string):
    stack = Stack()
    stack.push('$')
    stack.push('E')

    index = 0
    action = ""

    while not stack.is_empty():
        top = stack.pop()
        if top == input_string[index]:
            index += 1
        elif (top, input_string[index]) in parsing_table:
            production = parsing_table[top, input_string[index]]
            if production[0] != 'epsilon':
                for symbol in reversed(production):
                    stack.push(symbol)
        action += f"Input: {input_string[index:]}\nStack: {stack}\n"


    if index == len(input_string) and stack.is_empty() and input_string[index - 1] == '$':
        action += "Output: String is accepted/valid."
    else:
        action += "Output: String is not accepted/invalid."
        
    return action


# Test the predictive parsing function
input_string = input("Please put in an input string Ex:(a+a)$: ")

output = predictive_parse(input_string)
print(output)
