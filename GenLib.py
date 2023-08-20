"""
---------------------------GenLib-DOC-------------------------
-------------------------1-General-----------------------------
- To-do list is to be emptied between large 0.x version changes
- Naming exceptions for GenLib in GenLib documentation
-------------------------2-Naming------------------------------
Class name rules
-Project unique
-CamelCaseNoUnderscore

Function name rules
-Class or File unique
-completely_lower_case
-type_meaningful_return
-types: gen(erator), main, gui, maker, sticher
-eg. gen_adj() ; gui_open_placename_window

Variable name rules
-short_gen_name_meaningful_content
-PlaceNameGen -> place etc.
-completely_lower_case
-as simple and meaningful as possible

---------------------------END-OF-DOC--------------------------
"""
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
       ]

place_relatives = ["smaller than", "larger than", "a lot larger than", "a lot smaller than"
                   ]

place_noun = ["love", "peace", "freedom", "virtue", "lust", "greed", "sin", "defensiveness", "fertility", "glory", "ruggedness", "fairness",
              "beauty", "ugliness", "quality", "style", "age", "builder", "builders", "mystique", "sanctity", "quietness", "hiddenness",
              "wideness", "obscurity", "remoteness", "secrecy", "isolation", "openness", "approachability", "unapproachability", "bigotry",
              "narrow-mindedness", "inhibition", "formality", "modesty", "coldness", "warmness", "wetness", "dryness", "normalcy", "artfulness",
              "sophistication", "cynicism", "piety", "grace", "misery", "violence", "sadness", "joy", "sorrow", "worry", "busyness", "happiness",
              "solidarity", "rebellion", "disobedience", "concealment", "cover", "protection", "safety", "surety", "covertness", "lightness",
              "darkness", "sensibility", "bluntness"
              ]

place_top_eng_nouns = ["people", "history", "way", "art", "world", "information", "map", "family", "government", "health", "meat", "music", "food",
                       "understanding", "law", "literature", "control", "knowledge", "power", "product", "temperature", "society", "industry",
                       "technology", "magic", "army", "militia", "university", "fishing", "medicine", "philosophy", "disease", "corruption"
                       ]

place_object = ["loch", "hill", "borough", "grave", "croft", "fjord", "sea", "land", "court", "way", "star", "maze", "arena", "arch", "cottage",
                "vale", "valley", "way", "bridge", "cross", "manor", "field", "lane", "wharf", "junction", "quay", "river", "city",
                "house", "castle", "mill", "mountain", "palace", "village", "town", "farm", "forrest", "mountain range", "mine", "region",
                "capitol", "fort", "river", "stream", "floodplain", "canyon", "inland sea", "ocean", "street", "alley", "crossroads", "camp",
                "dam", "hunters lodge", "lodge", "hideout", "manufactury", "town hall", "pub", "lake", "tavern", "ale house", "city hall",
                "square", "promenade", "avenue", "country house", "county", "earldom", "fiefdom", "dukedom", "wood", "reserve"
                ]

place_single = ["Fair", "Border", "Castle", "Glass", "Rock", "East", "West", "South", "North", "Strong", "Weak", "Winter", "City", "House", "Marble",
                "Summer", "Drac", "Snow", "Sand", "Wood", "Dirt", "Green", "Red", "Blue", "Yellow", "Gold", "Silver", "Witch", "New", "Queens",
                "Marsh", "Marble", "Granite", "Apple", "Cold", "Starry", "Clear", "Eri", "Deep", "Brook", "Wild", "River", "Elms", "Oval", "Quays",
                "Ricer", "Mallow", "Falcon", "Owl", "Raven", "Flower", "Bush", "Grass", "Rose", "Ice", "Crystal", "Imperial", "Wharf", "Junction",
                "Shadow", "Old", "Moor", "Park", "Hills", "Royal", "Lane", "Line", "Central", "Cross", "Manor", "Fields", "Green", "Way", "Bridge",
                "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Arch", "Cottage", "Vale", "Valley", "Bush", "Birch",
                "Asp", "Wood", "Brick", "Steel", "Star", "Maze", "Arena", "White", "Black", "Red", "Green", "Blue", "Old", "Cray", "Grey", "Cloud",
                "Sea", "Land", "Court", "Way", "Stead", "Ford", "Fjord", "Raven", "Amber", "Sand", "Rock", "Dirt", "Buck", "High", "Low", "Croft",
                "Dart", "Grave", "Wool", "Roth", "Borough", "Old", "New", "Northern", "Western", "Eastern", "East", "West", "South", "North",
                "Lower", "Middle", "Great", "Greater", "Hilly", "Flat", "Deep", "Shallow", "Royal", "Loch", "Deeper", "Kings", "Southern", "Upper"
                ]
