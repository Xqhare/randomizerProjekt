import random
import sqlite3
import os

import CurrencyGen
import EmpireGen
import GenLib
import LanguageGen
import OperationGen
import PeopleNameGen
import PlaceNameGen

"""
You need to provide the number of empires AND the number of Turns AND the number of actions per turn
"""


# (Xqhare): Startup functions and most important functions
def sql_create_db():
    # (Xqhare): Empire Table with linking ID's
    db_connection.execute('''create table EMPIRES(
        ID              INT PRIMARY KEY      NOT NULL,
        NAME            TEXT,
        LEADER_ID       INT,
        LANGUAGE_ID     INT,
        POP             INT,
        AREA            INT,
        CURRENCY_ID     INT,
        GOVERNMENT_ID   INT,
        MIL_TECH        INT,
        DIP_TECH        INT,
        SOC_TECH        INT);''')

    # (Xqhare): Government Table with linking ID's
    db_connection.execute('''create table GOVERNMENTS(
        ID                  INT PRIMARY KEY      NOT NULL,
        NAME                TEXT,
        EMPIRE_ID           INT,
        LEADER_ID           INT,
        TYPE                INT,
        LEADER_TITLE        TEXT,
        FULL_TITLE          TEXT,
        NAME_SHORT          TEXT,
        LEGISLATIVE_TERM    INT,
        REP_OR_STATE        TEXT,
        NEXT_ELECTION_TURN  INT);''')

    # (Xqhare): Leader Table with linking ID's
    db_connection.execute('''create table CHARACTERS(
            ID              INT PRIMARY KEY      NOT NULL,
            NAME            TEXT,
            TITLE           TEXT,
            GOVERNMENT_ID   INT,
            TOWN_ID         INT,
            TRAIT           TEXT,
            BORN_TURN       INT,
            RULER           INT);''')

    db_connection.execute('''create table TRADERS(
        ID              INT PRIMARY KEY     NOT NULL,
        CHAR_ID         INT                 NOT NULL,
        TRADE_FACTOR    REAL                NOT NULL,
        END_TURN        INT                 NOT NULL,
        CURRENT_TOWN_ID INT                 NOT NULL,
        EMPIRE_ID       INT                 NOT NULL,
        PRUNED          INT)''')

    # (Xqhare): Language Table with linking ID's
    db_connection.execute('''create table LANGUAGES(
        ID              INT PRIMARY KEY      NOT NULL,
        NAME            TEXT,
        EMPIRE_ID       INT);''')

    # (Xqhare): Currency Table with linking ID's - MOCKUP
    db_connection.execute('''create table CURRENCYS(
        ID              INT PRIMARY KEY      NOT NULL,
        NAME            TEXT,
        EMPIRE_ID       INT);''')

    db_connection.execute('''create table HISTORY(
        ID              INT PRIMARY KEY     NOT NULL,
        TURN            INT                 NOT NULL,
        EMPIRE_A_ID     INT,
        ACTION          TEXT                NOT NULL,
        EMPIRE_B_ID     INT,
        TOWN_ID         INT,
        TOWN_B_ID       INT,
        CHAR_A_ID       INT,
        CHAR_B_ID       INT,
        OP_NAME         TEXT)''')

    db_connection.execute('''create table EMPIRE_RELATIONS(
        EMPIRE_ID       INT PRIMARY KEY,
        ALLY_ID         INT)''')

    db_connection.execute('''create table TOWNS(
        ID                      INT PRIMARY KEY     NOT NULL,
        NAME                    TEXT,
        CAPITOL                 INT,
        POP                     INT,
        GDP                     INT,
        EMPIRE_ID               INT,
        SETTLE_DATE             INT,
        MAYOR_ID                INT,
        RIVER_ID                INT,
        MAJOR_TRADE_GOOD        TEXT,
        MAJOR_TRADE_GOOD_PRICE  REAL)''')

    db_connection.execute('''create table ROADS(
        ID              INT PRIMARY KEY     NOT NULL,
        ROAD_ID         INT                 NOT NULL,
        TURN            INT                 NOT NULL,
        EMPIRE_A_ID     INT                 NOT NULL,
        TOWN_ID         INT)''')

    db_connection.execute('''create table RIVERS(
        ID              INT PRIMARY KEY     NOT NULL,
        NAME            TEXT                NOT NULL,
        FLOWS_INTO      INT,
        EMPIRE_A_ID     INT                 NOT NULL,
        EMPIRE_B_ID     INT)''')

    db_connection.execute('''create table REGIONS(
        ID              INT PRIMARY KEY     NOT NULL,
        NAME            TEXT                NOT NULL,
        EMPIRE_ID       INT                 NOT NULL,
        TOWN_A_ID       INT,
        TOWN_B_ID       INT,
        TOWN_C_ID       INT,
        RIVER_ID        INT,
        AREA            INT)''')

    db_connection.commit()
    # (Xqhare): Debug
    print("Database tables created")


# (Xqhare): Tooling:
# (Xqhare): HOT SINGLES IN YOUR AREA!!11!
def strip_single_naked(to_strip):
    """
    IMPORTANT: returns a string
    Strip structure from single value, returns value without surrounding structure.
    :param: to_decode takes in a single value
    :return: str returns the value of the given parameter without any brackets or commas as a string
    """
    decode_single = to_strip
    decode_string = str(decode_single)
    decode_osbr = decode_string.replace('[', '')
    decode_obr = decode_osbr.replace('(', '')
    decode_com = decode_obr.replace(',', '')
    decode_cbr = decode_com.replace(')', '')
    decode_csbr = decode_cbr.replace(']', '')
    decode_qt = decode_csbr.replace('"', '')
    decode_ap = decode_qt.replace("'", '')
    decode_final = decode_ap
    return decode_final


def sql_road_prev_next_town(road_id, town_id, prev_nxt: str):
    """
    Sample explanation of the function
    :param road_id: the road id
    :param town_id: the town id
    :param prev_nxt: string to be passed in; choose from ["prev", "next"]
    :return the next or previous town id, if return == 0 end of road reached
    """
    cur = db_connection.cursor()

    match prev_nxt:
        case "prev":
            all_id_of_road0 = cur.execute('select TOWN_ID from ROADS where ROAD_ID = ?', (road_id,))
            all_town_id_of_road_list = all_id_of_road0.fetchall()

            # (Xqhare): do I really need a tuple?? - yes. with hindsight somewhat obvious BUT still very stoopid
            stupid_test = (int(town_id),)
            '''print(f' stoopid {stupid_test},{town_id} {all_town_id_of_road_list};{len(all_town_id_of_road_list)}')'''

            if len(all_town_id_of_road_list) <= 1:
                # (Xqhare): returning 0 as town id... what could possibly go wrong?
                output = 0
            else:
                all_town_id_index = all_town_id_of_road_list.index(stupid_test)
                prev_town_index = all_town_id_index - 1
                prev_town_id = all_town_id_of_road_list[prev_town_index]
                output = strip_single_naked(prev_town_id)

        case _:
            # (Xqhare): untested but should work? -- apparently it does now - jk it doesn't - but after a slight rework it does now? fingers crossed
            all_id_of_road0 = cur.execute('select TOWN_ID from ROADS where ROAD_ID = ?', (road_id,))
            all_town_id_of_road_list = all_id_of_road0.fetchall()

            # (Xqhare): do I really need a tuple?? - yes. with hindsight somewhat obvious BUT still very stoopid
            stupid_test = (int(town_id),)
            '''print(f' stoopid {stupid_test},{town_id} {all_town_id_of_road_list};{len(all_town_id_of_road_list)}')'''

            if len(all_town_id_of_road_list) <= 1:
                # (Xqhare): returning 0 as town id... what could possibly go wrong?
                output = 0
            else:
                all_town_id_index = all_town_id_of_road_list.index(stupid_test)
                if stupid_test == all_town_id_of_road_list[all_town_id_index]:
                    all_town_id_index = all_town_id_of_road_list.index(stupid_test)
                    prev_town_index = all_town_id_index - 1
                    prev_town_id = all_town_id_of_road_list[prev_town_index]
                    output = strip_single_naked(prev_town_id)
                else:
                    prev_town_index = all_town_id_index + 1
                    prev_town_id = all_town_id_of_road_list[prev_town_index]
                    output = strip_single_naked(prev_town_id)

    cur.close()

    return int(output)


def sql_choose_river(chosen_empire: int):
    cur = db_connection.cursor()
    empire_id = chosen_empire
    river_id_rowcount0 = cur.execute('select ID from RIVERS where EMPIRE_A_ID = ?', (empire_id,))
    river_id_rowcount = river_id_rowcount0.fetchall()
    river_id_test = len(river_id_rowcount)

    if river_id_test <= 1:
        river_id = sql_create_river(empire_id)
    else:
        seed0 = random.randint(0, 2)
        match seed0:
            case 0:
                river_id = sql_create_river(empire_id)
            case _:
                pos_river_ids = cur.execute('select ID from RIVERS where EMPIRE_A_ID = ?', (empire_id,))
                pos_river_ids0 = pos_river_ids.fetchall()
                chosen_river = random.choice(pos_river_ids0)
                river_id = strip_single_naked(chosen_river)

    return river_id


