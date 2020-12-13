import re
from collections import Counter

def get_input(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line.replace('\n',' ')
    data = re.split(r'  ', data)
    return data

# PI
# def customs(data):
#     count = 0
#     for group in data:
#         group = group.replace(' ','')
#         group = set(group)
#         count += (len(group))
#     return count

# PII
def customs(data):
    count = 0
    for group in data:
        showcount = Counter()
        showcount.update(group)
        group = group.split(' ')
        for char in showcount:
            if showcount[char] == len(group):
                count += 1
    return count


print(customs(get_input('input.txt')))