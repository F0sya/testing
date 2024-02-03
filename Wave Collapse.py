

with open('matrix.txt', 'r') as f:
    matrix = [[num.replace("\n",'') for num in line.split(',')] for line in f]
for row in matrix:
    if 'S' in row:
        rat_x = row.index('S')
        rat_y = matrix.index(row)
    elif 'E' in row:
        cheese_x = row.index('E')
        cheese_y = matrix.index(row)
    print(*row)
directions = [-1,]