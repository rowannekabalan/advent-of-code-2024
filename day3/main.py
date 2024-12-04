import re

input = ''
with open('./inputs/input3.txt', 'r') as file: 
    input = file.read()

def part1(input):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern,input)

    sum = 0
    for match in matches:
        ints = [int(num) for num in re.findall(r'\d+', match)]
        sum += ints[0] * ints[1]
    return sum

def part2():
    sum = 0
    valid_chunks = input.split('do()')
    for chunk in valid_chunks:
        invalid_chunks = chunk.split('don\'t()')
        sum += part1(invalid_chunks[0])
    return sum