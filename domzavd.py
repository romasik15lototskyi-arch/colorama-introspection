while True:
    user_input = input("Введіть число: ")
    try:
        number = int(user_input)
        print("Введене число як ціле:", number)
        break
    except ValueError:
        print("Помилка: введено не число! Спробуйте ще раз.")