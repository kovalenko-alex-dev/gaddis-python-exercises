try:
    with open('subscribes.txt', 'r') as f:
        test = f.readline()
except FileNotFoundError:
    print('Файл не найден, работаю без кэша')
finally:
    print(f'Попытка чтения завершена')


