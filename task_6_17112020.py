num_a = int(input("Введите результат в 1-й день: "))
num_b = int(input("Введите ожидаемый результат: "))
days = 0
km = 0
while km < num_b:
    km = num_a * (1.1**days)
    days = days + 1
print("Через ", days, "days ")
