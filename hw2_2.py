spisok = list(input("Введите числа - "))

for i in range(1, len(spisok), 2):
    spisok[i - 1], spisok[i] = spisok[i], spisok[i - 1] #не уверен что именно это просят сделать, но вроде похоже
print(spisok)