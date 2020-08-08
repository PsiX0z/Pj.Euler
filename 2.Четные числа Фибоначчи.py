# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

f1 = 1 # Первое число
f2 = 2 # Второе число

n = 50 # кол-во чисел в ряде (берем от балды большое, у нас ограничитель)
a = [f1, f2] # список ряда фибиначи начиная с 1 и 2

for i in range(3,n): # Наш цикл чисел начиная с третьего (1,2 уже есть в списке)
    f3 = f1 + f2 # Третье число = сумма предыдущих
    f1 = f2 # Первое число = второе (следующее)
    f2 = f3 # Второе число = третье (следующее)
    if f2 > 4000000: # Ограничение макс числа в 4.000.000
        break
    a.append(f2) # Добавляем каждое число в наш список


num = len(a) # Кол-во чисел в ряде (32)
b = [] # Будующий список с четными числами из предыдущего


for i in range(num): # Делаем операцию с каждым числом списка а
    if a[0] % 2 == 0: # Если "первое число списка а" делиться на 2 без остатка: (ищем четное число)
        b.append(a[0]) # То добавляем его в список с четными
        a.remove(a[0]) # Удаляем первое значение?
    else: # Если нечетное
        a.remove(a[0]) # Просто удаляем его

print(sum(b)) # Показать сумму списка
