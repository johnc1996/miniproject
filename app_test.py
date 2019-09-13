import os
import round
import json


def clear_screen():
    os.system('clear')


def print_header(title):
    print("| " + title.upper())


def print_row(rows):
    rows.sort()
    for row in rows:
        print("| " + row.capitalize())


# TODO redo border making method to be more efficient
def print_border(title, row):
    print(f"+{'=' * (calculate_row_length(title, row) + 7)}")


def print_table_header(title, row):
    print_border(title, row)
    print_header(title)
    print_border(title, row)


def print_table(title, rows):
    print_table_header(title, rows)
    print_row(rows)
    print_border(title, rows)


def calculate_row_length(title, rows):
    max_value = len(title)
    for row in rows:
        if len(row) > max_value:
            max_value = len(row)
    return max_value


def print_row_with_id(title, rows):
    rows.sort()
    id_number = 1
    for row in rows:
        print(f"| {row.capitalize()}{' ' * (calculate_row_length(title, rows) - len(row))} => {str(id_number)}")
        id_number += 1


def print_table_with_id(title, rows):
    print_table_header(title, rows)
    print_row_with_id(title, rows)
    print_border(title, rows)


def print_menu():
    print("""Welcome to BrIW!

         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \\
   |             | )  )
   |             |/  /
   |             /  /    
   |            (  /
   \\             y'
    `-.._____..-'

Please select an option below by entering a number:

    [1]  Show all people
    [2]  Show all drinks
    [3]  Add person
    [4]  Add drink
    [5]  Delete person
    [6]  Delete drink
    [7]  Add favourite
    [8]  Show favourites
    [9]  Create round
    [10] Exit
""")


def get_selection():
    number_of_menu_options = 10
    menu_options_array = list(range(1, number_of_menu_options + 1))
    while True:
        choice = input("Enter your selection: ")
        try:
            return menu_options_array[int(choice) - 1]
        except ValueError:
            print("You didn't enter a number")
        except IndexError:
            print("That isn't an option")


def return_user_selection(user_selection):
    if user_selection == 1:
        print_dict(people, "people")
    elif user_selection == 2:
        print_dict(drinks, "drinks")
    elif user_selection == 3:
        get_adds_from_user(people)
    elif user_selection == 4:
        get_adds_from_user(drinks)
    elif user_selection == 5:
        print_dict(people, "people")
        get_deletes_from_user(people)
    elif user_selection == 6:
        print_dict(drinks, "drinks")
        get_deletes_from_user(drinks)
    elif user_selection == 7:
        print_dict(people, "people")
        print_dict(drinks, "drinks")
        add_favourite()
    elif user_selection == 8:
        print_favourites()
    elif user_selection == 9:
        brew_master = input("Who is making the round? ")
        round1 = round.Round(brew_master)
        person = input("Who wants a drink? ")
        drink = input("What do they want? ")
        round1.add_to_order(person, drink)
        with open("rounds.txt", "r") as f:
            past_rounds = json.load(f)
        new_round_id = int(max(list(past_rounds.keys())))+1
        past_rounds[new_round_id] = {round1.brew_master: round1.get_drink_orders()}
        save_data_to_file("rounds.txt", past_rounds)
        # save_data_to_file("rounds.txt", {1: {round1.brew_master: round1.get_drink_orders()}})
    elif user_selection == 10:
        exit_app()


def return_to_menu():
    input("\nPress ENTER to return to the main menu")


def does_user_want_to_continue_yes_or_no(choice):
    if choice == 'Y':
        return True
    else:
        return False


def get_value_to_add():
    value_to_add = input("Enter a value to add to the dictionary: ")
    return value_to_add


def get_dictionary_length(dictionary):
    return len(dictionary)


def add_to_dictionary(dictionary):
    dictionary_length = get_dictionary_length(dictionary)
    key = dictionary_length + 1
    dictionary[key] = get_value_to_add()


def get_adds_from_user(dictionary):
    while True:
        add_to_dictionary(dictionary)
        wants_to_add = input("Do you want to add another? [y/n] ").capitalize()
        if not does_user_want_to_continue_yes_or_no(wants_to_add):
            break


def get_key_to_delete():
    while True:
        # get user input of id they want to delete
        value_to_delete = input("Enter a the id of the item you want to delete from the dictionary: ")
        try:
            # convert to int if possible
            value_to_delete = int(value_to_delete)
            return value_to_delete
        except ValueError:
            print("You didn't enter an id")
        except IndexError:
            print("You entered an id not in the dictionary")


def delete_from_dictionary(dictionary):
    del dictionary[get_key_to_delete()]


def get_deletes_from_user(dictionary):
    while True:
        delete_from_dictionary(dictionary)

        wants_to_delete = input("Do you want to delete another? [y/n] ").capitalize()
        if not does_user_want_to_continue_yes_or_no(wants_to_delete):
            break


def get_id():
    id_choice = input("Enter the id of the value you want: ")
    try:
        id_choice = int(id_choice)
        return id_choice
    except ValueError:
        print("Please enter a number")


def check_and_return_id_in_dictionary(dictionary):
    while True:
        id_to_check = get_id()
        if id_to_check in dictionary.keys():
            return id_to_check
        else:
            print("Please enter an id in the list")


def add_favourite():
    print("Enter person id")
    person_id = check_and_return_id_in_dictionary(people)
    print("Enter drink id")
    drink_id = check_and_return_id_in_dictionary(drinks)
    favourite_drink[person_id] = drink_id


def exit_app():
    save_all()
    print("Thank you for using the app")
    exit()


def load_data_to_dict(filepath):
    with open(filepath, "r") as f:
        return_dict = json.load(f)
    return return_dict


def save_data_to_file(filepath, dictionary_name):
    with open(filepath, "w") as f:
        json.dump(dictionary_name, f)


def main():
    clear_screen()
    print_menu()
    user_selection = get_selection()
    clear_screen()
    return_user_selection(user_selection)
    return_to_menu()


# person_id: name
people = load_data_to_dict("people.txt")

# drink_id: drink
drinks = load_data_to_dict("drinks.txt")

# person_id: drink_id
favourite_drink = load_data_to_dict("favourites.txt")


def print_dict(dictionary, title):
    print(f"| {'=' * 25}")
    print(f"| {title.capitalize()}")
    print(f"| {'=' * 25}")
    for key, value in dictionary.items():
        print(f"| {key} => {value.strip().capitalize()}")
    print(f"| {'=' * 25}")


def print_favourites():
    print(f"| {'=' * 25}")
    print("| Favourites")
    print(f"| {'=' * 25}")
    for key, value in favourite_drink.items():
        person_name = people.get(key).strip().capitalize()
        print(person_name)
        print(value)
        drink_name = drinks.get(value).strip().capitalize()
        print(f"| {person_name} => {drink_name}")
    print(f"| {'=' * 25}")


def save_all():
    save_data_to_file("people.txt", people)
    save_data_to_file("drinks.txt", drinks)
    save_data_to_file("favourites.txt", favourite_drink)


while True:
    main()
