import random

import PlaceNameGen
import PeopleNameGen


def gen_lang_name():
    match random.randint(0, 1):
        case 0:
            return PlaceNameGen.gen_simple_name()
        case _:
            return PeopleNameGen.gen_comp_name()


def main_language():
    return gen_lang_name()
