list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
vsego_v_kashdoy_komande = round(len(list_players)/2)

first = list_players[:vsego_v_kashdoy_komande]
second = list_players[vsego_v_kashdoy_komande:]

print(first)
print(second)
