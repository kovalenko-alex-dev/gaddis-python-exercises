# Чтение данных из текстового файла в чистый список Python
def read_clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        # Цикл 'for line in f' перебирает файл построчно, экономя память.
        # Метод '.rstrip('\n')' аккуратно срезает перенос строки с правого края.
        return [line.rstrip('\n') for line in f]

# Пример использования:
# cities = read_clean_file('cities.txt')
# print(cities)

