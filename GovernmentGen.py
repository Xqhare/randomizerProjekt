import random

import GenLib
import EmpireGen


def gen_rep_or_state():
    match random.randint(0, 9):
        case 0:
            return "State"
        case _:
            return "Republic"


def gen_gov_form():
    match random.randint(0, 2):
        case 0:
            form0 = random.choice(GenLib.government_name0)
            form1 = random.choice(GenLib.government_name1)
            rep_or_state = gen_rep_or_state()
            return form0 + " " + form1 + " " + rep_or_state
        case 1:
            form0 = "Semi-"
            form1 = random.choice(GenLib.government_name0)
            rep_or_state = gen_rep_or_state()
            return form0 + form1 + " " + rep_or_state
        case _:  # (Xqhare): And we fall back on the good old monarchy, as god intended
            form0 = random.choice(GenLib.government_name_monarchy)
            form1 = "Monarchy"
            return form0 + " " + form1


def main_government(empire_name: str):
    match empire_name:
        case "":
            return gen_gov_form() + " of " + EmpireGen.gen_empire_name()
        case _:
            return gen_gov_form() + " of " + empire_name
