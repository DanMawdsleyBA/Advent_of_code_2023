import pandas as pd

f = open("C:/Users/u236618/Documents/Github/Advent_of_code_2023/day2/input.txt", "r")

df=pd.DataFrame(columns=['Game', 'Set', 'red', 'blue', 'green'])

for line in f.readlines():
    game = line.split(':')[0].split(' ')[-1]
    for set, set_data in enumerate(line.split(':')[-1].split(';')):
        row={'Game': game, 'Set': set+1, 'red': 0, 'blue': 0, 'green': 0}
        for set_data_part in set_data.split(','):
            colour=set_data_part.strip().split(' ')[-1]
            num=int(set_data_part.strip().split(' ')[0])
            row[colour]=num
        row=pd.DataFrame([row])
        df=pd.concat([df,row])

non_matches= df[(df['red']>12) | (df['green']>13) | (df['blue']>14)]

unique_non_matches=non_matches['Game'].unique().astype(int).sum()

total_number=df['Game'].unique().astype(int).sum()

print(f'Part 1 answer is: {total_number-unique_non_matches}')

df[['red', 'blue', 'green']]=df[['red', 'blue', 'green']].astype(int)
game_group_by = df.groupby(['Game'])[['red', 'blue', 'green']].max()

game_group_by['Total']=game_group_by['red']*game_group_by['blue']*game_group_by['green']

part_2_anser=game_group_by['Total'].sum()

print(f'Part 2 answer is: {part_2_anser}')
    