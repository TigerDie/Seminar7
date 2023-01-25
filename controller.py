import model
import view
import sys

def show_status_bd():
    if model.state and len(model.get_db()) == 0:
        view.show_message('\nТелефонный справочник пуст!\n')
    elif not model.state and len(model.get_db) == 0:
        view.show_message('\nТелефонны справочник не открыт!\n')

def input_handler(command: int):
    match command:
        case 1:
            model.read_db('/Users/tigerdie/Desktop/обучение/PYTHON/PYTHON_GB/Seminars/Seminar7/database.txt')
            view.show_message('\nТелефонный справочник открыт\n')
        case 2:
            if model.get_db() and model.state:
                view.show_all(model.get_db())
            else:
                show_status_bd
        case 3:
            if model.get_db() and model.state:
                found_contact = model.found_contacts(view.find_choice())
                view.show_contact(found_contact)
            else:
                show_status_bd()
        case 4:
            if model.state:
                new_contact = view.create_contact(model.get_db())
                model.set_db(new_contact)
                if view.save_answer():
                    model.save_in_db('/Users/tigerdie/Desktop/обучение/PYTHON/PYTHON_GB/Seminars/Seminar7/database.txt', new_contact)
            else:
                view.show_message('\nТелефонный справочник не открыт!')
        case 5:
            if model.state and model.get_db():
                change = view.change_contact(model.get_db())
                if change is not None:
                    model.change_contact(change)
        case 6:
            if model.state and model.get_db():
                id_contact = view.delete_contact(model.get_db())
                if id_contact is not None:
                    model.delete_in_db(id_contact)
            else:
                show_status_bd()
        case 7:
            if model.state and model.get_db():
                if view.save_answer():
                    model.rewrite_db('/Users/tigerdie/Desktop/обучение/PYTHON/PYTHON_GB/Seminars/Seminar7/database.txt', model.get_db())
                else:
                    show_status_bd()
        case 8:
            view.exit_programm()

def start():            
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)

def exit_program():
    if view.exit_answer():
        sys.exit()