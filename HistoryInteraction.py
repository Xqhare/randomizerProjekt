import random

import GenLib
import OperationGen
import HistoryTooling as Tool
import HistoryFactories as Factory
import HistoryMappers as Mapper


def gen_empire_interaction(turn: int, db_connection):

    # (Xqhare): Selecting acting Empires
    cur = db_connection.cursor()
    max_empires = Tool.sql_select_all_id('empires', db_connection)
    cur.close()

    chosen_empires = random.sample(max_empires, k=2)
    empire_a_id = int(Tool.strip_single_naked(chosen_empires[0]))
    empire_b_id = int(Tool.strip_single_naked(chosen_empires[1]))

    # (Xqhare): Fetching rest data from database

    gen_action = random.choice(GenLib.story_empire_interactions)

    match gen_action:
        case "ally":
            sql_interaction_ally(turn, empire_a_id, empire_b_id, db_connection)

        case "attack":
            # (Xqhare): check alliance status if an empire is already allied they visit
            ally_check = Tool.sql_check_alliance(empire_a_id, empire_b_id, db_connection)
            if ally_check:
                sql_interaction_visit(turn, empire_a_id, empire_b_id, db_connection)
            else:
                sql_interaction_attack(db_connection, empire_a_id, empire_b_id, turn)

        case "settle":
            sql_interaction_settle(empire_a_id, empire_b_id, turn, db_connection)
            sql_interaction_settle(empire_b_id, empire_a_id, turn, db_connection)
        case "had a parade in":
            sql_interaction_parade(turn, empire_a_id, gen_action, db_connection)
            sql_interaction_parade(turn, empire_b_id, gen_action, db_connection)
        case "developed technologies":
            sql_interaction_tech_development(turn, empire_a_id, gen_action, db_connection)
            sql_interaction_tech_development(turn, empire_b_id, gen_action, db_connection)
        case "developed economy":
            sql_interaction_dev_economy(empire_a_id, empire_b_id, turn, db_connection)
            sql_interaction_dev_economy(empire_b_id, empire_a_id, turn, db_connection)
        case "connected by road to":
            sql_interaction_connect_by_road(empire_a_id, turn, db_connection)
            sql_interaction_connect_by_road(empire_b_id, turn, db_connection)
        case "funded new empire":
            Factory.sql_create_empire(turn, db_connection)
            # (Xqhare): DONE: There is missing history of empire founding!
        case _:
            return "Error - SQL.1"


def sql_interaction_dev_economy(empire_a_id, empire_b_id, turn, db_connection):
    all_town_id_list = Tool.sql_select_from_where('id', 'towns', 'empire_id', empire_a_id, db_connection)
    if len(all_town_id_list) == 0:
        Tool.sql_refresh_empire_pop(empire_a_id, empire_b_id, db_connection)
    elif len(all_town_id_list) == 1:
        starting_town_id = int(Tool.strip_single_naked(all_town_id_list[0]))
        Factory.sql_create_trader(empire_a_id, starting_town_id, turn, db_connection)
    else:
        town_id_unstripped = random.choice(all_town_id_list)
        starting_town_id = int(Tool.strip_single_naked(town_id_unstripped))
        Factory.sql_create_trader(empire_a_id, starting_town_id, turn, db_connection)


def sql_interaction_connect_by_road(empire_a_id, turn, db_connection):
    all_towns_list = Tool.sql_select_from_where('id', 'towns', 'empire_id', empire_a_id, db_connection)
    if len(all_towns_list) > 1:
        chosen_town_ns = random.choice(all_towns_list)
        chosen_town = Tool.strip_single_naked(chosen_town_ns)
        sql_interaction_connect_road(empire_a_id, turn, chosen_town, db_connection)
    elif len(all_towns_list) == 1:
        chosen_town = Tool.strip_single_naked(all_towns_list)
        sql_interaction_connect_road(empire_a_id, turn, chosen_town, db_connection)


