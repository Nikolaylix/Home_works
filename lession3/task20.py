eng = 'qwertyuiopasdfghjklzxcvbnm'

ru = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_Eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово: ')

if word[0].lower() in eng:
    sum = 0
    for letter in word:
        for key, value in list_Eng.items():
            if letter.upper() in value:
                sum += key
    print(sum)
else:
    if word[0].lower() in ru:
        sum = 0
        for letter in word:

            for key, value in list_Ru.items():
                if letter.upper() in value:
                    sum += key
    print(sum)