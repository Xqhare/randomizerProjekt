Xqhare's randomizer project 0.6.x
This is my attempt at generating "english text" in various forms.

ca 3.700 loc, las tcount dec.23

---------------------------GENERAL-DOC-------------------------
To start type in terminal: "python3 main.py"; for tester type: "python3 tester.py".

-------------------------0-Vision------------------------------
-Have a generator that returns a story
    -Have a world generator that returns a markup (think obsidian/wikipedia) folder filled with a fully generated world.

-------------------------1-General-----------------------------
- To-do list is to be emptied between large 0.x version changes
- Naming exceptions for GenLib in GenLib documentation
- Generators are split off into modules
- Decided on yaml and SQLite as data-format of choice for saving and parsing data
    - Yaml is a superset of json, has more tools, and is apparently faster
    - SQLite just works! TODD IT JUST FUCKING WORKS!! TODD!!!!!!!
- There is a very basic Error messaging system
    - The Errors are just passed along as output until they reach the user
    - Now it's not very helpful for anyone but me BUT at least it makes hunting bugs in the function-stack easier
    - They are now also printed in console!
    - BUT these Errors also don't crash the program, so it's a win in my book
        - I want to note that this system has helped several times debugging bad inputs! (granted only like twice but still)

- For future stress testing:
    - Using 500 turns with 20 interactions speeds the stress test up considerably;
    - However it still takes two hours right now - 2023-08-02@21:17:21
-------------------------2-Naming------------------------------
Class name rules
-Project unique
-CamelCaseConventionNoUnderscore

Function name rules
-Class or File unique
-completely_lower_case
-type_meaningful_return
-types: gen(erator), main, gui, maker, sticher
-eg. gen_adj() ; gui_open_placename_window

Variable name rules
-completely_lower_case
-as simple and meaningful as possible

Error-Messages
location.id
id = last error id with same location +1

-------------------------3-Error-Messages----------------------
Error - Tester.1 == Wrong string entered in tester.py generator choose interaction
Error - ShipClass.1 == Something went wrong in "gen_ship_type"'s string match; end of cases reached
Error - ShipClass.2 == Something went wrong in "gen_tech_ship_data"'s string match; end of cases reached
Error - Currency.1 == Something went wrong with the dropdown user choice decoding for decimal/non-decimal/time in "main_currency"
Error - Currency.2 == match random.choice(GenLib.currency_icon_inscription) in "gen_coin_iconography" returned not valid value
Error - Currency.3 == match random.choice(GenLib.currency_icon_figure) in "gen_coin_iconography" returned not valid value
Error - SQL.1 == unknown action was chosen in gen_empire_interaction
Error - SQL.2 == unexpected action between empires in history during decoding in main
Error - SQL.3 == unexpected government form in create_empire
Error - Number.1 == couldn't decode passed text parameter
---------------------------END-OF-DOC--------------------------



TODO: --------------------TO-DO-LIST---------------------------

TODO: --------------------General------------------------------
TODO: The codebase for HistoryGen is starting to become less performant than I'd like; it will get worse though -> I plan a lot more possible interactions, and update services!
	-> running the 5000 turns at 2 actions would take about 3.5 hours. 250 took 12min! - 2023-08-02@19:23:46
DONE: learn decorators
TODO: learn vim
TODO: Version control
TODO: Themes -> english, fantasy, all, german, dwarfen
    TODO: -> needs a full library rework
DONE: Just add yaml / sql you lazy fuck. JUST DO IT. It can't be that hard
    DONE: Turns out it is A LOT more complicated than expected
        "For device-local storage with low writer concurrency and less than a terabyte of content, SQLite is almost always a better solution.
        SQLite is fast and reliable, and it requires no configuration or maintenance. It keeps things simple. SQLite "just works"."
        IT JUST FUCKING WORKS TODD!!!!
        -> SQLite it is, thank you todd

TODO: GUI
    TODO: find a scalable solution, so it works for all resolutions

TODO: Rework Error handling with an actual (the in-build) system

TODO: --------------------Generators---------------------------
TODO: Persons physical and personality description
TODO: Artefact Personality && special abilities
TODO: Race generator
    TODO: fantasy races generator
    TODO: GUI
TODO: Metal / Alloy generator
    TODO: Very bare bones at the moment
