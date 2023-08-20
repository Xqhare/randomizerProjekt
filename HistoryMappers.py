# (Xqhare): Mapper Classes:
class LanguageMapper(object):
    """A data mapper for the languages table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, language_id, language_name, empire_id):
        """Insert a new language into the database."""
        query = "insert into languages (id, name, empire_id) values(?, ?, ?)"
        cur = self.db_connection.cursor()
        cur.execute(query, (language_id, language_name, empire_id))
        self.db_connection.commit()
        cur.close()


class CurrencyMapper(object):
    """A data mapper for the currencys table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, currency_id, currency_name, empire_id):
        """Insert a new currency into the database."""
        query = "insert into currencys (id, name, empire_id) values(?, ?, ?)"
        cur = self.db_connection.cursor()
        cur.execute(query, (currency_id, currency_name, empire_id))
        self.db_connection.commit()
        cur.close()


class GovernmentMapper(object):
    """A data mapper for the governments table. This time written by me!"""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, government_id, government_name, empire_id, gov_type, leader_id, leader_title, full_title, government_short_name, legislative_term,
               rep_or_state, first_election):
        cur = self.db_connection.cursor()
        query = ("insert into governments "
                 "(id, name, empire_id, type, leader_id, leader_title, full_title, name_short, legislative_term, rep_or_state, next_election_turn)"
                 "values(?,?,?,?,?,?,?,?,?,?,?)")
        cur.execute(query, (government_id, government_name, empire_id, gov_type, leader_id, leader_title, full_title, government_short_name, legislative_term,
                            rep_or_state, first_election))
        self.db_connection.commit()
        cur.close()


# (Xqhare): language_id, government_id, town_id, trait,
class CharacterMapper(object):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, leader_id: int, leader_name: str, leader_title: str, language_id: int, leader_trait: str, turn: int, ruler: int, government_id=0,
               town_id=0):
        cur = self.db_connection.cursor()
        query = ("insert into characters (id, name, title, language_id, government_id, town_id, trait, born_turn, ruler)"
                 "values(?,?,?,?,?,?,?,?,?)")
        cur.execute(query, (leader_id, leader_name, leader_title, language_id, government_id, town_id, leader_trait, turn, ruler))
        self.db_connection.commit()
        cur.close()


class EmpireMapper(object):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, empire_id, empire_name, leader_id, language_id, empire_pop, empire_area, currency_id, government_id, mil_tech, dip_tech,
               soc_tech):
        cur = self.db_connection.cursor()
        query = ("insert into empires (id, name, leader_id, language_id, pop, area, currency_id, government_id, mil_tech, dip_tech, soc_tech)"
                 "values(?,?,?,?,?,?,?,?,?,?,?)")
        cur.execute(query, (empire_id, empire_name, leader_id, language_id, empire_pop, empire_area, currency_id, government_id, mil_tech, dip_tech,
                            soc_tech))
        self.db_connection.commit()
        cur.close()


# (Xqhare): New hot different version of making a mapper by Bard: I like it!
class TownMapper(object):
    """A data mapper for the towns table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, town_id, town_name, capitol, town_pop, town_gdp, empire_id, turn, mayor_char_id, river_id, trade_good, trade_good_price):
        """Insert a new town into the database."""
        data = {
            'id': town_id,
            'name': town_name,
            'capitol': capitol,
            'pop': town_pop,
            'gdp': town_gdp,
            'empire_id': empire_id,
            'settle_date': turn,
            'mayor_char_id': mayor_char_id,
            'river_id': river_id,
            'major_trade_good': trade_good,
            'major_trade_good_price': trade_good_price,
        }

        query = ('insert into towns (id, name, capitol, pop, gdp, empire_id, settle_date, mayor_char_id, river_id, major_trade_good, major_trade_good_price)'
                 'values(:id, :name, :capitol, :pop, :gdp, :empire_id, :settle_date, :mayor_char_id, :river_id, :major_trade_good, :major_trade_good_price)')
        cur = self.db_connection.cursor()
        cur.execute(query, data)
        self.db_connection.commit()
        cur.close()


# (Xqhare): Thankfully Bard returns a lot of different kinds of code; didn't know you could write a comment that way
class HistoryMapper(object):
    """A data mapper for the history table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, history_id_rowcount, turn, action, empire_a_id=0, empire_b_id=0, town_a_id=0, town_b_id=0, char_a_id=0, char_b_id=0, op_name='None'):
        """
        Inserts a new history entry into the database.

        Args:
            history_id_rowcount: The ID of the newly created history entry.
            turn: The current turn number.
            action: The type of action that was performed.
            empire_a_id: The ID of the empire that performed the action.
            empire_b_id: The ID of the empire that was affected by the action, if any.
            town_a_id: The ID of the town that was affected by the action, if any.
            town_b_id: The ID of the town that was affected by the action, if any.
            char_a_id: The ID of the character that performed the action, if any.
            char_b_id: The ID of the character that was affected by the action, if any.
            op_name: The name of the operation that was performed.
        """
        data = {
            'ID': history_id_rowcount,
            'TURN': turn,
            'EMPIRE_A_ID': empire_a_id,
            'ACTION': action,
            'EMPIRE_B_ID': empire_b_id,
            'TOWN_A_ID': town_a_id,
            'TOWN_B_ID': town_b_id,
            'CHAR_A_ID': char_a_id,
            'CHAR_B_ID': char_b_id,
            'OP_NAME': op_name
        }

        query = ('insert into HISTORY (ID, TURN, EMPIRE_A_ID, ACTION, EMPIRE_B_ID, TOWN_A_ID, TOWN_B_ID, CHAR_A_ID, CHAR_B_ID, OP_NAME) '
                 'values(:ID, :TURN, :EMPIRE_A_ID, :ACTION, :EMPIRE_B_ID, :TOWN_A_ID, :TOWN_B_ID, :CHAR_A_ID, :CHAR_B_ID, :OP_NAME)')
        cur = self.db_connection.cursor()
        cur.execute(query, data)
        self.db_connection.commit()
        cur.close()


