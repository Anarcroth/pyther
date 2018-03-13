#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import time

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
    input = stdscr.getstr(y, x, 20)
    return input

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
        stdscr.addstr(main_panel_y - 5, main_panel_x + n, "-") # TODO use -> (curses.ACS_HLINE)
        stdscr.addstr(main_panel_y - 1, main_panel_x + n, "-")

    # Add side borders
    stdscr.addstr(main_panel_y - 4, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 4, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x * 2 - 1, "|")

def init_pyther(stdscr):
    height, width = stdscr.getmaxyx()

    main_panel_y, main_panel_x = int(height / 3), int(width / 3)

    player_str = 0

    stdscr.clear()
    stdscr.refresh()

    words = open("./word_lists/200.txt").read().split("\n")
    random.shuffle(words)

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (player_str != "q"):

        # Initialization
        stdscr.clear()
        stdscr.border()

        stdscr.addstr("height: " + str(height))
        stdscr.addstr("width: " + str(width))

        paint_main_panel(stdscr, main_panel_y, main_panel_x)

        put_words(stdscr, main_panel_y, main_panel_x, words)

        # Wait for next input
        player_str = player_input(stdscr, 1, 0)

        stdscr.addstr(10, 10, player_str)

        # Refresh the screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main_menu)

#def calc_words_score():

#def is_correct():

#def print_text():
