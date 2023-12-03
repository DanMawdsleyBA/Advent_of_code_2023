import re

f = open("C:/Users/u236618/Documents/Github/Advent_of_code_2023/day1/input.txt", "r")
total=0

part = 2

def first_last_num_in_string(part, line):
    num_strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_word_dict={'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    first_char=None
    first_index=None
    current_valid_char=None
    current_valid_index=None
    for try_first_index, char in enumerate(line):
        if char in num_strings:
            current_valid_char = char
            current_valid_index = try_first_index
            if first_char is None:
                first_char = char
                first_index = try_first_index
    last_char = current_valid_char 
    last_index = current_valid_index

    if part == 2:
        for num_word, num_string in num_word_dict.items():
            try_first_index = line.find(num_word)
            try_last_index = line.rfind(num_word)
            if try_first_index == -1:
                continue 
            if first_index is None:
                first_index = try_first_index
                first_char = num_string
            elif try_first_index < first_index:
                first_index = try_first_index
                first_char = num_string
            if last_index is None:
                last_index = try_last_index
                last_char = num_string     
            elif try_last_index > last_index:
                last_index = try_last_index
                last_char = num_string
    # print(first_char,last_char)
    return int(first_char+last_char)
        

for line in f.readlines():
    total+=first_last_num_in_string(2,line)

print(f'Part {part} Total number is :\n{total}')

