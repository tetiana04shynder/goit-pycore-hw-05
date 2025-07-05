def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except ValueError:
            return "Дай ім'я та номер телефону."
        except IndexError:
            return "Вкаже імʼя "
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    name, phone = args.split()
    if name in contacts:
        contacts[name] = phone
        return "Контакт Оновлено."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    name = args.strip()
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result) if result else "Контактів немає"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            args = input("Enter the argument for the command: ")
            print(add_contact(args, contacts))
        
        elif command == "change":
            args = input("Enter the argument for the command: ")
            print(change_contact(args, contacts))
        
        elif command == "phone":
            args = input("Enter the argument for the command: ")
            print(get_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        elif command in ["exit", "close", "good bye"]:
            print("Good bye!")
            break
        
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
