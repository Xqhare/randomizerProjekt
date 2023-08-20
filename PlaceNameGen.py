import random
import GenLib
import PeopleNameGen


def gen_simple_name():
    match random.randint(0, 2):
        case 0:
            return random.choice(GenLib.place_single)
        case 1:
            return random.choice(GenLib.people_nickname)
        case _:
            return PeopleNameGen.gen_comp_name()


def gen_adj():
    match random.randint(0, 1):
        case 0:
            return gen_simple_name() + " "
        case _:
            return ""


def sticher_full_name():
    match random.randint(0, 3):
        case 0:
            return gen_simple_name()
        case 1:
            return gen_simple_name() + " " + gen_simple_name()
        case 2:
            return PeopleNameGen.gen_comp_name() + "'s " + gen_simple_name()
        case _:
            return PeopleNameGen.gen_comp_name()


def gen_fame():
    match random.randint(0, 2):
        case 0:
            match random.randint(0, 1):
                case 0:
                    fame = random.choice(GenLib.place_noun)
                    return '\n' + "It's known for it's " + fame + "."
                case _:
                    fame = random.choice(GenLib.place_top_eng_nouns)
                    return '\n' + "It's known for it's " + fame + "."
        case _:
            return ""


def gen_relative():
    match random.randint(0, 2):
        case 0:
            return "It's " + random.choice(GenLib.place_relatives) + " normal."
        case _:
            return ""


def gen_place_description():
    return "It's a " + random.choice(GenLib.place_object) + ". " + gen_relative() + gen_fame()


def main_place_name():
    return gen_adj() + sticher_full_name() + '\n' + gen_place_description() + '\n'
