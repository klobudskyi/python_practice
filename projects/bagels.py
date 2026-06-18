import random, time

num_digits = 3
max_guesses = 10

def typewrite(text, delay=0.05):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(delay)
    print()

def getSecretNum():
    digits = list("0123456789")
    random.shuffle(digits)

    secretNum = ""

    for i in range(num_digits):
        secretNum += str(digits[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return("Ти вгадав!")

    clues = []

    for i in range(len(guess)):
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
підказки будуть такими: Fermi Pico.'''.format(num_digits))
    
    while True:
        secretNum = getSecretNum()
        print()
        typewrite("Я думаю про число.")
        typewrite("Ти маєш {} спроб, щоб відгадати його.".format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ""

            while len(guess) != num_digits or not guess.isdecimal():
                typewrite("Спроба №{}: ".format(num_guesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            typewrite(clues)
            num_guesses += 1

            if guess == secretNum:
                break
            if num_guesses > max_guesses:
                typewrite("У тебе закінчились спроби.")
                typewrite("Відповідь: {}.".format(secretNum))
        
        typewrite("Бажаєш зіграти знову? (так чи ні)")
        if not input("> ").lower().startswith("т"):
            break
    
    typewrite("Дякую за гру!")

if __name__ == '__main__':
    main()