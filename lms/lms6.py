# №1
players = {

    ("Will", "Smith"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}
print([sum((key, value), ()) for key, value in players.items()])
# №2
# ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# k1 = (s[0],s[1])
# k2 = (s[2],s[3])
# k3 = (s[4],s[5])
# k4 = (s[6],s[7])
# k5 = (s[8],s[9])
# print([k1],[k2],[k3],[k4],[k5])
# №3
# text="ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# D= text.count('А')
# L= text.count('О')
# print(D+L)
# №4

# while True:

# num1 = int(input('Vvedite 1-oe chislo: '))
# num2 = int(input('Vvedite 2-oe chislo: '))
# znak = input('+, -, *, /, q: ')
# if znak == '+':
#         print(f'{num1} {znak} {num2} = {num1 + num2}')
# elif znak == '-':
#     print(f'{num1} {znak} {num2} = {num1 - num2}')
# elif znak == '*':
#         print(f'{num1} {znak} {num2} = {num1 * num2}') 
# elif znak == '/':
#         print(f'{num1} {znak} {num2} = {num1 / num2}')
# elif znak ==' ':
#     print('Нет ничего приятнее, чем знание о твоих знаниях!')        
# elif znak =='q':
#     print('Нет ничего приятнее, чем знание о твоих знаниях!') 

# 5
# violator_songs = {

#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
# num_songs = int(input("Введите количество песен: "))
# selected_songs = []
# for _ in range(num_songs):
#     song = input("Введите название песни: ")
#     selected_songs.append(song)
# total_time = sum(violator_songs.get(song, 0) for song in selected_songs)
# print("Общее время звучания:", total_time)









