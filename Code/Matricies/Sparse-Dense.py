import sys

filename = sys.argv[1]

file = open(filename,'r')

size = file.readline().split()
rows = int(size[0])
cols = int(size [1])
if rows>cols:
    val = rows
else:
    val = cols
matrix = [[0 for i in range(val)] for j in range(val)]

with file:
    for line in file:
        value = line.split()
        x = int(value[0])
        y = int(value[1])
        matrix[x][y] = int(value[2])

file.close()

file = open(filename,'w')

file.write(str(rows) + " " + str(cols) + "\n")

for i in range(rows):
    for j in range(cols):
        file.write(str(i)+ " " + str(j)+ " " +str(matrix[i][j])+ "\n")
file.close()
