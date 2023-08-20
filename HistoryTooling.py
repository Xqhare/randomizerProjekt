import HistoryFactories as Factory
import HistoryMappers as Mapper
import random
import datetime
import time


# (Xqhare): General Tooling
def strip_single_naked(to_strip) -> str:
    """
    Strip structure from single value, returns value without surrounding structure.

    Args:
        to_strip: takes in a single value

    Returns:
         str returns the value of the given parameter without any brackets or commas as a string
    """
    decode_single = str(to_strip)
    decode_string = decode_single
    decode_osbr = decode_string.replace('[', '')
    decode_obr = decode_osbr.replace('(', '')
    decode_com = decode_obr.replace(',', '')
    decode_cbr = decode_com.replace(')', '')
    decode_csbr = decode_cbr.replace(']', '')
    decode_qt = decode_csbr.replace('"', '')
    decode_ap = decode_qt.replace("'", '')
    decode_final = decode_ap
    return decode_final


def filter_list_content_with_list(list1: list, list2: list) -> list:
    """Removes the contents of list2 from list1.

    Args:
        list1: The list to be filtered.
        list2: The list whose contents should be filtered from list1.

    Returns:
        A new list that contains the contents of list1 with the contents of list2
        removed.
    """

    new_list = []
    for item in list1:
        if item not in list2:
            new_list.append(item)
        return new_list


def filter_list_content_with_variable(list1: list, variable) -> list:
    """Removes variable from list1.

        Args:
            list1: The list to be filtered.
            variable: The variable which should be filtered from list1.

        Returns:
            A new list that contains the contents of list1 with the contents of variable
            removed.
        """
    output = [x for x in list1 if x != variable]
    return output


def check_variable_type(variable_to_check):
    x = variable_to_check
    if isinstance(x, int):
        return "Integer"
    elif isinstance(x, str):
        return "String"
    elif isinstance(x, dict):
        return "Dictionary"
    elif isinstance(x, list):
        return "List"
    elif isinstance(x, tuple):
        return "Tuple"
    else:
        return "Other"


# (Xqhare): format example: "%Y-%m-%d_%H:%M:%S" for YYYY-MM-DD_HH:MM:SS
def get_timestamp(format_string):
    """Returns a timestamp in the specified format."""
    now = datetime.datetime.now()
    return now.strftime(format_string)


def timeit(func):

    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        to_write = f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds'
        date_time = str(get_timestamp("%Y-%m-%d_%H:%M:%S"))
        log_file = open('log_file.txt', 'a')
        log_file.write(date_time + ' ' + to_write + '\n')
        return result
    return timeit_wrapper


# (Xqhare): ATTENTION! Untested AI code rewritten by me because it was shit before ever using it! But hey I learned a new formatting trick!
# -> IT JUST FUCKING WORKS TODD!!!! (after a small adjustment, removed conditions that returned always none if element was first or last)
def next_or_previous(element_list, variable, direction="next"):
    """
    This function takes in a list, a variable, and a direction and returns the next or previous entry if any.

    Args:
        element_list: The list of elements.
        variable: The variable to search for.
        direction: The direction of the entry to return. Can be "next" or anything else.

    Returns:
        The next or previous entry in the list, or None if the variable is not found.
    """
    index = element_list.index(variable)

    if direction == "next":
        # (Xqhare): Check if variable is last element in list. If so return none. The -1 is because index starts at 0 and len at 1
        if index == len(element_list) - 1:
            return None
        else:
            return element_list[index + 1]
    else:
        # (Xqhare): Check if variable is first element in list. If so return none.
        if index == 0:
            return None
        else:
            return element_list[index - 1]


# (Xqhare): SQL Tooling
# (Xqhare): db_connection is not last for uniqueness! (a.k.a -I'm too lazy to change it now-)
def sql_table_next_id(db_connection, table_name: str) -> int:
    cur = db_connection.cursor()
    query = "select max(id) from {}".format(table_name)
    cur.execute(query)
    row = cur.fetchall()
    cur.close()
    if strip_single_naked(row) == 'None':
        return 1
    else:
        next_id = int(strip_single_naked(row)) + 1
        return next_id


