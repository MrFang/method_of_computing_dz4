from findRoots import findRoots
from utils import readMatrixFromFile
import matplotlib.pyplot as plt

from math import exp, sin, pi

matrix = readMatrixFromFile('input.txt')

# Выделяем столбец свободных членов
col = [row[len(matrix)] for row in matrix]

# Удаляем столбец свободных членов из матрицы
for i in range(len(matrix)):
    matrix[i] = matrix[i][:-1]

coff = findRoots(matrix, col)

coff_1 = coff[:4]
coff_2 = coff[4:]

def f(x):
    return exp(2*sin(x))

def S_1(x):
    return coff_1[0] * x**3 \
        + coff_1[1] * x**2 \
        + coff_1[2] * x \
        + coff_1[3]

def S_2(x):
    return coff_2[0] * x**3 \
        + coff_2[1] * x**2 \
        + coff_2[2] * x \
        + coff_2[3]

def integrate(f, start, end):
    EPS = 5 * 10**(-5)

    def sympson_integrate(n):
        r = 0;
        step = (end - start) / n

        for k in range(1, n+1):
            c = start + (end -start)*(k - 0.5)/n
            r += f(start + step*(k-1)) + 4*f(c) + f(start + step*k)
        
        return r*(end - start)/(6*n)

    n = 2
    s1 = sympson_integrate(n)

    while(True):
        s2 = sympson_integrate(2*n)

        if (abs(s1 - s2)) < 15*EPS:
            return s2
        
        s1 = s2
        n = 2*n

x = [i*pi/200 for i in range(101)]

f_y = [f(x) for x in x]
S_y = [S_1(x) if x < pi/4 else S_2(x) for x in x]

plt.plot(x, f_y, label='f')
plt.plot(x, S_y, label = 'S')
plt.legend()
plt.show()

print(
    f'Первый многочлен (0 <= x <= pi/4): {coff_1[0]:3.2f}(x^3) + {coff_1[1]:3.2f}(x^2) + {coff_1[2]:3.2f}x + {coff_1[3]:3.2f}\n'
    f'Второй многочлен (pi/4 <= x <= pi/2): {coff_2[0]:3.2f}(x^3) + {coff_2[1]:3.2f}(x^2) + {coff_2[2]:3.2f}x + {coff_2[3]:3.2f}\n'
    f'Интеграл от f на [0, pi/2] = {integrate(f, 0, pi/2):3.2f}'
)
