def get_report():
    return int(input('Enter value: '))

def write_data(value):
    with open('filename.txt', 'a') as f:
        f.write(f'{value}\n')

def process_reports():
    total = 0
    report = get_report()          # priming read
    while report != 0:
        try:
            write_data(report)
            total += report
        except ValueError:
            print('Input error')
        finally:
            print('Value saved')
        report = get_report()      # следующий ввод — в конце тела цикла
    return total

def main():
    total = process_reports()
    print(total)

if __name__ == '__main__':
    main()



