n = int(input("Введите длину шоколадки: "))
a = int(input("Введите ширину шоколадки: "))
b = int(input("Сколько долек ломим: "))
if b < n * a and ((b % n == 0) or (b % a == 0)):
    print('yes')
else:
    print('no')