""" Day 18: Operation Order """

import ast

def solve(l):
    root = ast.parse(l, mode='eval')
    for node in ast.walk(root):
       if type(node) is ast.BinOp:
           node.op = ast.Add() if type(node.op) is ast.Div else ast.Mult()
    return eval(compile(root, '<string>', 'eval'))


with open('in.txt', 'r', encoding='utf-8') as file:
    ls = list(map(str.strip, file.readlines()))
    print(sum(solve(l.replace('+', '/')) for l in ls))
    print(sum(solve(l.replace('+', '/').replace('*', '+')) for l in ls))