def sql_choose_region(empire_id: int):
    cur = db_connection.cursor()

    all_regions0 = cur.execute('select ID from REGIONS where EMPIRE_ID = ?', (empire_id,))
    all_regions_lst = all_regions0.fetchall()

    for element in all_regions_lst:
        this_region_id = int(strip_single_naked(element))
        town_c_id0 = cur.execute('select TOWN_C_ID from REGIONS where ID = ?', (this_region_id,))
        town_c_id_unstripped = town_c_id0.fetchall()
        # (Xqhare): print(f'REGION TOWN CHECK: {town_c_id_unstripped};; len: {len(town_c_id_unstripped)}')
        if strip_single_naked(town_c_id_unstripped) == 'None':
            return this_region_id
        else:
            new_region_id = sql_create_region(empire_id)
            return new_region_id

    db_connection.commit()
    cur.close()


# (Xqhare): Main Startup Sequence:
'''Deletes database as failsafe if file wasn't cleaned up
connect is used to creates a new db as it is always deleted (by design); it also connects to it'''

if os.path.exists('Storygen.db') == 1:
    os.remove('Storygen.db')
db_connection = sqlite3.connect('Storygen.db')
print("Database created")
sql_create_db()


# (Xqhare): sql factories
def sql_create_road(empire_a_id, turn, town_id):
    cur = db_connection.cursor()

    r_id_rowcount = cur.execute('select ID from ROADS')
    r_id = len(r_id_rowcount.fetchall()) + 1

    road_id_max = cur.execute('select ROAD_ID from ROADS')
    road_id_max0 = len(road_id_max.fetchall())
    road_id = road_id_max0 + 1

    cur.execute('insert into ROADS (ID, ROAD_ID, TURN, EMPIRE_A_ID, TOWN_ID) values(?,?,?,?,?)',
                (r_id, road_id, turn, empire_a_id, town_id))

    # (Xqhare): History:
    action = "built road"
    empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
    empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1

    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, TOWN_ID) values(?,?,?,?,?)',
                (empire_interaction_id, turn, empire_a_id, action, town_id))

    db_connection.commit()
    cur.close()


def sql_create_river(empire_a_id):
    cur = db_connection.cursor()

    river_id_rowcount = cur.execute('select ID from RIVERS')
    river_id = len(river_id_rowcount.fetchall()) + 1
    river_name = PlaceNameGen.gen_simple_name()

    cur.execute('insert into RIVERS (ID, NAME, EMPIRE_A_ID) values(?,?,?)',
                (river_id, river_name, empire_a_id))

    db_connection.commit()
    cur.close()
    return river_id


def sql_create_mayor(gov_id, town_id, turn):
    cur = db_connection.cursor()

    leader_id_rowcount = cur.execute('select ID from CHARACTERS')
    leader_id = len(leader_id_rowcount.fetchall()) + 1
    this_turn = int(strip_single_naked(turn))

    mayor_name = PeopleNameGen.sticher_legal_name()
    mayor_title = "Mayor"
    mayor_trait = PeopleNameGen.gen_trait()

    cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TOWN_ID, TRAIT, BORN_TURN) values(?,?,?,?,?,?,?)",
                (leader_id, mayor_name, mayor_title, gov_id, town_id, mayor_trait, this_turn))

    return leader_id


def sql_create_trader(empire_a_id, starting_town_id: int, this_turn):
    cur = db_connection.cursor()

    empire_id = strip_single_naked(empire_a_id)
    starting_town_id_int = starting_town_id
    turn = strip_single_naked(this_turn)
    trader_id_rowcount = cur.execute('select ID from TRADERS')
    trader_id = len(trader_id_rowcount.fetchall()) + 1
    char_id_rowcount = cur.execute('select ID from CHARACTERS')
    char_id = len(char_id_rowcount.fetchall()) + 1
    trader_name = PeopleNameGen.sticher_legal_name()
    trader_title = "Trader"
    trader_trait = PeopleNameGen.gen_trait()
    gov_id_get = cur.execute('select ID from GOVERNMENTS where EMPIRE_ID = ?', (empire_id,))
    gov_id_unstripped = gov_id_get.fetchall()
    gov_id = strip_single_naked(gov_id_unstripped)
    trade_factor = round(random.uniform(0.05, 0.15), 3)
    turn_offset = random.randint(5, 50) + int(turn)
    end_turn = int(turn_offset)
    pruned = 0

    cur.execute('insert into TRADERS (ID, CHAR_ID, TRADE_FACTOR, END_TURN, CURRENT_TOWN_ID, EMPIRE_ID, PRUNED) values(?,?,?,?,?,?,?)',
                (trader_id, char_id, trade_factor, end_turn, starting_town_id_int, empire_id, pruned))

    cur.execute('insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN) values(?,?,?,?,?,?)',
                (char_id, trader_name, trader_title, gov_id, trader_trait, turn))

    # (Xqhare): History:
    action = "funded trader"
    empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
    empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1

    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, TOWN_ID, CHAR_A_ID) values(?,?,?,?,?,?)',
                (empire_interaction_id, turn, empire_id, action, starting_town_id_int, char_id))

    db_connection.commit()
    cur.close()


def sql_create_region(chosen_empire: int):
    # (Xqhare): returns region_id stripped and as int
    cur = db_connection.cursor()

    region_id_rowcount = cur.execute('select ID from HISTORY')
    region_id = len(region_id_rowcount.fetchall()) + 1
    region_name = PlaceNameGen.gen_simple_name()
    empire_id = chosen_empire
    river_id = sql_choose_river(empire_id)
    cur.execute('insert into REGIONS (ID, NAME, EMPIRE_ID, RIVER_ID) values(?,?,?,?)',
                (region_id, region_name, empire_id, river_id))

    db_connection.commit()
    cur.close()

    return region_id


def sql_settle_town(empire_id: int, turn: int):
    cur = db_connection.cursor()

    '''empire_id0 = strip_single_naked(empire_id0)'''

    town_id_rowcount = cur.execute('select ID from TOWNS')
    town_id_temp = len(town_id_rowcount.fetchall())
    '''town_id_test = int(strip_single_naked(town_id_temp))'''
    town_id = town_id_temp + 1

    town_name = PlaceNameGen.sticher_full_name()

    town_pop = random.randint(50, 100000)
    # (Xqhare): How did this just work? wtf did I do, I never used dictionaries before!
    trade_good_dict = random.choice(list(GenLib.story_town_trade_goods_dict.items()))
    trade_good = trade_good_dict[0]
    trade_good_price = trade_good_dict[1]
    town_gdp = round(town_pop * trade_good_price)
    mayor_id = sql_create_mayor(empire_id, town_id, turn)

    emp_roads_num = cur.execute('select ROAD_ID from ROADS where EMPIRE_A_ID = ?', (empire_id,))
    num_roads = len(emp_roads_num.fetchall())

    # (Xqhare): if empire has 0 roads = capitol -> 2 roads! and a new region
    if num_roads == 0:
        sql_create_road(empire_id, turn, town_id)
        sql_create_road(empire_id, turn, town_id)
        region_id = sql_create_region(empire_id)
        capitol = 1
    # (Xqhare): else what every other town gets
    else:
        # (Xqhare): New road connection
        sql_interaction_connect_road(empire_id, turn, town_id)
        # (Xqhare): Choose region
        region_id = sql_choose_region(empire_id)
        capitol = 0

    town_b_id0 = cur.execute('select TOWN_B_ID from REGIONS where ID = ?', (region_id,))
    town_b_id_unstripped = town_b_id0.fetchall()
    town_a_id0 = cur.execute('select TOWN_A_ID from REGIONS where ID = ?', (region_id,))
    town_a_id_unstripped = town_a_id0.fetchall()

    if strip_single_naked(town_a_id_unstripped) == 'None':
        cur.execute('update REGIONS set TOWN_A_ID = ? where ID = ?', (town_id, region_id))
    elif strip_single_naked(town_b_id_unstripped) == 'None':
        cur.execute('update REGIONS set TOWN_B_ID = ? where ID = ?', (town_id, region_id))
    else:
        cur.execute('update REGIONS set TOWN_C_ID = ? where ID = ?', (town_id, region_id))

    river_id0 = cur.execute('select RIVER_ID from REGIONS where ID = ?', (region_id,))
    river_id_unstripped = river_id0.fetchall()
    river_id = int(strip_single_naked(river_id_unstripped))

    cur.execute('insert into TOWNS '
                '(ID, NAME, CAPITOL, POP, GDP, EMPIRE_ID, SETTLE_DATE, MAYOR_ID, RIVER_ID, MAJOR_TRADE_GOOD, MAJOR_TRADE_GOOD_PRICE) '
                'values(?,?,?,?,?,?,?,?,?,?,?)',
                (town_id, town_name, capitol, town_pop, town_gdp, empire_id, turn, mayor_id, river_id, trade_good, trade_good_price))

    # (Xqhare): History:
    action = "settle"
    empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
    empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1

    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, TOWN_ID) values(?, ?, ?, ?, ?)',
                (empire_interaction_id, turn, empire_id, action, town_id))

    db_connection.commit()

    cur.close()
    return town_id


