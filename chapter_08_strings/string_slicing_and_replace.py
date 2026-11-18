# Демонстрация тонкостей работы со срезами и методом replace()

def demonstrate_slicing():
    print("--- 1. Базовые и отрицательные срезы ---")
    word = "abcdef"
    print(f"Исходная строка: '{word}'")
    print(f"Последние два символа (word[-2:]): '{word[-2:]}'")
    print(f"Срез с конца без последнего символа (word[-4:-1]): '{word[-4:-1]}'")
    
    # Движение в обратную сторону (отрицательный шаг)
    code = "123456"
    # Граница стоп (-5) не включается, поэтому остановка происходит на индексе -4 ('3')
    print(f"Обратный срез code[-1:-5:-1]: '{code[-1:-5:-1]}'")


def demonstrate_slicing_traps():
    print("\n--- 2. Ловушки и пустые срезы ---")
    text = "python"
    
    # -0 в Python равен 0, поэтому срез [0:0] возвращает пустую строку
    print(f"Срез с -0 (text[:-0]): '{text[:-0]}'")
    
    # Индекс 3 и индекс -3 указывают на одну и ту же букву 'h'
    print(f"Встреча границ в одной точке (text[3:-3]): '{text[3:-3]}'")
    
    # Старт правее стопа при положительном шаге по умолчанию (+1)
    print(f"Неверное направление (text[-1:-4]): '{text[-1:-4]}'")


def demonstrate_string_modification():
    print("\n--- 3. Изменение строк: replace() против срезов ---")
    # Строки неизменяемы, поэтому создаем новые на основе старых
    city = "Moscaw"
    
    # Способ 1: Метод replace() ищет по значению
    fixed_city_replace = city.replace("a", "o")
    print(f"Исправление через replace(): {fixed_city_replace}")
    
    # Использование третьего параметра (count) для ограничения числа замен
    fruit = "banana"
    print(f"Замена только первой 'a' в '{fruit}': {fruit.replace('a', 'o', 1)}")
    
    # Способ 2: Замена строго по индексу через срезы (если букв несколько)
    # Меняем символ с индексом 4 ('a') на 'o'
    fixed_city_slice = city[:4] + "o" + city[5:]
    print(f"Точечная замена по индексу через срезы: {fixed_city_slice}")


def main():
    demonstrate_slicing()
    demonstrate_slicing_traps()
    demonstrate_string_modification()


if __name__ == "__main__":
    main()
