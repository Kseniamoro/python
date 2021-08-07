proceeds = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {proceeds / costs:.2f}")
    workers = int(input("Введите численность сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника сотавила {proceeds / workers:.2f}")
elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")