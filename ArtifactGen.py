import random
import GenLib
import PeopleNameGen


def gen_name():
    return random.choice(GenLib.artifact_adjective) + " " + PeopleNameGen.gen_comp_name()


def gen_material():
    return random.choice(GenLib.artifact_material)


def gen_quality():
    return random.choice(GenLib.artifact_quality)


def gen_art():
    return random.choice(GenLib.artifact_art)


def gen_dedication():
    return random.choice(GenLib.artifact_dedication)


# (Xqhare): LOOK BEFORE TOUCHING
# (Xqhare):  DOC: This function calls arti mat0 for the variables to generate a repeated statement in the output
def main_artifact():
    arti_type = random.choice(GenLib.artifact_type)
    arti_mat_gen0 = random.choice(GenLib.artifact_material)
    arti_mat_gen1 = random.choice(GenLib.artifact_material)
    arti_mat_gen2 = random.choice(GenLib.artifact_material)
    arti_mat_full = arti_mat_gen0 + ", " + arti_mat_gen1 + " and " + arti_mat_gen2
    arti_native_name = PeopleNameGen.gen_comp_name()
    return "This is " + gen_name() + ". Also known as: " + arti_native_name + ". It is a " + arti_type + \
        " made of " + arti_mat_full + " and is of " + gen_quality() + " quality." + '\n' + " It shows " + gen_art() + \
        " in " + arti_mat_gen1 + " with highlights in " + arti_mat_gen2 + ". It also shows " + gen_art() + \
        " in " + gen_material() + ". It is dedicated to " + gen_dedication() + "."
