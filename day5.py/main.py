from functools import cmp_to_key

def load_input():
    rules, updates = {}, []

    with open('./inputs/input4.txt', 'r') as file:
        lines = file.read().strip().split('\n\n')

    for line in lines[0].splitlines(): 
        key, value = map(int, line.strip().split('|'))
        rules.setdefault(key, []).append(value)

    for line in lines[1].splitlines(): 
        updates.append(list(map(int, line.strip().split(','))))

    return rules, updates


rules, updates = load_input()

def is_ordered(update):
    for i, key in enumerate(update):
        if key in rules:
            for j, follower in enumerate(update):
                if follower in rules[key] and j < i:
                    return False
    return True

def sum_middle_numbers(updates):
    return sum([update[len(update)//2] for update in updates if is_ordered(update)])

print(sum_middle_numbers(updates))

########## Part 2 ############

def compare(a, b):
    if a in rules and b in rules[a]:
        return -1  # a should come before b
    elif b in rules and a in rules[b]:
        return 1  # b should come before a
    return 0  # order doesn't matter
        
def order_unordered_updates(updates):
    return [sorted(update, key=cmp_to_key(compare)) for update in updates if not is_ordered(update)]

print(sum_middle_numbers(order_unordered_updates(updates)))

