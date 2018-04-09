import mrs
import string
import os

class MatrixMultiply(mrs.MapReduce):
	CurrentFile = '0'
	Col = 0
	Row = 0
	OutputCol = 0
	OutputRow = 0

	def map(self, key, value):
		for line in value.splitlines():

			word = (str(line)).split(' ')
		if len(word) == 2:
			MatrixMultiply.CurrentFile = str(int(MatrixMultiply.CurrentFile) + 1)
			MatrixMultiply.Row = int(word[0])
			MatrixMultiply.Col = int(word[1])
		if len(word) == 3:
			i,j,val = word[0],word[1],word[2]
			if int(j) < 10:
				j = '0' + j
			if int(i) < 10:
				i = '0' + i
			if line:
				if MatrixMultiply.CurrentFile == '1':
					for k in range(MatrixMultiply.Col):
						if k < 10:
							yield ('0'+str(k)+' '+j, i+' '+val)
						else:
							yield (str(k)+' '+j, i+' '+val)
				if MatrixMultiply.CurrentFile == '2':
					for k in range(MatrixMultiply.Row):
						if k < 10:
							yield (i+' '+'0'+str(k), j+' '+val)
						else:
							yield (i+' '+str(k), j+' '+val)

	def reduce(self, key, values):
		val = []
		for k in range(MatrixMultiply.Col):
			indexTemp, valTemp = values.next().split(' ')
			val.append(int(valTemp))
		for k in range(MatrixMultiply.Col):
			indexTemp, valTemp = values.next().split(' ')
			val[k] *= int(valTemp)
		yield sum(val)

if __name__ == '__main__':
    mrs.main(MatrixMultiply)
