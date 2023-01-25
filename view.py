def main_menu() -> int:
    print('Главное меню')
    menu_list = ['Открыть справочник',
                 'Показать все контакты',
                 'Найти контакт',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Сохранить изменения',
                 'Выход'
                ]
    for i in range(len(menu_list)):
        print(f'    {i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду :> '))
    return user_input
    


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end = '. ')
            for v in db[i].values():
                print(f'{v}', end =' ')
            print()

def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return True

def exit_programm():
    print('Завершение программы. ')
    exit()

def create_contact(contacts: list):
    print('Создание нового контакта')
    new_contact = {'ID': 'id_' + str(len(contacts) + 1),
                   'Lastname': input('\tФамилия: '),
                   'Firstname': input('\tИмя: '),
                   'Phone': input('\tТелефон'),
                   'Comment': input('\tКомментарии')}
    return new_contact

def delete_contact(contacts: list):
    print('\n Удаление контакта.\nДля исключения потери информации удаления '
          'контакта осуществляется по ID контакта.\nЕсли вы не знаете ID контакта, выберите '
          'команду в главном меню "Найти контакт" или "Показать все контакты".'
          '\nДля отмены удаления выберите "Отмена"\n')
    print('1. Ввести ID\n2.Отмена')
    while True:
        try:
            command = int(input('Введите номер команды: '))
            if command < 1 or command > 2:
                print('\nВведите номер команды (1 или 2).\n')
            else:
                match command:
                    case 1:
                        id_contact: str = input('Введите ID: ')
                        if id_contact.isdigit() and 1 <= int(id_contact) <= len(contacts):
                            contact = ' '.join(contacts[int(id_contact) - 1].values())
                            print(f'\nКонтакт "{contact}" удален.\nID контактов обновлены.\n'
                                   'Для сохранения изменений выберите "Сохранить Изменения"'
                                   'в главном меню.')
                            return id_contact
                        if not id_contact.isdigit() or int(id_contact) < 1 or \
                            int(id_contact) > len(contacts):
                            print('\nID введен некорректно или отсутсвует!\n'
                                  'Для удаления контакта выберите необходимую команду.')
                            return None
                    case 2:
                        print('\nУдаление отменено\n')
                        return None
        except ValueError:
            print('\nОшибка! Введите номер команды\n')

def find_choice() -> tuple:
    print('\n Критерии поиска: ')
    find_list = ['Фамилия',
                 'Имя',
                 'Фамилия и имя',
                 'Номер телефона',
                 'ID контакта'
                ]
    for i, value in enumerate(find_list, start = 1):
        print(f'\t{i}. {value}')
    print()
    while True:
        try:
            user_choice = int(input('Выберите номер критерия поиска: '))
            if user_choice < 1 or user_choice > 5:
                print('Введите номер команды от 1 до 4.\n')
            else:
                find_data =input('Введите данные для поиска в соответствии с критерием поиска: ')
            if user_choice < 5:
                return user_choice, find_data
            if user_choice == 5 and find_data.isdigit():
                find_data = 'id_' + str(find_data)
                return user_choice, find_data
            if user_choice == 5 and not find_data.isdigit():
                print('\n Некорректный ID ')
        except ValueError:
            print('\n Ошибка ! Введите номер команды.\n')

def show_contact(contacts: list):
    print('Контакт(ы): ')
    if contacts:
        for i, item in enumerate(contacts):
            print(f'\t{i + 1}', end=' ')
            print(f'{" ".join(item.values())}')
    else:
        print('\t Контакт не найден!\n')

def change_contact(contacts: list):
    print('\n Изменение контакта.\nДля исключения потери информации изменение '
          'контакта осуществляется по ID контакта.\nЕсли вы не знаете ID контакта, выберите '
          'команду в главном меню "Найти контакт" или "Показать все контакты".'
          '\nДля отмены изменения выберите "Отмена"\n')
    print('1. Ввести ID\n2.Отмена')
    while True:
        try:
            command = int(input('Введите номер команды: '))
            if command < 1 or command > 2:
                print('\nВведите номер команды (1 или 2).\n')
            else:
                match command:
                    case 1:
                        id_contact = input('Введите ID: ')
                        if id_contact.isdigit() and 1 <= int(id_contact) <= len(contacts):
                            print(f'\nИзмените данные контакта: id_{id_contact}'
                                  f'{contacts[int(id_contact) - 1]["Lastname"]}'
                                  f'{contacts[int(id_contact) - 1]["Firstname"]}'
                                  f'{contacts[int(id_contact) - 1]["Phone"]}'
                                  f'{contacts[int(id_contact) - 1]["Comment"]}:\n')
                            new_contact = {'ID': 'id_' + id_contact,
                                           'Lastname': input('\tФамилия: '),
                                           'Firstname': input('\tИмя: '),
                                           'Phone': input('\tНомер телефона: '),
                                           'Comment': input('\tКомментарии: ')}
                            print('\nКонтакт изменен.\nДля сохранения измененийв файле выберите '
                                  '"Сохранить изменения" в главном меню.')
                            return id_contact
                        if not id_contact.isdigit() or int(id_contact) < 1 or \
                            int(id_contact) > len(contacts):
                            print('\nID введен некорректно или отсутсвует!\n'
                                  'Для удаления контакта выберите необходимую команду.')
                            return None
                    case 2:
                        print('\nУдаление отменено\n')
                        return None
        except ValueError:
            print('\nОшибка! Введите номер команды\n')

def question_yes_no(question: str, answer_yes: str, answer_no: str):
    print(question)
    while True:
        user_inp = input('Введите Да или Нет: ')
        if user_inp.lower() not in ['да', 'нет']:
            print('\nОшибка ! Введите да или нет.\n')
        if user_inp.lower() == 'да':
            print(answer_yes)
            return True
        if user_inp.lower() == 'нет':
            print(answer_no)
            return False

def save_answer() -> bool:
    print('\nСохранение изменении.\n')
    question = 'Сохранение изменении.\n'
    answer_yes = 'Изменения сохранены'
    answer_no = 'Изменения не сохранены'
    return question_yes_no(question, answer_yes, answer_no)

def exit_answer() -> bool:
    print('\nЗаврешение работы программы.\n')
    question = 'Завершить работу программы?\n'
    answer_yes = 'Работа программы завершена'
    answer_no = 'Работа программы не завершена'
    return question_yes_no(question, answer_yes, answer_no)

def show_message(text: str):
    print(text)

