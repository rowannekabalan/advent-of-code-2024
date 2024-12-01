from collections import Counter

list1 = []
list2 = []

with open('./inputs/input1.txt', 'r') as file: 
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)


def calculate_distances(list1, list2):
    l1, l2 = sorted(list1), sorted(list2)
    return sum([abs(l1[i] - l2[i])  for i in range(len(l1))])


def calculate_similarity(list1, list2):
    counts = Counter(list2)
    return sum([n * counts[n] for n in list1 if n in counts])

#list1 = [3,4,2,1,3,3]
#list2 = [4,3,5,3,9,3]

print(calculate_distances(list1,list2))
print(calculate_similarity(list1, list2))