def sql_create_empire(turn):
    cur = db_connection.cursor()
    # (Xqhare): check max id first, then add entry at max id +1
    empire_id_rowcount = cur.execute('select ID from EMPIRES')
    empire_id = len(empire_id_rowcount.fetchall()) + 1
    empire_name = EmpireGen.gen_empire_name()
    empire_pop = EmpireGen.gen_empire_pop()
    empire_area = EmpireGen.gen_empire_area()

    government_id_rowcount = cur.execute('select ID from GOVERNMENTS')
    government_id = len(government_id_rowcount.fetchall()) + 1

    leader_id_rowcount = cur.execute('select ID from CHARACTERS')
    leader_id = len(leader_id_rowcount.fetchall()) + 1

    this_turn = int(strip_single_naked(turn))

    # (Xqhare): Create Language and currency
    language_id_rowcount = cur.execute('select ID from LANGUAGES')
    language_id = len(language_id_rowcount.fetchall()) + 1
    language_name = LanguageGen.gen_lang_name()
    cur.execute("insert into LANGUAGES (ID, NAME, EMPIRE_ID) values(?,?,?)", (language_id, language_name, empire_id))

    currency_id_rowcount = cur.execute('select ID from CURRENCYS')
    currency_id = len(currency_id_rowcount.fetchall()) + 1
    currency_name = CurrencyGen.gen_general_currency_name()
    cur.execute("insert into CURRENCYS (ID, NAME, EMPIRE_ID) values(?,?,?)", (currency_id, currency_name, empire_id))

    # (Xqhare): Government generator
    seed0 = random.randint(0, 2)
    rep_or_state_list = ["Republic", "State"]
    ruler = 1
    match seed0:
        # (Xqhare): Democracy
        case 0:
            seed1 = random.randint(0, 9)
            if seed1 >= 8:
                semi = "Semi-"
            else:
                semi = ""

            type_adj_01_list = GenLib.story_government_type_adj_01
            type_sec_01_list = GenLib.story_government_type_sec_01
            gov_type = 0
            form0 = random.choice(type_adj_01_list)

            if form0 == "Presidential":
                temp_list = ["Parliamentary", "Democratic", "Constitutionary"]
                form1 = random.choice(temp_list)
                leader_title = "President"
            elif form0 == "Democratic":
                temp_list = ["Parliamentary", "Constitutionary", "Presidential"]
                form1 = random.choice(temp_list)
                leader_title = random.choice(GenLib.story_government_leader_title_01)
            elif form0 == "Constitutional":
                temp_list = ["Parliamentary", "Democratic", "Presidential"]
                form1 = random.choice(temp_list)
                leader_title = random.choice(GenLib.story_government_leader_title_01)
            else:
                form1 = random.choice(type_sec_01_list)
                leader_title = random.choice(GenLib.story_government_leader_title_01)

            rep_or_state = random.choice(rep_or_state_list)
            legislative_term = random.randint(2, 12)
            government_short_name = EmpireGen.gen_empire_name()
            first_election = turn + legislative_term

            full_title = semi + form0 + " " + form1 + " " + rep_or_state
            government_name = full_title + " of " + government_short_name

            cur.execute("insert into GOVERNMENTS (ID, NAME, EMPIRE_ID, TYPE, LEADER_TITLE, FULL_TITLE, NAME_SHORT, LEGISLATIVE_TERM, REP_OR_STATE, "
                        "LEADER_ID, NEXT_ELECTION_TURN)"
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (government_id, government_name, empire_id, gov_type, leader_title, full_title,
                         government_short_name, legislative_term, rep_or_state, leader_id, first_election))

            leader_name = PeopleNameGen.sticher_legal_name()
            leader_trait = PeopleNameGen.gen_trait()
            cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                        (leader_id, leader_name, leader_title, government_id, leader_trait, this_turn, ruler))
        case 1:
            seed1 = random.randint(0, 9)
            if seed1 >= 8:
                semi = "Semi-"
            else:
                semi = ""

            gov_type = 1
            form0 = random.choice(GenLib.story_government_type_adj_1)
            if form0 == "Council":
                seed1 = random.randint(0, 2)
                leader_title = random.choice(GenLib.story_government_leader_title_1)
                match seed1:
                    case 0:
                        form1 = random.choice(GenLib.story_government_type_sec_01)
                        rep_or_state = random.choice(rep_or_state_list)
                        full_title = semi + form0 + " " + form1 + " " + rep_or_state
                    case 1:
                        seed2 = random.randint(0, 3)
                        match seed2:
                            case 0:
                                form1 = random.choice(GenLib.story_government_type_adj_01)
                                rep_or_state = random.choice(rep_or_state_list)
                                full_title = semi + form1 + " " + form0 + " " + rep_or_state
                            case _:
                                form1 = random.choice(GenLib.story_government_type_adj_01)
                                rep_or_state = random.choice(rep_or_state_list)
                                full_title = semi + form0 + " " + form1 + " " + rep_or_state
                    case _:
                        rep_or_state = "Republic"
                        full_title = semi + form0 + " " + rep_or_state
            else:
                leader_title = random.choice(GenLib.story_government_leader_title_1)
                form1 = random.choice(GenLib.story_government_type_sec_01)
                rep_or_state = random.choice(rep_or_state_list)
                full_title = semi + form1 + " " + form0 + " " + rep_or_state

            legislative_term = random.randint(2, 12)
            government_short_name = EmpireGen.gen_empire_name()
            government_name = full_title + " of " + government_short_name
            first_election = turn + legislative_term

            cur.execute("insert into GOVERNMENTS (ID, NAME, EMPIRE_ID, TYPE, LEADER_TITLE, FULL_TITLE, NAME_SHORT, LEGISLATIVE_TERM, REP_OR_STATE, "
                        "LEADER_ID, NEXT_ELECTION_TURN)"
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (government_id, government_name, empire_id, gov_type, leader_title, full_title,
                         government_short_name, legislative_term, rep_or_state, leader_id, first_election))

            leader_name = PeopleNameGen.sticher_legal_name()
            leader_trait = PeopleNameGen.gen_trait()
            cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                        (leader_id, leader_name, leader_title, government_id, leader_trait, this_turn, ruler))

        case _:
            seed1 = random.randint(0, 9)
            if seed1 >= 8:
                semi = "Semi-"
            else:
                semi = ""

            form1 = random.choice(GenLib.story_government_type_adj_0)
            gov_type = 2

            match form1:
                case "Corporate":
                    leader_title = random.choice(GenLib.story_government_leader_title_0_cor)
                    legislative_term = random.randint(10, 25)
                    government_short_name = EmpireGen.gen_empire_name()
                    rep_or_state = "Corporation"
                    seed2 = random.randint(0, 1)
                    match seed2:
                        case 0:
                            form0 = random.choice(GenLib.story_government_type_sec_0)
                            full_title = semi + form1 + " " + form0
                        case _:
                            form0 = random.choice(GenLib.story_government_type_sec_01)
                            full_title = semi + form1 + " " + form0 + " State"
                    government_name = full_title + " of " + government_short_name
                    first_election = turn + legislative_term

                    cur.execute(
                        "insert into GOVERNMENTS (ID, NAME, EMPIRE_ID, TYPE, LEADER_TITLE, FULL_TITLE, NAME_SHORT, LEGISLATIVE_TERM, REP_OR_STATE, "
                        "LEADER_ID, NEXT_ELECTION_TURN)"
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (government_id, government_name, empire_id, gov_type, leader_title, full_title,
                         government_short_name, legislative_term, rep_or_state, leader_id, first_election))

                    leader_name = PeopleNameGen.sticher_legal_name()
                    leader_trait = PeopleNameGen.gen_trait()
                    cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                                (leader_id, leader_name, leader_title, government_id, leader_trait, this_turn, ruler))

                case "Religious":
                    seed1 = random.randint(0, 9)
                    if seed1 >= 8:
                        semi = "Semi-"
                    else:
                        semi = ""

                    gov_type = 2
                    leader_title = random.choice(GenLib.story_government_leader_title_0_reli)
                    legislative_term = 100
                    government_short_name = EmpireGen.gen_empire_name()
                    rep_or_state = random.choice(rep_or_state_list)
                    seed2 = random.randint(0, 1)
                    match seed2:
                        case 0:
                            form0 = random.choice(GenLib.story_government_type_sec_01)
                            full_title = semi + form1 + " " + form0 + " " + rep_or_state
                        case _:
                            form0 = random.choice(GenLib.story_government_type_adj_01)
                            full_title = semi + form0 + " " + form1 + " " + rep_or_state
                    government_name = full_title + " of " + government_short_name
                    first_election = turn + legislative_term

                    cur.execute(
                        "insert into GOVERNMENTS (ID, NAME, EMPIRE_ID, TYPE, LEADER_TITLE, FULL_TITLE, NAME_SHORT, LEGISLATIVE_TERM, REP_OR_STATE, "
                        "LEADER_ID, NEXT_ELECTION_TURN)"
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (government_id, government_name, empire_id, gov_type, leader_title, full_title,
                         government_short_name, legislative_term, rep_or_state, leader_id, first_election))

                    leader_name = PeopleNameGen.sticher_legal_name()
                    leader_trait = PeopleNameGen.gen_trait()
                    cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                                (leader_id, leader_name, leader_title, government_id, leader_trait, this_turn, ruler))

                case "Monarchy":
                    seed1 = random.randint(0, 9)
                    if seed1 >= 8:
                        semi = "Semi-"
                    else:
                        semi = ""

                    gov_type = 2
                    leader_title = random.choice(GenLib.story_government_leader_title_0_mon)
                    legislative_term = 100
                    government_short_name = EmpireGen.gen_empire_name()
                    rep_or_state = "Monarchy"
                    form0 = random.choice(GenLib.government_name_monarchy)
                    full_title = semi + form0 + " " + form1 + " "
                    government_name = full_title + " of " + government_short_name
                    first_election = turn + legislative_term

                    cur.execute(
                        "insert into GOVERNMENTS (ID, NAME, EMPIRE_ID, TYPE, LEADER_TITLE, FULL_TITLE, NAME_SHORT, LEGISLATIVE_TERM, REP_OR_STATE, "
                        "LEADER_ID, NEXT_ELECTION_TURN)"
                        "values(?,?,?,?,?,?,?,?,?,?,?)",
                        (government_id, government_name, empire_id, gov_type, leader_title, full_title,
                         government_short_name, legislative_term, rep_or_state, leader_id, first_election))

                    leader_name = PeopleNameGen.sticher_legal_name()
                    leader_trait = PeopleNameGen.gen_trait()
                    cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                                (leader_id, leader_name, leader_title, government_id, leader_trait, this_turn, ruler))
                case _:
                    print("Error - SQL.3")

    # (Xqhare): Technology level creator:
    mil_tech = 1
    dip_tech = 1
    soc_tech = 1

    # (Xqhare): Dump everything into database:
    cur.execute('insert into EMPIRES (ID, NAME, LEADER_ID, LANGUAGE_ID, POP, AREA, CURRENCY_ID, GOVERNMENT_ID, MIL_TECH, DIP_TECH, SOC_TECH) '
                'values(?,?,?,?,?,?,?,?,?,?,?)',
                (empire_id, empire_name, leader_id, language_id, empire_pop, empire_area, currency_id, government_id, mil_tech, dip_tech, soc_tech))

    # (Xqhare): create 1 starting town; history should be in settle_town
    num_start_town = 1
    for n in range(num_start_town):
        sql_settle_town(empire_id, turn)

    db_connection.commit()
    cur.close()


