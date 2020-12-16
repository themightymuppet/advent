import re

def get_input(file):
    data = ''
    instructions = []
    with open(file) as f:
        for line in f:
            data += line
    data = (re.split(r'\n', data))
    for instruction in data:
        instruction = (re.split(r' ', instruction))
        instructions.append(instruction)
    return instructions

# #PI
def get_acc(data):
    acc = 0
    tracker = 0
    parsed = []
    while tracker not in parsed:
        if 'acc' in data[tracker][0]:
            parsed.append(tracker)
            acc += int(data[tracker][1])
            tracker += 1
        if 'jmp' in data[tracker][0]:
            parsed.append(tracker)
            tracker += (int(data[tracker][1]))
        if 'nop' in data[tracker][0]:
            parsed.append(tracker)
            tracker += 1
    return acc

print(get_acc(get_input('input.txt')))
