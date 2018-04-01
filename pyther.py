#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import threading
import time
from draw import Draw
from player import Player

class Pyther(object):

    def __init__(self, file_path):
        self.time = 0

        self.line_words = ['']

    def make_choice(self, stdscr, draw, player):
        choice = draw.main_menu(screen)
        if choice == 0:
            self.init_pyther_screen()
            self.run(draw, player)
        elif choice == 1:
            # TODO show different modes
            return;
        elif choice == 2:
            # TODO shows high scores
            return;
        elif choice == 3:
            sys.exit();

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

<<<<<<< HEAD
        pl_str = ''
=======
        while draw.time < 61:
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

            self.drwords()

            _input = screen.getch(pl_input_y, pl_input_x + len(pl_str))
            self.inp(player, _input, pl_str, word_counter)
            #player.input(stdscr, draw.pl_input_y, draw.pl_input_x)

            word_counter += 1

            screen.refresh()

        #type_clock.set()
        #del type_clock

        player.save_score()
        self.make_choice(screen)

    def init_pyther_screen(self):

        screen.clear()
        screen.refresh()

        screen.nodelay(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

def setup_pyther(stdscr):
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

if __name__ == "__main__":
    curses.wrapper(setup_pyther)
