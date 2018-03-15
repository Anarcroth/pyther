#!bin/python3

import curses
import _type

def _main_menu(stdscr):
    stdscr.nodelay(0);
    stdscr.clear();
    stdscr.border();

    height, width = stdscr.getmaxyx();
    option = 0;
    selection = -1;
    while selection < 0:
        graphics = [0] * 4;
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
            _type.init_pyther(stdscr);
        elif selection == 1:
            # TODO show different modes
            return;
        elif selection == 2:
            # TODO shows high scores
            return;
        elif selection == 3:
            sys.exit();

def _main_panel(stdscr, main_panel_y, main_panel_x):
    for n in range(main_panel_x):
        stdscr.addstr(main_panel_y - 5, main_panel_x + n, "-") # TODO use -> (curses.ACS_HLINE)
        stdscr.addstr(main_panel_y - 1, main_panel_x + n, "-")

    stdscr.addstr(main_panel_y - 4, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x, "|")
    stdscr.addstr(main_panel_y - 4, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 3, main_panel_x * 2 - 1, "|")
    stdscr.addstr(main_panel_y - 2, main_panel_x * 2 - 1, "|")

def _input_panel(stdscr, input_panel_y, input_panel_x_lf, input_panel_x_ri):
    for n in range(input_panel_x_ri - input_panel_x_lf + 1):
        stdscr.addstr(input_panel_y, input_panel_x_lf + n, "-")
        stdscr.addstr(input_panel_y + 2, input_panel_x_lf + n, "-")

    stdscr.addstr(input_panel_y + 1, input_panel_x_lf, "|")
    stdscr.addstr(input_panel_y + 1, input_panel_x_ri , "|")

def _words(stdscr, main_panel_y, main_panel_x, words):
    current_word = True
    lines = 4
    prev_pos_x = 0
    for word in words:
        if main_panel_x + prev_pos_x + len(word) > main_panel_x * 2 - 2:
            lines -= 1
            prev_pos_x = 0
        if lines < 2:
            break
        if words[word] == True:
            stdscr.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.color_pair(1))
        elif not current_word:
            stdscr.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word)
        else:
            stdscr.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.A_BOLD)
            current_word = False
        prev_pos_x += len(word + " ")
