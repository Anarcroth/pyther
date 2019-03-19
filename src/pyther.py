#!bin/python3
# -*- coding: utf-8 -*-

import sys
import curses
import threading
import json
from words import Words
from draw import Draw
from player import Player


class Pyther(object):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, file_path):
        self.time = 0

        self.line_words = ['']

    def make_choice(self, stdscr, draw, player):
        choice = draw.main_menu(screen)
        if choice == 0:
            self.init_pyther_screen()
            self.run(draw, player)
=======
    def make_choice(self):
        choice = draw.main_menu(screen)
=======
    def make_choice(self, player = None):
=======
    def make_choice(self, player=None):
>>>>>>> 83cf9bb... Formats code to pip and adds curses key codes
        choice = draw.main_menu(screen, player)
>>>>>>> c8d258d... Added score when game is finished
        if choice == 0:
            self.init_pyther_screen()
            self.run()
>>>>>>> 3bb0c9e... Refactored code to use globals instead of passing big objects
        elif choice == 1:
            screen.addstr(int(self.height / 2 - 1),
                          int(self.width / 2 - 3), "TBA")
        elif choice == 2:
            draw.high_scores(screen, self.get_scores("../scores"))
            self.make_choice()
        elif choice == 3:
            sys.exit()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #def randomize_words(self):

    def inp(self, player, _input, pl_str, word_counter):
        if _input != -1:
            if _input == 32: # SPACE
                player.is_correct(words, word_counter, pl_str)
            elif _input == 263: # BACKSPACE
                if len(pl_str) == 0:
                    return
                screen.addstr(y, x + len(pl_str) - 1, ' ')
                pl_str = pl_str[:-1]
                player.num_key_presses += 1
            elif _input == 269: # F5
                pyther.init_pyther_screen(screen)
            elif _input > 0:
                pl_str += chr(_input)
                player.num_key_presses += 1

    def drwords(self):
        lines = 4
        prev_pos_x = 0
        current_word = True
        current_line = True
        self.line_words = []
        for word in words:
            if main_panel_x + prev_pos_x + len(word) > max_panel_len:
                current_line = False
                lines -= 1
                prev_pos_x = 0
            if current_line and word != None:
                self.line_words.append(word)
            if lines < 2:
                break
            if words[word] == True:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.color_pair(1))
            elif words[word] == False:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.color_pair(2))
            elif not current_word:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word)
            else:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.A_BOLD)
                current_word = False

            prev_pos_x += len(word + " ")


    def check_first_line(self):
        if words[self.line_words[-1]] != None:
            for w in self.line_words: del words[w]
            return True
        return False

    def run(self, player):
        #type_clock = threading.Event()
        #draw.init_clock(stdscr, type_clock)

        word_counter = 0
        #self.randomize_words()

        screen.nodelay(True)
        curses.echo()
=======
    def run(self):
        words = open("./word_lists/200.txt").read().split("\n")
=======
=======
    def get_scores(file_path):
        with open(file_path, "r") as pl_file:
            for line in pl_file:
                #TODO
                return
=======
    def get_scores(self, file_path):
        with open(file_path) as pl_file:
            data = json.load(pl_file)
            return data[:3]
>>>>>>> 6f3dda2... Added json files for scores, where now everthing outputst properly

>>>>>>> 51f3a16... WIP: output the top 3 best scores from the third menu option
    def init_clock(self, clk):
        draw.time += 1
        if not clk.is_set():
            threading.Timer(1, self.init_clock, [clk]).start()
        return draw.time

<<<<<<< HEAD

<<<<<<< HEAD
    def get_words_from(self, path):
        words = open(path).read().split("\n")
>>>>>>> da75115... General bug fixes and exception handling
        random.shuffle(words)
        return { w : None for w in words }

=======
>>>>>>> ad2b5a7... Added words class,WIP
=======
>>>>>>> 83cf9bb... Formats code to pip and adds curses key codes
    def run(self):
        player = Player(draw.pl_input_y, draw.pl_input_x)

        words.get_words()

        draw.time = 0
        word_counter = 0
>>>>>>> 3bb0c9e... Refactored code to use globals instead of passing big objects

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        pl_str = ''
=======
=======
        type_clock = threading.Event()
        self.init_clock(type_clock)

>>>>>>> 992da1c... Minot changes and fixes
        while draw.time < 61:
<<<<<<< HEAD
            time.sleep(1)
            stdscr.clear()
            stdscr.border()