def sql_populate_database(n: int, turn):
    """
    Populates the database with n entries
    :param: n the number of entries to be generated
    """
    for n in range(n):
        sql_create_empire(turn)


def sql_town_conquest(empire_id_winner, empire_id_looser):
    cur = db_connection.cursor()

    town_ids_looser = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (empire_id_looser,))
    town_ids_looser = town_ids_looser.fetchall()
    chosen_town_ran = random.choice(town_ids_looser)
    chosen_town = strip_single_naked(chosen_town_ran)
    cur.execute('update TOWNS set EMPIRE_ID = ? where ID = ?', (empire_id_winner, chosen_town))
    db_connection.commit()
    cur.close()
    return chosen_town


# (Xqhare): DONE: needs rework; made sense to limit pop cycle, now it doubles up with pop_gdp_cycle
# (Xqhare): keeping itr here makes sense; it is only called when an empire is attacked and looses pops -> only chance it has to be destroyed
def sql_update_empire_pop(empire_id, empire_b_id):
    # (Xqhare): select all pop in towns of empire, add together -> push to table
    cur = db_connection.cursor()

    empire_winner = empire_b_id
    empire_id_internal = strip_single_naked(empire_id)
    all_empire_pop_tuple = cur.execute('select SUM(POP) from TOWNS where EMPIRE_ID = ?', (empire_id_internal,))
    all_empire_pop_pre = all_empire_pop_tuple.fetchall()
    all_empire_pop = strip_single_naked(all_empire_pop_pre)
    cur.execute('update EMPIRES set POP = ? where ID = ?', (all_empire_pop, empire_id_internal))

    # (Xqhare): prooning check
    if len(all_empire_pop) <= 0:
        # (Xqhare): print("Pruning: ", empire_id_internal)
        interact_turn_rowcount = cur.execute('select TURN from HISTORY')
        interact_turn = strip_single_naked(max(interact_turn_rowcount.fetchall()))
        sql_prune_empire(empire_id_internal, interact_turn)
        empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
        empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
        action = "destroyed"
        cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, EMPIRE_B_ID) values(?, ?, ?, ?, ?)',
                    (empire_interaction_id, interact_turn, empire_winner, action, empire_id_internal))

    db_connection.commit()
    cur.close()


def sql_prune_empire(empire_id, turn):
    cur = db_connection.cursor()

    empire_id_internal = strip_single_naked(empire_id)

    cur.execute('update TRADERS set PRUNED = 1 where EMPIRE_ID = ?', (empire_id_internal,))
    trader_char_id_lst0 = cur.execute('select CHAR_ID from TRADERS where EMPIRE_ID = ?', (empire_id_internal,))
    trader_char_id_lst = trader_char_id_lst0.fetchall()
    turn_stripped = int(strip_single_naked(turn))
    # (Xqhare): Trader retirement HISTORY:
    for char_id in trader_char_id_lst:
        trader_char_id = int(strip_single_naked(char_id))
        this_town0 = cur.execute('select CURRENT_TOWN_ID from TRADERS where CHAR_ID = ?', (trader_char_id,))
        this_town_unstripped = this_town0.fetchall()
        this_town = int(strip_single_naked(this_town_unstripped))
        action = "retired in"
        empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
        empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
        cur.execute('insert into HISTORY (ID, TURN, ACTION, TOWN_ID, CHAR_A_ID) values(?,?,?,?,?)',
                    (empire_interaction_id, turn_stripped, action, this_town, trader_char_id))

    cur.execute('delete from EMPIRES where ID = ?', (empire_id_internal,))
    cur.execute('delete from CURRENCYS where EMPIRE_ID = ?', (empire_id_internal,))
    cur.execute('delete from CURRENCYS where EMPIRE_ID = ?', (empire_id_internal,))
    cur.execute('delete from EMPIRE_RELATIONS where EMPIRE_ID = ?', (empire_id_internal,))
    cur.execute('delete from EMPIRE_RELATIONS where ALLY_ID = ?', (empire_id_internal,))
    # (Xqhare): Don't prune GOVERNMENT -> for output; works only as long as new empires are added at the end of THIS table
    """cur.execute('delete from GOVERNMENTS where EMPIRE_ID = ?', (empire_id_internal,))"""
    cur.execute('delete from LANGUAGES where EMPIRE_ID = ?', (empire_id_internal,))
    # (Xqhare): CHARACTERS need to stay; also -> unique ID and all that
    """cur.execute('delete from CHARACTERS where GOVERNMENT_ID = ?', (empire_id_internal,))"""

    db_connection.commit()
    cur.close()


def sql_interaction_settle(chosen_empire_a, chosen_empire_b, turn):
    cur = db_connection.cursor()
    sql_settle_town(chosen_empire_a, turn)
    db_connection.commit()
    sql_update_empire_pop(chosen_empire_a, chosen_empire_b)
    sql_update_empire_pop(chosen_empire_b, chosen_empire_a)
    cur.close()


def sql_interaction_attack(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b):
    # (Xqhare): Empire A wins!
    empire_interaction_id_stripped = int(strip_single_naked(empire_interaction_id))
    town_id = sql_town_conquest(chosen_empire_a, chosen_empire_b)
    action = "attack"
    op_name = OperationGen.main_operation_name()

    cur = db_connection.cursor()

    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, EMPIRE_B_ID, TOWN_ID, OP_NAME) values(?,?,?,?,?,?,?)',
                (empire_interaction_id_stripped, turn, chosen_empire_a, action, chosen_empire_b, town_id, op_name))

    db_connection.commit()
    cur.close()

    # (Xqhare): this prunes; pruning gets a history => commit has to happen before for correct history
    sql_update_empire_pop(chosen_empire_a, chosen_empire_b)
    sql_update_empire_pop(chosen_empire_b, chosen_empire_a)


