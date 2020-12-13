import re

rule_dict = {}
contains_gold = []

def get_input(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line
    data = re.split(r'\n', data)
    for rule in data:
        key, val = rule.split(" bags contain ")
        rule_dict[key] = val
    return data

# PI
def find_gold(data):
    for k, v in rule_dict.items():
        if 'shiny gold' in v:
            contains_gold.append(k)
    for bag in contains_gold:
        check_rules(bag)
    return len(set(contains_gold))        

def check_rules(bag):
    # print (bag)
    for k, v in rule_dict.items():
        if bag in v:
            contains_gold.append(k)

print(find_gold(get_input('input.txt')))
