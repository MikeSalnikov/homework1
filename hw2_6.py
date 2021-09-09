my_list = []
title = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
feature = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:

    for f in title.keys():
        product = input(f'Введите данные по товару {f} - ')
        title[f] = int(product) if (f == 'цена' or f == 'количество') else product
        feature[f].append(title[f])
    my_list.append((num, title.copy()))
    print(f"\nИтого\n{my_list}")
    for key, value in feature.items():
        print(f"{key[:25]:>30}: {value}")