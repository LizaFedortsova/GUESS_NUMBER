from random import randint
number = randint(1, 100)
print('Угадай число от 1 до 100')
#НАписала
#еще 
while True:
    if p_number:= int(input()) < number:
        print('Загаданное число больше.')
    elif p_number > number:
        print('Загаданное число меньше.')
    else:
        print('Угадал')
        break