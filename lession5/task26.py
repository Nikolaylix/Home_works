A = int(input('Введите A: '))
B = int(input('Введите B: '))

def fact(A, B):
    if B == 1:
        return A
    if B != 1:
        return(A*fact(A, B -1))

print(fact(A, B))