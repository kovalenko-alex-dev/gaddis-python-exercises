def has_secret(text):
    return 'secret' in text.split()

def main():
    while True:
        words = input('Введите текст: ')
        if has_secret(words):
            print('Обнаружен шпион!')
        else:
            print('Текст безопасен')
            more = input('повторить? ')
            if more != 'yes':
                break

main()
