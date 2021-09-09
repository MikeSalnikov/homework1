proceeds = float(input("Введите занчение выручки - "))
costs = float(input("Введите занчение издержек - "))
result = proceeds - costs
if result > 0:
    print(f"Ваша компания работает с прибылью {result} !")
    print(f"Рентабельность выручки - {result / proceeds:.2f}")
    employees = int(input("Сколько человек работает в вашей комапании? - "))
    print(f"Прибыль в расчете на одного сотрудника - {result / employees:.2f}")
elif result < 0:
    print(f"Вы работаете с убытком, необходимо сократить издержки на - {-result} а потом пересмотреть стратегию компании")
else:
    print(f"Ноль, нужно улучшить показатели!")
