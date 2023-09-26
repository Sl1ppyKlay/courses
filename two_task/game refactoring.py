import random

def main():
    ans = input('Привет!\nБудешь угадывать? (да/нет)').lower()
    if ans == 'да':
        play_game()
    elif ans == 'нет':
        print('Пока!')
    else:
        print('Ошибка ввода!')

def play_game():
    guess = input('Угадай чисто от 1 до 10: ')
    rand = random.randint(1, 10)
    