# (Xqhare): DOC: Lists for compound names
# (Xqhare): DOC: this is the first part of the main word
general_comp0 = ["Lor", "Pry", "Ches", "Chal", "Amers", "Chorley", "Wat", "Crox", "North", "South", "East", "West", "Pin", "Har", "Icken", "Rui",
                 "Sud", "Nor", "Alper", "Han", "Dray", "Lang", "Tap", "Chis", "Stam", "Put", "Raven", "Win", "Rei", "Butt", "Wand", "Toot", "Hay",
                 "Dun", "Sut", "Cars", "Hack", "Mit", "Streat", "Brix", "Tul", "Lough", "Peck", "Syd", "Chan", "Hol", "Lan", "Mare", "Mary", "Mare",
                 "Fin", "War", "Harles", "Head", "Turn", "Asp", "High", "Low", "Hig", "Fair", "Chig", "Buck", "Lough", "They", "Epp", "Can", "Gal",
                 "Cut", "Croft", "Coom", "Orp", "Dart", "Grave", "Wool", "Roth", "Ald", "Her", "Dundon", "Crof", "Dome", "Is", "Sin", "Az", "Mok",
                 "Nem", "Nemb", "Dou", "Gam", "Norag", "Odro", "Thond", "Umit", "Za", "Alo", "Gary", "Elm", "Theo", "Kel", "Elep", "Myri", "Thy",
                 "Adore", "Jass", "Bren", "Dari", "Bran", "Moar", "Brin", "Dari", "Jere", "Rem", "Riem", "Wil", "Zan", "Full", "Ingel", "Kri", "Hart",
                 "Cris", "Del", "Gise", "Ebt", "Gis", "Lis", "Xil", "Bea", "Mae", "Hadv", "Jene", "Sae", "Jazz", "Aevan", "Mare", "Kyn", "Vies",
                 "Opal", "Olo", "Pad", "Jola", "Mag", "Iar", "Sha", "Vap", "Carm", "Neag", "Deri", "Grem", "Hei", "Yalla", "Bryx", "Wys", "Uri",
                 "Rova", "Syls", "Ina", "Qui", "Aen", "Rov", "Ili", "Adr", "Bira", "Laro", "Kaila", "Oni", "Poew", "Kedo", "Wae", "Mae", "Asoe",
                 "Osea", "Esao", "Lit", "Thy", "Alay", "Ala", "Wera", "Wers", "Thi", "Tha", "Thu", "The", "Gwei", "Adig", "Alex", "Vila", "Vile",
                 "Via", "Vie", "Viu", "Chili", "Giran", "Sevi", "Sewig", "Miro", "Mari", "Dwa", "Dwu", "Dwd", "Edria", "Proi", "Boe", "Beo", "Wef",
                 "Kedrin", "Kedira", "Toer", "Zapu", "Zau", "Agra", "Cardo", "Glau", "Barb"
                 ]
# (Xqhare): DOC: the second part of the main word
general_comp1 = ["rona", "sen", "ola", "yna", "sa", "ielle", "isa", "aril", "bra", "ren", "nel", "han", "dod", "feth", "erlum", "otir", "drolin",
                 "mal", "hra", "etelin", "bryn", "enelyn", "ehilda", "aelydd", "the", "vara", "aria", "dras", "meck", "nour", "aeth", "aeck", "mon",
                 "deck", "grick", "uki", "atir", "ion", "has", "thir", "this", "oris", "no", "roth", "ali", "nak", "raa", "driel", "deim", "uryn",
                 "ok", "red", "aze", "ard", "dan", "jan", "jorl", "rax", "don", "faelor", "duin", "rach", "parin", "lael", "uni", "odus", "up",
                 "annon", "cre", "onydd", "ynott", "arwen", "rid", "jan", "stead", "sean", "ean", "acia", "aella", "oav", "andria", "darien", "gotha",
                 "icia", "ecia", "ocia", "ucia", "ald", "hald", "owin", "gord", "awa", "vil", "hiel", "ewyr", "arian", "ham", "font", "wood", "worth",
                 "ford", "ley", "wood", "ner", "row", "rim", "cote", "cute", "lip", "eye", "toe", "nose", "finger", "arm", "leg", "head", "lingdon",
                 "don", "burry", "ton", "well", "low", "fields", "wick", "court", "way", "ney", "sea", "sons", "cham", "an", "se", "on", "de",
                 "borough", "hithe", "gate", "aster", "caster", "ware", "stead", "burn", "den", "fosters", "forrest", "plains", "ish", "pike", "lop",
                 "hurst", "ty", "horse", "end", "mill", "wynne", "beach", "shore", "rose", "wood", "wilde", "wlyn", "land", "crest", "hill",
                 "mountain", "fay", "flower", "rock", "hollow", "light", "dale", "heat", "bush", "creek", "govo", "done", "way", "mist", "field",
                 "forrest", "nesse", "stone", "apple", "loch", "vale", "dell", "bourne", "ani", "dia", "holt", "hold", "burn", "pond", "lake", "town",
                 "mallow", "hall", "house", "farm", "moor", "sage", "ham", "marble", "granite", "wolf", "wyn", "ness", "thumb", "halton", "dome"
                 ]

