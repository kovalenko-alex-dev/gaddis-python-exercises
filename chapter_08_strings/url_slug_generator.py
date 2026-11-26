raw_titles = [
    "  Новый iPhone 16 Pro: обзор и цены!  ",
    "Как написать Telegram-бота на Python??? ",
    "   Скидки до 50% на все ноутбуки!  "]

bad_chars = ":!?%,"

for title in raw_titles:
    # 1. Чистим края и переводим в нижний регистр
    slug = title.strip().lower()
    
    # 2. Удаляем запрещенные для URL символы
    for ch in bad_chars:
        slug = slug.replace(ch, "")
        
    # 3. Меняем пробелы на дефисы
    slug = slug.replace(" ", "-")
    print(f"Было: '{title.strip()}'  --->  URL: https://site.com{slug}")
