import random


def main_number_gen(usr_min, usr_max, text):
    match text:
        case "int":
            output = random.randint(usr_min, usr_max)
            return str(output)
        case "float":
            output = random.uniform(usr_min, usr_max)
            return str(output)
        case _:
            print("Error - Number.1")
            return "Error - Number.1"
