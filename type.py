#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import time
import draw

correct_words = 0
errors = 0

def player_input(stdscr, y, x):
    curses.echo()
    # I am at this stage of my programming life where I hate encodings
    #                          Fuck this thing \/
    str_in = stdscr.getstr(y, x, 20).decode(encoding="utf-8")
    return str_in

def is_pl_correct(pl_str, words):
    if pl_str in words: words[pl_str] = True

def net_wpm():
    return (correcrt_words / 5 + errors) / time

def get_words_from(_file):
    words = open(_file).read().split("\n")
    random.shuffle(words)
    return { w : False for w in words }

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

    randomized_words = get_words_from("./word_lists/200.txt")

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:

        # Initialization
        stdscr.clear()
        stdscr.border()

        stdscr.addstr("height: " + str(len(randomized_words)))
        stdscr.addstr("width: " + str(width))

        draw._main_panel(stdscr, main_panel_y, main_panel_x)
        draw._input_panel(stdscr, input_panel_y, input_panel_x_lf, input_panel_x_ri)

        draw._words(stdscr, main_panel_y, main_panel_x, randomized_words)

        pl_str = player_input(stdscr, pl_input_y, pl_input_x)
        is_pl_correct(pl_str, randomized_words)

        # Refresh the screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(draw._main_menu)
