import random

def main():
    minimal = 1
    maximum = 10

    rand = random.randint(minimal, maximum)
    ans = input('Привет!\nБудешь угадывать? (да/нет): ').lower()

    if ans != 'да':
        print('Ошибка ввода!')

    if ans == 'нет':
        print ('Пока')

    while True:
        try:
            number = int(input(f'\nУгадай чисто от {minimal} до {maximum}: '))
            if minimal <= number <= maximum:
                control = abs(number - rand)
                if control > 5:
                    print('Холодно!\n')
                elif control > 2:
                    print ('Тепло!\n')
                else:
                    print ('Жгётся!\n')
                
                if number == rand:
                    print('Вы угадали число! Число было -', rand)
                    break
            else: 
                print (f'\n\nЧисло должно быть в пределах от {minimal} до {maximum}!')
        except ValueError:
            print(f'\nОшибка! Должно быть введено число!')

if __name__ == '__main__':
    main()