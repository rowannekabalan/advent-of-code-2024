from itertools import product
import operator

equations = {}

with open('./inputs/input7.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(':')
        equations[parts[0]] = list(map(int, parts[1].split()))

def eval_ltr(operands, operators):
    ops = {
        '+' : operator.add,
        '*' : operator.mul,
        '||': lambda x, y: int(str(x) + str(y))
    }

    result = operands[0]
    for i in range(len(operands)-1):
        result = ops[operators[i]](result, operands[i+1])
    return result


def valid_equation(test, operators):
    operands = equations[test]
    options = set(product(operators, repeat=len(operands)-1))

    while options:
        ops = options.pop()
        if eval_ltr(operands, ops) == int(test):
            return True  
    return False


def sum_valid(equations, operators):
    return sum(int(test) for test in equations if valid_equation(test, operators))


print(sum_valid(equations, operators = ['+','*']))
print(sum_valid(equations, operators = ['+','*', '||']))
