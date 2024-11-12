import re
from datetime import datetime

def is_valid_date(date_string):
    # Регулярное выражение для проверки формата даты
    pattern = r'^\d{1,2} (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек), \d{4}$'
    
    if not re.match(pattern, date_string):
        return False
    
    # Извлечение дня, месяца и года
    day, month_str, year = date_string.split()
    month_str = month_str.replace(",", "")
    day = int(day)
    year = int(year)

    # Словарь для соответствия месяцев
    months = {
        'Янв': 1,
        'Фев': 2,
        'Мар': 3,
        'Апр': 4,
        'Май': 5,
        'Июн': 6,
        'Июл': 7,
        'Авг': 8,
        'Сен': 9,
        'Окт': 10,
        'Ноя': 11,
        'Дек': 12
    }

    month = months[month_str]

    # Проверка корректности даты
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

# Пример использования
date_input = "14 Дек, 1978"
if is_valid_date(date_input):
    print(f"Дата '{date_input}' корректна.")
else:
    print(f"Дата '{date_input}' некорректна.")
