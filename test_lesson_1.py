# task_1 Work with variables
print("Hello world! This is my task 1")

a = 2
print(a)

b = int(input("Введите число: "))
print(b)

# task_2 Counting hours, minutes, seconds

time = int(input("Введите время в секундах: "))
hours = time//3600
minutes = (time-hours*3600)//60
seconds = (time-hours*3600-minutes*60)
print("{}:{}:{}".format(hours, minutes, seconds))

# task_3 Find the sum of the numbers
num = input("Введите число: ")
one_num = int(num)
two_num = int(num + num)
three_num = int(num + num + num)
print(one_num + two_num + three_num)

# task_4 Find the largest number
num = input("Введите целое положительное число: ")
i = 0
big_num = 0
while i < len(num):
    if big_num < int(num[i]):
        big_num = int(num[i])
    else:
        i = i + 1
print("Самое большое число: ", big_num)

# task_5 Project profitability
revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
delta = revenue - costs
if delta > 0:
    print("Проект прибыльный")
    profit = delta/revenue*100
    workers = int(input("Введите количество работников: "))
    print("Рентабельность проекта = ", "{:.2f}".format(profit), "%")
    print("Прибыль на 1 сотрудника ", delta/workers, " руб.")
elif delta < 0:
    print("Проект убыточный")
else:
    print("Разница равна 0")

# task_6 Count days and kilometers
num_a = int(input("Введите результат в 1-й день: "))
num_b = int(input("Введите ожидаемый результат: "))
days = 0
km = 0
while km < num_b:
    km = num_a * (1.1**days)
    days = days + 1
print("Через ", days, "days ")



