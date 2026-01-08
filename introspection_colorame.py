# introspection_colorama.py
import colorama
from colorama import Fore, Back, Style

# Ініціалізація colorama
colorama.init()

# Приклади використання кольорів та стилів
print(Fore.RED + "Це червоний текст" + Style.RESET_ALL)
print(Fore.GREEN + "Це зелений текст" + Style.RESET_ALL)
print(Back.YELLOW + "Жовтий фон" + Style.RESET_ALL)
print(Style.BRIGHT + "Яскравий текст" + Style.RESET_ALL)

# Інтроспекція модуля
print("\nАтрибути модуля colorama:")
print(sorted(dir(colorama), key=str.lower))

# Доступні кольори тексту
print("\nДоступні кольори Fore:")
print(dir(Fore))

# Доступні кольори фону
print("\nДоступні кольори Back:")
print(dir(Back))

# Доступні стилі
print("\nДоступні стилі:")
print(dir(Style))
