# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import random

d = input('Введите число d c заданной точност: ').count("0")
number = random.uniform(0, 10.0)
print(f'Число с заданной точностью {d} знаков после запятой - {round(number, d)}')
