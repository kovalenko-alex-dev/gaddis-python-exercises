# Практика: парсинг «грязной» строки заказа и генерация адаптивного чека для Telegram-бота

# Входящие данные от парсера (формат: "КодЗаказа | Название товара | Цена | Дата")
raw_order = '  ORD-9482 | Игровая клавиатура RGB | 4 590 руб. | 2026-11-23  '

# 1. Разбиваем строку на части и убираем лишние пробелы по краям каждой ячейки
parts = [item.strip() for item in raw_order.split('|')]
order_id, product_name, raw_price, raw_date = parts

# 2. Парсим дату в одну строку (цепочка split + индекс) и цену (удаление лишнего через replace)
month_num = raw_date.split('-')
clean_price = int(raw_price.replace(' ', '').replace('руб.', ''))

# 3. Считаем количество слов в названии товара (для тегов/статистики бота)
word_count = len(product_name.split())

# 4. Формируем адаптивную шапку чека, ширина которой подстраивается под название товара
header = f'ЧЕК ЗАКАЗА #{order_id.split("-")}'
# Выбираем максимальную длину между заголовком и названием товара, чтобы рамка не «поехала»
box_width = max(len(header), len(product_name)) + 4
border = '=' * box_width

# 5. Собираем итоговое сообщение для отправки в чат
receipt = (
    f'{border}\n'
    f'| {header:<{box_width - 4}} |\n'
    f'{border}\n'
    f'Товар: {product_name} ({word_count} сл.)\n'
    f'Месяц оформления: {month_num}\n'
    f'К оплате: {clean_price:,} ₽'.replace(',', ' ') + '\n'
    + '-' * box_width
)

print(receipt)

# 6. Имитация визуального таймера удаления сообщения в боте (обратный range)
print('\nСообщение самоуничтожится через:')
for sec in range(3, 0, -1):
    print('⏳ ' + '• ' * sec + f'({sec} сек.)')
