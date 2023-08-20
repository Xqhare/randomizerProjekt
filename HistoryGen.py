import os
import sqlite3
import random

import HistoryTooling as Tool
import HistoryFactories as Factory
import HistoryInteraction as Action
import HistoryMappers as Mapper
import PeopleNameGen
# (Xqhare): NOTE: This refactor is achieved with AI. Let's see how it goes!


def startup_sql_db():
    """
    Deletes old db if present and creates a new one with empty tables.

    Returns:
        The db_connection
    """
    if os.path.exists('History.db') == 1:
        os.remove('History.db')
    db_connection = sqlite3.connect('History.db')
    print("Database created")

    # (Xqhare): Table creation
    # (Xqhare): Empire Table with linking ID's
    emp_table_name = "empires"
    emp_columns = ("id integer PRIMARY KEY, name text, leader_id int, language_id int, pop int, area int, currency_id int, government_id int, "
                   "mil_tech int, dip_tech int, soc_tech int, capitol_id int")
    Factory.sql_create_table(emp_table_name, emp_columns, db_connection)

    # (Xqhare): Government Table with linking ID's
    gov_table_name = "governments"
    gov_columns = ("id integer PRIMARY KEY, name text, empire_id int, type int, leader_id int, leader_title text, full_title text, name_short text,"
                   "legislative_term int, rep_or_state text, next_election_turn int, capitol_id int")
    Factory.sql_create_table(gov_table_name, gov_columns, db_connection)

    # (Xqhare): Leader Table with linking ID's
    char_table_name = "characters"
    char_columns = ("id integer PRIMARY KEY, name text, title text, language_id int, government_id int, town_id int, trait text, born_turn int,"
                    "ruler int")
    Factory.sql_create_table(char_table_name, char_columns, db_connection)

    # (Xqhare): Trader table
    trader_table_name = "traders"
    trader_columns = "id integer PRIMARY KEY, character_id int, trade_factor real, end_turn int, current_town_id int, empire_id int, pruned int"
    Factory.sql_create_table(trader_table_name, trader_columns, db_connection)

    # (Xqhare): Language Table with linking ID's
    language_table_name = "languages"
    language_columns = "id integer PRIMARY KEY, name text, empire_id int"
    Factory.sql_create_table(language_table_name, language_columns, db_connection)

    # (Xqhare): Currency Table with linking ID's
    currency_table_name = "currencys"
    currency_columns = "id integer PRIMARY KEY, name text, empire_id int"
    Factory.sql_create_table(currency_table_name, currency_columns, db_connection)

    # (Xqhare): History table
    history_table_name = "history"
    history_columns = ("id integer PRIMARY KEY, turn int, empire_a_id int, action text, empire_b_id int, town_a_id int, town_b_id int, char_a_id int,"
                       "char_b_id int, op_name text")
    Factory.sql_create_table(history_table_name, history_columns, db_connection)

    # (Xqhare): Empire relations table
    emp_relation_table_name = "empire_allies"
    emp_relation_columns = "empire_id integer PRIMARY KEY, ally_id int"
    Factory.sql_create_table(emp_relation_table_name, emp_relation_columns, db_connection)

    # (Xqhare): Towns table
    towns_table_name = "towns"
    towns_columns = ("id integer PRIMARY KEY, name text, empire_id int, capitol int, pop int, gdp int, settle_date int, mayor_char_id int,"
                     "river_id int, major_trade_good text, major_trade_good_price real")
    Factory.sql_create_table(towns_table_name, towns_columns, db_connection)

    # (Xqhare): Roads table
    roads_table_name = "roads"
    roads_columns = "id integer PRIMARY KEY, road_id int, turn int, empire_a_id int, town_id int"
    Factory.sql_create_table(roads_table_name, roads_columns, db_connection)

    # (Xqhare): Rivers table
    rivers_table_name = "rivers"
    rivers_columns = "id integer PRIMARY KEY, name text, flows_into int, empire_a_id int, empire_b_id int"
    Factory.sql_create_table(rivers_table_name, rivers_columns, db_connection)

    # (Xqhare): Regions table
    regions_table_name = "regions"
    regions_columns = "id integer PRIMARY KEY, name text, empire_id int, town_a_id int, town_b_id int, town_c_id int, river_id int, area int"
    Factory.sql_create_table(regions_table_name, regions_columns, db_connection)

    print("Database tables created")

    return db_connection


