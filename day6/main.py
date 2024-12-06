import copy 

grid, path = [], []
start_point= (-1,-1)
directions = {'up' : (-1, 0), 'right': (0, 1), 'down': (1,0), 'left': (0, -1)}

with open('./inputs/input6.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

def find_start_point():
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '^':
                grid[i][j] = '.'
                return (i,j)
                   
def turn_right(direction):
    return {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}[direction]

def in_bounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid)

def find_path(grid, start_point):
    x, y = start_point
    stack = [(x, y, 'up')]
    path = set()
    loop_detected = False

    while stack:
        x, y, dir = stack.pop()
        if (x,y, dir) in path:
            loop_detected = True
            return path, loop_detected

        new_x, new_y = x + directions[dir][0], y + directions[dir][1]

        if in_bounds(new_x, new_y):
            if grid[new_x][new_y] != '#':
                path.add((x, y, dir))
                stack.append((new_x, new_y, dir))
            else:
                new_dir = turn_right(dir)
                stack.append((x, y, new_dir))
        else:
            path.add((x, y, dir))

    path = set((a, b) for a, b, _ in path)          
    return path, loop_detected

start_point = find_start_point()

########### Part 1 #############

path, _ = find_path(grid,start_point)
print(len(path))

########### Part 2 #############

def find_loops(path):
    loops = []
    grid_copy = copy.deepcopy(grid)

    for x, y in path:
        if (x,y) != start_point:
            grid_copy[x][y] = '#'
            _ , loop = find_path(grid_copy, start_point)
            loops.append(loop)
            grid_copy[x][y] = grid[x][y]
    return sum(loops)

print(find_loops(path))