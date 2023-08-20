import ArtifactGen
import GenLib
import random

import GovernmentGen
import OperationGen
import PeopleNameGen
# (Xqhare):  Dwarfs + dancing +-/
# (Xqhare):     and + singing +/
# (Xqhare):     at + PlaceGen +/
# (Xqhare):     because + something /


def gen_actor():
    match random.randint(0, 2):
        case 0:
            return random.choice(GenLib.scene_actors)
        case 1:
            return GovernmentGen.main_government("")
        case _:
            return PeopleNameGen.gen_comp_name()


def gen_verb():
    return random.choice(GenLib.scene_verbs)


def gen_obj():
    match random.randint(0, 3):
        case 0:
            return random.choice(GenLib.scene_objects)
        case 1:
            return PeopleNameGen.gen_comp_name()
        case 2:
            return OperationGen.main_operation_name()
        case _:
            return ArtifactGen.gen_name()


def main_scene():
    return gen_actor() + " " + gen_verb() + " " + gen_obj()