# (Xqhare): Populate-functions
def sql_populate_database(n: int, turn, db_connection):
    """
    Populates the database with n entries
    :param: n the number of entries to be generated
    """
    for n in range(n):
        Factory.sql_create_empire(turn, db_connection)


# (Xqhare): Basically the real main function; if you want to do anything major per turn do it here NOT in empire_interaction
def sql_populate_story(db_connection, num_empires: int, num_turns: int, num_actions: int):
    sql_populate_database(num_empires, 1, db_connection)
    history_generation_cycle(num_turns, num_actions, db_connection)


# (Xqhare): Sql cycles:
def history_generation_cycle(num_turns, num_actions, db_connection):
    turn_count = 1
    action_count = 1
    for n in range(num_turns):
        for t in range(num_actions):
            history_action_cycle(turn_count, db_connection)
            action_count += 1

        history_turn_cycle(turn_count, db_connection)
        turn_count += 1


def history_action_cycle(turn_count, db_connection):
    Action.gen_empire_interaction(turn_count, db_connection)
    print(f'{turn_count} : INTERACTION')
    # (Xqhare): Add pruning??
    sql_empire_pruning_cycle(turn_count, db_connection)
    print(f'{turn_count} : EMPIRE PRUNING CYCLE')


# (Xqhare): This needs 0.8550 s!!!!
# (Xqhare): DONE: Optimize this shit! URGENTLY -> execution time of entire program dropped from ~70s to ~20s
# (Xqhare): TODO: Optimize election and trader.
def history_turn_cycle(turn_count, db_connection):
    # (Xqhare): A absolute performance menace: severity 2
    sql_empire_election_cycle(turn_count, db_connection)
    print(f'{turn_count} : ELECTION')
    # (Xqhare): Still a performance menace: severity 10 -> Now fixed with sql optimization!!!
    sql_gdp_and_pop_all_town_cycle(db_connection)
    print(f'{turn_count} : GDP and POP CYCLE')
    # (Xqhare): performance menace: severity 5
    sql_trader_cycle(turn_count, db_connection)
    print(f'{turn_count} : TRADER CYCLE')


# (Xqhare): timed at 0.0001 s
def sql_empire_pruning_cycle(turn: int, db_connection):
    all_empire_ids = Tool.sql_select_all_id('empires', db_connection)
    for empire_id in all_empire_ids:
        this_empire_id = int(Tool.strip_single_naked(empire_id))
        pop_this_empire_unstripped = Tool.sql_select_from_where('pop', 'empires', 'id', this_empire_id, db_connection)
        pop_this_empire = Tool.strip_single_naked(pop_this_empire_unstripped)
        if pop_this_empire == 'None' or len(pop_this_empire) == 0:
            Tool.sql_prune_empire(this_empire_id, turn, db_connection)


# (Xqhare): timed at 0.8931 s
# (Xqhare): NOW at   0.1983 s!!!!
@Tool.timeit
def sql_gdp_and_pop_all_town_cycle(db_connection):
    """
    Calculates population and GDP in all towns and updates the database accordingly.
    Pop growth is also implemented here!
    GDP is also raised here!
    Args:
        db_connection: The database connection
    """

    cur = db_connection.cursor()
    query_test = cur.execute('select id, gdp, major_trade_good_price, pop from towns order by id')
    query = query_test.fetchall()
    # (Xqhare): print(f'TEST {query}')
    for town in query:

        this_id, this_gdp, this_trade_price, this_pop = town
        # (Xqhare): print(f'test2 {this_id}: {this_gdp}: {this_pop}')

        new_gdp = round(this_gdp + ((this_gdp / 100) * (this_trade_price / 100)))

        growth_rate_offset = random.uniform(0.01, 0.04)
        growth_rate = growth_rate_offset * (this_gdp / 100)
        new_pop = round(this_pop + growth_rate)

        cur.execute('update towns set pop = ?, gdp = ? where id = ?', (new_pop, new_gdp, this_id))
        db_connection.commit()

    cur.close()


