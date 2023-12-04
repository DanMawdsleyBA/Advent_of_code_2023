import pandas as pd
import numpy as np
import re

f = open("C:/Users/u236618/Documents/Github/Advent_of_code_2023/day3/input.txt", "r")

column_width=140

df=pd.DataFrame()

for line in f.readlines():
    line_list=list(line)
    tmp=re.split(r'\D+', line)
    numbers = list(filter(None, tmp))
    start_index=0
    for num in numbers: #edge case what if two of the same number comup find all
        index=line.find(num,start_index)
        num_length=len(str(num))
        for i in range(num_length):
            line_list[index+i]=int(num)
        start_index=index+num_length
    df_row = pd.DataFrame([line_list])
    df=pd.concat([df,df_row])
df.replace('.', 0, inplace= True)
df.replace('*', -99999, inplace= True)

df=df[range(column_width)]

df = df.map(lambda x: pd.to_numeric(x, errors='coerce') if isinstance(x, (int, float)) else 0)

def check_if_cell_not_near_bomb(df,row,col):   
    row_deltas=[-1,0,1]
    col_deltas=[-1,0,1]
    if row == 0:
        row_deltas.remove(-1)
    elif row == len(df)-1:
        row_deltas.remove(1)
    if col == 0:
        col_deltas.remove(-1)
    elif col == column_width-1:
        col_deltas.remove(1)
    for row_delta in row_deltas:
        for col_delta in col_deltas:
            if df.iloc[row+row_delta,col+col_delta] < 0:
                return False 
    return True

# Replace any numbers that are not near a bomb with 0
for col in range(column_width):
    for row in range(len(df)):
        if df.iloc[row,col] > 0:
            if check_if_cell_not_near_bomb(df,row,col):
                df.iloc[row,col] = 0

# if two of the same number are in order then remove one
for row in range(len(df)):
    for col in range(column_width-1):
        if df.iloc[row,col] > 0:
            if df.iloc[row,col] == df.iloc[row,col+1]:
                df.iloc[row,col]=0

# This is inefficent code but it'll do 

def calculate_gear_value(df,row,col):
    gear_list=[] 
    row_deltas=[-1,0,1]
    col_deltas=[-1,0,1]
    if row == 0:
        row_deltas.remove(-1)
    elif row == len(df)-1:
        row_deltas.remove(1)
    if col == 0:
        col_deltas.remove(-1)
    elif col == column_width-1:
        col_deltas.remove(1)
    for row_delta in row_deltas:
        for col_delta in col_deltas:
            if df.iloc[row+row_delta,col+col_delta] > 0:
                gear_list.append(df.iloc[row+row_delta,col+col_delta])
    if len(gear_list) >= 2:
        gear_value = 1
        for num in gear_list:
            gear_value *= num
        return gear_value
    else:
        return 0 

total_value = 0
for col in range(column_width):
    for row in range(len(df)):
        if df.iloc[row,col] < 0:
            total_value+=calculate_gear_value(df,row,col)

print(f'Total value is: {total_value}')