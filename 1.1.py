import math


sqrt_62 = math.sqrt(62)
division_7_22 = 7 / 22


print(f"Точне значення √62: {sqrt_62}")
print(f"Точне значення 7/22: {division_7_22}")


error_sqrt_62 = abs(sqrt_62 - 7.87)
error_division_7_22 = abs(division_7_22 - 0.318)


print(f"Абсолютна похибка для √62: {error_sqrt_62}")
print(f"Абсолютна похибка для 7/22: {error_division_7_22}")


if error_sqrt_62 < error_division_7_22:
    print("Рівність для √62 є точнішою.")
else:
    print("Рівність для 7/22 є точнішою.")
