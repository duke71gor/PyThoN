print('{:*^20s}'.format('Задача-1'))
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruite = ['apple', 'banan', 'kiwi', 'watermelon']
for i in range(len(fruite)):
	print('# {} {:>10}'.format(i+1, fruite[i]))

# Подсказка: воспользоваться методом .format()

print('{:*^20s}'.format('Задача-2'))
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = [0,1,2,3,4,5,6]
print('list1 = ', list1)
list2 = [4,5,6,7,8,9,10]
print('list2 = ', list2)
list1ex2 = []
for item in set(list1).difference(list2):
	list1ex2.append(item)
print('list1 without elements of  list2', list1ex2)

print('{:*^20s}'.format('Задача-3'))
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
listNew = []
print('произвольный список:', list)
for i in list:
	if (i % 2 == 0):
		i = i / 4
		listNew.append(i)
	else:
		i = i * 2
		listNew.append(i)
print('NEW list is: ', listNew)