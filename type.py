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


def init_pyther(stdscr):
    height, width = stdscr.getmaxyx()

    main_panel_y, main_panel_x = int(height / 3), int(width / 3)

    player_input = 0
    cursor_x = 0
    cursor_y = 0

    stdscr.clear()
    stdscr.refresh()

    words = open("./word_lists/200.txt").read().split("\n");

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (player_input != ord('q')):

        # Initialization
        stdscr.clear()
        stdscr.border()

        stdscr.addstr("height: " + str(height))
        stdscr.addstr("width: " + str(width))

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

        # TODO optimize selection of words and outputting them to the screen
        prev_pos_x1, prev_pos_x2, prev_pos_x3 = 0, 0, 0;
        for word in words:
            rand_word1 = random.choice(words)
            rand_word2 = random.choice(words)
            rand_word3 = random.choice(words)
            if main_panel_x + prev_pos_x1 + len(rand_word1) > main_panel_x * 2 - 2:
                break;
            if main_panel_x + prev_pos_x2 + len(rand_word2) > main_panel_x * 2 - 2:
                break;
            if main_panel_x + prev_pos_x3 + len(rand_word3) > main_panel_x * 2 - 2:
                break;
            stdscr.addstr(main_panel_y - 4, main_panel_x + prev_pos_x1 + 1, rand_word1)
            stdscr.addstr(main_panel_y - 3, main_panel_x + prev_pos_x2 + 1, rand_word2)
            stdscr.addstr(main_panel_y - 2, main_panel_x + prev_pos_x3 + 1, rand_word3)
            prev_pos_x1 += len(rand_word1 + " ")
            prev_pos_x2 += len(rand_word2 + " ")
            prev_pos_x3 += len(rand_word3 + " ")


        if player_input == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif player_input == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif player_input == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif player_input == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Centering title screen
        #start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        #start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        #start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        #start_y = int((height // 2) - 2)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        player_input = stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main_menu)

#def calc_words_score():

#def is_correct():

#def print_text():
