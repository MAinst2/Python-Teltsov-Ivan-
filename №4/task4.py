import numpy as np

np.random.seed(0)

A = np.random.randint(1, 11, (5, 5))
B = np.random.randint(1, 11, (5, 5))

elem = A * B
mat = A @ B
detA = np.linalg.det(A)
BT = B.T

print("A:")
print(A)
print("\nB:")
print(B)
print("\nПоэлементное произведение:")
print(elem)
print("\nМатричное произведение A@B:")
print(mat)
print("\nОпределитель A:")
print(detA)
print("\nТранспонированная матрица B^T:")
print(BT)

try:
    invA = np.linalg.inv(A)
    np.set_printoptions(suppress=True, precision=4)
    print("\nОбратная матрица A^-1:")
    print(invA)
except np.linalg.LinAlgError:
    print("\nОбратная матрица не существует")

C = A.sum(axis=1)
print("\nC (суммы строк A):")
print(C)

if abs(detA) > 1e-12:
    x = np.linalg.solve(A, C)
    print("\nРешение A*x = C:")
    print(x)
else:
    x = np.ones(A.shape[1], dtype=float)
    print("\nA вырождена. Частное решение A*x = C:")
    print(x)

print("\nПроверка A@x и C:")
print(A @ x)
print(C)
