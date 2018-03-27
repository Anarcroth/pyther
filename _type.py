#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import time
import _draw
from _player import Player as _player

correct_words = 0
errors = 0
num_key_presses = 0

def is_pl_correct(pl_str, words, word_counter):
    current_word = list(words.keys())[word_counter]
    if current_word == pl_str:
        words[pl_str] = True
    else:
        words[current_word] = False


def get_words_from(_file):
    words = open(_file).read().split("\n")
    random.shuffle(words)
    return { w : None for w in words }

def init_pyther(stdscr):
    height, width = stdscr.getmaxyx()

    main_panel_y, main_panel_x = int(height / 3), int(width / 3)

    input_panel_y = int(main_panel_y)
    input_panel_x_lf = int(main_panel_x + main_panel_x / 4)
    input_panel_x_ri = int(main_panel_x * 2 - main_panel_x / 4)

    pl_input_y, pl_input_x = input_panel_y + 1, input_panel_x_lf + 1

    pl_str = ""

    stdscr.clear()
    stdscr.refresh()

    word_counter = 0
    randomized_words = get_words_from("./word_lists/200.txt")

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        # Initialization
        stdscr.clear()
        stdscr.border()

        stdscr.addstr("height: " + str(word_counter))
        stdscr.addstr("width: " + str(num_key_presses))

        _draw._main_panel(stdscr, main_panel_y, main_panel_x)
        _draw._input_panel(stdscr, input_panel_y, input_panel_x_lf, input_panel_x_ri)

        _draw._words(stdscr, main_panel_y, main_panel_x, randomized_words)

        pl_str = _player._input(stdscr, pl_input_y, pl_input_x)
        is_pl_correct(pl_str, randomized_words, word_counter)
        word_counter += 1

        # Refresh the screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(_draw._main_menu)
