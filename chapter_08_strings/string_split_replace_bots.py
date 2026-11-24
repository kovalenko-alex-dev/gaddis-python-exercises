```
# Демонстрация методов split() и replace() для парсинга и обработки команд ботов

# 1. Удаление ненужных фрагментов через replace() на пустую строку ''
print('--- 1. Очистка строк через replace() ---')
raw_price = '12 990 руб.'
# Удаляем пробелы и валюту, чтобы превратить строку в чистое число
clean_price = raw_price.replace(' ', '').replace('руб.', '')
print(f"Было: '{raw_price}' -> Стало число: {int(clean_price)}")

raw_phone = '+7 (999) 123-45-67'
clean_phone = raw_phone.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
print(f"Очищенный телефон: {clean_phone}")

# Ограничение количества замен (третий аргумент count)
messy_log = 'ERROR: ERROR: файл не найден'
fixed_log = messy_log.replace('ERROR: ', '', 1)  # Удаляем только первое повторение
print(f"Исправленный лог: {fixed_log}")

# 2. Разбиение строк на списки через split()
print('\n--- 2. Разбор данных через split() ---')
# Разбор CSV-строки или данных из базы
user_row = 'ivan_dev;25;Python;Kherson'
user_data = user_row.split(';')
print('Список данных пользователя:', user_data)
print(f'Имя: {user_data[0]}, Город: {user_data[3]}')

# 3. Фишки для Telegram-ботов: разбор команд с несколькими аргументами
print('\n--- 3. Фишки для ботов ---')
# Сценарий: админ отправляет команду вида "/mute @username 60 Спам в чате"
admin_msg = '/mute @bad_user 60 Спам в чате'

# maxsplit=3 делит строку только по первым 3 пробелам, сохраняя причину бана целиком!
parts = admin_msg.split(' ', 3)
if len(parts) == 4 and parts[0] == '/mute':
    cmd, target, minutes, reason = parts
    print(f'Команда: {cmd} | Юзер: {target} | Время: {minutes} мин. | Причина: {reason}')

# 4. Фишки для парсеров: очистка текста от мусорных переносов и HTML-тегов
print('\n--- 4. Фишки для парсеров ---')
scraped_html = '<p>Товар:   Ноутбук\n\t\nЦена:  45 000</p>'

# Удаляем теги заменой на пустую строку
no_tags = scraped_html.replace('<p>', '').replace('</p>', '')

# Хитрый приём: split() без аргументов режет по любым пробелам, \n и \t,
# а ' '.join() склеивает слова обратно через один аккуратный пробел
normalized_text = ' '.join(no_tags.split())
print(f'Идеально чистый текст: {normalized_text}')
```
