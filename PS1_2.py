#test2-1
import random
rows_m1 = 5
columns_m1 = 10

rows_m2 = 10
columns_m2 = 5

from_value = 0
to_value = 50  

M1 = [[random.randint(from_value, to_value) for _ in range(columns_m1)] for _ in range(rows_m1)]
M2 = [[random.randint(from_value, to_value) for _ in range(columns_m2)] for _ in range(rows_m2)]
print("Matrix M1:")
for row in M1:
    print(row)

print("\nMatrix M2:")
for row in M2:
    print(row)
#test2-2
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError
    
    # 创建相乘后矩阵的模型
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result  # 返回结果矩阵

result = matrix_multiply(M1, M2)
print("\nMatrix Multiplication Result:")
for row in result:
    print(row)
