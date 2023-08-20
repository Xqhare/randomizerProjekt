import random

import HistoryTooling as Tool
import HistoryInteraction as Action
import HistoryMappers as Mapper
import GenLib
import EmpireGen
import PeopleNameGen
import LanguageGen
import CurrencyGen
import PlaceNameGen


# (Xqhare): SQL creator-factories
def sql_create_table(table_name, columns, db_connection):
    """Create a table in the SQLite database."""
    cursor = db_connection.cursor()

    create_table_sql = "create table {} ({})".format(table_name, columns)
    cursor.execute(create_table_sql)

    db_connection.commit()
    cursor.close()


# (Xqhare): Story creator-factories
# (Xqhare): - People
def sql_create_trader(empire_a_id: int, starting_town_id: int, this_turn: int, db_connection):

    starting_town_id_int = starting_town_id

    trader_id_rowcount = Tool.sql_table_next_id(db_connection, 'traders')

    char_id_rowcount = Tool.sql_table_next_id(db_connection, 'characters')

    trader_name = PeopleNameGen.sticher_legal_name()
    trader_title = "Trader"
    trader_trait = PeopleNameGen.gen_trait()
    trade_factor = round(random.uniform(0.05, 0.15), 3)
    turn_offset = random.randint(5, 50) + int(this_turn)
    end_turn = int(turn_offset)
    ruler = 0
    pruned = 0

    gov_lang_unstripped = Tool.sql_select_from_where('id', 'languages', 'empire_id', empire_a_id, db_connection)
    if len(gov_lang_unstripped) > 1:
        lang_id = int(Tool.strip_single_naked(random.choice(gov_lang_unstripped)))
    else:
        lang_id = int(Tool.strip_single_naked(gov_lang_unstripped))

    gov_id_unstripped = Tool.sql_select_from_where('id', 'governments', 'empire_id', empire_a_id, db_connection)
    gov_id = int(Tool.strip_single_naked(gov_id_unstripped))

    trader_mapper = Mapper.TraderMapper(db_connection)
    trader_mapper.insert(trader_id_rowcount, char_id_rowcount, trade_factor, end_turn, starting_town_id_int, empire_a_id, pruned)

    character_mapper = Mapper.CharacterMapper(db_connection)
    character_mapper.insert(char_id_rowcount, trader_name, trader_title, lang_id, trader_trait, this_turn, ruler, gov_id)

    # (Xqhare): History:
    action = "funded trader"
    history_id_rowcount = Tool.sql_table_next_id(db_connection, 'history')

    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, this_turn, action, empire_a_id, town_a_id=starting_town_id_int, char_a_id=char_id_rowcount)


def sql_create_mayor(gov_id, town_id, turn, empire_id, db_connection):

    leader_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="characters")

    mayor_name = PeopleNameGen.sticher_legal_name()
    mayor_title = "Mayor"
    mayor_trait = PeopleNameGen.gen_trait()
    ruler = 0
    mayor_lang0 = Tool.sql_select_from_where('id', 'languages', 'empire_id', empire_id, db_connection)
    mayor_lang = int(Tool.strip_single_naked(mayor_lang0[0]))

    char_mapper = Mapper.CharacterMapper(db_connection)
    char_mapper.insert(leader_id_rowcount, mayor_name, mayor_title, mayor_lang, mayor_trait, turn, ruler, gov_id, town_id)

    return leader_id_rowcount


# (Xqhare): - Objects
def sql_create_road(empire_a_id, turn, town_id, db_connection):
    """Creates a new road for the given empire.

    Args:
        empire_a_id: The ID of the empire that is creating the road.
        turn: The current turn number.
        town_id: The ID of the town where the road is being created.
        db_connection: The sql database connection
    Returns:
        The ID of the newly created road.
    """
    cur = db_connection.cursor()

    road_rowcount = Tool.sql_table_next_id(db_connection, table_name="roads")

    road_id0 = cur.execute("select max(road_id) from roads")
    road_id1 = road_id0.fetchall()
    if Tool.strip_single_naked(road_id1) == 'None':
        road_id = 1
    else:
        next_id = int(Tool.strip_single_naked(road_id1)) + 1
        road_id = next_id

    road_mapper = Mapper.RoadMapper(db_connection)
    road_mapper.insert(road_rowcount, road_id, turn, empire_a_id, town_id)

    # (Xqhare): History:
    action = "built road"
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")

    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_a_id)

    cur.close()

    return road_id


def sql_create_river(empire_a_id, db_connection):

    river_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="rivers")
    river_name = PlaceNameGen.gen_simple_name()

    river_mapper = Mapper.RiverMapper(db_connection)
    river_mapper.insert(river_id_rowcount, river_name, empire_a_id)

    return river_id_rowcount


