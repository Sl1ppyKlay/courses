import random

def main():
    rand = random.randint(1, 10)
    ans = input('Привет!\nБудешь угадывать? (да/нет): ').lower()

    if ans != 'да':
        print('Ошибка ввода!')

    if ans == 'нет':
        print ('Пока')

    while True:
        try:
            number = int(input('Угадай чисто от 1 до 10: '))
            if 1 <= number <= 10:
                control = abs(number - rand)
                if control > 5:
                    print('\nХолодно!\n')
                elif control > 2:
                    print ('\nТепло!\n')
                else:
                    print ('\nЖгётся!\n')
                
                if number == rand:
                    print('Вы угадали число! Число было -', rand)
                    break
            else: 
                print ('\nЧисло должно быть в пределах от 1 до 10!')
        except ValueError:
            print(f'\nОшибка! Должно быть введено число!')

if __name__ == '__main__':
    main()