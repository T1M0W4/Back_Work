thre_dig_num = int(input("Введите трехзначное число: "))

sec_num = (thre_dig_num // 10 % 10)
#VN:      ^                       ^  скобки не нужны

print("Ваше двухзначное число: ", sec_num)
#VN:        ^^^^^^^^^^^  наверное, вы имели в виду "Вторая цифра вашего числа: "