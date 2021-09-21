string = input("Введите слова через пробел - ").split()
for i, words in enumerate(string, 1):
    print(i, words) if len(words) <= 10 else print(i, words[:10])
