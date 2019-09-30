import os
import pyfiglet
from prettytable import PrettyTable

import database
from person import Person
from drink import Drink
from round import Round


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
    [4] View favourites
    [5] Add favourites
    [6] Main menu
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


def get_pretty_people_table_from_database():
    people_table = PrettyTable()
    people_table.field_names = ["ID", "Name"]

    people_table_data = database.get_person_id_and_person_name_from_people_database_table()

    for row in people_table_data:
        person_id = row[0]
        person_name = row[1].capitalize()
        people_table.add_row([person_id, person_name])

    return people_table


def get_pretty_drinks_table_from_database():
    drinks_table = PrettyTable()
    drinks_table.field_names = ["ID", "Name"]

    drinks_table_data = database.get_drink_id_and_drink_name_from_drink_database_table()

    for row in drinks_table_data:
        drink_id = row[0]
        drink_name = row[1].capitalize()
        drinks_table.add_row([drink_id, drink_name])

    return drinks_table


def get_pretty_favourites_table_from_database():
    favourites_table = PrettyTable()
    favourites_table.field_names = ["Person", "Favourite Drink"]

    favourites_table_data = database.get_person_and_favourite_drink_from_people_database_table()

    for row in favourites_table_data:
        person_name = row[0].capitalize()
        drink_name = row[1].capitalize()
        favourites_table.add_row([person_name, drink_name])

    return favourites_table


def get_pretty_rounds_table():
    rounds_table = PrettyTable()
    rounds_table.field_names = ["ID", "Active", "StartTime", "Initiator"]

    rounds_table_data = database.get_rounds_info_from_rounds_database_table()

    for row in rounds_table_data:
        round_id = row[0]
        active_status = row[1]
        start_time = row[2]
        initiator = row[3].capitalize()
        rounds_table.add_row([round_id, active_status, start_time, initiator])

    return rounds_table


if __name__ == "__main__":
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
                                                              type_=int, min_=1, max_=6)
                clear_screen()

                # view people
                if people_menu_user_choice == 1:
                    print(get_pretty_people_table_from_database())
                    return_to_menu()

                # add people
                elif people_menu_user_choice == 2:
                    while True:
                        clear_screen()
                        person_to_add = get_sanitised_input("Enter a name to add: ").lower()
                        clear_screen()

                        if person_to_add is not "":
                            person = Person(person_to_add)
                            person.insert_person_into_database_and_update_id_with_database_value()
                            print("Person added")
                        else:
                            print("You didn't enter a name")

                        user_continue = get_sanitised_input("Do you want to add another name? [y/n]: ",
                                                            type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                        if user_continue.upper() == 'N':
                            break

                # delete people
                elif people_menu_user_choice == 3:
                    while True:
                        clear_screen()
                        print(get_pretty_people_table_from_database())
                        id_to_delete = get_sanitised_input("Enter the ID of the person you want to delete: ",
                                                           type_=int)
                        clear_screen()
                        database.delete_person_from_database(id_to_delete)
                        user_continue = get_sanitised_input("Do you want to delete another person? [y/n]: ",
                                                            type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                        if user_continue.upper() == 'N':
                            break

                elif people_menu_user_choice == 4:
                    # view favourites
                    print(get_pretty_favourites_table_from_database())
                    return_to_menu()

                # add favourites
                elif people_menu_user_choice == 5:
                    # TODO add add favourites option
                    while True:
                        clear_screen()
                        print(get_pretty_people_table_from_database())
                        person_to_add_favourite_to = get_sanitised_input("Enter the ID of the person you want to add a "
                                                                         "favourite to: ", type_=int)
                        clear_screen()

                        print(get_pretty_drinks_table_from_database())
                        person_favourite_drink = get_sanitised_input("Enter the ID of the drink that is the persons "
                                                                     "favourite: ", type_=int)
                        clear_screen()

                        database.update_favourite_pairing_of_person_id_and_drink_id(person_to_add_favourite_to,
                                                                                    person_favourite_drink)

                        user_continue = get_sanitised_input("Do you want to add another favourite? [y/n]: ",
                                                            type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                        if user_continue.upper() == 'N':
                            break

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
                    print(get_pretty_drinks_table_from_database())
                    return_to_menu()

                # add drinks
                elif drinks_menu_user_choice == 2:
                    while True:
                        clear_screen()
                        drink_to_add = get_sanitised_input("Enter a drink to add: ").lower()
                        clear_screen()

                        if drink_to_add is not "":
                            drink = Drink(drink_to_add)
                            drink.insert_drink_into_database_and_update_id_with_database_value()
                            print("Drink added")
                        else:
                            print("You didn't enter a drink")

                        user_continue = get_sanitised_input("Do you want to add another drink? [y/n]: ",
                                                            type_=str.lower, range_=('y', 'Y', 'n', 'N'))
                        if user_continue.upper() == 'N':
                            break

                # delete drinks
                elif drinks_menu_user_choice == 3:
                    while True:
                        # show table of drinks and ID's
                        print(get_pretty_drinks_table_from_database())
                        id_to_delete = get_sanitised_input("Enter the ID of the drink you want to delete: ", type_=int)
                        clear_screen()

                        database.delete_drink_from_database(id_to_delete)

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
                clear_screen()
                print_rounds_menu()
                rounds_menu_user_choice = get_sanitised_input("Choose a rounds menu option: ",
                                                              type_=int, min_=1, max_=3)
                clear_screen()

                # view past rounds list
                if rounds_menu_user_choice == 1:
                    # TODO add view rounds option
                    # print table of past rounds with round id and drink maker of round
                    print(get_pretty_rounds_table())
                    return_to_menu()

                # add round
                elif rounds_menu_user_choice == 2:
                    # create a round object
                    people_table = get_pretty_people_table_from_database()
                    print(people_table)
                    initiator = get_sanitised_input("Enter the id of the person making the round: ", type_=int)

                    drink_round = Round(initiator)
                    drink_round.insert_round_into_database_and_update_id_with_database_value()
                    return_to_menu()

                # return to main menu
                else:
                    break

        # help
        elif main_menu_user_choice == 4:
            # TODO add help option
            pass

        # exit
        elif main_menu_user_choice == 5:
            print("Thank you for brIWing!")
            exit()
