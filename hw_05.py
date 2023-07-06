contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please provide name and phone number separated by a space."
    return inner

@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_phone(command):
    _, name = command.split()
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def user_command(command):
    command = command.lower()

    if command == "hello":
        return "How can I help you?"
    if command.startswith("add"):
        return add_contact(command)
    if command.startswith("change"):
        return change_contact(command)
    if command.startswith("phone"):
        return get_phone(command)
    if command == "show all":
        return show_all_contacts()
    if command in ["good bye", "close", "exit"]:
        return "Good bye!"
    return "Invalid command. Please try again."

def main():
    print("Welcome!")
    while True:
        command = input("Enter a command: ")
        result = user_command(command)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()
