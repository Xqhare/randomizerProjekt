import GenLib
import random


def gen_comp_name():
    return random.choice(GenLib.general_comp0) + random.choice(GenLib.general_comp1)


def gen_first_name():
    match random.randint(0, 1):
        case 0:
            return gen_comp_name()
        case _:
            return random.choice(GenLib.people_first_name)


def gen_last_name():
    match random.randint(0, 1):
        case 0:
            return gen_comp_name()
        case _:
            return random.choice(GenLib.people_last_name)


def sticher_legal_name():
    return gen_first_name() + " " + gen_last_name()


# (Xqhare): Bodge way of getting 33% nicknames
def gen_nickname():
    match random.randint(0, 2):
        case 0:
            return random.choice(GenLib.people_nickname)
        case _:
            return ""


def gen_formal_name():
    return random.choice(GenLib.people_title) + " " + sticher_legal_name()


def gen_formal_last_name():
    return random.choice(GenLib.people_title) + " " + gen_last_name()


def sticher_full_name():
    nick = gen_nickname()
    legal = sticher_legal_name()
    return "Name: " + legal + ". Nickname: " + nick


def gen_skill():
    skill_lvl = random.choice(GenLib.people_skill_level)
    skill = random.choice(GenLib.people_skill)
    return skill_lvl + " " + skill


def gen_trait():
    seed = random.randint(0, 1)
    match seed:
        case 0:
            output = random.choice(GenLib.people_trait_ck3)
            return output
        case _:
            output = random.choice(GenLib.people_trait_ck2)
            return output


def main_generated_person():
    skill0 = gen_skill()
    skill1 = gen_skill()
    skill2 = gen_skill()
    trait0 = gen_trait()
    trait1 = gen_trait()
    trait2 = gen_trait()
    full_name = sticher_full_name()
    return full_name + '\n' + \
        "They are a " + skill0 + "," + '\n' + \
        " a " + skill1 + "," + '\n' + \
        " and a " + skill2 + "." + '\n' + \
        "They are " + trait0 + ", " + trait1 + " and " + trait2 + '\n'
