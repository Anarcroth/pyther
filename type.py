#!bin/python3

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

        stdscr.addstr(int(height / 2 - 5), int(width / 2 - 3), "Pyther");
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
            return;
        elif selection == 1:
            # TODO show different modes
            return;
        elif selection == 2:
            # TODO shows high scores
            return;
        elif selection == 3:
            sys.exit();


def draw_menu(stdscr):
    main_menu(stdscr);
    player_input = 0
    cursor_x = 0
    cursor_y = 0

    stdscr.clear()
    stdscr.refresh()

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
        height, width = stdscr.getmaxyx()

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

        # Declaration of strings
        title = "Welcome to Pyther"[:width-1]
        subtitle = "Select mode"[:width-1]
        mode = "Last key pressed: {}".format(player_input)[:width-1]
        if player_input == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering title screen
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y, start_x_title, title, curses.color_pair(2))
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        player_input = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()

#def calc_words_score():

#def is_correct():

#def print_text():