people_first_name = ["Paul", "Harold", "Alan", "Richard", "Alisa", "Alison", "Margaret", "James", "Susan", "Katherine", "Katie", "John", "Mark",
                     "Pfj", "Martin", "Jayne", "Steven", "Jayne", "Jorris", "Bonson", "Saul", "Kayleigh", "Barbara", "Julie", "Penny", "Kay", "Julia",
                     "Deana", "Janet", "Natalie", "Angela", "Sylvia", "June", "Rita", "Nigel", "Shaun", "Easton", "Marc", "Joseph", "Giuseppe",
                     "Emanuel", "Antonio", "Martin", "Malcom", "Ian", "John", "Juliett", "Julia", "Noah", "Muhammad", "Ahmed", "Ahmet", "Oscar",
                     "Olivia", "Amelia", "Isla", "Isia", "Ava", "Ivy", "Lily", "Mia", "Willow", "Robert", "Michael", "David", "William", "Richard",
                     "Mark", "Mary", "Patricia", "Linda", "Elizabeth", "Betty", "Sandra", "Lori", "Isawa"
                     ]

people_last_name = ["Barber", "Almond", "Dey", "Dawson", "Dixon", "Briggs", "Betts", "Chadwick", "Fowler", "Harris", "Miller", "Lamb", "Malik", "Ali",
                    "Mayhew", "McEwan", "Moore", "Tyson", "Wood", "Venn", "Tribe", "Orru", "Nnamsah", "Relzab", "Tiago", "Tucker", "Herz", "Girad",
                    "Manno", "Casi", "Fisher", "Hunter", "Baker", "Butcher", "Menninger", "Prince", "Silva", "Sarno", "Nair", "Marso", "Tatr",
                    "Loats", "Zhou", "Strauss", "Boyer", "Bower", "Viola", "Barro", "Isawa"
                    ]

people_nickname = ["Baby", "Kindle", "Big", "Dog", "Glide", "Red", "Blue", "Green", "Yellow", "Bear", "Wolf", "Hog", "Chief", "Dice", "Skin", "Bud",
                   "Slayer", "Grenade", "Axe", "Hammer", "Anvil", "Potato", "Bullet", "Dragon", "Sizzle", "Mono", "Mad dog", "Mad", "Black", "White",
                   "Gator", "Shadow", "Torch", "Compass", "Dazzle", "Candy", "Rock", "Iron", "Gem", "Diamond", "Ruby", "Sapphire", "Peanut", "Cashew",
                   "Dino", "Rogue", "Jewel", "Chipper", "Chopper", "Gutter", "Brick", "Cutie", "Belle", "Maul", "Stone", "Genius", "Rusty", "Serpent",
                   "Snake", "Gibbs", "Speedy", "Kier", "Aroz", "Harley", "Amye", "Gunther", "Nanette", "Engelbert", "Tiffie", "Athifanus", "Tiffany",
                   "Isaac", "Esmaria", "Olympe", "Bondon", "Rondon", "Tondon", "Reginald", "Baxie", "Iormia", "Brandi", "Branda", "Roy", "Richard",
                   "Harold", "Barbarian", "Jr.", "Moe", "Dixi", "Barbs", "Alis", "Rob", "Isawa",  "Isaak"
                   ]

people_title = ["Professor", "Doctor", "Sir", "Lord", "Lady", "Baron", "Baroness", "Count", "Countess", "King", "Queen", "Emperor", "Empress",
                "Mayor", "Politician", "Officer", "General", "Admiral", "Chancellor", "Minister", "Prime Minister", "Sheriff", "Guardian"
                ]

people_skill_level = ["Novice", "Dabbling", "Beginner", "Capable beginner", "Weak amateur", "Amateur", "Capable amateur", "Weak professional",
                      "Employable professional", "Solid professional", "Skilled professional", "Very skilled professional", "Expert", "Strong expert",
                      "Master", "Strong Master", "Region-known master", "Region-leading master", "Planet-known master", "Planet-leading master",
                      "Legendary Master"
                      ]

