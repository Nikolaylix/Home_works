n = int(input("Введите колличество монеток: "))
count_0 = 0
count_1 = 0
i = 0
coins = []
for i in range(n):
    coins.append(int(input()))
    if coins[i] == 0:
        count_0 += 1
        i += 1
    else:
        count_1 += 1
        i += 1     
if count_1 > count_0:
    print(f'{coins} -> {count_0}')
else:
    print(f'{coins} -> {count_1}')