def sql_interaction_visit(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b):
    cur = db_connection.cursor()
    # (Xqhare): Updating interaction table:
    no_action = "visited"
    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, EMPIRE_B_ID) values(?, ?, ?, ?, ?)',
                (empire_interaction_id, turn, chosen_empire_a, no_action, chosen_empire_b))
    dip_tech_a_ex = cur.execute('select DIP_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
    dip_tech_a_t = dip_tech_a_ex.fetchall()
    dip_tech_a = int(strip_single_naked(dip_tech_a_t)) + 1
    dip_tech_b_ex = cur.execute('select DIP_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
    dip_tech_b_t = dip_tech_b_ex.fetchall()
    dip_tech_b = int(strip_single_naked(dip_tech_b_t)) + 1
    cur.execute('update EMPIRES set DIP_TECH = ? where ID = ?', (dip_tech_a, chosen_empire_a))
    cur.execute('update EMPIRES set DIP_TECH = ? where ID = ?', (dip_tech_b, chosen_empire_b))
    db_connection.commit()
    cur.close()


def sql_interaction_parade(empire_interaction_id, turn, chosen_empire_a, action):
    # (Xqhare): This is a single interaction for only empire A!
    cur = db_connection.cursor()

    # (Xqhare): Selecting owned town to be paraded in:
    owned_town_list_e = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (chosen_empire_a,))
    owned_town_list = owned_town_list_e.fetchall()
    chosen_town_pp = random.choice(owned_town_list)
    chosen_town = int(strip_single_naked(chosen_town_pp))

    # (Xqhare): Updating interaction table:
    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, TOWN_ID) values(?, ?, ?, ?, ?)',
                (empire_interaction_id, turn, chosen_empire_a, action, chosen_town))

    # (Xqhare): Mil-tech advancement for parade:
    mil_tech_a_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
    mil_tech_a_t = mil_tech_a_ex.fetchall()
    mil_tech_a = int(strip_single_naked(mil_tech_a_t)) + 1
    cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_a, chosen_empire_a))

    # (Xqhare): Housekeeping:
    db_connection.commit()
    cur.close()


def sql_interaction_tech_development(empire_interaction_id, turn, chosen_empire_a, action):
    cur = db_connection.cursor()
    num_tech = random.randint(1, 3)

    # (Xqhare): Updating interaction table:
    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION) values(?, ?, ?, ?)',
                (empire_interaction_id, turn, chosen_empire_a, action))

    for n in range(num_tech):
        seed = random.randint(0, 2)
        match seed:
            case 0:
                mil_tech_a_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
                mil_tech_a_t = mil_tech_a_ex.fetchall()
                mil_tech_a = int(strip_single_naked(mil_tech_a_t)) + 1
                cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_a, chosen_empire_a))
            case 1:
                dip_tech_a_ex = cur.execute('select DIP_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
                dip_tech_a_t = dip_tech_a_ex.fetchall()
                dip_tech_a = int(strip_single_naked(dip_tech_a_t)) + 1
                cur.execute('update EMPIRES set DIP_TECH = ? where ID = ?', (dip_tech_a, chosen_empire_a))
            case _:
                soc_tech_a_ex = cur.execute('select SOC_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
                soc_tech_a_t = soc_tech_a_ex.fetchall()
                soc_tech_a = int(strip_single_naked(soc_tech_a_t)) + 1
                cur.execute('update EMPIRES set SOC_TECH = ? where ID = ?', (soc_tech_a, chosen_empire_a))

    # (Xqhare): Housekeeping:
    db_connection.commit()
    cur.close()


def sql_interaction_ally(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b):
    cur = db_connection.cursor()

    gen_action = "ally"

    # (Xqhare): Insert or Update relations for both allies:
    cur.execute('insert into EMPIRE_RELATIONS(EMPIRE_ID, ALLY_ID) values(?, ?) '
                'on conflict(EMPIRE_ID) do update set EMPIRE_ID = ?, ALLY_ID = ?',
                (chosen_empire_a, chosen_empire_b, chosen_empire_a, chosen_empire_b))
    cur.execute('insert into EMPIRE_RELATIONS(EMPIRE_ID, ALLY_ID) values(?, ?) '
                'on conflict(EMPIRE_ID) do update set EMPIRE_ID = ?, ALLY_ID = ?',
                (chosen_empire_b, chosen_empire_a, chosen_empire_b, chosen_empire_a))
    cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, EMPIRE_B_ID) values(?, ?, ?, ?, ?)',
                (empire_interaction_id, turn, chosen_empire_a, gen_action, chosen_empire_b))

    # (Xqhare): DONE: new ally bonus:
    # (Xqhare): Dip-tech advancement for allies:
    dip_tech_a_ex = cur.execute('select DIP_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
    dip_tech_a_t = dip_tech_a_ex.fetchall()
    dip_tech_a = int(strip_single_naked(dip_tech_a_t)) + 1
    dip_tech_b_ex = cur.execute('select DIP_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
    dip_tech_b_t = dip_tech_b_ex.fetchall()
    dip_tech_b = int(strip_single_naked(dip_tech_b_t)) + 1
    cur.execute('update EMPIRES set DIP_TECH = ? where ID = ?', (dip_tech_a, chosen_empire_a))
    cur.execute('update EMPIRES set DIP_TECH = ? where ID = ?', (dip_tech_b, chosen_empire_b))

    # (Xqhare): Social-tech advancement for allies:
    soc_tech_a_ex = cur.execute('select SOC_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
    soc_tech_a_t = soc_tech_a_ex.fetchall()
    soc_tech_a = int(strip_single_naked(soc_tech_a_t)) + 1
    soc_tech_b_ex = cur.execute('select SOC_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
    soc_tech_b_t = soc_tech_b_ex.fetchall()
    soc_tech_b = int(strip_single_naked(soc_tech_b_t)) + 1
    cur.execute('update EMPIRES set SOC_TECH = ? where ID = ?', (soc_tech_a, chosen_empire_a))
    cur.execute('update EMPIRES set SOC_TECH = ? where ID = ?', (soc_tech_b, chosen_empire_b))

    # (Xqhare): Mil-tech advancement for allies (1/3 chance for level up):
    chance = random.randint(0, 2)
    match chance:
        case 0:
            mil_tech_a_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
            mil_tech_a_t = mil_tech_a_ex.fetchall()
            mil_tech_a = int(strip_single_naked(mil_tech_a_t)) + 1
            cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_a, chosen_empire_a))
            mil_tech_b_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
            mil_tech_b_t = mil_tech_b_ex.fetchall()
            mil_tech_b = int(strip_single_naked(mil_tech_b_t)) + 1
            cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_b, chosen_empire_b))
        case _:
            mil_tech_a_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
            mil_tech_a_t = mil_tech_a_ex.fetchall()
            mil_tech_a = int(strip_single_naked(mil_tech_a_t))
            cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_a, chosen_empire_a))
            mil_tech_b_ex = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
            mil_tech_b_t = mil_tech_b_ex.fetchall()
            mil_tech_b = int(strip_single_naked(mil_tech_b_t))
            cur.execute('update EMPIRES set MIL_TECH = ? where ID = ?', (mil_tech_b, chosen_empire_b))

    # (Xqhare): Update empire pop:
    sql_update_empire_pop(chosen_empire_a, chosen_empire_b)
    sql_update_empire_pop(chosen_empire_b, chosen_empire_a)

    # (Xqhare): Housekeeping:
    db_connection.commit()
    cur.close()


# (Xqhare): TODO: this needs optimizing - but updating pop and gdp of every town IS resource intensive...
def sql_gdp_and_pop_all_town_cycle():
    cur = db_connection.cursor()
    all_empire_ids = cur.execute('select ID from EMPIRES')
    all_empire_id = all_empire_ids.fetchall()
    for emp_id in all_empire_id:
        empire_id = int(strip_single_naked(emp_id))
        town_ids = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (empire_id,))
        town_ids0 = town_ids.fetchall()

        for town in town_ids0:
            this_town = int(strip_single_naked(town))

            town_gdp0 = cur.execute('select GDP from TOWNS where ID = ?', (this_town,))
            town_gdp_unstripped = town_gdp0.fetchall()
            town_gdp = int(strip_single_naked(town_gdp_unstripped))
            trade_good_price0 = cur.execute('select MAJOR_TRADE_GOOD_PRICE from TOWNS where ID = ?', (this_town,))
            trade_good_price_unstripped = trade_good_price0.fetchall()
            trade_good_price = float(strip_single_naked(trade_good_price_unstripped))
            new_gdp = round(town_gdp + ((town_gdp / 100) * (trade_good_price / 100)))
            cur.execute('update TOWNS set GDP = ? where ID = ?', (new_gdp, this_town))

            town_pop0 = cur.execute('select POP from TOWNS where ID = ?', (this_town,))
            town_pop_unstripped = town_pop0.fetchall()
            town_pop = int(strip_single_naked(town_pop_unstripped))
            growth_rate_offset = random.uniform(0.01, 0.04)
            growth_rate = growth_rate_offset * (town_gdp / 100)
            new_pop = round(town_pop + growth_rate)
            cur.execute('update TOWNS set POP = ? where ID = ?', (new_pop, this_town))

            db_connection.commit()

    cur.close()


