import random
import GenLib
import ShipNameGen


def gen_ship_size():
    return random.choice(GenLib.ship_sizes)


# (Xqhare): returns a ship type, e.g. Battleship, Fighter
def gen_ship_type(ship_size: str):
    """
    Returns the user chosen ship size or generates a new one
    :param ship_size is the string provided to be decoded
    :return: A string containing the generated ship size
    """
    match ship_size:
        case "SS":
            return random.choice(GenLib.ship_type_ss)
        case "XS":
            return random.choice(GenLib.ship_type_xs)
        case "S":
            return random.choice(GenLib.ship_type_s)
        case "M":
            return random.choice(GenLib.ship_type_m)
        case "L":
            return random.choice(GenLib.ship_type_l)
        case "XL":
            return random.choice(GenLib.ship_type_xl)
        case "XXL":
            return random.choice(GenLib.ship_type_xxl)
        case "U":
            return random.choice(GenLib.ship_type_u)
        case "XU":
            return random.choice(GenLib.ship_type_xu)
        case "T":
            return random.choice(GenLib.ship_type_t)
        case _:
            print("Error - ShipClass.1", ship_size)
            return "Error - ShipClass.1"


def gen_ftl_capability(avg_range: int, lower_speed_bound: float, upper_speed_bound: float, ftl_chance: int):
    """
    Generates if a ship is ftl capable, if it is, the jump range is returned.
    :param avg_range is the user supplied average range in light-years
    :param lower_speed_bound is the shortest range possible
    :param upper_speed_bound is the furthest range possible
    :param ftl_chance is the chance of generating a ftl capable ship, the higher the number the more likely it is to be ftl capable
    :return: A string containing the generated prefix
    """
    match random.randint(0, ftl_chance):
        case 0:
            return "No FTL capability"
        case _:
            range_ly = avg_range * random.uniform(lower_speed_bound, upper_speed_bound)
            return str(round(range_ly, 1))


