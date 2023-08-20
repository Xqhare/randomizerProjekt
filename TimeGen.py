import SceneGen


# (Xqhare):  Doc: Generates random Scenes in a user defined year range.
# (Xqhare):  Doc: The output is provided in chronological order, in ascending order as a list
def gen_year_list(year0: int, year1: int, y_length: int):
    """
    Generates a sorted list of integers
    :param year0 is the start year
    :param year1 is the end year
    :param y_length is the length of entries the returned list has
    :return: a List of years
    """
    year_list = []
    year_start = year0
    for n in range(y_length):
        year_list.append(year_start)
        year_start += (year1-year0)/y_length
    return year_list


def main_timeline(year0: int, year1: int, y_length: int):
    get_year_list = gen_year_list(year0, year1, y_length)
    timeline_list = []
    for n in get_year_list:
        timeline_list.append(str(n) + " " + str(SceneGen.main_scene()))
    return timeline_list