# (Xqhare): timed at 0.0002 s
def sql_empire_election_cycle(turn, db_connection):
    turn_stripped = int(Tool.strip_single_naked(turn))

    all_empire_id = Tool.sql_select_all_id('empires', db_connection)

    for entry in all_empire_id:
        emp_id = int(Tool.strip_single_naked(entry))
        next_election = Tool.sql_select_from_where('next_election_turn', 'governments', 'id', emp_id, db_connection)
        next_election_stripped = int(Tool.strip_single_naked(next_election))

        test_turn = Tool.sql_select_from_where_and('turn', 'history', 'empire_a_id', emp_id, 'action', 'was elected', db_connection)
        test_turn_stripped = Tool.strip_single_naked(test_turn)

        # (Xqhare): Test if it is election time and if an election has been held this turn for this empire.
        if turn_stripped == next_election_stripped and test_turn_stripped != turn_stripped:

            title = Tool.sql_select_from_where('leader_title', 'governments', 'id', emp_id, db_connection)
            title_stripped = Tool.strip_single_naked(title)

            leader_id_rowcount = Tool.sql_table_next_id(db_connection, 'characters')
            leader_name = PeopleNameGen.sticher_legal_name()
            leg_term = Tool.sql_select_from_where('legislative_term', 'governments', 'id', emp_id, db_connection)
            leg_term_stripped = int(Tool.strip_single_naked(leg_term))
            language_id = Tool.sql_select_from_where('language_id', 'empires', 'id', emp_id, db_connection)
            government_id = Tool.sql_select_from_where('government_id', 'empires', 'id', emp_id, db_connection)
            new_election_turn = (turn_stripped + leg_term_stripped)
            leader_trait = PeopleNameGen.gen_trait()

            history_id_rowcount = Tool.sql_table_next_id(db_connection, 'history')
            action = "was elected"
            ruler = 1

            Tool.sql_update_table_where('governments', 'leader_id', leader_id_rowcount, 'id', emp_id, db_connection)
            Tool.sql_update_table_where('governments', 'next_election_turn', new_election_turn, 'id', emp_id, db_connection)
            Tool.sql_update_table_where('empires', 'leader_id', leader_id_rowcount, 'id', emp_id, db_connection)

            character_mapper = Mapper.CharacterMapper(db_connection)
            character_mapper.insert(leader_id_rowcount, leader_name, title_stripped, int(Tool.strip_single_naked(language_id)), leader_trait, turn_stripped,
                                    ruler, int(Tool.strip_single_naked(government_id)))

            history_mapper = Mapper.HistoryMapper(db_connection)
            history_mapper.insert(history_id_rowcount, turn_stripped, action, emp_id, char_a_id=leader_id_rowcount)


# (Xqhare): timed at 0.4065 s
def sql_trader_cycle(turn, db_connection):

    all_trader_id = Tool.sql_select_from_where('id', 'traders', 'pruned', 0, db_connection)

    if len(all_trader_id) > 0:
        pass
    for entry in all_trader_id:
        trader_id = int(Tool.strip_single_naked(entry))

        this_town_unstripped = Tool.sql_select_from_where('current_town_id', 'traders', 'id', trader_id, db_connection)
        this_town = int(Tool.strip_single_naked(this_town_unstripped))

        trade_factor_unstripped = Tool.sql_select_from_where('trade_factor', 'traders', 'id', trader_id, db_connection)
        trade_factor = float(Tool.strip_single_naked(trade_factor_unstripped))

        road_id_unstripped = Tool.sql_select_from_where('road_id', 'roads', 'town_id', this_town, db_connection)
        road_id = random.choice(road_id_unstripped)
        selected_road_id = Tool.strip_single_naked(road_id)

        trader_char_id_unstripped = Tool.sql_select_from_where('character_id', 'traders', 'id', trader_id, db_connection)
        trader_char_id = int(Tool.strip_single_naked(trader_char_id_unstripped))

        # (Xqhare): DONE: Rework when economy system done
        gdp_this_town_unstripped = Tool.sql_select_from_where('gdp', 'towns', 'id', this_town, db_connection)

        gdp_this_town = int(Tool.strip_single_naked(gdp_this_town_unstripped))

        trade_good_price_unstripped = Tool.sql_select_from_where('major_trade_good_price', 'towns', 'id', this_town, db_connection)
        trade_good_price = float(Tool.strip_single_naked(trade_good_price_unstripped))

        final_trade_factor = trade_good_price * trade_factor
        new_gdp = round(gdp_this_town + ((gdp_this_town / 100) * final_trade_factor))

        Tool.sql_update_table_where('towns', 'gdp', new_gdp, 'id', this_town, db_connection)

        list_of_all_towns_on_road = Tool.sql_select_from_where('town_id', 'roads', 'road_id', selected_road_id, db_connection)
        search_list = [x for x, in list_of_all_towns_on_road]

        first_test_town = Tool.next_or_previous(search_list, this_town, direction='next')
        if first_test_town is None:
            test_next_town = Tool.next_or_previous(search_list, this_town, direction='previous')
        else:
            test_next_town = first_test_town

        if test_next_town is not None:
            chosen_next_town = test_next_town
        else:
            chosen_next_town = this_town
        # (Xqhare): Trader death check!
        death_check_unstripped = Tool.sql_select_from_where('end_turn', 'traders', 'id', trader_id, db_connection)
        death_check = int(Tool.strip_single_naked(death_check_unstripped))
        if death_check == turn:
            Tool.sql_update_table_where('traders', 'pruned', 1, 'id', trader_id, db_connection)
            # (Xqhare): HISTORY: Trader xx retired in xy
            action = "retired in"
            history_id_rowcount = Tool.sql_table_next_id(db_connection, 'history')

            history_mapper = Mapper.HistoryMapper(db_connection)
            history_mapper.insert(history_id_rowcount, turn, action, town_a_id=this_town, char_a_id=trader_char_id)

        else:
            Tool.sql_update_table_where('traders', 'current_town_id', chosen_next_town, 'id', trader_id, db_connection)
            # (Xqhare): HISTORY: Trader xx continued on to yx
            action = "trader continued to"
            history_id_rowcount = Tool.sql_table_next_id(db_connection, 'history')

            history_mapper = Mapper.HistoryMapper(db_connection)
            history_mapper.insert(history_id_rowcount, turn, action, town_a_id=this_town, char_a_id=trader_char_id, town_b_id=chosen_next_town)


