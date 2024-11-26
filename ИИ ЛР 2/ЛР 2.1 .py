money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

money_capital, salary, spend, increase = 20000, 5000, 6000, 0.05
months = 0
cur_capital = money_capital
budget = cur_capital + salary

while True:
    if budget>=spend:
        months+=1
        budget+=salary-spend
        spend*=(1+increase)
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months,)
