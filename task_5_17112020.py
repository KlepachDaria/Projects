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