people_skill = ["Miner", "Woodworker", "Bowyer", "Carpenter", "Wood cutter", "Engraver", "Stone worker", "Mason", "Ranger",
                "Ambusher", "Caretaker", "Animal caretaker", "Dissector", "Animal trainer", "Trapper", "Metalsmith", "Armoursmith",
                "Merchant", "Broker", "Metal crafter", "Blacksmith", "Weaponsmith", "Jeweler", "Gem cutter", "Gem setter",
                "Craftsman", "Clothier", "Glassmaker", "Bone carver", "Leatherworker", "Stone crafter", "Weaver", "Extractor",
                "Appraiser", "Architect", "Manager", "Record keeper", "Bookkeeper", "Fisherman", "Farmer", "Brewer", "Butcher",
                "Cook", "Shepard", "Grower", "Herbalist", "Miller", "Milker", "Tanner", "Potash maker", "Thresher", "Engineer",
                "Mechanic", "Operator", "Siege engineer", "Civil engineer", "Professor", "Comedian", "Consoler", "Conversationalist",
                "Flatterer", "Intimidator", "Judge of intent", "Liar", "Negotiator", "Pacifier", "Persuader", "Officer", "Wrestler",
                "Gunner", "Marksman", "Sprinter", "Knife user", "Soldier", "General", "Swimmer", "Thrower", "Tracker", "Scientist",
                "Doctor", "Driver", "Surgeon", "Suterer", "Beekeeper", "Brewer", "Butcher", "Spinner", "Bookbinder", "Potter",
                "Paper maker", "Wax worker", "Dodger", "Fighter", "Kicker", "Climber", "Leader", "Rider", "Teacher", "Dancer", "Singer",
                "Musician", "Poet", "Logician", "Mathematician", "Astronomer", "Chemist", "Geographer", "Optics engineer", "Writer"
                ]

people_trait_ck3 = ["Brave", "Craven", "Calm", "Wrathful", "Chaste", "Lustful", "Content", "Ambitious", "Diligent", "Lazy", "Fickle", "Stubborn",
                    "Forgiving", "Vengeful", "Generous", "Greedy", " Gregarious", "Shy", "Honest", "Deceitful", "Humble", "Arrogant", "Just",
                    "Arbitrary", "Patient", "Impatient", "Temperate", "Gluttonous", "Trusting", "Paranoid", "Zealous", "Cynical", "Compassionate",
                    "Callous", "Sadistic", "Genius", "Beautiful", "Herculean", "Melancholic", "Lunatic", "Possessed", "Fecund", "Giant",
                    "Dwarf", "Sterile", "Spindly", "Hideous", "Imbecile", "Feeble", "Shrewd", "Strong", "Scarred", "Disfigured", "Bossy",
                    "Charming", "Curious", "Pensive", "Rowdy"
                    ]

people_trait_ck2 = ["Affectionate", "Playful", "Haughty", "Conscientious", "Fussy", "Brooding", "Indolent", "Willful", "Idolizer", "Timid", "Groomed",
                    "Uncouth", "Charitable", "Kind", "Wroth", "Proud", "Erudite", "Decadent"
                    ]

artifact_type = ["Statue", "War-axe", "Crown", "Barrel", "Bucket", "Bin", "Goblet", "Mug", "Cup", "Figurine", "Ring", "Earring", "Amulet", "Bracelet",
                 "Scepter", "Book", "Sword", "Shield", "Skull", "Coin", "Backpack", "Coffin", "Flask", "Fork", "Knife", "Jug", "Quiver",
                 "Scroll Roller", "Scroll", "Glove", "Hat", "Shoe", "Bell", "Sigil", "Longsword", "Gun", "Cube", "Slab", "Sphere", "Pendant", "Idol",
                 "Ring", "Key", "Lamp", "Box", "Tome", "Tiara", "Horn", "Fountain"
                 ]

artifact_adjective = ["Abysmal", "Benevolent", "Great", "Chaotic", "Crazed", "Demonic", "Lordly", "Sly", "Wonderful", "Hellish", "Compassionate",
                      "Resolute", "All-seeing", "Primal", "Exile", "Anguish", "Tempting", "Virtuous", "Holy", "Divine", "Godly", "White", "Green",
                      "Yellow", "Brown", "Red", "Black", "Hated"
                      ]

artifact_material = ["Aluminium", "Bismuth", "Copper", "Gold", "Silver", "Bronze", "Brass", "Fine pewter", "Iron", "Steel", "Lead", "Nickel",
                     "Platinum", "Tin", "Zinc", "Uranium", "Clay", "Limestone", "Rock", "Sandstone", "Granite", "Marble", "Basalt", "Obsidian",
                     "Gneiss", "Schist", "Slate", "Coal", "Cobalt", "Jet", "Kaolinite", "Mica", "Olivine", "Pitchblende", "Puddingstone", "Serpentine"
                     "Teak", "Papaya", "Willow", "Alder", "Cherry", "Cashew", "Pine", "Maple", "Walnut", "Cedar", "Hazel", "Acacia", "Ash",
                     "Mahogany", "Mangrove", "Rubber", "Coral", "Ivory", "Alpaca leather", "Cow leather", "Donkey leather", "Horse leather",
                     "Pig leather", "Yak leather", "Dog leather", "Crocodile leather", "Badger leather", "Bear leather", "Small bird feathers",
                     "Emu feathers", "Ceramic", "Earthenware", "Stoneware", "Porcelain", "Glass", "Crystal", "Opal", "Moonstone", "Jade", "Tigereye",
                     "Black zircon", "Purple spindel", "Topaz", "Emerald", "Sapphire", "Diamond", "Ruby", "Bloodstone", "Amber"
                     ]

