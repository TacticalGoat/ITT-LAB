mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]

def mat_mul(a,b):
	rows_a = len(a)
	rows_b = len(b)
	cols_a = len(a[0])
	cols_b = len(b[0])
	if cols_a != rows_b:
		print "Cannot Multiply"
		return None
	c = [[0 for row in range(cols_b)] for col in range(rows_a)]
	for i in range(rows_a):
		for j in range(cols_b):
			for k in range(cols_a):
				c[i][j] += a[i][k] * b[k][j]

	return c

print mat_mul(mat1,mat2)