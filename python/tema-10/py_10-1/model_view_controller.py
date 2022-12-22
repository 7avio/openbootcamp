import tkinter as tk
import random as rand
from tkinter import W, E
from tkinter import DISABLED, ACTIVE
from tkinter import LEFT


class Model(object):
    options = ['Rock', 'Paper', 'Scissors']

    score = [0, 0]

    def set_pc_choice(self, options):
        choice = options[(round(rand.random() * (len(options)-1)))]
        return choice

    def battle(self, player_choice, pc_choice):
        self.player_choice = player_choice
        self.pc_choice = pc_choice
        self.messages = ['It\'s a draw', 'You Win!', 'You Lose']
        # self.match_result = ''

        if player_choice == pc_choice:
            print(self.messages[0], self.score)
            # self.score[0] += 0
            return self.messages[0]
        elif (self.player_choice == 'Rock') and (self.pc_choice == 'Scissors'):
            print(self.messages[1])
            self.score[0] += 1
            return self.messages[1]
        elif (self.player_choice == 'Paper') and (self.pc_choice == 'Rock'):
            print(self.messages[1])
            self.score[0] += 1
            return self.messages[1]
        elif (self.player_choice == 'Scissors') and (self.pc_choice == 'Paper'):
            print(self.messages[1])
            self.score[0] += 1
            return self.messages[1]
        else:
            print(self.messages[2])
            self.score[1] += 1
            return self.messages[2]


class View(object):

    def disable_rematch_button(self, button):
        self.button = button
        self.button.config(state=DISABLED)

    def enable_button(self, button):
        self.button = button
        if not self.button.config(state=DISABLED):
            self.button.config(state=ACTIVE)

    def place_radio_buttons(self, frame, options):
        self.i = 0
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        for item in options:
            rb_player = tk.Radiobutton(
                frame,
                text=item,
                value=item,
                tristatevalue=0,
                variable=self.player_selection,
                justify=LEFT,
                anchor=E,
                command=lambda: self.enable_button(self.btn_play)
            )
            rb_player.grid(column=0, row=self.i, sticky=W)
            self.i += 1

    def __init__(self, root):
        self.root = root
        self.pc_choice = tk.StringVar()
        self.pc_choice.set('')
        self.player_selection = tk.StringVar()
        self.player_selection.set('')
        self.result = tk.StringVar()
        self.result.set('')
        self.player_score = tk.IntVar()
        self.pc_score = tk.IntVar()
        self.frm_scoreboard = tk.Frame(root)
        self.frm_options = tk.Frame(root)
        self.fnt_title = "OpenSans", 20, "bold"
        self.fnt_scorer = "OpenSans", 30, "bold"
        self.fnt_std = "OpenSans", 14, "bold"

        lbl_title = tk.Label(root, text='Let\'s play', fg='red', font=self.fnt_title)
        lbl_player = tk.Label(root, text='Select your choice', font=self.fnt_std)
        lbl_pc = tk.Label(root, text='Press start to see\n the PC\'s choice', font=self.fnt_std)
        self.lbl_pc_choice = tk.Label(root, textvariable=self.pc_choice)
        self.btn_play = tk.Button(root, text='Play', state=DISABLED)
        self.lbl_result = tk.Label(root, textvariable=self.result)
        self.lbl_player_score = tk.Label(
            self.frm_scoreboard,
            textvariable=self.player_score,
            bg='black',
            fg='white',
            font=self.fnt_scorer)
        self.lbl_score_hyphen = tk.Label(
            self.frm_scoreboard,
            text='-',
            bg='black',
            fg='white',
            font=self.fnt_scorer)
        self.lbl_pc_score = tk.Label(
            self.frm_scoreboard,
            textvariable=self.pc_score,
            bg='black',
            fg='white',
            font=self.fnt_scorer)
        self.btn_reset = tk.Button(root, text='Reset', state=DISABLED)

        # grid-configuration
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)

        # element' placement
        lbl_title.grid(column=1, row=0)
        lbl_player.grid(column=0, row=1)
        lbl_pc.grid(column=2, row=1)
        self.lbl_pc_choice.grid(column=2, row=2, rowspan=2)
        self.frm_options.grid(column=0, row=2, rowspan=2)
        self.btn_play.grid(column=1, row=3)
        self.lbl_result.grid(column=1, row=2)
        self.frm_scoreboard.grid(column=1, row=4)
        self.lbl_player_score.grid(column=0, row=0)
        self.lbl_score_hyphen.grid(column=1, row=0)
        self.lbl_pc_score.grid(column=2, row=0)
        self.btn_reset.grid(column=1, row=5)


class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.options = self.model.options
        self.view.btn_play.bind('<Button>', self.start_match)
        self.view.btn_reset.bind('<Button>', self.restart_game)

    def show_interface(self):
        self.view.place_radio_buttons(self.view.frm_options, self.options)

    def start_match(self, another):
        self.pc_turn = (self.model.set_pc_choice(self.options))
        self.player_turn = self.view.player_selection.get()
        self.view.pc_choice.set(self.pc_turn)
        print(self.player_turn)
        print(self.pc_turn)
        battle_result = self.model.battle(self.player_turn, self.pc_turn)
        print(type(battle_result))
        print(battle_result)
        self.view.result.set(battle_result)
        self.view.player_score.set(self.model.score[0])
        self.view.pc_score.set(self.model.score[1])
        self.view.enable_button(self.view.btn_reset)

    def restart_game(self, another):
        self.view.disable_rematch_button(self.view.btn_play)
        self.model.score = [0, 0]
        self.view.player_selection.set('')
        self.view.pc_score.set(0)
        self.view.player_score.set(0)


class App:

    root = tk.Tk()
    root.title('\U0001F311, \U0001F4DD, \U00002702')
    root.geometry('650x400')
    root.resizable(False, False)
    interface = Controller(Model(), View(root))
    interface.show_interface()

    root.mainloop()
