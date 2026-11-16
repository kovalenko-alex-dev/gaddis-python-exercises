# Модуль для бота магазина: каталог, правка, отчёт, файл (вариант 2: с функциями)


def show_catalog(catalog):
    for i in range(len(catalog)):
        print(i + 1, catalog[i][0], catalog[i][1])


def show_item(catalog):
    try:
        number = int(input('Введите номер: '))
        if number > 0:
            item = catalog[number - 1]
            print(item[0], item[1])
        else:
            print('Ошибка')
    except (ValueError, IndexError):
        print('Ошибка')


def edit_catalog(catalog):
    choice = input('Нажмите "a" для добавления или "d" для удаления: ')
    if choice == 'a':
        name = input('Введите название товара: ')
        price = int(input('Введите цену: '))
        catalog.append([name, price])
    elif choice == 'd':
        target = input('Введите название для удаления: ')
        for i in range(len(catalog)):
            if catalog[i][0] == target:
                del catalog[i]
                break


def make_report(catalog):
    prices = [item[1] for item in catalog]
    i_min = prices.index(min(prices))
    i_max = prices.index(max(prices))
    print('Самый дешёвый:', catalog[i_min][0], prices[i_min])
    print('Самый дорогой:', catalog[i_max][0], prices[i_max])
    return (len(catalog), sum(prices))


def save_names(catalog, file_name):
    with open(file_name, 'w') as f:
        for item in catalog:
            f.write(item[0] + '\n')


def load_names(file_name):
    names = []
    with open(file_name, 'r') as f:
        for line in f:
            names.append(line.rstrip('\n'))
    return names


def main():
    catalog = [['Мышь', 450], ['Кабель', 150], ['Хаб', 600], ['Флешка', 300], ['Чехол', 200]]

    show_catalog(catalog)
    show_item(catalog)

    edit_catalog(catalog)
    show_catalog(catalog)

    result = make_report(catalog)
    print(result)

    save_names(catalog, 'list.txt')
    new_list = load_names('list.txt')
    print(len(new_list))


if __name__ == '__main__':
    main()
