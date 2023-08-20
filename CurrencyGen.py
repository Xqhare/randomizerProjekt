import random

import GenLib
import MetalAlloyGen
import PeopleNameGen
import PlaceNameGen


def gen_currency_name_ending():
    match random.randint(0, 1):
        case 0:
            return random.choice(GenLib.currency_endings)
        case _:
            return " " + random.choice(GenLib.currency_second_word)


def gen_general_currency_name():
    match random.randint(0, 2):
        case 0:
            match random.randint(0, 2):
                case 0:
                    letter0 = random.choice(GenLib.abc)
                    letter1 = random.choice(GenLib.abc)
                    letter2 = random.choice(GenLib.abc)
                    return letter0.capitalize() + letter1 + letter2 + gen_currency_name_ending()
                case 1:
                    letter0 = random.choice(GenLib.abc)
                    letter1 = random.choice(GenLib.abc)
                    letter2 = random.choice(GenLib.abc)
                    letter3 = random.choice(GenLib.abc)
                    return letter0.capitalize() + letter1 + letter2 + letter3 + gen_currency_name_ending()
                case _:
                    letter0 = random.choice(GenLib.abc)
                    letter1 = random.choice(GenLib.abc)
                    letter2 = random.choice(GenLib.abc)
                    letter3 = random.choice(GenLib.abc)
                    letter4 = random.choice(GenLib.abc)
                    return letter0.capitalize() + letter1 + letter2 + letter3 + letter4 + gen_currency_name_ending()
        case _:
            match random.randint(0, 1):
                case 0:
                    return random.choice(GenLib.currency_real_fractional_names)
                case _:
                    return random.choice(GenLib.currency_real_names)


def gen_currency_abbreviation(name: str):
    """
    Returns a capitalized abbreviation of a supplied name
    :param name is the string provided to be abbreviated
    :return: A string containing the generated capitalized abbreviation
    """
    letter0 = name[0]
    name0 = name[1:]
    letter1 = random.choice(name0)
    letter2 = random.choice(name0)
    return letter0.capitalize() + letter1 + letter2


def gen_non_decimal_currency_system():
    subunit0 = gen_general_currency_name()
    subunit1 = gen_general_currency_name()
    subunit2 = gen_general_currency_name()
    subunit1_base = random.choice(GenLib.currency_non_decimal_base_120)
    subunit2_base = random.choice(GenLib.currency_non_decimal_base_120)
    return "1 " + subunit0 + " equals " + str(subunit1_base) + " " + subunit1 + '\n' + \
        "1 " + subunit1 + " equals " + str(subunit2_base) + " " + subunit2


def gen_decimal_currency_system():
    match random.randint(0, 1):
        case 0:
            superunit = gen_general_currency_name()
            unit = gen_general_currency_name()
            subunit = gen_general_currency_name()
            return "1 " + superunit + " equals 100 " + unit + '\n' + \
                "1 " + unit + " equals 100 " + subunit
        case _:
            unit = gen_general_currency_name()
            subunit = gen_general_currency_name()
            return "1 " + unit + " equals 100 " + subunit


def gen_coin_composition():
    match random.randint(0, 1):
        case 0:
            return "is made of " + MetalAlloyGen.main_metal_alloy()
            # (Xqhare): single metallic or alloy coin
        case _:
            return "is made with a " + MetalAlloyGen.main_metal_alloy() + " center plug, and a " + MetalAlloyGen.main_metal_alloy() + " outer ring."
            # (Xqhare): bi metallic coin


def gen_coin_iconography_bonus():
    match random.randint(0, 1):
        case 0:
            insignia = random.choice(GenLib.artifact_type)
            return "a " + insignia
        case _:
            insignia = random.choice(GenLib.currency_icon_insignia)
            return "a " + insignia


