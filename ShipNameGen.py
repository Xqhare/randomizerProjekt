import random

import GenLib
import PeopleNameGen


def gen_ship_name():
    match random.randint(0, 4):
        case 0:  # (Xqhare): for first and last name with a title
            return PeopleNameGen.gen_formal_name()
        case 1:  # (Xqhare): for last name with a title
            return PeopleNameGen.gen_formal_last_name()
        case 2:  # (Xqhare): for long names
            return random.choice(GenLib.ship_long_names)
        case 3:  # (Xqhare): for nouns
            lowercase_noun = random.choice(GenLib.place_noun)
            return lowercase_noun.capitalize()
        case _:  # (Xqhare): for adjectives and nouns
            lowercase_noun = random.choice(GenLib.place_noun)
            return random.choice(GenLib.artifact_adjective) + " " + lowercase_noun.capitalize()


def gen_ship_prefix(ship_prefix: str):
    """
    Returns the user chosen prefix or generates a new one
    :param ship_prefix is the string provided to be decoded
    :return: A string containing the generated prefix
    """
    match ship_prefix:
        case "":
            match random.randint(0, 1):  # (Xqhare): for random prefixes
                case 0:
                    return random.choice(GenLib.ship_prefixes) + " "
                case _:
                    match random.randint(0, 2):
                        case 0:  # (Xqhare): random prefix with 2 letters
                            letter0 = random.choice(GenLib.abc)
                            letter1 = random.choice(GenLib.abc)
                            prefix = letter0.upper() + letter1.upper()
                            return prefix + " "
                        case 1:  # (Xqhare): random prefix with 3 letters
                            letter0 = random.choice(GenLib.abc)
                            letter1 = random.choice(GenLib.abc)
                            letter2 = random.choice(GenLib.abc)
                            prefix = letter0.upper() + letter1.upper() + letter2.upper()
                            return prefix + " "
                        case _:  # (Xqhare): random prefix with 4 letters
                            letter0 = random.choice(GenLib.abc)
                            letter1 = random.choice(GenLib.abc)
                            letter2 = random.choice(GenLib.abc)
                            letter3 = random.choice(GenLib.abc)
                            prefix = letter0.upper() + letter1.upper() + letter2.upper() + letter3.upper()
                            return prefix + " "
        case " ":  # (Xqhare): for empty prefixes
            return ""
        case _:  # (Xqhare): for custom prefixes
            return ship_prefix + " "


def main_ship_name(ship_prefix: str):
    return gen_ship_prefix(ship_prefix) + gen_ship_name()
