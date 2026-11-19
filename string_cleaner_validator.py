# Демонстрация методов проверки, модификации строк и оператора in (Глава 8)

def check_substring_traps():
    print("--- 1. Подводные камни оператора 'in' ---")
    phrase = "Восемьдесят семь"
    
    # Ловушка 1: поиск подстроки внутри другого слова
    print(f"'семь' в '{phrase}':", "семь" in phrase)  # True (найдёт внутри 'Восемьдесят')
    
    # Ловушка 2: чувствительность к регистру и её решение через .lower()
    email = "User@Example.COM"
    print("Проверка без учёта регистра:", "@example.com" in email.lower())  # True


def clean_and_validate_inputs():
    print("\n--- 2. Очистка и валидация данных ---")
    
    # Сырые данные с "мусором" по краям
    raw_pin = "   4815\n\t"
    raw_username = "###Admin_2026!!!"
    raw_tag = "   python   "

    # Неизменяемость строк: метод возвращает копию, поэтому перезаписываем переменную
    clean_pin = raw_pin.strip()
    clean_username = raw_username.lstrip("#").rstrip("!")
    clean_tag = raw_tag.strip().upper()

    print(f"Очищенный PIN: '{clean_pin}' | Только цифры (isdigit): {clean_pin.isdigit()}")
    print(f"Очищенный логин: '{clean_username}' | Только буквы и цифры (isalnum): {clean_username.isalnum()}")
    print(f"Очищенный тег: '{clean_tag}' | Все буквы заглавные (isupper): {clean_tag.isupper()}")

    # Проверка на пустую/пробельную строку и отсутствие пробелов внутри
    empty_input = "   \t\n  "
    if empty_input.isspace():
        print("Ввод состоит только из невидимых пробельных символов (isspace = True).")

    if " " not in clean_username and "@" in email_check("test@mail.ru"):
        print(f"Логин '{clean_username}' прошёл базовую проверку без пробелов.")


def email_check(address):
    # Пример цепочки очистки и приведения к единому регистру
    return address.strip().lower()


if __name__ == "__main__":
    check_substring_traps()
    clean_and_validate_inputs()
