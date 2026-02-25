from script_1 import * # імпортуємо функції із script_1

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script_2")
    favorite_food("burger") # імпортована функція із script_1 для запуску без його головної частини
    favorite_drink("juice")
    print("Goodbye!")

if __name__ == '__main__': # дослівне пояснення - "Якщо ми запускаємо файл напряму: виконай цей код"
    main()