class RoadMapper(object):
    """A data mapper for the roads table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, road_rowcount, road_id, turn, empire_a_id, town_id):
        """Inserts a new road into the database."""
        data = {
            'ID': road_rowcount,
            'ROAD_ID': road_id,
            'TURN': turn,
            'EMPIRE_A_ID': empire_a_id,
            'TOWN_ID': town_id,
        }

        query = 'insert into ROADS (ID, ROAD_ID, TURN, EMPIRE_A_ID, TOWN_ID) values(:ID, :ROAD_ID, :TURN, :EMPIRE_A_ID, :TOWN_ID)'
        cur = self.db_connection.cursor()
        cur.execute(query, data)
        self.db_connection.commit()
        cur.close()


class RegionsMapper(object):
    """A data mapper for the regions table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, region_id, region_name, empire_id, river_id, town_a_id, town_b_id=0, town_c_id=0, area=0):
        """Inserts a new region into the database."""
        data = {
            'ID': region_id,
            'NAME': region_name,
            'EMPIRE_ID': empire_id,
            'RIVER_ID': river_id,
            'TOWN_A_ID': town_a_id,
            'TOWN_B_ID': town_b_id,
            'TOWN_C_ID': town_c_id,
            'AREA': area
        }

        query = ('insert into regions (id, name, empire_id, river_id, town_a_id, town_b_id, town_c_id, area) values(:ID, :NAME, :EMPIRE_ID, :RIVER_ID, '
                 ':TOWN_A_ID, :TOWN_B_ID, :TOWN_C_ID, :AREA)')
        cur = self.db_connection.cursor()
        cur.execute(query, data)
        self.db_connection.commit()
        cur.close()


class RiverMapper(object):
    """A data mapper for the rivers table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, river_id_rowcount, river_name, empire_a_id, flows_into=0, empire_b_id=0):
        """Inserts a new river into the database.

            Args:
                river_id_rowcount: The ID of the newly created history entry.
                river_name: The current turn number.
                empire_a_id: The ID of the empire.
                flows_into: The ID of the body of water the river flows into.
                empire_b_id: The ID of the second empire within this region.

        """
        data = {
            'ID': river_id_rowcount,
            'NAME': river_name,
            'EMPIRE_A_ID': empire_a_id,
            'FLOWS_INTO': flows_into,
            'EMPIRE_B_ID': empire_b_id
        }

        query = 'insert into rivers (id, name, flows_into, empire_a_id, empire_b_id) values(:ID, :NAME, :FLOWS_INTO, :EMPIRE_A_ID, :EMPIRE_B_ID)'
        cur = self.db_connection.cursor()
        cur.execute(query, data)
        self.db_connection.commit()
        cur.close()


class EmpireAlliesMapper(object):
    """A data mapper for the empire_allies table."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, empire_a_id, empire_b_id):
        """Insert a new currency into the database."""
        query = "insert into empire_allies (empire_id, ally_id) values(?, ?)"
        cur = self.db_connection.cursor()
        cur.execute(query, (empire_a_id, empire_b_id))
        self.db_connection.commit()
        cur.close()


class TraderMapper(object):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, trader_id, character_id, trade_factor, end_turn, starting_town_id, empire_id, pruned):
        query = "insert into traders (id, character_id, trade_factor, end_turn, current_town_id, empire_id, pruned) values(?,?,?,?,?,?,?)"
        cur = self.db_connection.cursor()
        cur.execute(query, (trader_id, character_id, trade_factor, end_turn, starting_town_id, empire_id, pruned))
        self.db_connection.commit()
        cur.close()
