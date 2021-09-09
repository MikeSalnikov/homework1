my_list = [6, 5, 4, 4, 3, 3, 2, 1]
number = int(input('Введите новое натуральное число - '))
i = 0
for n in my_list:
    if number <= n:
        i += 1
my_list.insert(i, int(number))
print(my_list)