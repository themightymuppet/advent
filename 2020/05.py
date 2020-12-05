import re
import math

def get_input(file):
    data = ''
    with open(file) as f:
        for line in f:
            data += line.replace("\n"," ")
    data = re.split(r' ', data)
    return data

seat_id = []

'''
messy conditionals, clean this up
'''
def get_seats(data):
    for seat in data:  
        seat_min, seat_max = 0, 127
        col_min, col_max = 0, 7
        r_val = 0
        for i, char in enumerate(seat):
            if i == 9:
                if char == 'R':
                    seat_id.append(int(seat_list(r_val, col_max)))
                if char == 'L':
                    seat_id.append(int(seat_list(r_val, col_min)))
            if i == 6:
                if char == 'B':
                    r_val = seat_max
                if char == 'F':
                    seat_max -= math.ceil(float(seat_max - seat_min)/2)
                    r_val = seat_min
            else:
                if char == 'F':
                    seat_max -= math.ceil(float(seat_max - seat_min)/2)
                if char == 'B':
                    seat_min += math.ceil(float(seat_max - seat_min)/2)
                if char == 'R':
                    col_min += math.ceil(float(col_max - col_min)/2)
                if char == 'L':
                    col_max -= math.ceil(float(col_max - col_min)/2)
            # print(char, 'SEAT', seat_min, seat_max, 'COL', col_min, col_max)      
    seat_id.sort()
    print('highest seat: ' + str(seat_id[-1]))
    print(my_seat())


def seat_list(seat, col):
    return seat * 8 + col

def my_seat():
    for x in range(seat_id[0],seat_id[-1]+1):
            if x not in seat_id and x + 1 in seat_id and x - 1 in seat_id:
                return 'my seat: ' + str(x)

get_seats(get_input('input.txt'))

