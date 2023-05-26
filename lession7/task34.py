song = 'пара-ра-рам рам-пам-папам па-ра-па-да'
keys = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
rythm = song.split()
result = list()
for i in rythm:
    count = 0
    for j in i:
        if j in keys:
            count +=1
    result.append(count)
if len(set(result)) == 1:
    print('Парам пам-пам')
else: print('Пам парам')