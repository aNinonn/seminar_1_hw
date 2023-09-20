# Треугольник существует только тогда, когда сумма любых двух его 
# сторон больше третьей. Дано a, b, c - стороны предполагаемого 
# треугольника. Требуется сравнить длину каждого отрезка-стороны с 
# суммой двух других. Если хотя бы в одном случае отрезок окажется 
# больше суммы двух других, то треугольника с такими сторонами не 
# существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

first_length = int(input("Введите длину 1 стороны треугольника: "))
second_length = int(input("Введите длину 2 стороны треугольника: "))
third_length = int(input("Введите длину 3 стороны треугольника: "))

if (first_length + second_length) <= third_length or (first_length + third_length) <= second_length or (second_length + third_length) <= first_length:
    print ("Такого треугольника не существует")
else:
    if first_length == second_length == third_length: 
        print("Ваш треугольник равносторонний")
    elif first_length == second_length or second_length == third_length or third_length == first_length:
        print("Ваш треугольник равнобедренный")
    else:
        print("Ваш треугольник разносторонний")