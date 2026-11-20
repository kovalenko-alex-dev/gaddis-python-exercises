# Демонстрация методов проверки, очистки и парсинга строк в Python

# 1. Проверка содержимого строк (валидация данных)
user_login = 'ab12'
pin_code = '4815'
weird_num = '½'

print('--- 1. Проверка символов ---')
print(f"'{user_login}'.isalnum(): {user_login.isalnum()}")   # True (буквы и цифры)
print(f"'{pin_code}'.isdigit(): {pin_code.isdigit()}")       # True (только обычные цифры)
print(f"'{weird_num}'.isnumeric(): {weird_num.isnumeric()}") # True (любые числовые символы, включая дроби)

# 2. Неизменяемость строк и очистка пробелов
raw_text = '  Hello World$#  '
print('\n--- 2. Очистка и регистр ---')
# Без lstrip() метод startswith('Hell') вернёт False из-за пробелов в начале
print('Начинается с Hell (с очисткой):', raw_text.lstrip().startswith('Hell'))

# Убираем пробелы по краям и лишние спецсимволы справа
clean_text = raw_text.strip().rstrip('$#')
print('Очищенная строка:', clean_text)
print('Исходная строка не изменилась:', repr(raw_text))

# 3. Разбор строки через поиск индекса (find) и срезы
print('\n--- 3. Парсинг Email ---')
email = 'anna@gmail.ru'
pos = email.find('@')

if pos == -1:
    print('Ошибка: символ @ не найден')
else:
    username = email[:pos]
    domain = email[pos + 1:]
    print(f'Имя пользователя: {username}')
    print(f'Домен: {domain}')

# 4. Фишки для Telegram-ботов и парсеров
print('\n--- 4. Приёмы для ботов и парсеров ---')

# Фишка 1: Нормализация команды от пользователя (убираем пробелы и приводим к нижнему регистру)
bot_input = '   /Start   '
normalized_cmd = bot_input.strip().lower()
if normalized_cmd == '/start':
    print('Бот: Команда /start успешно распознана!')

# Фишка 2: Извлечение аргумента из команды (например, реферальный код или ID)
command_with_arg = '/ban 987654321'
if command_with_arg.startswith('/ban '):
    space_pos = command_with_arg.find(' ')
    target_id = command_with_arg[space_pos + 1:].strip()
    if target_id.isdigit():
        print(f'Бот: Блокируем пользователя с ID {target_id}')

# Фишка 3: Вырезание значения между тегами при простом парсинге HTML/текста
html_snippet = '<div class="price">1490 руб.</div>'
start_tag = '>'
end_tag = '</'
start_idx = html_snippet.find(start_tag) + len(start_tag)
end_idx = html_snippet.find(end_tag, start_idx)
price = html_snippet[start_idx:end_idx]
print(f'Парсер: Найдена цена — {price}')
