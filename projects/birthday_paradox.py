import datetime, random

# повертає list рандомних об'єктів дат для Днів народження
def getBirthdays(numberOfBirthdays):

    birthdays = []
    for i in range(numberOfBirthdays):

        # рік не має значення для нашого моделювання
        startOfYear = datetime.date(2001, 1, 1)

        # отримуємо рандомний день року
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

# повертає об’єкт дати дня народження, який зустрічається у списку Днів народження більше ніж один раз 
def getMatch(birthdays):
    
    # всі Дні народження унікальні - повертаємо None
    if len(birthdays) == len(set(birthdays)):
        return None
    
    # порівнюємо всі Дні народження один з одним
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA # повертаємо однакові Дні народження

print('''
Парадокс Дня народження показує, що в групі з N осіб ймовірність того,
що у двох з них День народження припадає на одну й ту саму дату, є напрочуд великою.
Ця програма використовує метод Монте-Карло (тобто багаторазові випадкові
моделювання) для дослідження цього явища.
      
(Насправді це не парадокс, а просто несподіваний результат.)
''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

 