def sql_create_town(empire_id: int, turn: int, db_connection):

    town_id = Tool.sql_table_next_id(db_connection, table_name="towns")
    town_name = PlaceNameGen.sticher_full_name()
    town_pop = random.randint(50, 100000)

    trade_good, trade_good_price = random.choice(list(GenLib.story_town_trade_goods_dict.items()))
    town_gdp = round(town_pop * trade_good_price)

    mayor_id = sql_create_mayor(empire_id, town_id, turn, empire_id, db_connection)

    num_roads = len(Tool.sql_select_from_where('road_id', 'roads', 'empire_a_id', empire_id, db_connection))

    if num_roads == 0:
        region_id = sql_create_region(empire_id, town_id, db_connection)
        capitol = 1
        sql_create_road(empire_id, turn, town_id, db_connection)
        sql_create_road(empire_id, turn, town_id, db_connection)
    else:
        region_id = Tool.sql_choose_region(empire_id, town_id, db_connection)
        Action.sql_interaction_connect_road(empire_id, turn, town_id, db_connection)
        capitol = 0

    river_id_unstripped = Tool.sql_select_from_where('river_id', 'regions', 'id', region_id, db_connection)
    river_id = int(Tool.strip_single_naked(river_id_unstripped))

    town_mapper = Mapper.TownMapper(db_connection)
    town_mapper.insert(town_id, town_name, capitol, town_pop, town_gdp, empire_id, turn, mayor_id, river_id, trade_good, trade_good_price)

    # (Xqhare): History:
    action = "settle"
    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name="history")

    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action, empire_id, town_a_id=town_id)

    return town_id


def sql_create_region(chosen_empire: int, town_a_id, db_connection):
    # (Xqhare): returns region_id stripped and as int

    region_id = Tool.sql_table_next_id(db_connection, table_name="regions")
    region_name = PlaceNameGen.gen_simple_name()
    empire_id = chosen_empire
    river_id = Tool.sql_choose_river(empire_id, db_connection)

    region_mapper = Mapper.RegionsMapper(db_connection)
    region_mapper.insert(region_id, region_name, empire_id, river_id, town_a_id)

    return region_id


