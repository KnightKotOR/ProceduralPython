money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Количество  месяцев, которое можно протянуть без долгов
d = spend - salary

while d < money_capital:
    months += 1
    money_capital -= d
    spend *= 1 + increase
    d = spend - salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
