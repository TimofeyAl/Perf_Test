import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
circle = []
dots = []

def dot_location(R:int, x0:float, y0:float, x:float, y:float): # Функция принимает радиус, координаты центра окружности и координаты точки, выводит положение точки
	if (x - x0) * 2 + (y - y0) * 2 == R * 2:
		print(0, end="\n")
	elif (x - x0) * 2 + (y - y0) * 2 <= R * 2:
		print(1, end="\n")
	else:
		print(2, end="\n")

with open(f'{file1}', "r", encoding="utf-8") as file: # Открытие файла
    for i in file: 
        circle.append(i.strip().rsplit(maxsplit=-1)) # Перенос значений файла в список circle

R, x0, y0 = int(*circle[1]), float(circle[0][0]), float(circle[0][1])

with open(f'{file2}', "r", encoding="utf-8") as file: # Открытие файла
    for j in file:
        dots.append(j.strip().rsplit(maxsplit=-1)) # Перенос значений файла в список dots

counter = 1 # Cчет количества прошедших через функцию точек, значение не должно привышать 101
for k in dots:
    if counter <= 100:
        x, y = float(k[0]), float(k[1])
        dot_location(R, x0, y0, x, y) # Вызов функции для определения положения точки относительно
        counter += 1
    else:
        break