# 1/ Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open(r'task1.txt', 'w+') as f:
    lines = ["line 1", "\nline 2", "\nline 3", "\nline 4"]
    for line in lines:
        f.write(line)
    f.seek(0)
    f_obj = f.read()
    print(f_obj)

# 2/Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
print("\nTask 2")
with open(r'task2.txt', 'r') as f2:
    content2 = f2.readlines()
    print('Количество строк:', len(content2))
    for num_line, line in enumerate(content2):
        print('В {} строке {} слов'.format(num_line+1, len(line.split())))

# 3/ Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

print("\nTask 3")

names = []
salary = []

# считываем данные из документа
with open(r'task3.txt', 'r+') as f3:
    content3 = f3.readlines()
    for i in content3:
        new_list = i.split()
        names.append(new_list[0])
        salary.append(int(new_list[1]))

# считаем средний доход сотрудников
average = sum(salary)/len(names)
print('Средний доход работников {:.1f} рублей'.format(average))

# смотрим, ккие сотрудники зарабатывают меньше 20000
print('Список сотрудников, которые зарабатывают меньше 20000 рублей')
for i in range(len(salary)):
    if salary[i] < 20000:
        print(names[i])

# 4/ Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
print("\nTask 4")


# считываем данные из документа
lines_read = []

with open(r'task4.txt', 'r+') as f4:
    content4 = f4.readlines()
    for i in content4:
        lines_read.append(i)

with open(r'task41.txt', 'w+',  encoding='utf-8') as f41:
    for line in lines_read:
        content41 = line.split()
        if content41[0] == 'One':
            content41[0] = 'Один'
        elif content41[0] == 'Two':
            content41[0] = 'Два'
        elif content41[0] == 'Three':
            content41[0] = 'Три'
        elif content41[0] == 'Four':
            content41[0] = 'Четыре'
        content41 = str(content41[0] + ' - ' +content41[2] + '\n')
        print(content41)
        f41.write(content41)

# 5/ Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
print("\nTask 5")

lines_write = [1, 2, 3, 4, 5, 6, 7, 8, 9]
with open(r'task5.txt', 'w+',  encoding='utf-8') as f5:
    for line in lines_write:
        f5.write(str(line) + ' ')
sum = 0
with open(r'task5.txt', 'r+',  encoding='utf-8') as f51:
    content5 = f51.read()
    print(content5)
    content5 = content5.split()
    for i in content5:
        i = int(i)
        sum += i
print(sum)


# 6/ Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
# и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
print("\nTask 6")

dict = {}
lines_read6 = []
with open(r'task6.txt', 'r+', encoding='utf-8') as f6:
    content6 = f6.readlines()
    for line in content6:
        l = line.split()
        les = l[0]
        lect = ''.join(c for c in l[1] if c.isdigit())
        prac = ''.join(c for c in l[2] if c.isdigit())
        labs = ''.join(c for c in l[3] if c.isdigit())

        if lect == '':
            lect = 0
        if prac == '':
            prac = 0
        elif labs == '':
            labs = 0

        sum = int(lect) + int(prac) + int(labs)

        dict[les[0:-1]] = sum

print(dict)

# 7/ Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

print("\nTask 7")
import json
import math

firm_dict = {}
average_profit = []
with open('task7.txt') as f7:
    lines = f7.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)
print(average_profit)

#   у меня не получилось использовать функцию sum, выдавало ошибку int is not callable. не смогла разобраться из-за чего. составилас свою функцию посчета
def amount(list):
    for i in list:
        i += i
    return i

average_profit = amount(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('task7.json', 'w') as f7_json:
    json.dump(out_info,f7_json)

with open('task7.json') as f7_json:
    print(json.load(f7_json))


