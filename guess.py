# подключаем модуль
import random
myName = input('здравствуйте! Как вас зовут?')
number = random.randint(1,50)
for attNumber in range(10):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break
if guess == number:
    attNumber = str(attNumber + 1)
    print('Отлично, '+myName+'! Ты справился за '+attNumber+' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число '+number+'.')