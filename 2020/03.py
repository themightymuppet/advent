map = []
def get_map(file):
    with open(file) as f:
        for line in f:
            map.append((line.replace("\n", "")) * 200)
    
def travel(map):
    get_map('input.txt')
    trees = 0
    x = 0
    y = 0
    while y < (len(map)):
        if (map[y][x]) == '#':
            trees += 1
        x += 1
        y += 2
    return trees

print(travel(map))