def sql_create_empire(turn: int, db_connection):

    empire_id = Tool.sql_table_next_id(db_connection, table_name="empires")
    empire_name = EmpireGen.gen_empire_name()
    empire_pop = EmpireGen.gen_empire_pop()
    empire_area = EmpireGen.gen_empire_area()

    government_id = Tool.sql_table_next_id(db_connection, table_name="governments")
    government_short_name = EmpireGen.gen_empire_name()

    leader_id = Tool.sql_table_next_id(db_connection, table_name="characters")
    leader_name = PeopleNameGen.sticher_legal_name()
    leader_trait = PeopleNameGen.gen_trait()

    language_id = Tool.sql_table_next_id(db_connection, table_name="languages")
    language_name = LanguageGen.gen_lang_name()

    currency_id = Tool.sql_table_next_id(db_connection, table_name="currencys")
    currency_name = CurrencyGen.gen_general_currency_name()

    # (Xqhare): Technology level creator:
    mil_tech = 1
    dip_tech = 1
    soc_tech = 1

    # (Xqhare): Government generator
    seed0 = random.randint(0, 2)
    ruler = 1
    match seed0:
        # (Xqhare): Democracy
        case 0:
            seed1 = random.randint(0, 9)
            semi = "Semi-" if seed1 >= 8 else ""
            gov_type = 0

            form0 = random.choice(GenLib.story_government_type_adj_01)

            if form0 == "Presidential":
                temp_list = ["Parliamentary", "Democratic", "Constitutional"]
                form1 = random.choice(temp_list)
                leader_title = "President"
            elif form0 == "Democratic":
                temp_list = ["Parliamentary", "Constitutional", "Presidential"]
                form1 = random.choice(temp_list)
                leader_title = random.choice(GenLib.story_government_leader_title_01)
            elif form0 == "Constitutional":
                temp_list = ["Parliamentary", "Democratic", "Presidential"]
                form1 = random.choice(temp_list)
                leader_title = random.choice(GenLib.story_government_leader_title_01)
            else:
                form1 = random.choice(GenLib.story_government_type_sec_01)
                leader_title = random.choice(GenLib.story_government_leader_title_01)

            rep_or_state = random.choice(GenLib.rep_or_state_list)
            legislative_term = random.randint(2, 12)

            first_election = turn + legislative_term

            full_title = semi + form0 + " " + form1 + " " + rep_or_state
            government_name = full_title + " of " + government_short_name

        case 1:
            seed1 = random.randint(0, 9)
            semi = "Semi-" if seed1 >= 8 else ""
            gov_type = 1

            form0 = random.choice(GenLib.story_government_type_adj_1)

            if form0 == "Council":
                seed1 = random.randint(0, 2)
                leader_title = random.choice(GenLib.story_government_leader_title_1)
                if seed1 == 0:
                    form1 = random.choice(GenLib.story_government_type_sec_01)
                    rep_or_state = random.choice(GenLib.rep_or_state_list)
                    full_title = semi + form0 + " " + form1 + " " + rep_or_state
                elif seed1 == 1:
                    seed2 = random.randint(0, 3)

                    if seed2 == 0:
                        form1 = random.choice(GenLib.story_government_type_adj_01)
                        rep_or_state = random.choice(GenLib.rep_or_state_list)
                        full_title = semi + form1 + " " + form0 + " " + rep_or_state
                    else:
                        form1 = random.choice(GenLib.story_government_type_adj_01)
                        rep_or_state = random.choice(GenLib.rep_or_state_list)
                        full_title = semi + form0 + " " + form1 + " " + rep_or_state
                else:
                    rep_or_state = "Republic"
                    full_title = semi + form0 + " " + rep_or_state
            else:
                leader_title = random.choice(GenLib.story_government_leader_title_1)
                form1 = random.choice(GenLib.story_government_type_sec_01)
                rep_or_state = random.choice(GenLib.rep_or_state_list)
                full_title = semi + form1 + " " + form0 + " " + rep_or_state

            legislative_term = random.randint(2, 12)
            government_short_name = EmpireGen.gen_empire_name()
            government_name = full_title + " of " + government_short_name
            first_election = turn + legislative_term

        case _:
            form1 = random.choice(GenLib.story_government_type_adj_0)
            gov_type = 2

            if form1 == "Corporate":
                leader_title = random.choice(GenLib.story_government_leader_title_0_cor)
                legislative_term = random.randint(10, 25)
                rep_or_state = "Corporation"
                seed2 = random.randint(0, 1)
                if seed2 == 0:
                    form0 = random.choice(GenLib.story_government_type_sec_0)
                    full_title = form1 + " " + form0
                else:
                    form0 = random.choice(GenLib.story_government_type_sec_01)
                    full_title = form1 + " " + form0 + " State"

            elif form1 == "Religious":
                leader_title = random.choice(GenLib.story_government_leader_title_0_reli)
                legislative_term = 100
                rep_or_state = random.choice(GenLib.rep_or_state_list)
                seed2 = random.randint(0, 1)
                if seed2 == 0:
                    form0 = random.choice(GenLib.story_government_type_sec_01)
                    full_title = form1 + " " + form0 + " " + rep_or_state
                else:
                    form0 = random.choice(GenLib.story_government_type_adj_01)
                    full_title = form0 + " " + form1 + " " + rep_or_state

            elif form1 == "Monarchy":
                leader_title = random.choice(GenLib.story_government_leader_title_0_mon)
                legislative_term = 100
                rep_or_state = "Monarchy"
                form0 = random.choice(GenLib.government_name_monarchy)
                full_title = form0 + " " + form1 + " "

            # (Xqhare): This is only here to shut up the ide, and could be instantly removed as it is never reached.
            else:
                leader_title = random.choice(GenLib.story_government_leader_title_0_mon)
                legislative_term = 100
                rep_or_state = "Monarchy"
                form0 = random.choice(GenLib.government_name_monarchy)
                full_title = form0 + " " + form1 + " "

            government_name = full_title + " of " + government_short_name
            first_election = turn + legislative_term

    gov_mapper = Mapper.GovernmentMapper(db_connection)
    gov_mapper.insert(government_id, government_name, empire_id, gov_type, leader_id, leader_title, full_title, government_short_name, legislative_term,
                      rep_or_state, first_election)

    empire_mapper = Mapper.EmpireMapper(db_connection)
    empire_mapper.insert(empire_id, empire_name, leader_id, language_id, empire_pop, empire_area, currency_id, government_id, mil_tech, dip_tech,
                         soc_tech)

    language_mapper = Mapper.LanguageMapper(db_connection)
    language_mapper.insert(language_id, language_name, empire_id)

    currency_mapper = Mapper.CurrencyMapper(db_connection)
    currency_mapper.insert(currency_id, currency_name, empire_id)

    char_mapper = Mapper.CharacterMapper(db_connection)
    char_mapper.insert(leader_id, leader_name, leader_title, language_id, leader_trait, turn, ruler, government_id)

    # (Xqhare): create Capitol; history should be in settle_town
    # (Xqhare): HAS TO BE IN FRONT OF HISTORY AND AFTER EMPIRE MAPPER -> mayor lang dependency
    capitol = sql_create_town(empire_id, turn, db_connection)

    history_id_rowcount = Tool.sql_table_next_id(db_connection, table_name='history')

    history_mapper = Mapper.HistoryMapper(db_connection)
    history_mapper.insert(history_id_rowcount, turn, action='funded new empire', empire_a_id=empire_id, town_a_id=capitol)
