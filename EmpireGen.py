import random

import CurrencyGen
import GovernmentGen
import LanguageGen
import PeopleNameGen
import PlaceNameGen


def gen_empire_name():
    match random.randint(0, 1):
        case 0:
            return PlaceNameGen.gen_simple_name()
        case _:
            return PeopleNameGen.gen_comp_name()


def gen_empire_capital():
    return PlaceNameGen.sticher_full_name()


def gen_empire_leader():
    return PeopleNameGen.gen_formal_name()


def gen_empire_lang():
    return LanguageGen.gen_lang_name()


def gen_empire_pop():
    temp0 = random.randint(1, 1000000)
    return str(temp0)


def gen_empire_area():
    temp0 = random.randint(1, 10000000)
    return str(temp0)


def gen_empire_currency():
    return CurrencyGen.gen_general_currency_name()


def gen_empire_gov(empire_name: str):
    return GovernmentGen.main_government(empire_name)


def main_empire():
    temp_name = gen_empire_name()
    return "Name = " + temp_name + '\n' +\
        "Capital = " + gen_empire_capital() + '\n' +\
        "Leader = " + gen_empire_leader() + '\n' +\
        "Official Language = " + gen_empire_lang() + '\n' +\
        "Population = " + gen_empire_pop() + '\n' +\
        "Area = " + gen_empire_area() + '\n' +\
        "Currency = " + gen_empire_currency() + '\n' +\
        "Government = " + gen_empire_gov(temp_name) + '\n'
