'''В кружке по борьбе занимаются 8 человек: Круглов Алексей,
Ворожейкин Борис, Митин Сергей, Алешин Сергей, Кутиков
Владимир, Круглов Денис, Бочкин Иван и Мечников Алексей.
Выведите список учеников в алфавитном порядке. Подсчитайте,
сколько в группе Сергеев, Денисов и Алексеев? Есть ли в группе
однофамильцы? Через два месяца после начала занятий Бочкин
Иван перестал посещать кружок, однако пришли новые
мальчики: Фомин Петр и Краснов Дмитрий. Отредактируйте
список учеников соответствующим образом.'''

e = ['Круглов Алексей', 'Ворожейкин Борис', 'Митин Сергей', 'Алешин Сергей',
     'Кутиков Владимир', 'Круглов Денис', 'Бочкин Иван', 'Мечников Алексей']
f = ['Фомин Петр', 'Краснов Дмитрий']
new_e = sorted(e)
print(new_e)
c = str(e).count('Сергей')
d = str(e).count('Денис')
a = str(e).count('Алексей')
print(c, d, a)
new_e.remove('Бочкин Иван')
print(new_e)
new_e.extend(f)
print(new_e)