# (Xqhare): There are way better ways of doing this I'm sure
def gen_tech_ship_data(ship_size: str, avg_speed: int, avg_range: int):
    """
    Returns technical ship data
    :param ship_size is the decoded ship size
    :param avg_speed is the user supplied average speed in light-speed
    :param avg_range is the user supplied average range in light-years
    :return: A string containing the generated technical ship data
    """
    match ship_size:
        case "SS":
            tonnage = random.uniform(0, 1000)
            size_m = random.uniform(1, 100)
            speed_ls = avg_speed * random.uniform(0, 0.33)
            range_ly = gen_ftl_capability(avg_range, 0.33, 0.75, 1)
            crew_min = random.randint(0, 3)
            crew_max = random.randint(crew_min, 10)
            return "Tonnage: " + str(round(tonnage, 2)) + '\n' + "Length (m): " + str(round(size_m, 2)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "XS":
            tonnage = random.uniform(1000, 2000)
            size_m = random.uniform(100, 175)
            speed_ls = avg_speed * random.uniform(0.95, 1.05)
            range_ly = gen_ftl_capability(avg_range, 0, 0.33, 1)
            crew_min = random.randint(1, 12)
            crew_max = random.randint(crew_min, 25)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "S":
            tonnage = random.uniform(2000, 5000)
            size_m = random.uniform(175, 350)
            speed_ls = avg_speed * random.uniform(0.95, 1.10)
            range_ly = gen_ftl_capability(avg_range, 0.95, 1.05, 2)
            crew_min = random.randint(5, 25)
            crew_max = random.randint(crew_min, 50)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "M":
            tonnage = random.uniform(5000, 10000)
            size_m = random.uniform(350, 675)
            speed_ls = avg_speed * random.uniform(1.05, 1.15)
            range_ly = gen_ftl_capability(avg_range, 1.05, 1.10, 3)
            crew_min = random.randint(15, 175)
            crew_max = random.randint(crew_min, 350)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "L":
            tonnage = random.uniform(10000, 15000)
            size_m = random.uniform(675, 1000)
            speed_ls = avg_speed * random.uniform(1.15, 1.25)
            range_ly = gen_ftl_capability(avg_range, 1.10, 1.33, 3)
            crew_min = random.randint(25, 400)
            crew_max = random.randint(crew_min, 800)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "XL":
            tonnage = random.uniform(15000, 25000)
            size_m = random.uniform(1000, 2500)
            speed_ls = avg_speed * random.uniform(1.25, 1.40)
            range_ly = gen_ftl_capability(avg_range, 1.33, 1.50, 6)
            crew_min = random.randint(50, 500)
            crew_max = random.randint(crew_min, 1200)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "XXL":
            tonnage = random.uniform(25000, 75000)
            size_m = random.uniform(2500, 6000)
            speed_ls = avg_speed * random.uniform(1.40, 1.60)
            range_ly = gen_ftl_capability(avg_range, 1.50, 1.65, 8)
            crew_min = random.randint(150, 500)
            crew_max = random.randint(crew_min, 3000)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "U":
            tonnage = random.uniform(75000, 150000)
            size_m = random.uniform(6000, 10000)
            speed_ls = avg_speed * random.uniform(1.60, 1.60)
            range_ly = gen_ftl_capability(avg_range, 1.50, 1.65, 10)
            crew_min = random.randint(300, 800)
            crew_max = random.randint(crew_min, 8000)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "XU":
            tonnage = random.uniform(150000, 500000)
            size_m = random.uniform(10000, 15000)
            speed_ls = avg_speed * random.uniform(1.60, 1.65)
            range_ly = gen_ftl_capability(avg_range, 1.40, 1.55, 20)
            crew_min = random.randint(800, 1500)
            crew_max = random.randint(crew_min, 14000)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case "T":
            tonnage = random.uniform(500000, 1000000000)
            size_m = random.uniform(15000, 15000000)
            speed_ls = avg_speed * random.uniform(1.60, 1.70)
            range_ly = gen_ftl_capability(avg_range, 1.35, 1.50, 25)
            crew_min = random.randint(1000, 2000)
            crew_max = random.randint(crew_min, 14000000)
            return "Tonnage: " + str(round(tonnage)) + '\n' + "Length (m): " + str(round(size_m)) + '\n' + "Min. Landing-pad-size: " + \
                ship_size + '\n' + "Speed (c): " + str(round(speed_ls, 2)) + '\n' + "Range (ly): " + range_ly + '\n' + \
                "Min. Crew: " + str(crew_min) + '\n' + "Max. Crew: " + str(crew_max)
        case _:
            print("Error - ShipClass.2", ship_size)
            return "Error - ShipClass.2"


def gen_ship_fame(ship_size: str):
    """
    Returns characteristics the class is famous for, the bigger, the more characteristics are returned
    :param ship_size is the string provided to be decoded
    :return: A string containing the generated ship characteristics
    """
    match ship_size:
        case "L":
            return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame)
        case "XL":
            return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame)
        case "XXL":
            match random.randint(0, 1):
                case 0:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame)
                case _:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + " and it's " + random.choice(GenLib.ship_fame)
        case "U":
            match random.randint(0, 2):
                case 0:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame)
                case _:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + " and it's " + random.choice(GenLib.ship_fame)
        case "XU":
            match random.randint(0, 3):
                case 0:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame)
                case 1:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + " and it's " + random.choice(GenLib.ship_fame)
                case _:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + ", it's " + random.choice(GenLib.ship_fame) + \
                        " and it's " + random.choice(GenLib.ship_fame)
        case "T":
            match random.randint(0, 1):
                case 0:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + " and it's " + random.choice(GenLib.ship_fame)
                case _:
                    return "The Class gained notoriety for it's: " + random.choice(GenLib.ship_fame) + ", it's " + random.choice(GenLib.ship_fame) + \
                        " and it's " + random.choice(GenLib.ship_fame)
        case _:
            return ""


def main_ship_class(ship_size: str, avg_speed: int, avg_range: int):
    """
    Main function, returning the complete ship class
    :param ship_size is the user supplied ship size
    :param avg_speed is the user supplied average speed in light-speed
    :param avg_range is the user supplied average range in light-years
    :return: A string containing the generated ship class
    """
    if ship_size == "" or " ":
        ship_size_generated = random.choice(GenLib.ship_sizes)
        ship_type = gen_ship_type(ship_size_generated)
        ship_tech = gen_tech_ship_data(ship_size_generated, avg_speed, avg_range)
        ship_fame = str(gen_ship_fame(ship_size_generated))
        return ShipNameGen.gen_ship_name() + "-Class: " + '\n' + "It's a " + ship_type + "." + '\n' + ship_tech + '\n' +\
            ship_fame + '\n' + '\n'
    else:
        ship_type = gen_ship_type(ship_size)
        ship_tech = gen_tech_ship_data(ship_size, avg_speed, avg_range)
        ship_fame = str(gen_ship_fame(ship_size))
        return ShipNameGen.gen_ship_name() + "-Class: " + '\n' + "It's a " + ship_type + "." + '\n' + ship_tech + '\n' + \
            ship_fame + '\n' + '\n'