def sql_table_max_id(table_name: str, db_connection) -> int:
    cur = db_connection.cursor()
    query = "select max(id) from {}".format(table_name)
    cur.execute(query)
    output = cur.fetchall()
    cur.close()
    return output


def sql_update_table_where(table_name: str, set_variable: str, set_value, where_variable: str, where_value, db_connection):

    query = "update {} set {} = ? where {} = ?".format(table_name, set_variable, where_variable)

    cur = db_connection.cursor()
    cur.execute(query, (set_value, where_value))

    db_connection.commit()
    cur.close()


def sql_select_all_id(from_variable, db_connection):
    query = "select id from {}".format(from_variable)
    cur = db_connection.cursor()
    sql_output = cur.execute(query)
    output = sql_output.fetchall()
    cur.close()
    return output


def sql_select_from_where(select_variable: str, table_name: str, where_variable: str, where_value, db_connection):

    query = "select {} from {} where {} = ?".format(select_variable, table_name, where_variable)

    cur = db_connection.cursor()
    selected = cur.execute(query, (where_value,))
    output = selected.fetchall()
    cur.close()
    return output


def sql_select_from_where_and(select_variable: str, table_name: str, where_variable: str, where_value, where_variable2: str, where_value2, db_connection):

    query = "select {} from {} where {} = ? and {} = ?".format(select_variable, table_name, where_variable, where_variable2)

    cur = db_connection.cursor()
    selected = cur.execute(query, (where_value, where_value2))
    output = selected.fetchall()
    cur.close()
    return output


# (Xqhare): Pruning functions
def sql_prune_empire(empire_id, turn, db_connection):
    cur = db_connection.cursor()

    # (Xqhare): Trader pruning:
    sql_update_table_where('traders', 'pruned', 1, 'empire_id', empire_id, db_connection)
    # (Xqhare): Trader retirement:
    trader_char_id_lst0 = cur.execute('select character_id from traders where empire_id = ?', (empire_id,))
    trader_char_id_lst = trader_char_id_lst0.fetchall()
    for char_id in trader_char_id_lst:
        trader_char_id = int(strip_single_naked(char_id))
        this_town0 = cur.execute('select current_town_id from traders where character_id = ?', (trader_char_id,))
        this_town_unstripped = this_town0.fetchall()
        this_town = int(strip_single_naked(this_town_unstripped))
        action = "retired in"

        history_id_rowcount = sql_table_next_id(db_connection, 'history')

        history_mapper = Mapper.HistoryMapper(db_connection)
        history_mapper.insert(history_id_rowcount, turn, action, town_a_id=this_town, char_a_id=trader_char_id)

    # (Xqhare): General empire data pruning
    cur.execute('delete from empires where id = ?', (empire_id,))
    cur.execute('delete from empire_allies where empire_id = ?', (empire_id,))
    cur.execute('delete from empire_allies where ally_id = ?', (empire_id,))

    # (Xqhare): Don't prune GOVERNMENT -> for output; works only as long as new empires are added at the end of THIS table
    """cur.execute('delete from governments where empire_id = ?', (empire_id,))"""
    """cur.execute('delete from languages where empire_id = ?', (empire_id,))"""
    """cur.execute('delete from currencys where empire_id = ?', (empire_id,))"""
    # (Xqhare): CHARACTERS need to stay; also -> unique ID and all that
    """cur.execute('delete from characters where government_id = ?', (empire_id,))"""

    db_connection.commit()
    cur.close()


# (Xqhare): Refresh functions
def sql_refresh_empire_pop(empire_to_be_checked, potential_conqueror, db_connection):
    cur = db_connection.cursor()

    # (Xqhare): select all pop in towns of empire, add together -> push to table
    all_empire_pop_tuple = cur.execute('select sum(pop) from towns where empire_id = ?', (empire_to_be_checked,))
    all_empire_pop_pre = all_empire_pop_tuple.fetchall()
    all_empire_pop = strip_single_naked(all_empire_pop_pre)
    sql_update_table_where('empires', 'pop', all_empire_pop, 'id', empire_to_be_checked, db_connection)

    # (Xqhare): pruning check
    if len(all_empire_pop) <= 0:

        interact_turn_rowcount = cur.execute('select turn from history')
        interact_turn = strip_single_naked(max(interact_turn_rowcount.fetchall()))

        history_id_rowcount = sql_table_next_id(db_connection, 'history')
        action = "destroyed"

        history_mapper = Mapper.HistoryMapper(db_connection)
        history_mapper.insert(history_id_rowcount, interact_turn, action, potential_conqueror, empire_to_be_checked)

        print(f'Pruning: {empire_to_be_checked}')
        sql_prune_empire(empire_to_be_checked, interact_turn, db_connection)

    cur.close()


