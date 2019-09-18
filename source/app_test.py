import os
import round
import json
import saving_logic


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


def get_and_update_drink_round():
    print("Please enter the name of the person who is making the drink round")
    brew_master = input("$")
    round1 = round.Round(brew_master)
    print("Please enter name of the person who wants a drink and their chosen drink")
    while True:
        person = input("Person $")
        drink = input("Drink $")
        round1.add_to_order(person, drink)
        print("Do you want to add another person to the round? [y/n]")
        user_continue = input("$")
        break
    with open("rounds.txt", "r") as f:
        past_rounds = json.load(f)
    if len(past_rounds.keys()) == 0:
        new_round_id = 1
    else:
        new_round_id = int(max(list(past_rounds.keys()))) + 1
    past_rounds[new_round_id] = {round1.brew_master: round1.get_drink_orders()}
    saving_logic.save_data_to_file("rounds.txt", past_rounds)


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
        try:
            person_name = people.get(key).strip().capitalize()
            drink_name = drinks.get(str(value)).strip().capitalize()
            print(f"| {person_name} => {drink_name}")
        except AttributeError:
            pass
        except:
            print("Unexpected error occured")
    print(f"| {'=' * 25}")


def load_data_to_dict(filepath):
    with open(filepath, "r") as f:
        return_dict = json.load(f)
    return return_dict


def save_all():
    saving_logic.save_data_to_file("people.txt", people)
    saving_logic.save_data_to_file("drinks.txt", drinks)
    saving_logic.save_data_to_file("favourites.txt", favourite_drink)

#
#
#
#
#


# person_id: name
people = load_data_to_dict("people.txt")

# drink_id: drink
drinks = load_data_to_dict("drinks.txt")

# person_id: drink_id
favourite_drink = load_data_to_dict("favourites.txt")


def print_main_menu():
    print("""Welcome to BrIW!

    [1] People
    [2] Drinks
    [3] Rounds
    [4] Help
    [5] Exit
""")


def print_people_menu():
    print("""
    [1] View people
    [2] Add people
    [3] Delete people
    [4] Add favourites
    [5] Main menu
    """)


def print_drinks_menu():
    print("""
    [1] View drinks
    [2] Add drinks
    [3] Delete drinks
    [4] Main menu
    """)


def print_rounds_menu():
    print("""
    [1] View rounds
    [2] Add round
    [3] Main menu
    """)


def clear_screen():
    os.system('clear')


def return_to_menu():
    input("Press ENTER to return to the main menu")


def get_sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    # checks min is not larger than max
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min must be less than or equal to max_")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            # exception if user input is incorrect type
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        # checks if ui is too large
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        # checks if ui is too small
        elif min_ is not None and ui < min_:
            print("Input must be more than or equal to {0}".format(min_))
        # checks if ui is within range of values
        elif range_ is not None and ui not in range_:
            # output if range are all ints
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join((", ".join(map(str,
                                                                     range_[:-1])),
                                                       str(range_[-1])))))
        else:
            return ui


def get_key_for_new_value_as_string(dictionary):
    key = str(len(dictionary) + 1)
    return key


def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary


def delete_dictionary_entry(dictionary, key):
    del dictionary[key]
    return dictionary


if __name__ == "__main__":
    while True:
        clear_screen()
        print_main_menu()
        main_menu_user_choice = get_sanitised_input("Choose a main menu option: ", type_=int, min_=1, max_=5)
        clear_screen()

        # people
        if main_menu_user_choice == 1:
            print_people_menu()
            people_menu_user_choice = get_sanitised_input("Choose a people menu option: ", type_=int, min_=1, max_=5)
            clear_screen()
            # view people
            if people_menu_user_choice == 1:
                # TODO add view people method
                pass

            # add people
            elif people_menu_user_choice == 2:
                while True:
                    clear_screen()
                    name_to_add = get_sanitised_input("Enter a name to add: ")
                    new_name_key = get_key_for_new_value_as_string(people)
                    people = add_to_dictionary(people, new_name_key, name_to_add)
                    clear_screen()
                    print("Person added")
                    user_continue = get_sanitised_input("Do you want to add another name? [y/n]: ",
                                                        type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                    if user_continue.upper() == 'N':
                        break

            # delete people
            elif people_menu_user_choice == 3:
                while True:
                    # show table of people and ID's
                    clear_screen()
                    id_to_delete = get_sanitised_input("Enter the ID of the person you want to delete: ", type_=int)
                    clear_screen()
                    if str(id_to_delete) in people.keys():
                        # delete corresponding person from dictionary
                        people = delete_dictionary_entry(people, str(id_to_delete))
                        print("Person deleted")
                    else:
                        print("That ID is not in the list")
                    user_continue = get_sanitised_input("Do you want to delete another person? [y/n]: ",
                                                        type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                    if user_continue.upper() == 'N':
                        break

            # add favourites
            elif people_menu_user_choice == 4:
                # TODO add add favourites option
                pass

            else:
                print("Returning to menu...")
                continue

        # drinks
        elif main_menu_user_choice == 2:
            print_drinks_menu()
            drinks_menu_user_choice = get_sanitised_input("Choose a drinks menu option ", type_=int, min_=1, max_=4)
            clear_screen()

            # view drinks
            if drinks_menu_user_choice == 1:
                # TODO add view drinks option
                pass

            # add drinks
            elif drinks_menu_user_choice == 2:
                while True:
                    clear_screen()
                    drink_to_add = get_sanitised_input("Enter a drink to add: ")
                    new_drink_key = get_key_for_new_value_as_string(drinks)
                    drinks = add_to_dictionary(drinks, new_drink_key, drink_to_add)
                    clear_screen()
                    print("Drink added")
                    user_continue = get_sanitised_input("Do you want to add another drink? [y/n]: ",
                                                        type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                    if user_continue.upper() == 'N':
                        break

            # delete drinks
            elif drinks_menu_user_choice == 3:
                while True:
                    # show table of people and ID's
                    id_to_delete = get_sanitised_input("Enter the ID of the drink you want to delete: ", type_=int)
                    clear_screen()
                    if str(id_to_delete) in drinks.keys():
                        # delete corresponding person from dictionary
                        drinks = delete_dictionary_entry(drinks, str(id_to_delete))
                        print("Drink deleted")
                    else:
                        print("That ID is not in the list")
                    user_continue = get_sanitised_input("Do you want to delete another drink? [y/n]: ",
                                                        type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                    if user_continue.upper() == 'N':
                        break

        # rounds
        elif main_menu_user_choice == 3:
            print_rounds_menu()
            rounds_menu_user_choice = get_sanitised_input("Choose a rounds menu option: ", type_=int, min_=1, max_=2)
            clear_screen()

            # view rounds
            if rounds_menu_user_choice == 1:
                # TODO add view rounds option
                pass

            # add round
            elif rounds_menu_user_choice == 2:
                # TODO add add round option
                pass

        # help
        elif main_menu_user_choice == 4:
            # TODO add help option
            pass

        # exit
        elif main_menu_user_choice == 5:
            print("Thank you for BrIWing!")
            exit()

        clear_screen()
        return_to_menu()
        clear_screen()
