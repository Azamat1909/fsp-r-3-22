# Инфиксная запись – в постфиксную
from task97 import precedence
from task129 import tokenizing
from task130 import find_unary_sign

operator = ['+', '-', '*', '^', '/']


def convert_postfix(infix):
    operators = []
    postfix = []
    for lex in infix:
        if lex.isnumeric():
            postfix.append(lex)
        elif lex in operator:
            while operators != [] and operators[-1] != '(' and (precedence(lex) < operators[-1]):
                postfix.append(operators.pop())
            operators.append(lex)
        elif lex == '(':
            operators.append(lex)
        elif lex == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')
    while operators != []:
        postfix.append(operators.pop())
    return postfix


text = input()
print(convert_postfix(find_unary_sign(tokenizing(text))))
