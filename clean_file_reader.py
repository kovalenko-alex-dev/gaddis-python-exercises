def read_clean_file(filename):
    """
    Безопасно считывает данные из текстового файла, возвращая чистый список
    строк без служебных символов переноса строки (\\n).
    """
    # Менеджер контекста 'with' гарантирует автоматическое закрытие файла на диске.
    # Флаг 'r' — режим чтения, encoding='utf-8' — поддержка кириллицы.
    with open(filename, 'r', encoding='utf-8') as f:
        # Идиоматичный паттерн (генератор списка / List Comprehension):
        # 1. Цикл 'for line in f' перебирает файл построчно, не забивая память.
        # 2. Метод '.rstrip('\\n')' откусывает невидимый перенос строки с правого края.
        clean_lines = [line.rstrip('\n') for line in f]
        
    return clean_lines


# --- Блок демонстрации работы скрипта ---
if __name__ == '__main__':
    import os

    test_filename = 'shopping_list_sample.txt'
    
    # Вспомогательный шаг: временно создаем тестовый файл для демонстрации чтения
    with open(test_filename, 'w', encoding='utf-8') as temp_f:
        temp_f.write("молоко\nхлеб\nяблоки\n")

    print(f"Читаем данные из файла '{test_filename}'...")
    
    # Вызов функции импорта и чистки данных
    imported_data = read_clean_file(test_filename)
    
    print("Полученный чистый Python-список:")
    print(imported_data)
    
    # Удаляем временный файл после демонстрации
    if os.path.exists(test_filename):
        os.remove(test_filename)
