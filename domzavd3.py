import logging

logging.basicConfig(
    filename='error_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:

    user_input = input("Введіть число: ")
    number = int(user_input)
    print("Введене число:", number)

except ValueError as e:
    logging.error("Сталася помилка при конвертації введених даних у число", exc_info=True)
    print("Помилка: введено не число! Подробиці збережено у error_log.log")
