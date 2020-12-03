import re
db = []

def get_pws(file):
    result = 0
    with open(file) as f:
        for line in f:
            db.append(line)
    for line in db:
        if verify_pw(line) == True:
            result += 1
    return result

# PI
# def verify_pw(pw):
#     split_pass = re.split(r' |-|:|\n', pw)
#     print(split_pass)
#     min_rule = int(split_pass[0])
#     max_rule = int(split_pass[1])
#     char_rule = split_pass[2]
#     db_pw = split_pass[4]
#     pattern = re.findall(char_rule, db_pw)

    
#     if char_rule in db_pw and \
#         len(pattern) >= min_rule and \
#         len(pattern) <= max_rule:
#         return True

 # PII
def verify_pw(pw):
    split_pass = re.split(r' |-|:|\n', pw)
    p1 = int(split_pass[0]) - 1
    p2 = int(split_pass[1]) - 1
    char_rule = split_pass[2]
    db_pw = split_pass[4]
    
    if db_pw[p1] == char_rule or \
        db_pw[p2] == char_rule:
            if db_pw[p1] != db_pw[p2]:
                return True

print(get_pws('input.txt'))

