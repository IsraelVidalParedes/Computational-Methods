# Lab 2: Regular Expressions and Nondeterministic Finite Automata
# Author: Israel Vidal Paredes
import graphviz

class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transition_function = {}
        self.start_state = None
        self.accept_states = set()


def insert_concatenation_operator(regex: str) -> str:
    output = []
    for i, token in enumerate(regex):
        output.append(token)
        if i < len(regex) - 1 and token not in {'(', '|', '.'} and regex[i+1] not in {'*', '+', ')', '|', '.'}:
            output.append('.')
    return ''.join(output)

def infix_to_postfix(infix: str) -> str:
    # Implementation of the Shunting Yard Algorithm to convert infix to postfix
    output = []
    stack = []
    precedence = {'*': 100, '+': 10, '.': 1}
    for token in infix:
        if token in {'a', 'b'}:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    postfix = ''.join(output)
    if postfix[-1] == '.':
        postfix = postfix[:-1]
    return postfix

def thompson_construction(postfix_regex: str) -> NFA:
    # TODO: Implement Thompson's Construction Algorithm for NFAs

def to_dot(nfa: NFA) -> str:
    # TODO: Generate DOT language string for Graphviz

def main():
    regex = input("Enter a regex in infix notation using only 'a', 'b', '(', ')', '|', '.', and '*': ")
    postfix_regex = infix_to_postfix(regex)
    nfa = thompson_construction(postfix_regex)
    dot_graph = to_dot(nfa)
    graph = graphviz.Source(dot_graph)
    graph.view()

if __name__ == '__main__':
    main()
