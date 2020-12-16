import re

def get_input(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line
    data = re.split(r'\n', data)
    return data

# PI
def break_xmas(data):
    for n, d in enumerate(data):
        if n > 24:
            preamble = data[n-25:n]
            test_num = verify_sum(d,preamble)
            if test_num is False:
                return d

def verify_sum(num, preamble):
    verified_sums = []
    for x in set(preamble):
        y = int(num) - int(x)
        # print('!', num, x, y)
        if str(y) in preamble:
            verified_sums.append(y)
    if not verified_sums:
        return False
    return True

# PII
def find_weakness(num, data):
    data = list(map(int, data))
    for n in range(len(data)):
        for x in range(n+1, len(data)):
            if sum(data[n:x]) == int(num):
                preamble = data[n:x]
                preamble.sort()
                return preamble[0] + preamble[-1]

num = break_xmas(get_input('input.txt'))
data = (get_input('input.txt'))
print('PI',num)
print('PII', find_weakness(num,data))