
from pprint import pprint
data = {}


def add_info() -> None:
    skype = input('Введите Ваш Skype: ')
    data[skype] = {}
    name = input('Введите ФИО: ')
    data[skype]['ФИО'] = name
    tel = input('Введите телефон: ')
    data[skype]['Телефон'] = tel
    email = input('Введите рабочий email: ')
    data[skype]['Почта'] = email
    work = input('Введите Вашу должность: ')
    data[skype]['Должность'] = work
    cab = input('Номер кабинета: ')
    data[skype]['Кабинет'] = cab




def del_sm() -> None:
    del_skype = input('Введите скайп для удаления информации: ')
    if del_skype in data:
        data.pop(del_skype)
        print('Успешно удален')
    else:
        print('Ошибка')



def find_sm() -> None:
    find_skype = input('Введите skype: ')
    if find_skype in data:
        val = data.get(find_skype)
        pprint(val)
    else:
        print('Ошибка')


def edit_sm() -> None:
    skype = input('Введите skype: ')
    while True:
        pick = input('Какие данные хотите изменить (0-exit): ').lower()
        if pick == 'фио':
            pick_name = input('Введите новое фио: ')
            data[skype]['ФИО'] = pick_name

        elif pick == 'телефон':
            pick_tel = input('Введите новый телефон: ')
            data[skype]['Телефон'] = pick_tel

        elif pick == 'email':
            pick_email = input('Введите новую почту: ')
            data[skype]['Почта'] = pick_email

        elif pick == 'должность':
            pick_work = input('Введите новую должность: ')
            data[skype]['Должность'] = pick_work

        elif pick == 'кабинет':
            pick_cab = input('Введите новый кабинет: ')
            data[skype]['Кабинет'] = pick_cab

        elif pick == 'skype':
            pick_skype = input('Введите новый skype: ')
            val = data[skype]
            data.pop(skype)
            data[pick_skype] = val
            skype = pick_skype

        elif pick == '0':
            break
        else:
            print('Такой фильтр не найден')



def show() -> None:
    pprint(data)


def main() -> None:
    while True:
        choice = input('1-Добавить\n'
                        '2-Удалить\n'
                        '3-Поиск\n'
                        '4-Замена данных\n'
                       '5-Показать список\n'
                        'Ввод: ')
        if choice == '1':
            add_info()
        elif choice == '2':
            del_sm()
        elif choice == '3':
            find_sm()
        elif choice == '4':
            edit_sm()
        elif choice == '5':
            show()
        else:
            print('Такой функции к сожалению - нет')


main()