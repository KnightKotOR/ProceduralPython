list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


mid = int(len(list_players) // 2)
first_team, second_team = list_players[:mid], list_players[mid:]

print(first_team)
print(second_team)