def gen_coin_iconography_main(n: int):
    """
    Returns iconography for coins
    :param n is for decoding; n == for normal calls use 3; with 4 repeated motif is possible -> for reverse only
    :return: A string containing the generated iconography
    """
    match random.randint(0, n):  # (Xqhare): for obverse side | n == for normal calls use 3; with 4 repeated motif is possible -> for reverse only
        case 0:
            match random.choice(GenLib.currency_icon_inscription):
                case "Letter":
                    letter_temp = random.choice(GenLib.abc)
                    letter_out = letter_temp.capitalize()
                    return letter_out
                case "Monogram":
                    mono0 = random.choice(GenLib.abc)
                    mono1 = random.choice(GenLib.abc)
                    mono_out = mono0.capitalize() + mono1.capitalize()
                    return mono_out
                case "Name":
                    match random.randint(0, 1):
                        case 0:
                            return PeopleNameGen.gen_formal_name()
                        case _:
                            return PlaceNameGen.sticher_full_name()
                case _:
                    print("Error - Currency.2")
                    return "Error - Currency.2"
        case 1:
            match random.choice(GenLib.currency_icon_figure):
                case "Person":
                    m_f = ["male", "female", "indiscernible"]
                    match random.choice(m_f):
                        case "male":
                            return "a male figure with " + gen_coin_iconography_bonus()
                        case "female":
                            return "a female figure with " + gen_coin_iconography_bonus()
                        case "indiscernible":
                            return "a indiscernible figure with " + gen_coin_iconography_bonus()
                case "Creature":
                    match random.randint(0, 4):
                        case 0:
                            return "a mythical " + random.choice(GenLib.currency_icon_mythical_creature) + " and a " + gen_coin_iconography_bonus()
                        case _:
                            return "a mythical " + random.choice(GenLib.currency_icon_mythical_creature)
                case "Animal":
                    match random.randint(0, 4):
                        case 0:
                            return "a " + random.choice(GenLib.currency_icon_animal) + " and a " + gen_coin_iconography_bonus()
                        case _:
                            return "a " + random.choice(GenLib.currency_icon_animal)
                case "Plant":
                    match random.randint(0, 4):
                        case 0:
                            return "a " + random.choice(GenLib.currency_icon_plant) + " and a " + gen_coin_iconography_bonus()
                        case _:
                            return "a " + random.choice(GenLib.currency_icon_plant)
                case "Object":
                    return "a " + random.choice(GenLib.artifact_type)
                case _:
                    print("Error - Currency.3")
                    return "Error - Currency.3"
        case 2:
            match random.randint(0, 4):
                case 0:
                    return "a " + random.choice(GenLib.currency_icon_partial) + " and a " + gen_coin_iconography_bonus()
                case _:
                    return "a " + random.choice(GenLib.currency_icon_partial)
        case 3:
            return "a incuse of a " + random.choice(GenLib.currency_icon_incuse)
        case 4:
            return "the same motif repeated"


def sticher_coin_iconography():
    obverse = gen_coin_iconography_main(3)
    reverse = gen_coin_iconography_main(4)
    return "It shows " + obverse + " on it's front, and" + '\n' + \
        "it shows " + reverse + " on it's back."


# (Xqhare): IMPORTANT: coin value 1 is assumed to be done in function
# (Xqhare): TODO: there has to be a nice and simple loop to do this
def gen_coin_denomination_material_icon(name: str):
    """
    Returns what kind of coins are used
    :param name is the name of the coin needed for output
    :return: A string containing the generated coins used with material and iconography
    """
    coin_num = random.randint(0, 6)
    denomination = random.sample(GenLib.currency_coins_denomination, k=coin_num)
    unlisted_denomination = ", ".join(denomination)
    match len(denomination):
        case 0:
            return "The " + name + " has the 1 coin." + '\n' +\
                "The 1 " + name + " coin, " + gen_coin_composition()
        case 1:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'
        case 2:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[1] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'
        case 3:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[1] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[2] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'
        case 4:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[1] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[2] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[3] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'
        case 5:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[1] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[2] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[3] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[4] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'
        case _:
            return "The " + name + " has the 1, " + unlisted_denomination + " coins." + '\n' + \
                "The 1 " + name + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[0] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[1] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[2] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[3] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[4] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n' + \
                "The " + denomination[5] + " coin, " + gen_coin_composition() + '\n' + \
                sticher_coin_iconography() + '\n'


def gen_time_currency_system():
    name = gen_general_currency_name() + " HOUR"
    subunit = random.choice(GenLib.currency_time_fractions)
    return "The currency is called: " + name + '\n' + \
        "1 " + name + " is equal to " + str(subunit) + " hours of work for the good of society." + '\n' + \
        gen_coin_denomination_material_icon(name) + '\n' + '\n'


