import random
import time

NUM_DIGITS = 3
MAX_GUESSSES = 10

def typewrite(text, delay = 0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    
    print()

def getSecretNum():
    # повертає стрінг зроблений з NUM_DIGITS (трьох) унікальних рандомних чисел
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "Ти вгадав!"
    
    clues = []

    for i in range (len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    typewrite('''"Bagels" - гра на дедуктивну логіку.

Я думаю про {}-значне число, в якому немає повторюваних цифр.

Спробуй вгадати, яке це число. Ось кілька підказок:

Коли я кажу:   Це означає:
  Pico           Одна цифра правильна, але стоїть не на тому місці.
  Fermi          Одна цифра правильна і стоїть на правильному місці.
  Bagels         Жодна цифра не правильна.

Наприклад, якщо таємне число - 248, а ви загадали 843, то
підказки будуть такими: Fermi Pico.'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print()
        typewrite('Я думаю про число.')
        typewrite('Ти маєш {} спроб, щоб відгадати його.'.format(MAX_GUESSSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                typewrite('Спроба №{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            typewrite(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSSES:
                typewrite('У вас закінчилися спроби.')
                typewrite('Відповідь: {}.'.format(secretNum))

        typewrite('Бажаєте зіграти знову? (так чи ні)')
        if not input('> ').lower().startswith('т'):
            break

    typewrite('Дякую за гру!')

if __name__ == '__main__':
    main()