in_time = input("Введите часы и минуты(пример 07.30 или 13.15): ")

time = 23.60

try:
    in_time = float(in_time)
except ValueError:
    print("Вы не ввели дробное число!(пример 20:30 или 03.40)")
    exit()

try:
    if in_time > 23.59:
        raise ValueError()
except ValueError:
    print("Столько часов или минут не может быть! Введите число от 00.00 до 23.59")
    exit()

    
time_und = time-in_time
ts = str(time_und)

tn = ts[0] + ts[1] , ts[3] + ts[4] 

print("Первое число количество часов, второе количество минут до следуйщего дня: ", tn)

#VN: интересное решение)
#TW: согласен)))
