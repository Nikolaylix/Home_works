arr = [-2, 8, 1, -3, 0, -6, 6, 1, 4, 9, 1, -5, -10, 6, 9, 10, 0, -6, -1, 10]
print(arr)
maximum = 3
minimum = 1
for i in range(len(arr)):
	if minimum <= arr[i] <= maximum:
            print(i)