artifact_quality = ["Rubbish", "Tattered", "Awful", "Poor", "Normal", "Good", "Excellent", "Masterwork", "Legendary", "Fine", "Superior",
                    "Exceptional"
                    ]

artifact_art = ["a Pig", "Dancers", "Turkey", "a Box of dreams", "a dark alley", "a Vulcano", "a great battle", "a boy", "Children", "Lovers",
                "a spy", "a bridge", "a Castle", "Heroes", "a town", "a village", "a country", "Insects", "Ruins", "a great mountain range", "an eye",
                "a body", "abstract art", "a large city", "a portrait", "the king", "the president", "the mayor"
                ]

artifact_dedication = ["family", "virtue", "lust", "greed", "sin", "selflessness", "bravery", "the true god", "the true goddess", "love", "peace",
                       "freedom", "the king", "the queen", "the gods", "the community"
                       ]

scene_actors = ["Dwarfs", "Elves", "Humans", "Imperials", "Republicans", "Federals"
                ]

scene_verbs = ["are", "have", "do", "say", "get", "make", "go", "know", "take", "see", "come", "think", "look", "want", "give", "use", "find", "tell",
               "ask", "work", "seem", "feel", "try", "leave", "call", "become", "need", "help", "love", "despise", "settle",
               "befriend", "destroy", "kill"
               ]

scene_objects = ["sheep", "bananas", "books", "lamp", "door", "money", "chair", "cup", "mug", "bed", "hammer", "hamster", "egg",
                 "bag", "food", "table", "acorn", "goggles", "glasses"
                 ]

timeline_qualifier = ["Some", "Over", "Just", "", ""
                      ]

ship_prefixes = ["HMS", "HMSS", "SS", "ARA", "GDV", "USN", "CRS", "SMS", "FGS", "RN", "RS"
                 ]

ship_long_names = ["Dark Zone", "Carpe Diem"
                   ]
# (Xqhare): God I hate this -> Some items are doubled because they can exist over several types - and all the other semi doubling up below
ship_sizes = ["SS", "XS", "S", "M", "L", "XL", "XXL", "U", "XU", "T"
              ]
# (Xqhare): SS = SingleSeater
ship_type_ss = ["Fighter", "Explorer", "Utility vessel", "Landing craft", "Patrol vessel", "Personal ship", "Planetary Transport",
                "Planetary Ferry", "Mail ship", "Mining Ships", "High-speed craft", "Service vessel", "Barge", "Reefer vessel"
                ]
ship_type_xs = ["Shuttle", "Scout", "Freighter", "Frigate", "Fast attack craft", "Landing craft", "Minesweeper", "Patrol vessel", "Survey ship",
                "Yacht", "Mine layer", "Stealth attack vessel", "Corvette", "Ferry", "Monitor", "Mail ship", "Mining Ships", "Production Platform",
                "Floating Storage Unit", "Floating Production and Storage Unit", "Anchor handling vessels", "Pilot Craft", "Research vessel",
                "Salvage vessel", "Livestock Carrier", "High-speed craft", "Service vessel", "Barge", "Reefer vessel"
                ]
ship_type_s = ["Science vessel", "Destroyer", "Explorer", "Scout", "Freighter", "Light Cruiser", "Landing craft", "Minesweeper", "Survey ship",
               "Large Yacht", "Mine layer", "Stealth attack vessel", "Escort", "Ferry", "Monitor", "Tanker", "Mail ship", "Bulk Cargo Carrier",
               "Mining Ships", "Floating Storage Unit", "Floating Production and Storage Unit", "Anchor handling vessels", "Pilot Craft",
               "Research vessel", "Salvage vessel", "Livestock Carrier", "High-speed craft", "Service vessel", "Gas Carrier", "Barge",
               "Reefer vessel"
               ]
ship_type_m = ["Freighter", "Hospital ship", "Landing craft", "Mega Yacht", "Escort", "Cruiser", "Armored Cruiser", "Cruise ship", "Liner", "Tanker",
               "Mail ship", "Bulk Cargo Carrier", "Production Platform", "Floating Storage Unit", "Floating Production and Storage Unit",
               "Anchor handling vessels", "Research vessel", "Salvage vessel", "Livestock Carrier", "Service vessel", "Gas Carrier", "Reefer vessel",
               "Tender"
               ]
ship_type_l = ["Freighter", "Hospital ship", "Ultra Yacht", "Heavy Escort", "Escort Carrier", "Heavy Cruiser", "Cruiser Carrier", "Assault ship",
               "Large Cruise ship", "Liner", "Tanker", "Mail ship", "Bulk Cargo Carrier", "Production Platform", "Floating Storage Unit",
               "Floating Production and Storage Unit", "Salvage vessel", "Livestock Carrier", "Gas Carrier", "Reefer vessel", "Tender"
               ]
