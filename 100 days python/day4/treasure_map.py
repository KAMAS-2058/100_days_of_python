# using indicies
row1 = ['#','#','#']
row2 = ['#','#','#']
row3 = ['#','#','#']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to bury the treasure?')

horizontal = int(position[0])-1
vertical = int(position[1])-1

column_slt = map[vertical]
column_slt[horizontal] = "X"

print(f'{row1}\n{row2}\n{row3}')
#its pretty neat