# Кортежи: чтение, запятая и конвертация (Гэдис, 7.10)


def show_tuple(data):
    # Чтение кортежа: индекс, срез, длина, in, цикл for
    print("Первый элемент:", data[0])
    print("Срез с 1-го:", data[1:])
    print("Длина:", len(data))
    print("20 есть в кортеже:", 20 in data)
    for item in data:
        print(item)


def add_item(data, item):
    # Кортеж менять нельзя: переводим в список, добавляем, собираем новый кортеж
    temp_list = list(data)
    temp_list.append(item)
    return tuple(temp_list)


def main():
    numbers = (10, 20, 30)
    show_tuple(numbers)

    # Запятая создаёт кортеж, скобки сами по себе - нет
    single = (5,)
    not_tuple = (5)
    print(type(single))
    print(type(not_tuple))

    numbers = add_item(numbers, 40)
    print(numbers)


if __name__ == '__main__':
    main()
