import sys

n = int(sys.argv[1])  
m = int(sys.argv[2])

m -= 1
interv_m = [2]
result = []

def new_second_sp(): # Функция создает интервалы движения по заданному массиву длинной m
    interv_m = []
    interv_m.append(result[-1])
    ind = 1 + first_sp.index(result[-1])
    while len(interv_m) != m + 1:
        interv_m.append(first_sp[ind % len(first_sp)])
        ind += 1
    return interv_m

first_sp = [int(i) for i in range(1, n + 1)] # Формирование списка с длинной n

result.append(1)
result.append(first_sp[m % len(first_sp)]) # Деление с остатком m на длинну списка позволяет вызвать элемент с индесом m без создания кругового массива

while interv_m[-1] != 1: # Цикл продолжит работу пока последний элемент списка не будет равен 1
    interv_m = new_second_sp() # Вызов функции для создания списка с интервалом m
    result.append(interv_m[m % len(first_sp)])

result.pop(-1)
    
result = "".join(str(j) for j in result) 

print(result)