ship_type_xl = ["Large Freighter", "Hospital ship", "Battle Cruiser", "Carrier", "Pocket Battleship", "Super Cruise ship", "Star Liner",
                "Large Tanker", "Large Bulk Cargo Carrier", "Refinery Ship", "Production Platform", "Floating Storage Unit",
                "Floating Production and Storage Unit", "Salvage vessel", "Large Livestock Carrier", "Jump Ship", "Large Gas Carrier",
                "Large Reefer vessel", "Large Tender"
                ]
ship_type_xxl = ["Heavy Freighter", "Battleship", "Battle Carrier", "Mega Cruise ship", "Super Star Liner", "Heavy Tanker",
                 "Heavy Bulk Cargo Carrier", "Refinery Ship", "Production Platform", "Floating Storage Unit", "Floating Production and Storage Unit",
                 "Factory Ship", "Large Salvage vessel", "Heavy Livestock Carrier", "Large Jump Ship", "Heavy Gas Carrier", "Heavy Lift Ship",
                 "Heavy Reefer vessel", "Heavy Tender"
                 ]
ship_type_u = ["Super Freighter", "Super Battleship", "Super Carrier", "Ultra Cruise ship", "Mega Star Liner", "Super Tanker",
               "Super Bulk Cargo Carrier", "Large Refinery Ship", "Production Platform", "Floating Storage Unit",
               "Floating Production and Storage Unit", "Factory Ship", "Heavy Salvage vessel", "Super Livestock Carrier", "Heavy Jump Ship",
               "Super Gas Carrier", "Super Heavy Lift Ship", "Super Reefer vessel", "Super Tender"
               ]
ship_type_xu = ["Super Heavy Freighter", "Super Heavy Battleship", "Super Battle Carrier", "Titan Cruise ship", "Ultra Star Liner",
                "Super Heavy Tanker", "Super Heavy Bulk Cargo Carrier", "Large Refinery Ship", "Production Platform", "Floating Storage Unit",
                "Floating Production and Storage Unit", "Factory Ship", "Super Salvage vessel", "Super Heavy Livestock Carrier", "Super Jump Ship",
                "Super Heavy Gas Carrier", "Ultra Heavy Lift Ship", "Super Heavy Reefer vessel", "Super Heavy Tender"
                ]
ship_type_t = ["Titan Freighter", "Titan", "Ultra Titan Cruise Ship", "Titan Star Liner", "Titan Tanker", "Titan Bulk Cargo Carrier",
               "Heavy Refinery Ship", "Production Platform", "Floating Storage Unit", "Floating Production and Storage Unit", "Factory Ship",
               "Super Heavy Salvage vessel", "Titan Livestock Carrier", "Super Heavy Jump Ship", "Titan Gas Carrier", "Mega Heavy Lift Ship",
               "Titan Reefer vessel", "Fleet Tender"
               ]
ship_fame = ["Speed", "Armor", "Survivability", "Fortune", "Misfortune", "Accuracy", "Range", "Dependability", "Size", "Prestige", "Cost", "Safeness",
             "Repairability", "Design", "Comfort", "Discomfort", "Ugliness", "Spartanism", "Opulence", "Crampedness", "Spaciousness", "Armament",
             "Detectability", "Low Detectability", "Sensors", "Blindspots", "Emissions", "Fuel economy", "Bad Sensors", "Good Sensors",
             "Few Blindspots", "Many Blindspots", "Good Emissions", "Bad Emissions", "Good Fuel economy", "Bad Fuel economy"
             ]

