# Вычисление среднего балла с исключением худшего результата
def get_average_without_lowest(scores):
    # Если в списке 1 элемент или меньше, делить на len-1 нельзя (будет ZeroDivisionError)
    if len(scores) <= 1:
        return 0
        
    # sum(scores) находит общую сумму, а min(scores) находит самый низкий балл.
    # Мы вычитаем худший балл из общей суммы и делим на оставшееся количество элементов.
    total = sum(scores) - min(scores)
    
    # Скобки обязательны, чтобы деление шло на весь результат вычитания (len - 1)
    return total / (len(scores) - 1)

# Пример использования:
# my_scores = [8, 9, 7, 10]
# print(get_average_without_lowest(my_scores))
