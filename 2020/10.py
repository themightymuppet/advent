import re

def get_input(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line
    data = re.split(r'\n', data)
    data = list(map(int, data))
    data.sort()
    return data

diff = { 1:0, 2:0, 3:1 }

# PI
def check_adapters(data):
    adpt_tracker = 0
    index_tracker = 0
    for i, adpt in enumerate(data):
        if i == index_tracker:
            if adpt == adpt_tracker + 1:
                diff[1] += 1
                adpt_tracker += 1
            if adpt == adpt_tracker + 2:
                diff[2] += 1
                adpt_tracker += 2
            if adpt == adpt_tracker + 3:
                diff[3] += 1
                adpt_tracker += 3
            index_tracker += 1

def solution():
    check_adapters(get_input('input.txt'))
    ones, threes = diff.get(1), diff.get(3)
    solution = ones * threes
    return (solution, diff)

print(solution())