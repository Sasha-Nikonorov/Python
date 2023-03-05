import numpy as np
from scipy import stats

football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

f_value, p_value = stats.f_oneway(football_players, hockey_players, weightlifters)

print("F-value: ", f_value)
print("P-value: ", p_value)

if p_value < 0.05:
    print(
        "Отклонить нулевую гипотезу, существует разница в среднем росте футболистов, хоккеистов и тяжелоатлетов")
else:
    print("Принимаем нулевую гипотезу, нет разницы в среднем росте футболистов, хоккеистов и тяжелоатлетов")
