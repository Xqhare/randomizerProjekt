#!/usr/bin/env python3
from tkinter import ttk
import tkinter as tk

import CurrencyGen
import EmpireGen
import GenLib
import GovernmentGen
import LanguageGen
import MetalAlloyGen
import NumberGen
import PlaceNameGen
import PeopleNameGen
import ArtifactGen
import SceneGen
import ShipClassGen
import ShipNameGen
import HistoryGen
import TimeGen
import OperationGen
import OldHistoryGen
""" DOC:
Quotes-Master-List:
[Window Title == Quote - Qoutee]
Xqhare's Randomizer Project == The extraordinary is in what we do, not who we are. - Lara Croft
Xqhare's Place Name Generator == I don't have your STONE, and fuck you anyway! - Edward Carnby
Xqhare's People Generator == My past is not a memory. It's a force at my back. It pushes and steers. "I may not always like where it leads me,
                                but like any story, the past needs resolution. What's past is prologue. - Samus Aran
Xqhare's Artifact Generator == Words aren't the only way to tell someone how you feel. - Tifa Lockhart
Xqhare's Scene Generator == It's dangerous going alone. I'll come with you. - Jill Valentine
Xqhare's Timeline Generator == Link! - Zelda
Xqhare's Operation Generator == War... War never changes. - The narrator, Fallout: New Vegas
Xqhare's Ship Name Generator == Heed my words. I am Malenia. Blade of Miquella. - Malenia, Blade of Miquella
Xqhare's Ship Class Generator == Endure and survive. - Ellie
Xqhare's Currency Generator == Hey! Listen! - Na'vi
Xqhare's Metal and Alloy Generator == The ending isn’t any more important than any of the moments leading to it. - Dr. Rosalene
Xqhare's Empire Generator == No matter how dark the night, morning always comes, and our journey begins anew. - Lulu
Xqhare's Government Generator == Everyone I've known has either died or left me...everyone fucking except for you! 
                                Now don't tell me I'd be better off with someone else cuz the truth is I'd just be more scared. -Ellie
Xqhare's Government Generator == Booker are you afraid of god? -- No, but I am afraid of you. - Elizabeth
Xqhare's History Generator == Memories are nice, but that's all they are. - Rikku
Xqhare's Numbers Generator == Fate does not divide us. Fate brings us together - Tina
Xqhare's Old History Generator == I always thought you were my worst enemy but in the end it turned out you were my best friend. -GLaDOS
XYZ == A new hand touches the beacon. Listen. Hear me and obey. A foul darkness has seeped into my temple. A darkness that you will destroy. 
        Return my beacon to mount Kilkreath. And I will make you the instrument of my cleansing light. - Meridia (TESV)
XYZ == If I'm wearing a bikini, where do I put my poke-balls? Tee-hee...woman's secret. - Pokemon
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x525+50+50")
        self.minsize(400, 525)
        self.title("Xqhare's Randomizer Project")

        quote = tk.Label(text="The extraordinary is in what we do, not who we are.", fg="purple", bg="black", width=400)
        quote.pack()

        quote_name = tk.Label(text="- Lara Croft", fg="purple", bg="black", width=400)
        quote_name.pack()

        user_instruction = tk.Label(text="Please choose your generator:", bg="grey", width=400)
        user_instruction.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(side="top", padx=5, pady=5)

        left_button_frame = tk.Frame(master=button_frame)
        left_button_frame.pack(side="left")

        right_button_frame = tk.Frame(master=button_frame)
        right_button_frame.pack(side="left")

        tk.Button(master=left_button_frame,
                  text='Place Name Generator',
                  bg="greenyellow",
                  command=self.gui_open_place_name_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='People Generator',
                  bg="darkred",
                  command=self.gui_open_people_name_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Artifact Generator',
                  command=self.gui_open_artifact_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='Scene Generator',
                  command=self.gui_open_scene_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Timeline Generator',
                  command=self.gui_open_timeline_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='Operation Generator',
                  bg="yellow",
                  command=self.gui_open_operation_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Ship name Generator',
                  command=self.gui_open_ship_name_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='Ship class Generator',
                  command=self.gui_open_ship_class_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Currency Generator',
                  command=self.gui_open_currency_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='Metal and Alloy Generator',
                  command=self.gui_open_metal_alloy_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Empire Generator',
                  command=self.gui_open_empire_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='Government Generator',
                  command=self.gui_open_government_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Language Generator',
                  command=self.gui_open_language_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='History Generator',
                  bg="dodgerblue1",
                  command=self.gui_open_history_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='Numbers Generator',
                  bg="limegreen",
                  command=self.gui_open_numbers_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='OLD History Generator',
                  command=self.gui_open_old_history_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='BLANK Generator',
                  command=self.gui_open_language_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='BLANK Generator',
                  command=self.gui_open_government_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=left_button_frame,
                  text='BLANK Generator',
                  command=self.gui_open_language_window).pack(expand=True, side="top", pady=5)

        tk.Button(master=right_button_frame,
                  text='BLANK Generator',
                  command=self.gui_open_government_window).pack(expand=True, side="top", pady=5)

        p_exit = tk.Button(text="Quit", command=self.destroy, bg="red", fg="black")
        p_exit.pack(side="bottom")

    def gui_open_place_name_window(self):
        place_name_gen_window = PlaceWindow(self)
        place_name_gen_window.grab_set()

    def gui_open_people_name_window(self):
        people_name_gen_window = PeopleWindow(self)
        people_name_gen_window.grab_set()

    def gui_open_artifact_window(self):
        artifact_gen_window = ArtifactWindow(self)
        artifact_gen_window.grab_set()

    def gui_open_scene_window(self):
        scene_gen_window = SceneWindow(self)
        scene_gen_window.grab_set()

    def gui_open_timeline_window(self):
        timeline_gen_window = TimelineWindow(self)
        timeline_gen_window.grab_set()

    def gui_open_operation_window(self):
        operation_gen_window = OperationsWindow(self)
        operation_gen_window.grab_set()

    def gui_open_ship_name_window(self):
        ship_name_gen_window = ShipNameWindow(self)
        ship_name_gen_window.grab_set()

    def gui_open_ship_class_window(self):
        ship_class_gen_window = ShipClassWindow(self)
        ship_class_gen_window.grab_set()

    def gui_open_currency_window(self):
        currency_gen_window = CurrencyWindow(self)
        currency_gen_window.grab_set()

    def gui_open_metal_alloy_window(self):
        metal_alloy_gen_window = MetalAlloyWindow(self)
        metal_alloy_gen_window.grab_set()

    def gui_open_empire_window(self):
        empire_gen_window = EmpireWindow(self)
        empire_gen_window.grab_set()

    def gui_open_government_window(self):
        government_gen_window = GovernmentWindow(self)
        government_gen_window.grab_set()

    def gui_open_language_window(self):
        language_gen_window = LanguageWindow(self)
        language_gen_window.grab_set()

    def gui_open_history_window(self):
        history_gen_window = HistoryWindow(self)
        history_gen_window.grab_set()

    def gui_open_numbers_window(self):
        numbers_gen_window = NumbersWindow(self)
        numbers_gen_window.grab_set()

    def gui_open_old_history_window(self):
        old_history_gen_window = OldHistoryWindow(self)
        old_history_gen_window.grab_set()


class PlaceWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Place Name Generator")

        tk.Label(self,
                 text="I don't have your STONE, and fuck you anyway!",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Edward Carnby",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of places you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=100)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (PlaceNameGen.main_place_name() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class PeopleWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('1300x1000')
        self.minsize(1300, 1000)
        self.title("Xqhare's People Generator")

        tk.Label(self,
                 text="My past is not a memory. It's a force at my back. It pushes and steers. "
                      "I may not always like where it leads me, but like any story, the past needs resolution. "
                      "What's past is prologue.",
                 fg="purple",
                 bg="black",
                 width=1300).pack()

        tk.Label(self,
                 text="- Samus Aran",
                 fg="purple",
                 bg="black",
                 width=1300).pack()

        tk.Label(self,
                 text="Please enter the number of people you want to generate:",
                 bg="grey",
                 width=1300).pack()

        num_pl = tk.IntVar(value=100)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack()
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (PeopleNameGen.main_generated_person() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class ArtifactWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('800x1000')
        self.minsize(800, 1000)
        self.title("Xqhare's Artifact Generator")

        tk.Label(self,
                 text="Words aren't the only way to tell someone how you feel.",
                 fg="purple",
                 bg="black",
                 width=800).pack()

        tk.Label(self,
                 text="- Tifa Lockhart",
                 fg="purple",
                 bg="black",
                 width=800).pack()

        tk.Label(self,
                 text="Please enter the number of artifacts you want to generate:",
                 bg="grey",
                 width=800).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (ArtifactGen.main_artifact() + '\n' + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class SceneWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Scene Generator")

        tk.Label(self,
                 text="It's dangerous going alone. I'll come with you.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Jill Valentine",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of scenes you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (SceneGen.main_scene() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class TimelineWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('600x1000')
        self.minsize(600, 1000)
        self.title("Xqhare's Timeline Generator")

        tk.Label(self,
                 text="Link!",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Zelda",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the start year of the timeline you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar()
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please enter the end year of the timeline you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl0 = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl0)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please enter the number of events in the timeline you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl1 = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl1)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            year0 = num_pl.get()
            year1 = num_pl0.get()
            y_length = num_pl1.get()
            result = (TimeGen.main_timeline(year0, year1, y_length))
            result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class OperationsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Operation Generator")

        tk.Label(self,
                 text="War... War never changes.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- The narrator, Fallout: New Vegas",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of Operations you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (OperationGen.main_operation_name() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class ShipNameWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x1000')
        self.minsize(500, 1000)
        self.title("Xqhare's Ship Name Generator")

        tk.Label(self,
                 text="Heed my words. I am Malenia. Blade of Miquella.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Malenia, Blade of Miquella",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of ship names you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please enter the prefix for the ship names you want to generate: ",
                 bg="grey",
                 width=400).pack()

        tk.Label(self,
                 text="(For empty put space, if left empty it returns a random prefix)",
                 bg="grey",
                 width=400).pack()

        str_prefix = tk.StringVar()
        str_prefix_entry = tk.Entry(self, textvariable=str_prefix)
        str_prefix_entry.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            ship_prefix = str_prefix.get()
            for x in range(pl_length):
                result = (ShipNameGen.main_ship_name(ship_prefix) + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class ShipClassWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('700x800')
        self.minsize(700, 800)
        self.title("Xqhare's Ship Class Generator")

        tk.Label(self,
                 text="Endure and survive.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Ellie",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of ship classes you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please choose the size for the ship classes you want to generate: ",
                 bg="grey",
                 width=400).pack()

        tk.Label(self,
                 text="(For random leave empty)",
                 bg="grey",
                 width=400).pack()

        ship_size_dropdown = ttk.Combobox(self, state="readonly", values=GenLib.ship_sizes)
        ship_size_dropdown.pack(pady=2)

        tk.Label(self,
                 text="Please enter the average speed in units of lightspeed(c) for the ship classes you want to generate: ",
                 bg="grey",
                 width=400).pack()

        avg_speed_ls = tk.IntVar(value=1)
        avg_speed_ls_entry = tk.Entry(self, textvariable=avg_speed_ls)
        avg_speed_ls_entry.pack(pady=2)

        tk.Label(self,
                 text="Please enter the average range in units of light-years(ly) for the ship classes you want to generate: ",
                 bg="grey",
                 width=400).pack()

        avg_range_ly = tk.IntVar(value=100)
        avg_range_ly_entry = tk.Entry(self, textvariable=avg_range_ly)
        avg_range_ly_entry.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            ship_size = ship_size_dropdown.get()
            avg_speed = avg_speed_ls.get()
            avg_range = avg_range_ly.get()
            for x in range(pl_length):
                result = (ShipClassGen.main_ship_class(ship_size, avg_speed, avg_range) + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class CurrencyWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Currency Generator")

        tk.Label(self,
                 text="Hey! Listen!",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Na'vi",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of Currencies you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please choose the base of your currency:",
                 bg="grey",
                 width=400).pack()

        tk.Label(self,
                 text="(Decimal, non-Decimal or Time.)",
                 bg="grey",
                 width=400).pack()

        dropdown_values = ["Decimal", "Non-Decimal", "Time based"]

        decimal_dropdown = ttk.Combobox(self, state="readonly", values=dropdown_values)
        decimal_dropdown.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            user_choice_decimal = decimal_dropdown.get()
            for x in range(pl_length):
                result = (CurrencyGen.main_currency(user_choice_decimal) + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class MetalAlloyWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Metal and Alloy Generator")

        tk.Label(self,
                 text="The ending isn’t any more important than any of the moments leading to it.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Dr. Rosalene",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of metal's or alloy's you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please choose what you want to generate from the dropdown:",
                 bg="grey",
                 width=400).pack()

        tk.Label(self,
                 text="(Metal, Alloy or Random.)",
                 bg="grey",
                 width=400).pack()

        dropdown_values = ["Metal", "Alloy", "Random"]

        material_dropdown = ttk.Combobox(self, state="readonly", values=dropdown_values)
        material_dropdown.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            user_choice_material = material_dropdown.get()
            for x in range(pl_length):
                match user_choice_material:
                    case "Metal":
                        result = (MetalAlloyGen.gen_metal() + '\n')
                        result_label.insert('1.0', result)
                    case "Alloy":
                        result = (MetalAlloyGen.gen_alloy() + '\n')
                        result_label.insert('1.0', result)
                    case "Random":
                        result = (MetalAlloyGen.main_metal_alloy() + '\n')
                        result_label.insert('1.0', result)
                    case _:
                        return "!!! Error 5 !!!"

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class EmpireWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Empire Generator")

        tk.Label(self,
                 text="No matter how dark the night, morning always comes, and our journey begins anew.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Lulu",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of Empires you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (EmpireGen.main_empire() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class GovernmentWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Government Generator")

        tk.Label(self,
                 text="Everyone I've known has either died or left me...everyone fucking except for you!"
                      " Now don't tell me I'd be better off with someone else cuz the truth is I'd just be more scared.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text=" -Ellie",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of Empires you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Enter empire name, if left empty it returns with a random name:",
                 bg="grey",
                 width=400).pack()

        str_gov_name = tk.StringVar()
        str_gov_name_entry = tk.Entry(self, textvariable=str_gov_name)
        str_gov_name_entry.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            usr_gov_name = str_gov_name.get()
            for x in range(pl_length):
                result = (GovernmentGen.main_government(usr_gov_name) + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class LanguageWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Language Generator")

        tk.Label(self,
                 text="Booker are you afraid of god? -- No, but I am afraid of you.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Elizabeth",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of Languages you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            for x in range(pl_length):
                result = (LanguageGen.main_language() + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class HistoryWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's History Generator")

        tk.Label(self,
                 text="Memories are nice, but that's all they are.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Rikku",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of empires you want to populate the world:",
                 bg="grey",
                 width=400).pack()

        num_emp = tk.IntVar(value=25)
        num_emp_entry = tk.Entry(self, textvariable=num_emp)
        num_emp_entry.pack(pady=2)
        num_emp_entry.focus()

        tk.Label(self,
                 text="Please enter the number of turns the story is to be generated with:",
                 bg="grey",
                 width=400).pack()

        num_turn = tk.IntVar(value=50)
        num_turn_entry = tk.Entry(self, textvariable=num_turn)
        num_turn_entry.pack(pady=2)

        tk.Label(self,
                 text="Please enter the number of actions you want to perform per turn:",
                 bg="grey",
                 width=400).pack()

        num_act = tk.IntVar(value=2)
        num_act_entry = tk.Entry(self, textvariable=num_act)
        num_act_entry.pack(pady=2)

        tk.Label(self,
                 text="Save the database?",
                 bg="grey",
                 width=400).pack()

        dropdown_values = ["No", "Yes"]

        save_dropdown = ttk.Combobox(self, state="readonly", values=dropdown_values)
        save_dropdown.current(1)
        save_dropdown.pack(pady=2)

        def gui_generate_button_clicked():
            num_emp_int = num_emp.get()
            num_turn_int = num_turn.get()
            num_act_int = num_act.get()
            usr_save = save_dropdown.get()
            result = (HistoryGen.main(num_emp_int, num_turn_int, num_act_int, usr_save))
            index = 0
            for n in result:
                result_part = result[index] + '\n'
                result_label.insert('1.0', result_part)
                index += 1

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class NumbersWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Numbers Generator")

        tk.Label(self,
                 text="Fate does not divide us. Fate brings us together",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="- Tina",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the amount of numbers you want to generate:",
                 bg="grey",
                 width=400).pack()

        num_pl = tk.IntVar(value=10)
        num_pl_entry = tk.Entry(self, textvariable=num_pl)
        num_pl_entry.pack(pady=2)
        num_pl_entry.focus()

        tk.Label(self,
                 text="Please enter the minimum:",
                 bg="grey",
                 width=400).pack()

        num_pl_min = tk.IntVar()
        num_pl_min_entry = tk.Entry(self, textvariable=num_pl_min)
        num_pl_min_entry.pack(pady=2)

        tk.Label(self,
                 text="Please enter the maximum:",
                 bg="grey",
                 width=400).pack()

        num_pl_max = tk.IntVar(value=100)
        num_pl_max_entry = tk.Entry(self, textvariable=num_pl_max)
        num_pl_max_entry.pack(pady=2)

        tk.Label(self,
                 text="Please choose between int and float:",
                 bg="grey",
                 width=400).pack()

        dropdown_values = ["int", "float"]

        numbers_dropdown = ttk.Combobox(self, state="readonly", values=dropdown_values)
        numbers_dropdown.current(1)
        numbers_dropdown.pack(pady=2)

        def gui_generate_button_clicked():
            pl_length = num_pl.get()
            usr_min = num_pl_min.get()
            usr_max = num_pl_max.get()
            user_choice = numbers_dropdown.get()
            for x in range(pl_length):
                result = (NumberGen.main_number_gen(usr_min, usr_max, user_choice) + '\n')
                result_label.insert('1.0', result)

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


class OldHistoryWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x1000')
        self.minsize(400, 1000)
        self.title("Xqhare's Old History Generator")

        tk.Label(self,
                 text="I always thought you were my worst enemy but in the end it turned out you were my best friend.",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text=" - GLaDOS",
                 fg="purple",
                 bg="black",
                 width=400).pack()

        tk.Label(self,
                 text="Please enter the number of empires you want to populate the world:",
                 bg="grey",
                 width=400).pack()

        num_emp = tk.IntVar(value=25)
        num_emp_entry = tk.Entry(self, textvariable=num_emp)
        num_emp_entry.pack(pady=2)
        num_emp_entry.focus()

        tk.Label(self,
                 text="Please enter the number of turns the story is to be generated with:",
                 bg="grey",
                 width=400).pack()

        num_turn = tk.IntVar(value=50)
        num_turn_entry = tk.Entry(self, textvariable=num_turn)
        num_turn_entry.pack(pady=2)

        tk.Label(self,
                 text="Please enter the number of actions you want to perform per turn:",
                 bg="grey",
                 width=400).pack()

        num_act = tk.IntVar(value=2)
        num_act_entry = tk.Entry(self, textvariable=num_act)
        num_act_entry.pack(pady=2)

        tk.Label(self,
                 text="Save the database?",
                 bg="grey",
                 width=400).pack()

        dropdown_values = ["No", "Yes"]

        save_dropdown = ttk.Combobox(self, state="readonly", values=dropdown_values)
        save_dropdown.current(1)
        save_dropdown.pack(pady=2)

        def gui_generate_button_clicked():
            num_emp_int = num_emp.get()
            num_turn_int = num_turn.get()
            num_act_int = num_act.get()
            usr_save = save_dropdown.get()
            result = (OldHistoryGen.main_story(num_emp_int, num_turn_int, num_act_int, usr_save))
            index = 0
            for n in result:
                result_part = result[index] + '\n'
                result_label.insert('1.0', result_part)
                index += 1

        tk.Button(self,
                  text='Run Generator', command=gui_generate_button_clicked).pack(expand=True)

        tk.Button(self,
                  text='Close Generator', bg="red", fg="black",
                  command=self.destroy).pack(expand=True)

        result_label = tk.Text(self, height=50)
        result_label.pack(fill="both", anchor="s")


if __name__ == "__main__":
    app = App()
    app.mainloop()
