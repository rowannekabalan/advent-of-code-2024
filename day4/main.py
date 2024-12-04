grid = []
with open('./inputs/input4.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

size = len(grid)

def word_search():
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]
    return sum(
        find_xmas((i, j), direction)
        for i in range(size)
        for j in range(size)
        if grid[i][j] == 'X'
        for direction in directions
    )

def find_xmas(loc, direction, letter_index=1):
    new_i, new_j = loc[0] + direction[0], loc[1] + direction[1]
    target_letters = ['X', 'M', 'A', 'S']

    if letter_index == len(target_letters):
        return True

    if 0 <= new_i < size and 0 <= new_j < size and grid[new_i][new_j] == target_letters[letter_index]:
        return find_xmas((new_i, new_j), direction, letter_index + 1)
    return False

print(word_search())

################## Part 2 ###################

def word_search_2():
    return sum(
        find_xmas_2((i, j))
        for i in range(size)
        for j in range(size)
        if grid[i][j] == 'A'
    )

def find_xmas_2(loc):
    def get_diagonal_letters(loc, directions):
        return [
            grid[loc[0] + direction[0]][loc[1] + direction[1]]
            for direction in directions
            if 0 <= loc[0] + direction[0] < size and 0 <= loc[1] + direction[1] < size
        ]

    diag1_letters = get_diagonal_letters(loc, [(-1, -1), (1, 1)])
    diag2_letters = get_diagonal_letters(loc, [(1, -1), (-1, 1)])

    return {'M', 'S'}.issubset(diag1_letters) and {'M', 'S'}.issubset(diag2_letters)

print(word_search_2())
