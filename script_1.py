def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script_1")
    favorite_food("pizza")
    print("Goodbye!") # при запуску цього файлу в іншому файлі - нам не потрібно відображати цю частину коду, 
                      # тому ми використовуємо "if __name__ == '__main__'", тобто ця функція буде виконуватись лише при запуску напряму

if __name__ == '__main__': # дослівне пояснення - "Якщо ми запускаємо файл напряму: виконай цей код"
    main()

print(":)")

# Тобто, при запуску з конфігурацією script_1 термінал виведе: "This is script_1 Your favorite food is pizza Goodbye! :)"
# А при запуску з конфігурацією script_2 термінал виведе лише: ":)"