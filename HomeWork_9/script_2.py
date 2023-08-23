phone_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Error: contact not found.'
        except ValueError:
            return "Error: Invalid input. Please enter name and phone number."
        except IndexError:
            return "Error: Invalid input. Please enter name and phone number."

    return inner


@input_error
def chenge(name, number):
    if name not in phone_book:
        raise KeyError
    else:
        phone_book[name] = number
        return f'New number contact {name} is {number}'


@input_error
def add_contact(name, number):
    if name in phone_book:
        raise ValueError
    else:
        phone_book[name] = number
        return f'New contact {name} with number {number} - created!'


@input_error
def phone_check(name):
    if name not in phone_book:
        raise KeyError
    else:
        return f'Contact {name} number : {phone_book[name]}'


@input_error
def show_phone_book():
    if not phone_book:
        raise ValueError
    else:
        contact = 'Contact\n'
        for name, number in phone_book.items():
            contact += f'{name} : {number}'
    return contact


def main():
    commands = {
        "hello": lambda: print("How can I help you?"),
        "add": lambda: print(add_contact(devided_user_input[1], devided_user_input[2])) if len(
            devided_user_input) == 3 else print('Error: enter '
                                                'name and '
                                                'number'),
        "change": lambda: print(chenge(devided_user_input[1], devided_user_input[2])) if len(devided_user_input) == 3
        else print('Error: enter name and number'),
        "phone": lambda: print(phone_check(devided_user_input[1])) if len(devided_user_input) == 2 else print(
            'Contact not found'),
        "show all": lambda: print(show_phone_book()) if phone_book else print('Your phone book is empty :('),
        "good bye": lambda: print("Good bye!"),
        "close": lambda: print("Good bye!"),
        "exit": lambda: print("Good bye!")
    }
    while True:
        user_input = input('Enter your command: ')
        devided_user_input = user_input.split(maxsplit=2)
        user_command = devided_user_input[0].strip().lower()

        if user_command in commands:
            commands[user_command]()
            if user_command in ['close', 'exit']:
                break
        elif user_input.lower() in commands:
            commands[user_input.lower()]()
            if user_input.lower() == 'good bye':
                break
        else:
            print('Invalid input command. Available commands: hello/add/change/phone/show all/good bye/close/exit')


if __name__ == '__main__':
    main()