def sql_trader_cycle(turn):
    turn_stripped = int(strip_single_naked(turn))
    cur = db_connection.cursor()
    trader_id_all = cur.execute('select ID from TRADERS where PRUNED = 0')
    all_trader_id = trader_id_all.fetchall()

    if len(all_trader_id) > 0:
        for entry in all_trader_id:
            trader_id = int(strip_single_naked(entry))
            this_town0 = cur.execute('select CURRENT_TOWN_ID from TRADERS where ID = ?', (trader_id,))
            this_town_unstripped = this_town0.fetchall()
            this_town = strip_single_naked(this_town_unstripped)
            trade_factor0 = cur.execute('select TRADE_FACTOR from TRADERS where ID = ?', (trader_id,))
            trade_factor_unstripped = trade_factor0.fetchall()
            trade_factor = float(strip_single_naked(trade_factor_unstripped))
            road_id0 = cur.execute('select ROAD_ID from ROADS where TOWN_ID = ?', (this_town,))
            road_id_unstripped = road_id0.fetchall()
            road_id = strip_single_naked(road_id_unstripped)
            first_test_town = sql_road_prev_next_town(road_id, this_town, "next")
            trader_char_id0 = cur.execute('select CHAR_ID from TRADERS where ID = ?', (trader_id,))
            trader_char_id_unstripped = trader_char_id0.fetchall()
            trader_char_id = int(strip_single_naked(trader_char_id_unstripped))

            # (Xqhare): DONE: Rework when economy system done
            gdp_this_town0 = cur.execute('select GDP from TOWNS where ID = ?', (this_town,))
            gdp_this_town_unstripped = gdp_this_town0.fetchall()
            trade_good_price0 = cur.execute('select MAJOR_TRADE_GOOD_PRICE from TOWNS where ID = ?', (this_town,))
            trade_good_price_unstripped = trade_good_price0.fetchall()
            trade_good_price = float(strip_single_naked(trade_good_price_unstripped))
            final_trade_factor = trade_good_price * trade_factor
            gdp_this_town = float(strip_single_naked(gdp_this_town_unstripped))
            new_gdp = round(gdp_this_town + ((gdp_this_town / 100) * final_trade_factor))
            cur.execute('update TOWNS set GDP = ? where ID = ?', (new_gdp, this_town))

            if first_test_town == 0:
                test_next_town = sql_road_prev_next_town(road_id, this_town, "prev")
            else:
                test_next_town = first_test_town

            if test_next_town == 0:
                empire_id0 = cur.execute('select EMPIRE_ID from TRADERS where ID = ?', (trader_id,))
                empire_id_unstripped = empire_id0.fetchall()
                empire_id = int(strip_single_naked(empire_id_unstripped))
                cap_select0 = cur.execute('select ID from TOWNS where EMPIRE_ID = ?',
                                          (empire_id,))
                cap_select_unstripped = cap_select0.fetchall()
                # (Xqhare): print(f'HEY LISTEN {cap_select_unstripped}; {empire_id}; {road_id}; {this_town}')
                if len(cap_select_unstripped) > 1:
                    chosen_next_town_unstripped = random.choice(cap_select_unstripped)
                    chosen_next_town = strip_single_naked(chosen_next_town_unstripped)
                else:
                    # (Xqhare): This produces garbage data! why?
                    # chosen_next_town = int(strip_single_naked(cap_select_unstripped))

                    # (Xqhare): This is the workaround:
                    chosen_next_town = this_town
            else:
                chosen_next_town = test_next_town

            death_check0 = cur.execute('select END_TURN from TRADERS where ID = ?', (trader_id,))
            death_check_unstripped = death_check0.fetchall()
            death_check = int(strip_single_naked(death_check_unstripped))
            if death_check == turn_stripped:
                cur.execute('update TRADERS set PRUNED = 1 where ID = ?', (trader_id,))
                # (Xqhare): HISTORY: Trader xx retired in xy
                action = "retired in"
                empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
                empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
                cur.execute('insert into HISTORY (ID, TURN, ACTION, TOWN_ID, CHAR_A_ID) values(?,?,?,?,?)',
                            (empire_interaction_id, turn_stripped, action, this_town, trader_char_id))
            else:
                cur.execute('update TRADERS set CURRENT_TOWN_ID = ? where ID = ?', (chosen_next_town, trader_id))
                # (Xqhare): HISTORY: Trader xx continued on to yx
                action = "trader continued to"
                empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
                empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
                cur.execute('insert into HISTORY (ID, TURN, ACTION, TOWN_ID, CHAR_A_ID, TOWN_B_ID) values(?,?,?,?,?,?)',
                            (empire_interaction_id, turn_stripped, action, this_town, trader_id, chosen_next_town))
    db_connection.commit()

    cur.close()


def sql_empire_election_cycle(turn):
    turn_stripped = int(strip_single_naked(turn))
    cur = db_connection.cursor()

    empire_id_all = cur.execute('select ID from EMPIRES')
    all_empire_id = empire_id_all.fetchall()

    for entry in all_empire_id:
        emp_id = int(strip_single_naked(entry))
        next_election = cur.execute('select NEXT_ELECTION_TURN from GOVERNMENTS where ID = ?', (emp_id,))
        next_election0 = next_election.fetchall()
        next_election_stripped = int(strip_single_naked(next_election0))
        turn_stripped = int(strip_single_naked(turn_stripped))

        test_turn = cur.execute('select TURN from HISTORY where EMPIRE_A_ID = ? and ACTION = "was elected"', (emp_id,))
        test_turn0 = test_turn.fetchall()
        test_turn_stripped = strip_single_naked(test_turn0)

        # (Xqhare): Test if it is election time and if an election has been held this turn for this empire.
        if turn_stripped == next_election_stripped and test_turn_stripped != turn_stripped:
            title = cur.execute('select LEADER_TITLE from GOVERNMENTS where ID = ?', (emp_id,))
            title0 = title.fetchall()
            title_stripped = strip_single_naked(title0)
            leader_id_rowcount = cur.execute('select ID from CHARACTERS')
            leader_id = len(leader_id_rowcount.fetchall()) + 1
            leader_name = PeopleNameGen.sticher_legal_name()
            leg_term = cur.execute('select LEGISLATIVE_TERM from GOVERNMENTS where ID = ?', (emp_id,))
            leg_term = leg_term.fetchall()
            leg_term_stripped = int(strip_single_naked(leg_term))
            new_election_turn = (turn_stripped + leg_term_stripped)
            leader_trait = PeopleNameGen.gen_trait()
            history_id_rowcount = cur.execute('select ID from HISTORY')
            history_id = len(history_id_rowcount.fetchall()) + 1
            action = "was elected"
            ruler = 1

            cur.execute("insert into CHARACTERS (ID, NAME, TITLE, GOVERNMENT_ID, TRAIT, BORN_TURN, RULER) values(?,?,?,?,?,?, ?)",
                        (leader_id, leader_name, title_stripped, emp_id, leader_trait, turn_stripped, ruler))
            cur.execute('update GOVERNMENTS set LEADER_ID = ?, NEXT_ELECTION_TURN = ? where ID = ?',
                        (leader_id, new_election_turn, emp_id))
            cur.execute('update EMPIRES set LEADER_ID = ? where ID = ?',
                        (leader_id, emp_id))
            cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, CHAR_A_ID) values(?,?,?,?,?)',
                        (history_id, turn_stripped, emp_id, action, leader_id))

        db_connection.commit()

    cur.close()


