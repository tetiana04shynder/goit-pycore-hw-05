import re
from typing import Callable

def generator_numbers(text: str):
    matches = re.findall(r'\b\d+\.\d+\b', text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
text = "Прибуток цього місяця складався з кількох частин: 1500.75 як основна зарплата, 89.30 бонусів, і 410.50 премії."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
# Виведе Загальний дохід: 2000.55