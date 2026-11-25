import csv

# ==========================================
# 1. БОТ: Разбор команды от пользователя
# ==========================================
raw_command = "   /PAY @durov 500\n"

# Чистим края от пробелов и переносов (\n), приводим к нижнему регистру и режем на лексемы
clean_command = raw_command.strip().lower()
tokens = clean_command.split(" ")  # ['/pay', '@durov', '500']

if tokens[0] == "/pay" and tokens[2].isdigit():
    recipient = tokens[1]
    amount = int(tokens[2])  # Переводим строку в число для расчетов
    print(f"[Бот] Перевод {amount} грн пользователю {recipient} выполнен.")

# ==========================================
# 2. ПАРСЕР: Чистка сырого текста и проверка наличия
# ==========================================
raw_product_card = "  iPhone 15 Pro | 42000 | В наличии (Скидка) \n"

# Режем по разделителю и чистим каждый кусок от лишних пробелов (генератор списка — боевая фишка)
parts = [item.strip() for item in raw_product_card.split("|")]
title, price_str, status = parts[0], parts[1], parts[2]

# Проверяем наличие ключевых слов (подстрок)
if "в наличии" in status.lower() and price_str.isdigit():
    print(f"[Парсер] Товар доступен: {title} — {int(price_str)} грн")

# ==========================================
# 3. БАЗА ДАННЫХ: Запись и чтение CSV без костылей
# ==========================================
orders = [
    ["Чехол для iPhone", 350, 2],
    ["Защитное стекло", 150, 5],
    ["Кабель Type-C", 200, 3]
]

# Записываем данные в таблицу (newline="" защищает от пустых строк в Windows)
with open("parsed_items.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(orders)

# Читаем таблицу обратно и считаем общую выручку (цена * количество)
total_revenue = 0
with open("parsed_items.csv", "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        price = int(row[1])
        qty = int(row[2])
        total_revenue += price * qty

print(f"[CSV Отчет] Общая сумма всех заказов: {total_revenue} грн")
