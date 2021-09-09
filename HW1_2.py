time = int(input("Введите время в секундах - "))
hour = time // 3600
minut = (time // 60) - (hour * 60)
second = time % 60
print(f"{hour:02}:{minut:02}:{second:02}")


# time = int(input("Введите время в секундах"))
# hours = time // 3600
# minutes = time / 60
# seconds = minutes / 60
# print(f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}")

