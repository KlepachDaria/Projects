num = input("Введите целое положительное число: ")
i = 0
big_num = 0
while i < len(num):
    if big_num < int(num[i]):
        big_num = int(num[i])
    else:
        i = i + 1
print("Самое большое число: ", big_num)
