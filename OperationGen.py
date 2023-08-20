import random
import PeopleNameGen
import GenLib
import PlaceNameGen


def gen_adj():
    match random.randint(0, 3):
        case 0:
            return random.choice(GenLib.place_single)
        case 1:
            return random.choice(GenLib.artifact_adjective)
        case 2:
            return random.choice(GenLib.artifact_material)
        case _:
            return random.choice(GenLib.artifact_quality)


def gen_obj():
    match random.randint(0, 5):
        case 0:
            return PlaceNameGen.sticher_full_name()
        case 1:
            return PeopleNameGen.gen_comp_name()
        case 2:
            return random.choice(GenLib.people_nickname)
        case 3:
            return random.choice(GenLib.people_first_name)
        case 4:
            return random.choice(GenLib.people_last_name)
        case 5:
            return random.choice(GenLib.people_skill)
        case _:
            return random.choice(GenLib.artifact_type)


def sticher_name():
    match random.randint(0, 2):
        case 0:
            return gen_obj()
        case _:
            return gen_adj() + " " + gen_obj()


def main_operation_name():
    return "Operation: " + sticher_name()