def sql_interaction_attack(db_connection, empire_a_id, empire_b_id, turn):

    # (Xqhare): Fetching and manipulating data
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")
    empire_a_mil_pp = Tool.sql_select_from_where('mil_tech', 'empires', 'id', empire_a_id, db_connection)
    empire_a_mil = int(Tool.strip_single_naked(empire_a_mil_pp))

    empire_b_mil_pp = Tool.sql_select_from_where('mil_tech', 'empires', 'id', empire_b_id, db_connection)
    empire_b_mil = int(Tool.strip_single_naked(empire_b_mil_pp))

    empire_a_pop = Tool.sql_select_from_where('pop', 'empires', 'id', empire_a_id, db_connection)
    empire_a_start_pop = int(Tool.strip_single_naked(empire_a_pop))

    empire_b_pop = Tool.sql_select_from_where('pop', 'empires', 'id', empire_b_id, db_connection)
    empire_b_start_pop = int(Tool.strip_single_naked(empire_b_pop))

    # (Xqhare): Calculates a military score; using mil_tech and pop
    # TODO: temp anyway
    mil_a_offset = 100 - empire_a_mil
    mil_b_offset = 100 - empire_b_mil

    if mil_a_offset <= 0:
        mil_a_offset1 = 1
        empire_a_mil_off = round((empire_a_start_pop / mil_a_offset1))
    else:
        empire_a_mil_off = round((empire_a_start_pop / mil_a_offset))

    if mil_b_offset <= 0:
        mil_b_offset1 = 1
        empire_b_mil_off = round((empire_b_start_pop / mil_b_offset1))
    else:
        empire_b_mil_off = round((empire_b_start_pop / mil_b_offset))

    # (Xqhare): If B is stronger, there is a 90% chance of them winning
    if empire_a_mil_off > empire_b_mil_off:
        chance = random.randint(0, 9)
        match chance:
            case 0:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_a_id, empire_b_id, db_connection)
            case _:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_b_id, empire_a_id, db_connection)
    # (Xqhare): If A is stronger, there is a 90% chance of them winning
    elif empire_a_mil_off < empire_b_mil_off:
        chance = random.randint(0, 9)
        match chance:
            case 0:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_b_id, empire_a_id, db_connection)
            case _:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_a_id, empire_b_id, db_connection)
    # (Xqhare): If both have the same strength it's a 50/50
    else:
        chance = random.randint(0, 1)
        match chance:
            case 0:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_b_id, empire_a_id, db_connection)
            case _:
                sql_interaction_attack_won(history_id_rowcount, turn, empire_a_id, empire_b_id, db_connection)


def sql_interaction_attack_won(history_id_rowcount, turn, empire_a_id, empire_b_id, db_connection):
    # (Xqhare): Empire A wins!
    history_id_stripped = int(Tool.strip_single_naked(history_id_rowcount))
    town_id = sql_interaction_town_conquest(empire_a_id, empire_b_id, db_connection)
    action = "attack"
    op_name = OperationGen.main_operation_name()

    # (Xqhare): History Mapper
    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_stripped, turn, action, empire_a_id, town_a_id=town_id, empire_b_id=empire_b_id, op_name=op_name)

# (Xqhare): this prunes; pruning gets a history => commit has to happen before for correct history. It also can't be moved to town_conquest because of this.
    Tool.sql_refresh_empire_pop(empire_a_id, empire_b_id, db_connection)
    Tool.sql_refresh_empire_pop(empire_b_id, empire_a_id, db_connection)


def sql_interaction_town_conquest(empire_id_winner, empire_id_looser, db_connection):

    town_ids_looser = Tool.sql_select_from_where('id', 'towns', 'empire_id', empire_id_looser, db_connection)
    chosen_town_ran = random.choice(town_ids_looser)
    chosen_town = int(Tool.strip_single_naked(chosen_town_ran))

    Tool.sql_update_table_where('towns', 'empire_id', empire_id_winner, 'id', chosen_town, db_connection)

    return chosen_town


def sql_interaction_ally(turn, empire_a_id, empire_b_id, db_connection):

    # (Xqhare): check alliance status if already allied, visit
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")
    ally_check_a = Tool.sql_select_from_where('ally_id', 'empire_allies', 'empire_id', empire_a_id, db_connection)
    ally_check_a_fin = Tool.strip_single_naked(ally_check_a)

    ally_check_b = Tool.sql_select_from_where('ally_id', 'empire_allies', 'empire_id', empire_b_id, db_connection)
    ally_check_b_fin = Tool.strip_single_naked(ally_check_b)

    if ally_check_a_fin == '' and ally_check_b_fin == '':
        gen_action = "ally"

        # (Xqhare): Insert relations for both allies:
        relations_mapper_a = Mapper.EmpireAlliesMapper(db_connection)
        relations_mapper_a.insert(empire_a_id, empire_b_id)

        relations_mapper_b = Mapper.EmpireAlliesMapper(db_connection)
        relations_mapper_b.insert(empire_b_id, empire_a_id)

        history_mapper = Mapper.HistoryMapper(db_connection)
        history_mapper.insert(history_id_rowcount, turn, gen_action, empire_a_id, empire_b_id)

        # (Xqhare): DONE: new ally bonus:
        # (Xqhare): Dip-tech and Soc-tech advancement for allies;
        # (Xqhare): Mil-tech advancement for allies (1/3 chance for level up):
        chance = random.randint(0, 2)
        if chance == 0:
            mil_tech = 1
        else:
            mil_tech = 0

        Tool.sql_tech_advancement(empire_a_id, db_connection, advance_mil_by=mil_tech, advance_dip_by=1, advance_soc_by=1)
        Tool.sql_tech_advancement(empire_b_id, db_connection, advance_mil_by=mil_tech, advance_dip_by=1, advance_soc_by=1)

    else:
        sql_interaction_visit(turn, empire_a_id, empire_b_id, db_connection)