# (Xqhare): this was supposed to have a test with the town_id and if failed try with another for 100% success rate; boring? also harder to implement
# (Xqhare): Intra Empire pre-existing Roads:
def sql_interaction_connect_road(chosen_empire, turn, town_id):
    cur = db_connection.cursor()

    pos_road_ids = cur.execute('select ROAD_ID from ROADS where TOWN_ID = ?', (town_id,))
    pos_road_ids_lst = pos_road_ids.fetchall()
    if len(pos_road_ids_lst) > 1:
        chosen_road0 = random.choice(pos_road_ids_lst)
        chosen_road = strip_single_naked(chosen_road0)
    else:
        random_existing_road_lst0 = cur.execute('select ROAD_ID from ROADS where EMPIRE_A_ID = ?', (chosen_empire,))
        random_existing_road_lst = random_existing_road_lst0.fetchall()
        chosen_road_to_strip = random.choice(random_existing_road_lst)
        chosen_road = strip_single_naked(chosen_road_to_strip)

    # (Xqhare): needed for random road connections
    """pos_town_ids = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (chosen_empire,))
    pos_town_ids_lst = pos_town_ids.fetchall()
    chosen_test_town0 = random.choice(pos_town_ids_lst)
    chosen_test_town = strip_single_naked(chosen_test_town0)"""

    chosen_test_town = town_id

    road_connections_ls = cur.execute('select ROAD_ID from ROADS where TOWN_ID = ?', (chosen_test_town,))
    road_connections_lst = road_connections_ls.fetchall()

    checklist = []

    for element in road_connections_lst:
        this_road_connection = element
        this_road_connection_stripped = strip_single_naked(this_road_connection)
        if this_road_connection_stripped == chosen_road:
            check = 1
            checklist.append(check)
        else:
            check = 0
            checklist.append(check)

    checklist_sum = sum(checklist)
    r_id_rowcount = cur.execute('select ID from ROADS')
    r_id = len(r_id_rowcount.fetchall()) + 1

    if checklist_sum == 0:
        # (Xqhare): Road building successful
        cur.execute('insert into ROADS (ID, ROAD_ID, TURN, EMPIRE_A_ID, TOWN_ID) values(?,?,?,?,?)',
                    (r_id, chosen_road, turn, chosen_empire, chosen_test_town))
        db_connection.commit()

        # (Xqhare): History:
        action = "connected by road to"
        empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
        empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
        # (Xqhare): As this is only called when roads already exist, there has to be a previous city; except if only capitol exists
        prev_town_id = sql_road_prev_next_town(chosen_road, chosen_test_town, "prev")
        if prev_town_id != 0:
            cur.execute('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, TOWN_ID, TOWN_B_ID) values(?,?,?,?,?,?)',
                        (empire_interaction_id, turn, chosen_empire, action, prev_town_id, chosen_test_town))
    else:
        sql_create_road(chosen_empire, turn, chosen_test_town)

    db_connection.commit()
    cur.close()


def gen_empire_interaction(turn: int):
    cur = db_connection.cursor()

    # (Xqhare): Fetching data from database
    empire_id_rowcount = cur.execute('select ID from EMPIRES')
    max_empires = empire_id_rowcount.fetchall()
    chosen_empires = random.sample(max_empires, k=2)
    chosen_empire_a = strip_single_naked(chosen_empires[0])
    chosen_empire_b = strip_single_naked(chosen_empires[1])

    empire_interaction_id_rowcount = cur.execute('select ID from HISTORY')
    empire_interaction_id = len(empire_interaction_id_rowcount.fetchall()) + 1
    gen_action = random.choice(GenLib.story_empire_interactions)

    empire_a_mil_pf = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_a,))
    empire_a_mil_pp = empire_a_mil_pf.fetchall()
    empire_a_mil = int(strip_single_naked(empire_a_mil_pp))
    empire_b_mil_pf = cur.execute('select MIL_TECH from EMPIRES where ID = ?', (chosen_empire_b,))
    empire_b_mil_pp = empire_b_mil_pf.fetchall()
    empire_b_mil = int(strip_single_naked(empire_b_mil_pp))

    # (Xqhare): DEBUG section
    '''print("EmpA-ID, ", chosen_empire_a, "; EmpB-ID, ", chosen_empire_b, "; action: ", gen_action, "; turn: ", turn, "; History id: ",
    empire_interaction_id)'''

    empire_a_pop0 = cur.execute('select POP from EMPIRES where ID= ?', (chosen_empire_a,))
    empire_a_pop = empire_a_pop0.fetchall()
    empire_b_pop0 = cur.execute('select POP from EMPIRES where ID= ?', (chosen_empire_b,))
    empire_b_pop = empire_b_pop0.fetchall()

    # (Xqhare): The two if statements are for failsafe purposes only
    if strip_single_naked(empire_a_pop) == 'None':
        # (Xqhare): print("!Empire not pruned! ", chosen_empire_a)
        sql_update_empire_pop(chosen_empire_a, chosen_empire_b)
        empire_a_start_pop = 1
    else:
        empire_a_start_pop = int(strip_single_naked(empire_a_pop))

    if strip_single_naked(empire_b_pop) == 'None':
        # (Xqhare): print("!Empire not pruned! ", chosen_empire_b)
        sql_update_empire_pop(chosen_empire_b, chosen_empire_a)
        empire_b_start_pop = 1
    else:
        empire_b_start_pop = int(strip_single_naked(empire_b_pop))
    # (Xqhare): DEBUG section ends

    match gen_action:
        case "ally":
            # (Xqhare): check alliance status if already allied, visit
            ally_check_at = cur.execute('select ALLY_ID from EMPIRE_RELATIONS where EMPIRE_ID = ?', (chosen_empire_a,))
            ally_check_a = ally_check_at.fetchall()
            ally_check_a_fin = strip_single_naked(ally_check_a)
            ally_check_bt = cur.execute('select ALLY_ID from EMPIRE_RELATIONS where EMPIRE_ID = ?', (chosen_empire_b,))
            ally_check_b = ally_check_bt.fetchall()
            ally_check_b_fin = strip_single_naked(ally_check_b)
            if ally_check_a_fin == '' and ally_check_b_fin == '':
                sql_interaction_ally(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)
            else:
                sql_interaction_visit(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)

        case "attack":

            # (Xqhare): check alliance status if an empire is already allied they visit
            ally_check_at = cur.execute('select ALLY_ID from EMPIRE_RELATIONS where EMPIRE_ID = ?', (chosen_empire_a,))
            ally_check_a = ally_check_at.fetchall()
            ally_check_a_fin = strip_single_naked(ally_check_a)
            ally_check_bt = cur.execute('select ALLY_ID from EMPIRE_RELATIONS where EMPIRE_ID = ?', (chosen_empire_b,))
            ally_check_b = ally_check_bt.fetchall()
            ally_check_b_fin = strip_single_naked(ally_check_b)
            # (Xqhare): If allied they visit
            if ally_check_a_fin == chosen_empire_b or ally_check_b_fin == chosen_empire_a:
                sql_interaction_visit(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)
            else:
                # (Xqhare): Calculates a military score; using mil_tech and all_empire_pop; temp anyway
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
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)
                        case _:
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_b, chosen_empire_a)
                # (Xqhare): If A is stronger, there is a 90% chance of them winning
                elif empire_a_mil_off < empire_b_mil_off:
                    chance = random.randint(0, 9)
                    match chance:
                        case 0:
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_b, chosen_empire_a)
                        case _:
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)
                # (Xqhare): If both have the same strength it's a 50/50
                else:
                    chance = random.randint(0, 1)
                    match chance:
                        case 0:
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_b, chosen_empire_a)
                        case _:
                            sql_interaction_attack(empire_interaction_id, turn, chosen_empire_a, chosen_empire_b)
        case "settle":
            sql_interaction_settle(chosen_empire_a, chosen_empire_b, turn)
        case "had a parade in":
            sql_interaction_parade(empire_interaction_id, turn, chosen_empire_a, gen_action)
        case "developed technologies":
            sql_interaction_tech_development(empire_interaction_id, turn, chosen_empire_a, gen_action)
        case "developed economy":
            town_id_lst0 = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (chosen_empire_a,))
            town_id_lst = town_id_lst0.fetchall()
            if len(town_id_lst) == 0:
                sql_update_empire_pop(chosen_empire_a, chosen_empire_b)
            elif len(town_id_lst) == 1:
                starting_town_id = int(strip_single_naked(town_id_lst[0]))
                sql_create_trader(chosen_empire_a, starting_town_id, turn)
            else:
                town_id_unstripped = random.choice(town_id_lst)
                starting_town_id = int(strip_single_naked(town_id_unstripped))
                sql_create_trader(chosen_empire_a, starting_town_id, turn)
        case "connected by road to":
            all_towns_lst = cur.execute('select ID from TOWNS where EMPIRE_ID = ?', (chosen_empire_a,))
            all_towns_list = all_towns_lst.fetchall()
            if len(all_towns_list) > 1:
                chosen_town_ns = random.choice(all_towns_list)
                chosen_town = strip_single_naked(chosen_town_ns)
                sql_interaction_connect_road(chosen_empire_a, turn, chosen_town)
            elif len(all_towns_list) == 1:
                chosen_town = strip_single_naked(all_towns_list)
                sql_interaction_connect_road(chosen_empire_a, turn, chosen_town)
        case _:
            return "Error - SQL.1"

    cur.close()


