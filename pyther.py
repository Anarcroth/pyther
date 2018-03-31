#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import threading
from draw import Draw
from player import Player

class Pyther(object):

    def __init__(self, file_path):
        self.words = open(file_path).read().split("\n")

    def make_choice(self, stdscr, draw, player):
        choice = draw.main_menu(stdscr)
        if choice == 0:
            self.init_pyther_screen(stdscr)
            self.run(stdscr, draw, player)
        elif choice == 1:
            # TODO show different modes
            return;
        elif choice == 2:
            # TODO shows high scores
            return;
        elif choice == 3:
            sys.exit();

    def get_words_from(self):
        random.shuffle(self.words)
        return { w : None for w in self.words }

    def run(self, stdscr, draw, player):
        type_clock = threading.Event()
        draw.init_clock(stdscr, type_clock)

        word_counter = 0
        randomized_words = self.get_words_from()

        while draw.time < 61:
            stdscr.clear()
            stdscr.border()

            draw.main_panel(stdscr)
            draw.input_panel(stdscr)

            if draw.check_first_line(randomized_words):
                word_counter = 0

            draw.words(stdscr, randomized_words)

            player.input(stdscr, draw.pl_input_y, draw.pl_input_x)
            player.is_correct(randomized_words, word_counter)
            word_counter += 1

            stdscr.refresh()

        #type_clock.set()
        del type_clock

        player.save_score()
        self.make_choice(stdscr)

    def init_pyther_screen(self, stdscr):

        stdscr.clear()
        stdscr.refresh()

        stdscr.nodelay(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

def setup_pyther(stdscr):
    pyther = Pyther("./word_lists/200.txt")
    draw = Draw(stdscr)
    player = Player()
    pyther.make_choice(stdscr, draw, player)

if __name__ == "__main__":
    curses.wrapper(setup_pyther)
