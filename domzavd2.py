import random
import string

def random_letter_generator():
    """Генератор випадкових букв англійського алфавіту"""
    while True:
        yield random.choice(string.ascii_lowercase)

gen = random_letter_generator()

for _ in range(10):
    print(next(gen), end=' ')