currency_real_names = ["Aksa", "Angolar", "Apsar", "Argentinio", "Ariary", "Austral", "Auksinas", "Baht", "Balboa", "Birr", "Bitcoin", "Bolivar",
                       "Boliviano", "Budju", "Cedi", "Chervonets", "Colon", "Continental Currency", "Conventionsthaler", "Córdoba", "Crown",
                       "Cruzado", "Cruzeiro", "Cupon", "Customs Gold Unit", "Cryptocurrency", "Dalasi", "Daler", "Denar", "Denier", "Dong", "Dianr",
                       "Diner", "Dinero", "Dinherio", "Dirham", "Dobra", "Dollar", "Dong", "Drachma", "Dram", "Ekwele", "Escudo", "Euro", "Fanam",
                       "Florin", "Franc", "Franco", "Frange", "Frank", "Gazeta", "Genevoise", "Gineih", "Grivna", "Grosz", "Grzywna", "Guarani",
                       "Guilder", "Guinea", "Gulden", "Hryvnia", "Hwan", "Inca", "Inti", "Karbovanets", "Keping", "Kina", "Kip", "Kolion",
                       "Konvertibilna marka", "Kori", "Korona", "Koruna", "Koruuni", "Króna", "Krona", "Krone", "Kronenthaler", "Kroon", "Kuna",
                       "Kwachha", "Kwanza", "Kyat",  "Laari", "Lari", "Lats", "Lek", "Lempira", "Leone", "Leu", "Lev", "Libra", "Liangeni", "Lira",
                       "Litas", "Livre", "Manat", "Maneti", "Maravedi", "Mark", "Marka", "Markka", "Metica", "Mohar", "Mon", "Mun", "Nahar", "Naira",
                       "Nakfa", "New pence", "Ngultrum", "Obol", "Ode", "Ora", "Ostmark", "Ostrubel", "Ouguiya", "Pa'anga", "Paisa", "Pataca",
                       "Pengo", "Penning", "Perper", "Perun", "Peseta", "Peso", "Petro", "Phoenix", "Piastra", "Piastre", "Piaster", "Piso", "Pitis",
                       "Pond", "Pound", "Pula", "Punt", "Quetzal", "Rai stones", "Rand", "Reaal", "Real", "Reichsmark", "Reichsthaler", "Renminbi",
                       "Rentenmark", "Rial", "Riel", "Rigsdaler", "Riksdaler", "Rijksdaalder", "Ringgit", "Rixdollar", "Riyal", "Roephia", "Rouble",
                       "Rublis", "Rufiyah", "Rupee", "Rupiah", "Rupie", "Ryo", "Schilling", "Scudo", "Setu", "Shah", "Shekel", "Shilling", "Skender",
                       "Sol", "Soum", "Somalo", "Somoni", "Specidaler", "Speciethaler", "Srang", "Sterling", "Sucre", "Syli", "Tael", "Taka", "Tala",
                       "Tallero", "Talonas", "Tangka", "Tenge", "Thaler", "Tical", "Tögrög", "Tolar", "Toman", "Trade dollar", "Tugrik", "Vatu",
                       "Venezolano", "Vereinsthaler", "Wén", "Won", "Yang", "Yen", "Yuan", "Zloty", "Kreuzer"
                       ]

currency_real_fractional_names = ["Agora", "Att", "Avo", "Baisa", "Ban", "Butut", "Cent", "Chetrum", "Chon", "Copeck", "Deni", "Diram", "Dirham",
                                  "Eyrir", "Fenning", "Fillér", "Fils", "Grosz", "Halala", "Hào", "Heller", "Iraimbilanja", "Jeon", "Jiao", "Khoums",
                                  "Kobo", "Kopeck", "Kurus", "Laari", "Luma", "Millme", "Möngö", "Ngwee", "Ore", "Öre", "Oyra", "Paisa", "Penny",
                                  "Para", "Pesewa", "Piaster", "Piastre", "Poisha", "Pul", "Pya", "Qepik", "Qintar", "Rappen", "Rial", "Santeem",
                                  "Santim", "Satang", "Satoshi", "Sen", "Sene", "Seniti", "Stotinka", "Tambala", "Tenge", "Tetri", "Thebe", "Tiyn",
                                  "Tiyin", "Toea", "Tyiyn", "Kreuzer"
                                  ]
# (Xqhare): ATTENTION, 1 IS ASSUMED TO EXIST BY LIBRARY
currency_coins_denomination = ["2", "5", "10", "20", "50", "100"
                               ]
# (Xqhare): ATTENTION, 1 IS ASSUMED TO EXIST BY LIBRARY
currency_non_decimal_base_120 = ["2", "3", "4", "5", "6", "10", "12", "15", "20", "30", "60", "120"
                                 ]

currency_endings = ["ler", "ier", "ero", "ion", "ra", "ar", "er", "no", "en", "ro", "re", "ta", "ira", "avo", "simo", "ime", "timo"
                    ]

currency_second_word = ["thaler", "dollar", "real", "yuan", "yen", "thaler", "rouble", "rupee", "pound", "mark", "peso", "livre", "crown", "dinar",
                        "escudo", "florin", "franc", "gulden", "marka", "lira"
                        ]

currency_metals = ["Gold", "Guld", "Silver", "Silber", "Copper", "Kupfer", "Brass", "Messing", "Iron", "Eisen", "Steel", "Stahl", "Nickel", "Bronze",
                   "Aluminium"
                   ]

currency_time_fractions = [3, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60
                           ]

currency_icon_inscription = ["Letter", "Monogram", "Name"
                             ]

currency_icon_figure = ["Person", "Creature", "Animal", "Plant", "Object"
                        ]

currency_icon_partial = ["Head", "Forepart of an animal", "Hind-part of an animal"
                         ]

currency_icon_incuse = ["Square", "Shield", "Helmet", "Sword"
                        ]

currency_icon_insignia = ["Diadem", "Headband", "Crown", "Hat", "Staff", "Sword", "Scale", "Jewellery", "Armour"
                          ]

