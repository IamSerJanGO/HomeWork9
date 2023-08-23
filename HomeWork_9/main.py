from collections import defaultdict

phone_book = defaultdict(list)


def conversion(num_list) -> str:
    """
    This function is converted to a list of string.
    """
    str_num = ' '.join(num_list)
    return str_num


def converter_number_format(number):
    if len(number) == 10:
        return '+38' + number
    elif len(number) == 12:
        return '+' + number
    else:
        return f'{number} - not standard format'


def show_phone_book():
    """
    This func print all contact list
    """
    if not phone_book:
        print('Your phone book is empty :(')
    else:
        for name, number in phone_book.items():
            name_check = ' '.join([elem for elem in name])
            number_check = ' '.join(map(str, number))
            print(f'{name_check} : {number_check}')


def add_new_contact():
    new_contact_name = str(input('Enter your contact name: '))  # Запрашиваем имя контакта
    new_contact_number = str(input('Enter contact number/s: '))  # Запрпшиваем номер/а для контакта
    number_list = new_contact_number.split()  # Конвертируем строку в лист для дальнейшего форматирования
    if new_contact_name not in phone_book:
        phone_book[new_contact_name] = [converter_number_format(elem) for elem in number_list]
        print(f'Contact {new_contact_name} created!')
    else:
        print(f'Contact {new_contact_name} already exists!')


def change_contact():  # This func changed contact name
    user_input_contact = input('Enter your contact for change: ')
    if user_input_contact in phone_book:
        new_contact_name = input('Enter new neme: ')
        change = phone_book[user_input_contact]
        del phone_book[user_input_contact]
        phone_book[new_contact_name] = change
        print(f'{new_contact_name} : {conversion(change)}')
    else:
        print(f'Contact {user_input_contact} is unidentified')


def main():
    comand_list = {
        'hello': lambda: print('How can I help you? ?\n'),
        'show all': lambda: show_phone_book(),
        'close': lambda: print('Good bye!'),
        'add': add_new_contact(),
        'change name': change_contact()

    }
    while True:
        user_input = input('Enter your command: \n')

# if __name__ == '__main__':
#
# main()
