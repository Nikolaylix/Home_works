a = int(input('Введите a: '))
b = int(input('Введите b: '))

def result(a, b):
    if b == 0:
        return a
    return result(a + 1, b - 1)

print(result(a, b))