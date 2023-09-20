# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после 
# каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)
user_number = 0

while user_number != num:
    user_number = int(input("Введите предпологаемое число: "))
    if user_number < num:
        print("Загаданное число больше")
        continue
    else:
        print("Загаданное число меньше")
        continue

print("Ура! Вы угадали")