def sql_empire_pruning_cycle(turn: int):
    cur = db_connection.cursor()

    all_empire_ids0 = cur.execute('select ID from EMPIRES')
    all_empire_ids = all_empire_ids0.fetchall()
    for empire_id in all_empire_ids:
        this_empire_id = int(strip_single_naked(empire_id))
        pop_this_empire0 = cur.execute('select POP from EMPIRES where ID = ?', (this_empire_id,))
        pop_this_empire_unstripped = pop_this_empire0.fetchall()
        pop_this_empire = strip_single_naked(pop_this_empire_unstripped)
        if pop_this_empire == 'None' or len(pop_this_empire) == 0:
            sql_prune_empire(this_empire_id, turn)

    db_connection.commit()
    cur.close()


# (Xqhare): Basically the real main function; if you want to do anything major per turn do it here NOT in empire_interaction
def sql_populate_story(num_empires: int, num_turns: int, num_actions: int):
    sql_populate_database(num_empires, 1)
    turn_count = 1
    action_count = 1
    for n in range(num_turns):
        for t in range(num_actions):
            gen_empire_interaction(turn_count)
            print(f'{turn_count} : INTERACTION')

            action_count += 1

        sql_empire_election_cycle(turn_count)
        print(f'{turn_count} : ELECTION')
        sql_gdp_and_pop_all_town_cycle()
        print(f'{turn_count} : GDP and POP CYCLE')
        sql_trader_cycle(turn_count)
        print(f'{turn_count} : TRADER CYCLE')
        # (Xqhare): Add pruning??
        sql_empire_pruning_cycle(turn_count)
        print(f'{turn_count} : EMPIRE PRUNING CYCLE')
        turn_count += 1


def main_story(num_empires: int, num_turns: int, num_actions: int, usr_save: str):
    sql_populate_story(num_empires, num_turns, num_actions)
    cur = db_connection.cursor()
    relation_id = cur.execute('select ID from HISTORY')
    relation_id = relation_id.fetchall()

    output = []
    for relation in relation_id:
        # (Xqhare): Fetching data from database
        this_id0 = relation
        this_id = int(strip_single_naked(this_id0))

        empire_a_id = cur.execute('select EMPIRE_A_ID from HISTORY where ID = ?', (this_id,))
        empire_a_id_no = empire_a_id.fetchall()
        empire_a_id = strip_single_naked(empire_a_id_no[0])

        empire_b_id = cur.execute('select EMPIRE_B_ID from HISTORY where ID = ?', (this_id,))
        empire_b_id_no = empire_b_id.fetchall()
        empire_b_id = strip_single_naked(empire_b_id_no[0])

        this_turn = cur.execute('select TURN from HISTORY where ID = ?', (this_id,))
        this_turn_no = this_turn.fetchall()
        this_turn = strip_single_naked(this_turn_no)

        this_action_e = cur.execute('select ACTION from HISTORY where ID = ?', (this_id,))
        this_action_ts = this_action_e.fetchall()
        this_action = strip_single_naked(this_action_ts)

        empire_a_name = cur.execute('select NAME from GOVERNMENTS where EMPIRE_ID = ?', (empire_a_id,))
        empire_a_name0 = empire_a_name.fetchall()
        empire_a_name_stripped = strip_single_naked(empire_a_name0)

        empire_b_name = cur.execute('select NAME from GOVERNMENTS where EMPIRE_ID = ?', (empire_b_id,))
        empire_b_name0 = empire_b_name.fetchall()
        empire_b_name_stripped = strip_single_naked(empire_b_name0)

        town_id = cur.execute('select TOWN_ID from HISTORY where ID = ?', (this_id,))
        town_id_no = town_id.fetchall()
        town_id = strip_single_naked(town_id_no)
        town_name_s = cur.execute('select NAME from TOWNS where ID = ?', (town_id,))
        town_name0 = town_name_s.fetchall()
        town_name = strip_single_naked(town_name0)

        town_b_ids = cur.execute('select TOWN_B_ID from HISTORY where ID = ?', (this_id,))
        town_b_id_no = town_b_ids.fetchall()
        town_b_id = strip_single_naked(town_b_id_no)
        town_b_name_s = cur.execute('select NAME from TOWNS where ID = ?', (town_b_id,))
        town_b_name0 = town_b_name_s.fetchall()
        town_b_name = strip_single_naked(town_b_name0)

        char_a_id = cur.execute('select CHAR_A_ID from HISTORY where ID = ?', (this_id,))
        char_a_id0 = char_a_id.fetchall()
        char_a_id_stripped = strip_single_naked(char_a_id0)
        char_a_name = cur.execute('select NAME from CHARACTERS where ID = ?', (char_a_id_stripped,))
        char_a_name0 = char_a_name.fetchall()
        char_a_name_stripped = strip_single_naked(char_a_name0)
        char_a_title = cur.execute('select TITLE from CHARACTERS where ID = ?', (char_a_id_stripped,))
        char_a_title0 = char_a_title.fetchall()
        char_a_title_stripped = strip_single_naked(char_a_title0)
        char_a_trait = cur.execute('select TRAIT from CHARACTERS where ID = ?', (char_a_id_stripped,))
        char_a_trait0 = char_a_trait.fetchall()
        char_a_trait_stripped = strip_single_naked(char_a_trait0)

        """char_b_id = cur.execute('select CHAR_B_ID from HISTORY where ID = ?', (this_id,))
        char_b_id0 = char_b_id.fetchall()
        char_b_id_stripped = int(strip_single_naked(char_b_id0))
        char_b_name = cur.execute('select NAME from CHARACTERS where ID = ?', (char_b_id_stripped,))
        char_b_name0 = char_b_name.fetchall()
        char_b_name_stripped = str(strip_single_naked(char_b_name0))
        char_b_title = cur.execute('select TITLE from CHARACTERS where ID = ?', (char_b_id_stripped,))
        char_b_title0 = char_b_title.fetchall()
        char_b_title_stripped = str(strip_single_naked(char_b_title0))
        char_b_trait = cur.execute('select TRAIT from CHARACTERS where ID = ?', (char_b_id_stripped,))
        char_b_trait0 = char_b_trait.fetchall()
        char_b_trait_stripped = str(strip_single_naked(char_b_trait0))"""

        """# (Xqhare): DEBUG
        debug = str(strip_single_naked(town_name))
        print(debug)"""
        # (Xqhare): Comprehensive list of possible actions:
        # settle, had parade on, attack, ally, destroyed, developed technologies, visited, was elected, built road, connected by road to,
        # funded trader, trader continued to, retired in
        # (Xqhare): TODO : not implemented yet:
        match this_action:
            case "settle":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " ",
                          str(town_name)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "had a parade in":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " ",
                          str(town_name)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "attack":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " ",
                          str(empire_b_name_stripped), " and annexed ",
                          str(town_name)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "ally":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " ",
                          str(empire_b_name_stripped)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "destroyed":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " by ",
                          str(empire_b_name_stripped)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "developed technologies":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "visited":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(empire_a_name_stripped), " ",
                          str(this_action), " ",
                          str(empire_b_name_stripped)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "was elected":
                list_a = ["On Turn ", str(this_turn), " : ",
                          str(char_a_name_stripped), ", known to be ",
                          str(char_a_trait_stripped), ", ",
                          str(this_action), " ",
                          str(char_a_title_stripped), " of the ",
                          str(empire_a_name_stripped)]
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "connected by road to":
                inc_output = f'On Turn {this_turn} : In the {empire_a_name_stripped}, {town_name} was {this_action} {town_b_name}'
                output.append(inc_output)
            case "built road":
                inc_output = f'On Turn {this_turn} : In the {empire_a_name_stripped}, in {town_name} a new road was built.'
                output.append(inc_output)
            case "funded trader":
                inc_output = f'On Turn {this_turn} : In the {empire_a_name_stripped} a trader called {char_a_name_stripped} received funding ' \
                             f'for an trade-expedition, starting in {town_name}.'
                output.append(inc_output)
            case "trader continued to":
                inc_output = f'On Turn {this_turn} : {char_a_name_stripped}, a trader, continued onwards to {town_name}'
                output.append(inc_output)
            case "retired in":
                inc_output = f'On Turn {this_turn} : {char_a_name_stripped}, {this_action}, {town_name}. ' \
                             f'Their former profession was {char_a_title_stripped}'
                output.append(inc_output)
            case _:
                # (Xqhare): ALSO UPDATE POSSIBLE INTERACTION LIST ABOVE DUMMY
                print(f"Error - SQL.2, :{this_action}: has no decoding case!")
    cur.close()

    # (Xqhare): This deletes the database for an easy and clean reset
    match usr_save:
        case "Yes":
            if os.path.exists('Savedstory.db') == 1:
                os.remove('Savedstory.db')
            os.rename('Storygen.db', 'Savedstory.db')
            # (Xqhare): Debug
            print("Database saved")
        case _:
            os.remove('Storygen.db')
            # (Xqhare): Debug
            print("Database deleted")
    return output
