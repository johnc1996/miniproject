import os
import pyfiglet
from prettytable import PrettyTable

import saving_logic


def save_all():
    saving_logic.save_data_to_file("people.txt", people)
    saving_logic.save_data_to_file("drinks.txt", drinks)
    saving_logic.save_data_to_file("favourites.txt", favourite_drink)


def print_main_menu():
    main_menu_banner = pyfiglet.figlet_format("brIW")
    print(main_menu_banner)
    print("""
    [1] People
    [2] Drinks
    [3] Rounds
    [4] Help
    [5] Exit
""")


def print_people_menu():
    people_menu_banner = pyfiglet.figlet_format("People")
    print(people_menu_banner)
    print("""
    [1] View people
    [2] Add people
    [3] Delete people
    [4] Add favourites
    [5] Main menu
    """)


def print_drinks_menu():
    drinks_menu_banner = pyfiglet.figlet_format("Drinks")
    print(drinks_menu_banner)
    print("""
    [1] View drinks
    [2] Add drinks
    [3] Delete drinks
    [4] Main menu
    """)


def print_rounds_menu():
    rounds_menu_banner = pyfiglet.figlet_format("Rounds")
    print(rounds_menu_banner)
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


def return_list_of_dictionary_keys(dictionary):
    list_of_keys = list(dictionary.keys())
    return list_of_keys


def get_last_element_of_list_and_add_one_then_return_as_string(list_of_keys):
    try:
        last_key_in_list = int(list_of_keys[-1])
        last_key_in_list += 1
        return str(last_key_in_list)
    except IndexError:
        return str(1)


def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary


def delete_dictionary_entry(dictionary, key):
    del dictionary[key]
    return dictionary


def create_people_table_object():
    people_table_object = PrettyTable()
    people_table_object.field_names = ["ID", "People"]
    for id_, person in people.items():
        people_table_object.add_row([id_, person.capitalize()])
    return people_table_object


def create_table_object_of_dictionary_items_and_capitalize_table_name(table_name, dictionary):
    pretty_table_object = PrettyTable()
    pretty_table_object.field_names = ["ID", table_name.capitalize()]
    for id_, value in dictionary.items():
        pretty_table_object.add_row([id_, value.capitalize()])
    return pretty_table_object


if __name__ == "__main__":
    # load data from text files to corresponding dictionaries
    people = saving_logic.load_data_to_dict("people.txt")
    drinks = saving_logic.load_data_to_dict("drinks.txt")
    favourite_drink = saving_logic.load_data_to_dict("favourites.txt")

    while True:
        clear_screen()
        print_main_menu()
        main_menu_user_choice = get_sanitised_input("Choose a main menu option: ", type_=int, min_=1, max_=5)
        clear_screen()

        # people
        if main_menu_user_choice == 1:
            while True:
                clear_screen()
                print_people_menu()
                people_menu_user_choice = get_sanitised_input("Choose a people menu option: ",
                                                              type_=int, min_=1, max_=5)
                clear_screen()

                # view people
                if people_menu_user_choice == 1:
                    # creates people table object using Prettytable each time view people option is selected
                    # TODO create object one at program start and add delete rows based on what user adds/deletes in
                    #  the session
                    people_table = create_people_table_object()
                    print(people_table)
                    print("")
                    return_to_menu()

                # add people
                elif people_menu_user_choice == 2:
                    while True:
                        clear_screen()
                        name_to_add = get_sanitised_input("Enter a name to add: ")
                        list_of_people_keys = return_list_of_dictionary_keys(people)
                        new_name_key = get_last_element_of_list_and_add_one_then_return_as_string(list_of_people_keys)
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
                        people_table = create_people_table_object()
                        print(people_table)
                        id_to_delete = get_sanitised_input("Enter the ID of the person you want to delete: ",
                                                           type_=int)
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

                # return to main menu
                else:
                    break

        # drinks
        elif main_menu_user_choice == 2:
            while True:
                clear_screen()
                print_drinks_menu()
                drinks_menu_user_choice = get_sanitised_input("Choose a drinks menu option ", type_=int, min_=1, max_=4)
                clear_screen()

                # view drinks
                if drinks_menu_user_choice == 1:
                    drinks_table = create_table_object_of_dictionary_items_and_capitalize_table_name("drinks", drinks)
                    print(drinks_table)
                    print("")
                    return_to_menu()

                # add drinks
                elif drinks_menu_user_choice == 2:
                    while True:
                        clear_screen()
                        drink_to_add = get_sanitised_input("Enter a drink to add: ")
                        list_of_drinks_keys = return_list_of_dictionary_keys(drinks)
                        new_drink_key = get_last_element_of_list_and_add_one_then_return_as_string(list_of_drinks_keys)
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
                        # show table of drinks and ID's
                        drinks_table = create_table_object_of_dictionary_items_and_capitalize_table_name("drinks",
                                                                                                         drinks)
                        print(drinks_table)
                        print("")
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

                # return to main menu
                else:
                    break

        # rounds
        elif main_menu_user_choice == 3:
            while True:
                print_rounds_menu()
                rounds_menu_user_choice = get_sanitised_input("Choose a rounds menu option: ",
                                                              type_=int, min_=1, max_=2)
                clear_screen()

                # view rounds
                if rounds_menu_user_choice == 1:
                    # TODO add view rounds option
                    pass

                # add round
                elif rounds_menu_user_choice == 2:
                    # TODO add add round option
                    pass

                # return to main menu
                else:
                    break

        # help
        elif main_menu_user_choice == 4:
            # TODO add help option
            pass

        # exit
        elif main_menu_user_choice == 5:
            save_all()
            print("Thank you for BrIWing!")
            exit()
