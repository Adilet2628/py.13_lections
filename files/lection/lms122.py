
def add_task(path, task):
    try:
        with open(path, 'r') as f:
            old = f.read()
    except FileNotFoundError:
        with open(path, 'w') as f:
            old = ''

    with open(path, 'w') as f:
        f.write(old + task + '\n')

    with open(path, 'r') as f:
        old2 = f.readlines()

    with open(path, 'w') as f:
        for n, t in enumerate  ([i.replace(f'{i[0]} ', '') for i in old2]):
            f.write(str(n) + ' ' + t)


def read_task(path):
    try:
        with open(path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Такого файла нет!')


def delete_task(path, num):
    try:
        with open(path, 'r') as f:
            del_ = f.readlines()
            for i in del_:
                if str(num) == i.replace('\n', '')[0]:
                    del_.remove(i)

        with open(path, 'w') as f:
            f.write(''.join(del_))
    except FileNotFoundError:
        print('Такого файла нет!')


while True:
    try:
        user = input('''1 - Добавить
2 - Удалить
3 - Просмотр
4 - Выйти
Введи цифру: ''')
        if user == '1':
            add_task(input('Введи название файла: '), input('Введи задачу: '))
        elif user == '2':
            delete_task(input('Введи название файла: '), int(input('Введи номер задачи: ')))
        elif user == '3':
            read_task(input('Введи название файла: '))
        elif user == '4':
            break
    except ValueError:
        print('Введи корректный номер строки!')

   


