>>>>>>> b004280... Added time sleep to 1

        while True:
            time.sleep(0.09)
            screen.clear()
            screen.border()

            #draw.main_panel(stdscr)
            #draw.input_panel(stdscr)

            if self.check_first_line():
                word_counter = 0

<<<<<<< HEAD
<<<<<<< HEAD
            self.drwords()

            _input = screen.getch(pl_input_y, pl_input_x + len(pl_str))
            self.inp(player, _input, pl_str, word_counter)
            #player.input(stdscr, draw.pl_input_y, draw.pl_input_x)

<<<<<<< HEAD
=======
=======
        while draw.time < 60:
>>>>>>> 8ae3411... Added ESC char to exit pyther
=======
        while draw.time < 10:
>>>>>>> 0082a94... Bugfixes for words, game restart, exceptions for scores that are 0
=======
        while draw.time < 61:
>>>>>>> e964d78... Updated README and LICENSE
=======
        while draw.time < 10:
>>>>>>> c8d258d... Added score when game is finished
=======
        while draw.time < 61:
>>>>>>> 97b8c70... Fixed game length, fixed readme
            screen.clear()
            screen.border()

            if player.restart:
                type_clock.set()
                self.run()

            draw.main_panel(screen)
            draw.input_panel(screen)

            if draw.check_first_line(words._list):
                word_counter = 0

            draw.standard_words(screen, words._list)

<<<<<<< HEAD
            player.input(screen, type_clock)
<<<<<<< HEAD
            player.is_correct(words, word_counter)
>>>>>>> 3bb0c9e... Refactored code to use globals instead of passing big objects
=======
            player.is_correct(words._list, word_counter)
>>>>>>> ad2b5a7... Added words class,WIP
=======
            player.input(screen, type_clock, words._list, word_counter)
>>>>>>> 992da1c... Minot changes and fixes
            word_counter += 1

            screen.refresh()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #type_clock.set()
        #del type_clock

        player.save_score()
        self.make_choice(screen)
=======
=======
        #type_clock.wait
>>>>>>> 36f7f0c... Handeled KeyboardInterrupt
=======
        type_clock.wait(1)
>>>>>>> 0082a94... Bugfixes for words, game restart, exceptions for scores that are 0
=======
>>>>>>> da75115... General bug fixes and exception handling
        type_clock.set()

        screen.clear()
        screen.refresh()

        player.save_score()
<<<<<<< HEAD
        self.make_choice()
>>>>>>> 3bb0c9e... Refactored code to use globals instead of passing big objects
=======
        self.make_choice(player)
>>>>>>> c8d258d... Added score when game is finished

    def init_pyther_screen(self):
        curses.echo()

        screen.clear()
        screen.refresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


def setup_pyther(stdscr):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    global screen
    screen = stdscr.subwin(0,0)
    screen.box()

    global height, width, main_panel_y, main_panel_x, input_panel_y, input_panel_x_lf, input_panel_x_ri, pl_input_y, pl_input_x, max_panel_len, words

    height, width = screen.getmaxyx()
    main_panel_y, main_panel_x = int(height / 3), int(width / 3)

    input_panel_y = int(main_panel_y)
    input_panel_x_lf = int(main_panel_x + main_panel_x / 4)
    input_panel_x_ri = int(main_panel_x * 2 - main_panel_x / 4)

    pl_input_y, pl_input_x = input_panel_y + 1, input_panel_x_lf + 1
    max_panel_len = main_panel_x * 2 - 2

    words = open("./word_lists/200.txt").read().split("\n")
    random.shuffle(words)
    words = { w : None for w in words }

    pyther = Pyther("./word_lists/200.txt")
    draw = Draw(stdscr)
    player = Player()
    pyther.init_pyther_screen()
    pyther.run(player)
=======
    global draw, player, words, screen
=======
    global draw, player, screen
    global words
>>>>>>> 0082a94... Bugfixes for words, game restart, exceptions for scores that are 0
=======
    global draw, screen
>>>>>>> da75115... General bug fixes and exception handling
=======
    global draw, screen, words
>>>>>>> ad2b5a7... Added words class,WIP

    screen = stdscr
    pyther = Pyther()
    draw = Draw(screen)
    words = Words()

    pyther.make_choice()
>>>>>>> 3bb0c9e... Refactored code to use globals instead of passing big objects


if __name__ == "__main__":
    curses.wrapper(setup_pyther)
