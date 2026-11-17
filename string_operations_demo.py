# Создаем исходную строку с лишними пробелами по краям
raw_text = "   Python Basics   "

# Очищаем строку от пробелов и приводим к единому регистру
clean_text = raw_text.strip()
upper_text = clean_text.upper()
# Выведет: 'PYTHON BASICS'

# Извлекаем первый символ (индекс 0) и срез первых 6 символов
first_char = clean_text[0]
language = clean_text[0:6]

# Объединяем (конкатенация) и дублируем строки
greeting = "Изучаем: " + language + "!"
divider = "-" * 20

# Проверяем наличие подстроки и заменяем слово (создается НОВАЯ строка)
has_python = "Python" in clean_text
updated_text = clean_text.replace("Basics", "Pro")

# Печатаем результаты
print(divider)
print(greeting)
print("Исходная очищенная:", clean_text)
print("Обновленная строка:", updated_text)
# Обрати внимание: clean_text не изменилась, так как строки неизменяемы
