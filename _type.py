#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
#import sys.argv
import curses
import random
import time
import threading
from _draw import Draw
from _player import Player

class Pyther(object):

    def __init__(self, file_path):
        self.words = open(file_path).read().split("\n")
        self.draw = Draw()
        self.player = Player()

    def make_choice(self, stdscr):
        choice = self.draw.main_menu(stdscr)
        if choice == 0:
            self.init_screen(stdscr)
        elif choice == 1:
            # TODO show different modes
            return;
        elif choice == 2:
            # TODO shows high scores
            return;
        elif choice == 3:
            sys.exit();

    def init(self, stdscr):
        self.draw.init(stdscr)
        self.make_choice(stdscr)

    def get_words_from(self):
        random.shuffle(self.words)
        return { w : None for w in self.words }


    def incr_clock(self, stdscr, clk):
        self.draw.clock(stdscr)
        self.draw.time += 1
        if not clk.is_set():
            threading.Timer(1, self.incr_clock, [stdscr, clk]).start()

    def run(self, stdscr):
        word_counter = 0
        randomized_words = self.get_words_from()

        while self.draw.time < 61:
            stdscr.clear()
            stdscr.border()

            self.draw.main_panel(stdscr)
            self.draw.input_panel(stdscr)
            self.draw.clock(stdscr)

            if self.draw.check_first_line(randomized_words):
                word_counter = 0

            self.draw.words(stdscr, randomized_words)

            self.player.input(stdscr, self.draw.pl_input_y, self.draw.pl_input_x)
            self.player.is_correct(randomized_words, word_counter)
            word_counter += 1

            stdscr.refresh()

    def init_screen(self, stdscr):

        stdscr.clear()
        stdscr.refresh()

        stdscr.nodelay(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        type_clock = threading.Event()
        self.incr_clock(stdscr, type_clock)

        self.run(stdscr)

        #type_clock.set()

        del type_clock

        stdscr.clear()
        stdscr.refresh()

        self.make_choice(stdscr)

if __name__ == "__main__":
    pyther = Pyther("./word_lists/200.txt")
    curses.wrapper(pyther.init)