def main_currency(user_choice_decimal: str):
    """
    Main function, decoding user choice and returning a complete currency
    :param user_choice_decimal is the string provided to be decoded
    :return: A string containing the entire generated currency
    """
    name = gen_general_currency_name()
    superunit = gen_general_currency_name()
    unit = name
    subunit = gen_general_currency_name()
    match user_choice_decimal:
        case "Decimal":
            match random.randint(0, 2):
                case 0:  # (Xqhare): no superunit
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + unit + " = 100 " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
                case 1:  # (Xqhare): with superunit
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The super unit is called: " + superunit + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + superunit + " = 100 " + unit + " = 1000 " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(superunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
                case _:  # (Xqhare): only main unit
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
        case "Time based":
            return gen_time_currency_system()
        case "Non-Decimal":
            match random.randint(0, 3):
                case 0:  # (Xqhare): 3 units
                    base = random.sample(GenLib.currency_non_decimal_base_120, k=2)
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The super unit is called: " + superunit + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + superunit + " = " + base[0] + " " + unit + '\n' + \
                        "And 1 " + unit + " = " + base[1] + " " + subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(superunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
                case 1:  # (Xqhare): 4 units
                    sec_subunit = gen_general_currency_name()
                    base = random.sample(GenLib.currency_non_decimal_base_120, k=3)
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The super unit is called: " + superunit + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "The second sub unit is called: " + sec_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + superunit + " = " + base[0] + " " + unit + '\n' + \
                        "And 1 " + unit + " = " + base[1] + " " + subunit + '\n' + \
                        "And 1 " + subunit + " = " + base[2] + " " + sec_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(superunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(sec_subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
                case 2:  # (Xqhare): 5 units
                    sec_subunit = gen_general_currency_name()
                    third_subunit = gen_general_currency_name()
                    base = random.sample(GenLib.currency_non_decimal_base_120, k=4)
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The super unit is called: " + superunit + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "The second sub unit is called: " + sec_subunit + '\n' + \
                        "The third sub unit is called: " + third_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + superunit + " = " + base[0] + " " + unit + '\n' + \
                        "And 1 " + unit + " = " + base[1] + " " + subunit + '\n' + \
                        "And 1 " + subunit + " = " + base[2] + " " + sec_subunit + '\n' + \
                        "And 1 " + sec_subunit + " = " + base[3] + " " + third_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(superunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(sec_subunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(third_subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
                case _:  # (Xqhare): 6 units
                    sec_subunit = gen_general_currency_name()
                    third_subunit = gen_general_currency_name()
                    fourth_subunit = gen_general_currency_name()
                    base = random.sample(GenLib.currency_non_decimal_base_120, k=5)
                    return "The currency is called: " + name + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "It is abbreviated as: " + gen_currency_abbreviation(name) + '\n' + \
                        "The super unit is called: " + superunit + '\n' + \
                        "The main unit is called: " + unit + '\n' + \
                        "The sub unit is called: " + subunit + '\n' + \
                        "The second sub unit is called: " + sec_subunit + '\n' + \
                        "The third sub unit is called: " + third_subunit + '\n' + \
                        "The fourth sub unit is called: " + fourth_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        "The set exchange rate is: 1 " + superunit + " = " + base[0] + " " + unit + '\n' + \
                        "And 1 " + unit + " = " + base[1] + " " + subunit + '\n' + \
                        "And 1 " + subunit + " = " + base[2] + " " + sec_subunit + '\n' + \
                        "And 1 " + sec_subunit + " = " + base[3] + " " + third_subunit + '\n' + \
                        "And 1 " + third_subunit + " = " + base[4] + " " + fourth_subunit + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(superunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(unit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(subunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(sec_subunit) + '\n' + \
                        "------------------------------------------" + '\n' + \
                        gen_coin_denomination_material_icon(third_subunit) + '\n' + '\n' + \
                        "------------------------------------------" + '\n' + '\n'
        case _:
            print("Error - Currency.1", user_choice_decimal)
            return "Error - Currency.1"
