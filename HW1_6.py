while True:
    days = 1
    start = float(input('Введите дистанцию, которую пробеает спортсмен за первый день - '))
    last = float(input('Введите дистанцию, к которой готовиться спортсмен - '))
    if start <= 0 or last <= 0:
        print('Результаты должны быть больше нуля! Стартовое значение != 0')
    else:
        while start < last:
            start *= 1.10
            days += 1
        print(f'Спрортмену нужно на подготовку к забегу {days} день(дней)')