# (Xqhare): Choose functions
def sql_choose_river(chosen_empire: int, db_connection):
    cur = db_connection.cursor()
    empire_id = chosen_empire

    pos_river_ids = cur.execute('select id from rivers where empire_a_id = ?', (empire_id,))
    pos_river_ids0 = pos_river_ids.fetchall()

    cur.close()

    if len(pos_river_ids0) <= 2:
        river_id = Factory.sql_create_river(empire_id, db_connection)
    else:
        seed0 = random.randint(0, 2)
        match seed0:
            case 0:
                river_id = Factory.sql_create_river(empire_id, db_connection)
            case _:
                chosen_river = random.choice(pos_river_ids0)
                river_id = int(strip_single_naked(chosen_river))

    return river_id


def sql_choose_region(empire_id: int, town_id, db_connection):
    cur = db_connection.cursor()

    all_regions = cur.execute('select ID from REGIONS where EMPIRE_ID = ?', (empire_id,)).fetchall()

    for region in all_regions:
        this_region_id = int(region[0])
        town_c_id = cur.execute('select TOWN_C_ID from REGIONS where ID = ?', (this_region_id,)).fetchall()
        if town_c_id == 0:
            return this_region_id
        else:
            new_region_id = Factory.sql_create_region(empire_id, town_id, db_connection)
            return new_region_id

    db_connection.commit()
    cur.close()


# (Xqhare): Checker functions:
def sql_check_alliance(empire_a_id, empire_b_id, db_connection) -> bool:
    """
    Returns a boolean, True if allied to each other, False if not
    """
    cur = db_connection.cursor()
    # (Xqhare): check alliance status if already allied, visit
    ally_check_at = cur.execute('select ally_id from empire_allies where empire_id = ?', (empire_a_id,))
    ally_check_a = ally_check_at.fetchall()
    ally_check_a_fin = strip_single_naked(ally_check_a)
    cur.close()
    if ally_check_a_fin == empire_b_id:
        return True
    else:
        return False


def sql_tech_advancement(empire_a_id: int, db_connection, advance_mil_by: int = 0, advance_dip_by: int = 0, advance_soc_by: int = 0):
    cur = db_connection.cursor()

    if advance_mil_by != 0:
        # (Xqhare): Military tech
        mil_tech_a_ex = cur.execute('select mil_tech from empires where id = ?', (empire_a_id,))
        mil_tech_a_t = mil_tech_a_ex.fetchall()
        mil_tech_a = int(strip_single_naked(mil_tech_a_t)) + advance_mil_by
        sql_update_table_where('empires', 'mil_tech', mil_tech_a, 'id', empire_a_id, db_connection)

    if advance_dip_by != 0:
        # (Xqhare): Diplomatic tech
        dip_tech_a_ex = cur.execute('select dip_tech from empires where id = ?', (empire_a_id,))
        dip_tech_a_t = dip_tech_a_ex.fetchall()
        dip_tech_a = int(strip_single_naked(dip_tech_a_t)) + advance_dip_by
        sql_update_table_where('empires', 'dip_tech', dip_tech_a, 'id', empire_a_id, db_connection)

    if advance_soc_by != 0:
        # (Xqhare): Society tech
        soc_tech_a_ex = cur.execute('select soc_tech from empires where id = ?', (empire_a_id,))
        soc_tech_a_t = soc_tech_a_ex.fetchall()
        soc_tech_a = int(strip_single_naked(soc_tech_a_t)) + advance_dip_by
        sql_update_table_where('empires', 'soc_tech', soc_tech_a, 'id', empire_a_id, db_connection)

    cur.close()
