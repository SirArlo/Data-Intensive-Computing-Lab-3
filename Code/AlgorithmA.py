import mrs
import string
import os

class MatrixMultiply(mrs.MapReduce):
    CurrentFile = '0'
    Col = 0
    Row = 0
    Index = 0
    A = []
    B = []
    def map(self, key, value):
        for line in value.splitlines():
            word = (str(line)).split(' ')
            if len(word) == 2:
                MatrixMultiply.CurrentFile = str(int(MatrixMultiply.CurrentFile) + 1)
                if MatrixMultiply.CurrentFile == '1':
                    MatrixMultiply.Index = int(word[0])
                    MatrixMultiply.Row = int(word[1])
                if MatrixMultiply.CurrentFile == '2':
                    MatrixMultiply.Col = int(word[0])			
            if len(word) == 3:
                i,j,val = word[0],word[1],(word[2])
                if int(i) < 10:
                    i = '0'+i
                if int(j) < 10:
                    j = '0'+j
                if line:
                    if MatrixMultiply.CurrentFile == '1':
                        yield (j,MatrixMultiply.CurrentFile+' '+i+' '+val)
                    if MatrixMultiply.CurrentFile == '2':
                        yield (i,MatrixMultiply.CurrentFile+' '+j+' '+val)

    def reduce(self, key, values):
	listA = []
	listB = []
	output = [[0 for x in range(MatrixMultiply.Row)] for y in range(MatrixMultiply.Col)]
	matrixVal = 0
	for i in values:
		File, RowCol, val = i.split(' ')
		newVal = RowCol, val
		if File == '1':
			listA.append(newVal)
		if File == '2':
			listB.append(newVal)
	MatrixMultiply.A.append(sorted(listB, key=lambda value: value[0]))
	MatrixMultiply.B.append(sorted(listA, key=lambda value: value[0]))
	if len(MatrixMultiply.A) == MatrixMultiply.Row and len(MatrixMultiply.B) == MatrixMultiply.Col:	
		for i in range(MatrixMultiply.Row):
			for j in range(MatrixMultiply.Col):
				output[i][j] = 0
				tempA = MatrixMultiply.A[i]
				tempB = MatrixMultiply.B[j]			
				for k in range(MatrixMultiply.Index):
					output[i][j] += int(MatrixMultiply.A[i][k][1])*int(MatrixMultiply.B[j][k][1])
				yield i,j,output[i][j]

if __name__ == '__main__':
    mrs.main(MatrixMultiply)
