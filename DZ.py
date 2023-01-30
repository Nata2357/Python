import random
from random import randint, choice

print(
    'Добро пожаловать в ИГРУ!'
    'Ты играешь против computer'
    'Тот, кто возьмёт последнюю конфету - проиграл'
    'За ход можно взять не более 28 конфет'
    'Удачи!'
    )

messages = ['Ваш ход', 'Берите',
            'Сколько?', 'Еще', 'Ваш ход']
max_number_move = 0


def hello_players():
    player1 = input('Имя\n')
    player2 = 'Computer'
    print(f'Добро пожаловать в игру  {player2}')
    return [player1, player2]


def konfeta_game(players):
    global max_number_move
    total_konfeta = int(input('Введите cколько всего у нас конфет:\n'))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_konfeta, max_number_move, int(first)]


max_move = max_number_move

def game_player_vs_computer(sweets, players, messages):
    global max_number_move
    count = sweets[2]

    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Я забираю {move}')

        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Игра окончена. Ставок больше нет.')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Конфет больше нет.')
        count += 1
    return players[not count % 2]


players = hello_players()
sweets = konfeta_game(players)

winer = game_player_vs_computer(sweets, players, messages)
if not winer:
    print('Ничья')
else:
    print(
        f'Поздравляю! Победил {winer}! Конфеты ваши.')