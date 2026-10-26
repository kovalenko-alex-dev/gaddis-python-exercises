import random
def is_success(status_code):
    if status_code == 200:
        return True
    else:
        return False

def main():
    success = 0
    fail = 0
    for x in range(20):
        answer = random.choice([200, 403, 404, 500])
        if is_success(answer):
            success += 1
        else:
            fail += 1

    print(f'Успешно спарсилось: {success}, ошибок: {fail}')

if __name__ == '__main__':
    main()

    