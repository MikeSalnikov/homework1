num_integer = int(input('Введите целое положительное число - '))
max_num = num_integer % 10
num = num_integer

while num > 0:
    digit = num % 10
    if digit > max_num:
        max_num = digit
        if digit == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_integer} равна {max_num}")

