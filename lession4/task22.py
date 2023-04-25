n = int(input('Ввидите кол-во элементов 1-го множества: '))
m = int(input('Ввидите кол-во элементов 2-го множества: '))
list_1 = set(map(int, input(f'введи {n} цифр через пробел: ').split()))
list_2 = set(map(int, input(f'введи {m} цифр через пробел: ').split()))
n = len(list_1)
m = len(list_2)
list_3 = list_1.intersection(list_2)

print(sorted(list_3))