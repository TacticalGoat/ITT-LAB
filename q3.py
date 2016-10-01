mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]
mat3 = [map(sum,zip(*t)) for t in zip(mat1,mat2)]
print mat3