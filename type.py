#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import time

words = 0
errors = 0

def main_menu(stdscr):
    stdscr.nodelay(0);
    stdscr.clear();
    stdscr.border();

    height, width = stdscr.getmaxyx();
    option = 0;
    selection = -1;
    while selection < 0:
        graphics = [0]*4;
        graphics[option] = curses.A_REVERSE;

        stdscr.addstr(int(height / 2 - 5), int(width / 2 - 8), "Welcome to Pyther");
        stdscr.addstr(int(height / 2 - 2), int(width / 2 - 6), "Start typing", graphics[0]);
        stdscr.addstr(int(height / 2 - 1), int(width / 2 - 3), "Modes", graphics[1]);
        stdscr.addstr(int(height / 2), int(width / 2 - 5), "High scores", graphics[2]);
        stdscr.addstr(int(height / 2 + 1), int(width / 2 - 2), "Exit", graphics[3]);

        stdscr.refresh();

        action = stdscr.getch();
        if action == curses.KEY_UP:
            option = (option - 1) % 4;
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 4;
        elif action == ord("\n"):
            selection = option;

        if selection == 0:
            init_pyther(stdscr);
        elif selection == 1:
            # TODO show different modes
            return;
        elif selection == 2:
            # TODO shows high scores
            return;
        elif selection == 3:
            sys.exit();

def player_input(stdscr, y, x):
    curses.echo()
    # I am at this stage of my programming life where I hate encodings
    #                          Fuck this thing \/
    str_in = stdscr.getstr(y, x, 20).decode(encoding="utf-8")
    return str_in

def put_words(stdscr, main_panel_y, main_panel_x, words):
    n = 4;
    prev_pos_x = 0
    for word in words:
        if main_panel_x + prev_pos_x + len(word) > main_panel_x * 2 - 2:
            n -= 1
            prev_pos_x = 0
        if n < 2:
            break
        stdscr.addstr(main_panel_y - n, main_panel_x + prev_pos_x + 1, word)
        prev_pos_x += len(word + " ")

def paint_main_panel(stdscr, main_panel_y, main_panel_x):
    # Add top and bottom borders
    for n in range(main_panel_x):
        stdscr.addstr(main_panel_y - 5, main_panel_x + n, "-") # TODO use -> (curses.ACS_HELENE)
        stdscr.addstr(main_panel_y - 1, main_panel_x + n, "-")

    # Add side borders
    stdscr.addstr(main_panel_y - 4, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 4, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x * 2 - 1, "|")

def paint_input_panel(stdscr, input_panel_y, input_panel_x_lf, input_panel_x_ri):
    # Add top and bottom borders
    for n in range(input_panel_x_ri - input_panel_x_lf + 1):
        stdscr.addstr(input_panel_y, input_panel_x_lf + n, "-")
        stdscr.addstr(input_panel_y + 2, input_panel_x_lf + n, "-")

    # Add side borders
    stdscr.addstr(input_panel_y + 1, input_panel_x_lf, "|")
    stdscr.addstr(input_panel_y + 1, input_panel_x_ri , "|")

def is_pl_correct(pl_str, words):
    if pl_str == words[0]:
        words += len(words[0])
        del words[0]

def net_wpm():
    return (words / 5 + errors) / time

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

    words = open("./word_lists/200.txt").read().split("\n")
    random.shuffle(words)

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (pl_str != "q"):

        # Initialization
        stdscr.clear()
        stdscr.border()

        stdscr.addstr("height: " + str(len(words)))
        stdscr.addstr("width: " + str(width))

        paint_main_panel(stdscr, main_panel_y, main_panel_x)
        paint_input_panel(stdscr, input_panel_y, input_panel_x_lf, input_panel_x_ri)

        put_words(stdscr, main_panel_y, main_panel_x, words)

        pl_str = player_input(stdscr, pl_input_y, pl_input_x)
        is_pl_correct(pl_str, words)

        # Refresh the screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main_menu)

#def print_text():
