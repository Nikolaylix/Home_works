a = int(input('введи кол-во элементов первого множества: '))
b = int(input('введи кол-во элементов второго множества: '))
spisok_1 = set(map(int, input(f'введи {a} цифр через пробел: ').split()))
spisok_2 = set(map(int, input(f'введи {b} цифр через пробел: ').split()))
a = len(spisok_1)
b = len(spisok_2)
spisok_3 = spisok_1.intersection(spisok_2)

print(f'список уникальных символов {sorted(spisok_3)}')