import re

def get_passports(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line.replace("\n"," ")
    data = re.split(r'  ', data)
    return data

def verify_pspts(pspts):
    valid = 0
    for passport in pspts:
        validator = dict(item.split(":") for item in passport.split(" "))
        if 'byr' in validator.keys() and re.match(r'^(19)[2-9][0-9]|^(200)[0-2]', validator.get('byr')) and \
            'iyr' in validator.keys() and re.match(r'^(20)[1]{1}[0-9]{1}|2020$', validator.get('iyr')) and \
            'eyr' in validator.keys() and re.match(r'^(202)[0-9]{1}|2030$', validator.get('eyr')) and \
            'ecl' in validator.keys() and re.match(r'amb|blu|brn|gry|grn|hzl|oth', validator.get('ecl')) and \
            'hcl' in validator.keys() and re.match(r'^#[a-f0-9]{6}$', validator.get('hcl')) and \
            'pid' in validator.keys() and re.match(r'^[0-9]{9}$', validator.get('pid')) and \
            'hgt' in validator.keys():
            if re.match(r'(^(15|16|17|18)[0-9]|^(19)[0-3])(cm$)', validator.get('hgt')): #150-193
                valid += 1
            elif re.match(r'(^(59)|^(6)[0-9]|^(7)[0-6])(in$)', validator.get('hgt')): #59-76
                valid += 1
    print(valid)

verify_pspts(get_passports('input.txt'))