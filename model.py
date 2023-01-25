db_list: list = []
state: bool = False

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding = 'UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)

def open_1():
    global db_list

def get_db():
    global db_list
    return db_list

def set_db(new_data: str):
    global db_list
    db_list.append(new_data)

def delete_in_db(id_contact: str) -> list:
    db_list.pop(int(id_contact) - 1)
    for i, value in enumerate(db_list):
        value['ID'] = 'id_' + str(i + 1)
    return db_list

def save_in_db(path: str, new_contact: dict):
    contact = ''
    if len(db_list) == 1:
        contact = ';'.join(new_contact.values())
    elif len(db_list) > 1:
        contact ='\n' + contact
    with open(path, 'a', encoding='UTF-8') as data:
        data.write(contact)

def read_db(path: str):
    global state
    state = True
    with open(path, 'r', encoding='UTF-8') as data:
        data_list = data.readlines()
        for line in data_list:
            contact_info = line.strip().split(';')
            key_info = ['ID', 'Lastname', 'Firstname', 'Phone', 'Comment']
            dict_contact = dict(zip(key_info, contact_info))
            set_db(dict_contact)

def rewrite_db(path: str, new_contacts: list):
    new_data = []
    for item in new_contacts:
        contact = ';'.join(item.values())
        contact += '\n'
        new_data.append(contact)
    with open(path, 'w', encoding='UTF-8') as data:
        for item in new_data:
            data.write(item)

def change_contact(change_data: tuple) -> list:
    i = change_data[0] - 1
    new_contact = change_data[1]
    db_list[i]['Lastname'] = new_contact['Lastname']
    db_list[i]['Firstname'] = new_contact['Firstname']
    db_list[i]['Phone'] = new_contact['Phone']
    db_list[i]['Comment'] = new_contact['Comment']
    return db_list

def found_contacts(find_choice: tuple) -> list:
    
    def find() -> list:
        keys = ['Lastname', 'Firstname', 'Lastname_firstname', 'Phone', 'ID']
        found: list = []
        for value in db_list:
            if find_choice[1].lower() == value[keys[find_choice[0] - 1]].lower():
                found.append(value)
        return found
    
    match find_choice[0]:
        case 1:
            new_found: list = find()
            return new_found
        case 2:
            new_found: list = find()
            return new_found
        case 3:
            new_found: list = []
            find = list(find_choice[1].lower().split())
            if len(find) == 1:
                return new_found
            if len(find) == 2:
                for item in db_list:
                    if find[0] == item['Lastname'].lower() and find[1] == item['Firstname'].lower():
                        new_found.append(item)
                return new_found
        case 4:
            new_found: list = find()
            return new_found
        case 5: 
            new_found: list = find()
            return new_found