# (Xqhare): Official main function, handling startup and saving
@Tool.timeit
def main(num_empires, num_turns, num_actions, usr_save):
    db_connection = startup_sql_db()
    sql_populate_story(db_connection, num_empires, num_turns, num_actions)

    relation_id = Tool.sql_select_all_id('history', db_connection)

    output = []
    for relation in relation_id:
        # (Xqhare): Fetching data from database
        this_id0 = relation
        this_id = int(Tool.strip_single_naked(this_id0))

        empire_a_id_no = Tool.sql_select_from_where('empire_a_id', 'history', 'id', this_id, db_connection)
        empire_a_id = Tool.strip_single_naked(empire_a_id_no[0])

        empire_b_id_no = Tool.sql_select_from_where('empire_b_id', 'history', 'id', this_id, db_connection)
        empire_b_id = Tool.strip_single_naked(empire_b_id_no[0])

        this_turn_no = Tool.sql_select_from_where('turn', 'history', 'id', this_id, db_connection)
        this_turn = Tool.strip_single_naked(this_turn_no)

        this_action_ts = Tool.sql_select_from_where('action', 'history', 'id', this_id, db_connection)
        this_action = Tool.strip_single_naked(this_action_ts)

        town_id_no = Tool.sql_select_from_where('town_a_id', 'history', 'id', this_id, db_connection)
        town_id = Tool.strip_single_naked(town_id_no)

        town_b_id_no = Tool.sql_select_from_where('town_b_id', 'history', 'id', this_id, db_connection)
        town_b_id = Tool.strip_single_naked(town_b_id_no)

        empire_a_name0 = Tool.sql_select_from_where('name', 'governments', 'empire_id', empire_a_id, db_connection)
        empire_a_name_stripped = Tool.strip_single_naked(empire_a_name0)

        empire_b_name0 = Tool.sql_select_from_where('name', 'governments', 'empire_id', empire_b_id, db_connection)
        empire_b_name_stripped = Tool.strip_single_naked(empire_b_name0)

        town_name0 = Tool.sql_select_from_where('name', 'towns', 'id', town_id, db_connection)
        town_name = Tool.strip_single_naked(town_name0)

        town_b_name0 = Tool.sql_select_from_where('name', 'towns', 'id', town_b_id, db_connection)
        town_b_name = Tool.strip_single_naked(town_b_name0)

        char_a_id0 = Tool.sql_select_from_where('char_a_id', 'history', 'id', this_id, db_connection)
        char_a_id_stripped = Tool.strip_single_naked(char_a_id0)

        char_a_name0 = Tool.sql_select_from_where('name', 'characters', 'id', char_a_id_stripped, db_connection)
        char_a_name_stripped = Tool.strip_single_naked(char_a_name0)

        char_a_title0 = Tool.sql_select_from_where('title', 'characters', 'id', char_a_id_stripped, db_connection)
        char_a_title_stripped = Tool.strip_single_naked(char_a_title0)

        char_a_trait0 = Tool.sql_select_from_where('trait', 'characters', 'id', char_a_id_stripped, db_connection)
        char_a_trait_stripped = Tool.strip_single_naked(char_a_trait0)

        """
        char_b_id0 = Tool.sql_select_from_where('char_b_id', 'history', 'id', this_id, db_connection)
        char_b_id_stripped = int(strip_single_naked(char_b_id0))
        
        char_b_name0 = Tool.sql_select_from_where('name', 'characters', 'id', char_b_id_stripped, db_connection)
        char_b_name_stripped = str(strip_single_naked(char_b_name0))
        
        char_b_title0 = Tool.sql_select_from_where('title', 'characters', 'id', char_b_id_stripped, db_connection)
        char_b_title_stripped = str(strip_single_naked(char_b_title0))
        
        char_b_trait0 = Tool.sql_select_from_where('trait', 'characters', 'id', char_b_id_stripped, db_connection)
        char_b_trait_stripped = str(strip_single_naked(char_b_trait0))
        """

        # (Xqhare): Comprehensive list of possible actions:
        # settle, had parade on, attack, ally, destroyed, developed technologies, visited, was elected, built road, connected by road to,
        # funded trader, trader continued to, retired in, funded new empire
        # (Xqhare): TODO : not implemented yet:
        match this_action:
            # (Xqhare): | <- pipe needed for OR operation in match. Why? Fuck me that's why!
            case "settle" | "had a parade in":
                list_a = [f'On Turn {this_turn} : {empire_a_name_stripped} {this_action} {town_name}']
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "attack":
                list_a = [f'On Turn {this_turn} : {empire_a_name_stripped} {this_action} {empire_b_name_stripped}, and annexed {town_name}']
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "ally" | "destroyed" | "visited":
                list_a = [f'On Turn {this_turn} : {empire_a_name_stripped} {this_action} {empire_b_name_stripped}']
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "developed technologies":
                list_a = [f'On Turn {this_turn} : {empire_a_name_stripped} {this_action}']
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "was elected":
                list_a = [f'On Turn {this_turn} : '
                          f'{char_a_name_stripped}, known to be {char_a_trait_stripped}, '
                          f'{this_action} {char_a_title_stripped} of the {empire_a_name_stripped}']
                inc_output = "".join(list_a)
                output.append(inc_output)
            case "connected by road to":
                inc_output = (f'On Turn {this_turn} : '
                              f'In the {empire_a_name_stripped}, {town_name} was {this_action} {town_b_name}')
                output.append(inc_output)
            case "built road":
                inc_output = (f'On Turn {this_turn} : '
                              f'In the {empire_a_name_stripped}, in {town_name} a new road was built.')
                output.append(inc_output)
            case "funded trader":
                inc_output = (f'On Turn {this_turn} : '
                              f'In the {empire_a_name_stripped} a trader called {char_a_name_stripped} received funding '
                              f'for an trade-expedition, starting in {town_name}.')
                output.append(inc_output)
            case "trader continued to":
                inc_output = (f'On Turn {this_turn} : '
                              f'{char_a_name_stripped}, a trader, continued onwards to {town_name}')
                output.append(inc_output)
            case "retired in":
                inc_output = (f'On Turn {this_turn} : '
                              f'{char_a_name_stripped}, {this_action}, {town_name}. Their former profession was {char_a_title_stripped}')
                output.append(inc_output)
            case "funded new empire":
                inc_output = (f'On Turn {this_turn} : '
                              f'{empire_a_name_stripped} was founded with its capitol {town_name}')
                output.append(inc_output)
            case _:
                # (Xqhare): ALSO UPDATE POSSIBLE INTERACTION LIST ABOVE DUMMY
                print(f"Error - SQL.2, :{this_action}: has no decoding case!")

    # (Xqhare): This deletes the database for an easy and clean reset
    timestamp = Tool.get_timestamp("%Y-%m-%d@%H:%M:%S")
    final_filename = f'SavedHistory {timestamp}.db'
    match usr_save:
        case "Yes":
            os.rename('History.db', final_filename)
            # (Xqhare): Debug
            print("Database saved")
        case _:
            os.remove('History.db')
            # (Xqhare): Debug
            print("Database deleted")

    return output


if __name__ == "__main__":
    main(25, 50, 2, 'No')