TODO: Element Generator
    TODO: Add GUI
    TODO: Add it to MetalAlloyGen
TODO: God(s) generator
    TODO: with decoder for religion generator - e.g. one to Several gods (maybe just pass an int)
    TODO: Add GUI
    TODO: Add personality
TODO: Religion generator
    TODO: Add GUI
TODO: Magic system generator
    Todo: needs runes / ingredients / mana / life-force (from humans / animals / nature) / Gods favor
        - either exclusively or even together;
        - Sometimes they are required, or they are optional for better / faster casting
TODO: magic spell generator
    TODO: standalone and with passed in magic system rules
    TODO: Add GUI
TODO: pet generator
    TODO: Library entry for animals
    TODO: Add age?
    TODO: Add gender
    TODO: Add GUI
    TODO: Add physical description
    TODO: Add personality descriptor
        -> 1-3 personality types: loyal, playful, hungry , disloyal, intelligent, dumb, active, passive, outgoing, shy, loud, quiet
TODO: life / RP / cv generator - deeper PeopleName
    TODO: Add GUI
TODO: Drink / Potion generator
    TODO: Add GUI
TODO: Technology generator
    TODO: Add GUI
TODO: Planet generator
    TODO: Add GUI
TODO: Star-system generator
    TODO: Add GUI
TODO: Star-sector generator
    TODO: Add GUI
TODO: Story generator
    TODO: Deepen it
        TODO: Regions needs a owner refresh after conquest
            -> Regions isn't set up to handle what i ask of it
        TODO: rise of new empires
            TODO: -> A splinter of an existing Empire; taking with it a few regions
                    -> Do with revolutions together; -> disenfranchisement could be a good value for these
            DONE: -> formation in the unclaimed lands
        TODO: revolutions and reformations in empires
        TODO: Have an actual war state; with military campaign -> following the roads
        TODO: Navy; first for rivers then add larger bodies of water
        TODO: Diplomatic states; e.g. 'at war', 'allied', 'truce', 'good relations', 'bad relations'
            -> sliding scale from 0-1000 paradox style of dip relation with each country; start at 500, +- for different interacts; and ally, rival or war locked behind hard gates at whatever int; 350 for possible war? or even 600-750 for added realism?
        TODO: Town elections
        TODO: Use rivers for Trade
        TODO: Rework area to be like pop
        TODO: Mil rework -> actual mil numbers!
TODO: Government generator
    TODO: Government organization (Done in StoryGen)
TODO: Language generator
    TODO: Add: O(bject)V(erb)S(ubject), SVO, OSV, SOV, VOS, VSO
    TODO: generate custom endings for further generation -> -lingen and just a few others for a more "cultural feel" of the generators
TODO: Time system generator
    TODO: GUI
TODO: Symbol generator - graphic!
    TODO: Add GUI
TODO: Ship name generator
    TODO: Add Gods and planets as possibilities
    TODO: Make ship_long_name less shit (only 2 entries)
TODO: Custom Ship maker - normal / space - civ / mil
    TODO: Add GUI
TODO: Make Scene less shit
TODO: Have TimeGen have the same unified output as the rest
    TODO: OR Have all generators have a different unified output
TODO: Timeline: gen a list of actors, choose from them at random for tasks in timeline -> factions!
    TODO: Timeline: use more verbs like attack, defend, allie, rival

TODO: --------------------Main-Tester-Library------------------
TODO: Make the quotes randomized
TODO: replace GenLib with a yaml file and parser - maybe yaml for the generators?
TODO: For Themes, and better output control, split all comp components into more entries in the library
TODO: Add a runtime output in ms to Test.py

----General-Notes----

---Useful stuff:
https://www.inf-schule.de/software/gui/entwicklung_tkinter/layout/pack
https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.

JUST USE DJANGO!!!!!!!

--- GUI Framework for browsers:
https://justpy.io/
    -> already installed on home

--- Python in Html Framework:
https://www.digi.com/resources/documentation/digidocs/90001537/references/r_python_inside_html.htm?TocPath=Categories%7CWeb%20Access%7C_____2

--- Python easy web portal:
https://github.com/rawpython/remi


---For Documentation:
"""
Sample explanation of the function

Args:
    param: The list of elements.
    variable: The variable
    direction: The direction

Returns:
    None
"""
