list = [5, 6.5, None, False, 'Str', [5, 4], ('hello', 'word'),
           (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10},
           range(5)]

for i, item in enumerate(list, 1):
    print(f"{i}) {item} - {type(item)}")