currency_icon_mythical_creature = ["Shapeshifter", "Amphibious Bull", "Water Horse", "Vampire", "Hobgoblin", "Fenrir", "Hellhound", "Werewolf",
                                   "Two headed dog", "Blue Tiger", "Spectral cat", "Griffin", "Unicorn", "Pegasus", "Sphinx", "Chimera"
                                   ]

currency_icon_animal = ["Whale", "Bull", "Lion", "Tiger", "Cat", "Dog", "Fish", "Dolphin", "Bird", "Raven", "Moose", "Deer", "Rabbit", "Wolf"
                        ]

currency_icon_plant = ["Alder", "Almond", "Aloe vera", "Ambrosia", "Apple", "Ash", "Bamboo", "Banana", "Baobab", "Bean", "Berry", "Beech", "Cabbage",
                       "Carrot", "Cedar", "Cherry", "Chestnut", "Coconut", "Cress", "Daisy", "Fern", "Fig", "Flax", "Garlic", "Hemp", "Juniper",
                       "Lemon", "Lettuce", "Magnolia", "Maize", "Mango", "Maple", "Nettle", "Oak", "Olive", "Onion", "Orange", "Pea", "Peach",
                       "Pepper", "Pineapple", "Pistachio", "Poplar", "Poppy", "Potato", "Raspberry", "Rhubarb", "Rice", "Rose", "Rye", "Rosemary",
                       "Saffron", "Strawberry", "Sugarcane", "Sunflower", "Tomato", "Tulip", "Walnut", "Wheat", "Willow", "Zedoary"
                       ]

metals_list = ["Aluminium", "Bismuth", "Copper", "Gold", "Silver", "Bronze", "Brass", "Iron", "Steel", "Lead", "Nickel", "Zinc", "Indium", "Platinum",
               "Tin", "Zinc", "Uranium", "Cobalt", "Bloodstone", "Titanium", "Chromium", "Manganese", "Antimony", "Tellurioum", "Osmium", "Tungsten"
               ]

metals_alloy_list = ["Carbon", "Gallium", "Lithium", "Beryllium", "Sodium", "Magnesium"
                     ]

government_name0 = ["Federal", "Unitary", "Constitutional", "Religious", "Presidential", "Peoples", "Directorial", "Corporate", "Collective",
                    "Democratic"
                    ]

government_name1 = ["Parliamentary", "Democratic", "Council", "Constitutionary", "Presidential", "Directoral"
                    ]

government_name_monarchy = ["Absolute", "Constitutional", "Crowned", "Elective"
                            ]

rep_or_state_list = ["Republic", "State"
                     ]

story_empire_interactions = ["attack", "ally", "settle", "had a parade in", "developed technologies", "connected by road to", "developed economy",
                             "funded new empire"
                             ]

story_government_type_adj_0 = ["Corporate", "Religious", "Monarchy"
                               ]

story_government_type_adj_01 = ["Federal", "Unitary", "Constitutional", "Presidential", "Directorial", "Democratic"
                                ]

story_government_type_adj_1 = ["Peoples", "Collective", "Council"
                               ]

story_government_type_sec_0 = ["Directoral"
                               ]

story_government_type_sec_01 = ["Parliamentary", "Democratic", "Constitutionary", "Presidential"
                                ]

story_government_type_sec_1 = ["Council"
                               ]

story_government_leader_title_0_reli = ["Arch-Bishop", "Prophet", "Arch-Prophet", "Pope"
                                        ]

story_government_leader_title_0_cor = ["CEO", "Chairman", "Owner"
                                       ]

story_government_leader_title_0_mon = ["King", "Queen", "Emperor", "Empress"]

story_government_leader_title_01 = ["Chancellor", "Prime Minister", "Minister", "Supreme Minister", "Chief Chancellor", "Chairman", "President",
                                    "High Councillor"]

story_government_leader_title_1 = ["Chairman", "Party Leader", "Supreme Leader"
                                   ]

# (Xqhare): Directly from eu4, float == max ducat per good produced
story_town_trade_goods_dict = {"Chinaware": 3, "Cloth": 4.05, "Cloves": 8, "Coal": 10, "Coca": 5.4, "Coffee": 3.3, "Copper": 3.45, "Cotton": 4.95,
                               "Dyes": 4, "Fish": 2.5, "Fur": 3.5, "Gems": 4, "Glass": 3.45, "Gold": 16, "Grain": 2.5, "Incense": 3, "Iron": 4.5,
                               "Ivory": 5, "Livestock": 3.4, "Naval Supplies": 3, "Paper": 4.725, "Salt": 3.3, "Silk": 5, "Slaves": 2.2,
                               "Spices": 3.3, "Sugar": 5.25, "Tea": 3, "Tobacco": 4.5, "Tropical Wood": 3, "Wine": 3.125, "Wool": 2.875
                               }
