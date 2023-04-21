n = [2, 1, 6, 1, 5, 3, 8, 9, 2, 9]
k = 4
min = abs(n[0] - k)
for i in n:
    if (abs(n[i] - k)) < min:
        min = abs(n[i] - k)
        a = n[i]
print(a)
