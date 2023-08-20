import random

import GenLib


def gen_metal():
    return random.choice(GenLib.metals_list)


def gen_alloy():
    metal0 = gen_metal()
    match random.randint(0, 2):
        case 0:
            return metal0 + "-" + gen_metal() + " Alloy"
        case 1:
            return metal0 + "-" + random.choice(GenLib.metals_alloy_list) + " Alloy"
        case _:
            match random.randint(0, 2):
                case 0:
                    return metal0 + "-" + gen_metal() + "-" + gen_metal() + " Alloy"
                case 1:
                    return metal0 + "-" + gen_metal() + "-" + random.choice(GenLib.metals_alloy_list) + " Alloy"
                case _:
                    return metal0 + "-" + random.choice(GenLib.metals_alloy_list) + "-" + random.choice(GenLib.metals_alloy_list) + " Alloy"


def main_metal_alloy():
    match random.randint(0, 1):
        case 0:
            return gen_metal()
        case _:
            return gen_alloy()