def sql_interaction_visit(turn, empire_a_id, empire_b_id, db_connection):
    # (Xqhare): Updating interaction table:
    action = "visited"
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")
    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_a_id, empire_b_id)

    Tool.sql_tech_advancement(empire_a_id, db_connection, advance_dip_by=1)
    Tool.sql_tech_advancement(empire_b_id, db_connection, advance_dip_by=1)


def sql_interaction_parade(turn, empire_a_id, action, db_connection):
    # (Xqhare): This is a single interaction for only empire A!
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")
    # (Xqhare): Selecting owned town to be paraded in:
    owned_town_list = Tool.sql_select_from_where('id', 'towns', 'empire_id', empire_a_id, db_connection)
    chosen_town_pp = random.choice(owned_town_list)
    chosen_town = int(Tool.strip_single_naked(chosen_town_pp))

    # (Xqhare): Updating interaction table:
    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_a_id, town_a_id=chosen_town)

    # (Xqhare): Mil-tech advancement for parade:
    Tool.sql_tech_advancement(empire_a_id, db_connection, advance_mil_by=1)


def sql_interaction_tech_development(turn, empire_a_id, action, db_connection):

    num_tech = random.randint(1, 3)
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")
    # (Xqhare): Updating history:
    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_a_id)

    for n in range(num_tech):
        seed_mil = random.randint(0, 1)
        seed_dip = random.randint(0, 1)
        seed_soc = random.randint(0, 1)
        Tool.sql_tech_advancement(empire_a_id, db_connection, advance_mil_by=seed_mil, advance_dip_by=seed_dip, advance_soc_by=seed_soc)


def sql_interaction_settle(empire_a_id, empire_b_id, turn, db_connection):

    Factory.sql_create_town(empire_a_id, turn, db_connection)
    Tool.sql_refresh_empire_pop(empire_a_id, empire_b_id, db_connection)


def sql_interaction_connect_road(empire_a_id, turn, town_a_id, db_connection):
    # (Xqhare): Checking the amount of roads connecting the chosen town. If more than one -> choose random, if one choose that one and if none create one
    pos_road_ids_lst = Tool.sql_select_from_where('road_id', 'roads', 'town_id', town_a_id, db_connection)
    if len(pos_road_ids_lst) > 1:
        chosen_road0 = random.choice(pos_road_ids_lst)
        chosen_road = Tool.strip_single_naked(chosen_road0)
    elif len(pos_road_ids_lst) == 1:
        chosen_road = Tool.strip_single_naked(pos_road_ids_lst)
    else:
        # (Xqhare): Is only triggered when 0 roads are found. Create a road as a failsafe
        chosen_road = Factory.sql_create_road(empire_a_id, turn, town_a_id, db_connection)

    # I need to choose a Town where the chosen_road has NOT connected to; Take a list of all towns on chosen_road and check against a list of all empire towns
    # -> choose from left over towns when duplicates of all towns on chosen_road have been removed from all empire towns
    all_towns_chosen_road = Tool.sql_select_from_where('town_id', 'roads', 'road_id', chosen_road, db_connection)
    all_empire_towns = Tool.sql_select_from_where('id', 'towns', 'empire_id', empire_a_id, db_connection)

    search_list_road = [x for x, in all_towns_chosen_road]
    search_list_towns = [x for x, in all_empire_towns]

    filtered_towns = Tool.filter_list_content_with_list(search_list_towns, search_list_road)
    # (Xqhare): If all towns are connected to each other with the chosen_road, create a new one as a catchall and failsafe
    if filtered_towns is None:
        connected_town = town_a_id
        Factory.sql_create_road(empire_a_id, turn, town_a_id, db_connection)
    elif len(filtered_towns) < 1:
        connected_town = town_a_id
        Factory.sql_create_road(empire_a_id, turn, town_a_id, db_connection)
    elif len(filtered_towns) == 1:
        connected_town = int(Tool.strip_single_naked(filtered_towns[0]))
    else:
        connected_town_unstripped = random.choice(filtered_towns)
        connected_town = int(Tool.strip_single_naked(connected_town_unstripped))

    road_id_rowcount = Tool.sql_table_next_id(db_connection, 'roads')
    history_id_rowcount = Tool.sql_table_next_id(db_connection, 'history')
    action = "connected by road to"

    road_mapper = Mapper.RoadMapper(db_connection)
    road_mapper.insert(road_id_rowcount, chosen_road, turn, empire_a_id, connected_town)

    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_a_id, town_a_id=town_a_id, town_b_id=connected_town)
