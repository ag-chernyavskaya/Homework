t = input('Введите рускоязычный текст')
ls = t.split(' ')
n = 0
for i in ls:
    if i[0] == 'е':
        n += 1
if n == 0:
    print(f'Нет слов,начинающихся на е')
else:
    print(f'Количество слов, начинающихся на букву е: {n}')


t = input('Введите рускоязычный текст')
ls = t.split(' ')
n = 0
for i in ls:
    if i.startswith('е'):
        n += 1
if n == 0:
    print(f'Нет слов,начинающихся на е')
else:
    print(f'Количество слов, начинающихся на букву е: {n}')
