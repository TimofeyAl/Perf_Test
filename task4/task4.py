import sys

file = sys.argv[1]

nums = []

with open(f'{file}', "r", encoding="utf-8") as file: # Открытие и форматирование файла
    for line in file:
        Nums = line.strip().rsplit(maxsplit=-1)
        nums.append(*Nums)

nums = [int(i) for i in nums] # Приведение значений nums к типу данных int

counter = 0 # Счетчик ходов

md = sorted(nums)[len(nums) // 2] # Нахождение медианного значения

# Функция приводит каждый элемент к медианному значению, записывая каждый ход в счетчик
for i in range(len(nums)):
    if nums[i] < md:
        while nums[i] != md:
            nums[i] += 1
            counter += 1
    elif nums[i] == md:
        continue
    else:
        while nums[i] != md:
            nums[i] -= 1
            counter += 1

print(counter)