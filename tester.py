import CurrencyGen
import EmpireGen
import GovernmentGen
import LanguageGen
import MetalAlloyGen
import HistoryTooling
import PlaceNameGen
import PeopleNameGen
import ArtifactGen
import SceneGen
import ShipClassGen
import ShipNameGen
import HistoryGen
import TimeGen
import OperationGen
# (Xqhare): DOC: Error code 1 == input not valid - as in: not "pl" but "place" or "lp" was input
# (Xqhare): Fun-fact: This file is a literal zombie of an old main.py version
# (Xqhare): And it is the oldest file with the fewest reworks!

ui_input = input("Please choose the generator; Place[pl], People[pe], "
                 "Artifact[a], Scene[s], Timeline[ti], Operations[op], Ship Names[sn], Ship Classes[sc], MetalAlloy[ma], Currency[c], "
                 "Government[gov], Language[l], Empire[em], Test[t][t2]: ")
match ui_input:
    case "pl":
        pl_length = int(input("Please enter a number of places to be generated."))
        for x in range(pl_length):
            print(PlaceNameGen.main_place_name())
    case "s":
        s_length = int(input("Please enter a number of scenes to be generated."))
        for x in range(s_length):
            print(SceneGen.main_scene())
    case "pe":
        pe_length = int(input("Please enter a number of people to be generated."))
        for x in range(pe_length):
            print(PeopleNameGen.main_generated_person())
    case "a":
        a_length = int(input("Please enter a number of artifacts to be generated."))
        for x in range(a_length):
            print(ArtifactGen.main_artifact())
    case "ti":
        ti_length = int(input("Please enter a number of events to be generated."))
        ti_year0 = int(input("Please provide a start year."))
        ti_year1 = int(input("Please provide a end year."))
        print(TimeGen.main_timeline(ti_year0, ti_year1, ti_length))
    case "op":
        pe_length = int(input("Please enter a number of operations to be generated."))
        for x in range(pe_length):
            print(OperationGen.main_operation_name())
    case "sn":
        pe_length = int(input("Please enter a number of ship names to be generated."))
        prefix = str(input("Please enter a prefix; For empty put space, if left empty it returns a random prefix."))
        for x in range(pe_length):
            print(ShipNameGen.main_ship_name(prefix))
    case "sc":
        pe_length = int(input("Please enter a number of ship classes to be generated."))
        size = str(input("enter size"))
        speed = int(input("enter speed"))
        avg_range = int(input("enter range"))
        for x in range(pe_length):
            print(ShipClassGen.main_ship_class(size, speed, avg_range))
    case "ma":
        pe_length = int(input("Please enter a number of Metals or Alloys to be generated."))
        for x in range(pe_length):
            print(MetalAlloyGen.main_metal_alloy())
    case "c":
        pe_length = int(input("Please enter a number of tests to be generated."))
        usr_choice = str(input("Enter Decimal; Non-Decimal; or Time based"))
        for x in range(pe_length):
            print(CurrencyGen.main_currency(usr_choice))
    case "gov":
        pe_length = int(input("Please enter a number of Governments to be generated."))
        usr_choice = str(input("Enter empire name or leave empty for random."))
        for x in range(pe_length):
            print(GovernmentGen.main_government(usr_choice))
    case "l":
        pe_length = int(input("Please enter a number of Languages to be generated."))
        for x in range(pe_length):
            print(LanguageGen.main_language())
    case "em":
        pe_length = int(input("Please enter a number of Empires to be generated."))
        for x in range(pe_length):
            print(EmpireGen.main_empire())
    case "st":
        pe_length = int(input("Please enter a number of Turns the story is to be generated with."))
        num_empires = int(input("Please enter a number of Empires to populate the world."))
        num_actions = int(input("Please enter a number of Actions you want to perform per turn."))
        str_save = str(input("Save the database? y/n"))
        if str_save == 'y':
            save = 'Yes'
        else:
            save = 'No'
        print(HistoryGen.main(num_empires, pe_length, num_actions, save))
    case "t":
        pe_length = int(input("Please enter a number of tests to be run."))
        # (Xqhare): usr_choice = str(input("enter Decimal"))
        for x in range(pe_length):
            timestamp = HistoryTooling.get_timestamp("%Y-%m-%d_%H:%M:%S")
            time_type = HistoryTooling.check_variable_type(timestamp)
            print(f'{timestamp}, {time_type}')    # (Xqhare): DON'T FORGET TO CHANGE THIS DUMDUM
    case "t2":
        pe_length = int(input("Please enter a number of tests to be run."))
        for x in range(pe_length):
            print(HistoryTooling.check_variable_type(pe_length))  # (Xqhare): DON'T FORGET TO CHANGE THIS DUMDUM
    case _:
        print(ui_input + " is not a valid query. Please type the letters in [] corresponding to your needs. " + '\n' +
              "Closing Program with: Error - Tester.1")
