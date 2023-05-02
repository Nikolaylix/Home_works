a1 = int(input('Введите первый эллемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите кол-во элементов: '))
result = []
for i in range(1, n+1):
    result.append(a1 + d*(i-1))

print(result)