def get_valid_name(name_to_enter):
    print(f"Enter a {name_to_enter}")
    while True:
        name = input(">> ")
        if name.isalpha():
            return name
        print("Please only enter letters")


def get_valid_id(id_to_enter, valid_ids):
    print(f"Enter a {id_to_enter} ID")
    while True:
        _id = input(">> ")
        if _id.isdigit() and int(_id) in valid_ids:
            return int(_id)
        print("Invalid ID")


