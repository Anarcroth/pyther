#!bin/python3

import curses
import threading

class Draw(object):

    def __init__(self, stdscr):
        self.height, self.width = stdscr.getmaxyx()
        self.main_panel_y, self.main_panel_x = int(self.height / 3), int(self.width / 3)

        self.input_panel_y = int(self.main_panel_y)
        self.input_panel_x_lf = int(self.main_panel_x + self.main_panel_x / 4)
        self.input_panel_x_ri = int(self.main_panel_x * 2 - self.main_panel_x / 4)

        self.pl_input_y, self.pl_input_x = self.input_panel_y + 1, self.input_panel_x_lf + 1

        self.max_panel_len = self.main_panel_x * 2 - 2

        self.time = 0

    def main_menu(self, stdscr):
        #stdscr.nodelay(False);
        stdscr.clear();
        stdscr.border();

        option = 0;
        selection = -1;
        while selection < 0:
            graphics = [0] * 4;
            graphics[option] = curses.A_REVERSE;

            stdscr.addstr(int(self.height / 2 - 5), int(self.width / 2 - 8), "Welcome to Pyther");
            stdscr.addstr(int(self.height / 2 - 2), int(self.width / 2 - 6), "Start typing", graphics[0]);
            stdscr.addstr(int(self.height / 2 - 1), int(self.width / 2 - 3), "Modes", graphics[1]);
            stdscr.addstr(int(self.height / 2), int(self.width / 2 - 5), "High scores", graphics[2]);
            stdscr.addstr(int(self.height / 2 + 1), int(self.width / 2 - 2), "Exit", graphics[3]);

            stdscr.refresh();

            action = stdscr.getch();
            if action == curses.KEY_UP:
                option = (option - 1) % 4;
            elif action == curses.KEY_DOWN:
                option = (option + 1) % 4;
            elif action == ord("\n"):
                selection = option;

        return selection

    def main_panel(self, stdscr):
        for n in range(self.main_panel_x):
            stdscr.addstr(self.main_panel_y - 5, self.main_panel_x + n, "-") # TODO use -> (curses.ACS_HLINE)
            stdscr.addstr(self.main_panel_y - 1, self.main_panel_x + n, "-")

        stdscr.addstr(self.main_panel_y - 4, self.main_panel_x, "|")
        stdscr.addstr(self.main_panel_y - 3, self.main_panel_x, "|")
        stdscr.addstr(self.main_panel_y - 2, self.main_panel_x, "|")
        stdscr.addstr(self.main_panel_y - 4, self.main_panel_x * 2 - 1, "|")
        stdscr.addstr(self.main_panel_y - 3, self.main_panel_x * 2 - 1, "|")
        stdscr.addstr(self.main_panel_y - 2, self.main_panel_x * 2 - 1, "|")

    def clock(self, stdscr):
        stdscr.addstr(self.main_panel_y - 3, self.max_panel_len + 5, str(self.time))

    def input_panel(self, stdscr):
        for n in range(self.input_panel_x_ri - self.input_panel_x_lf + 1):
            stdscr.addstr(self.input_panel_y, self.input_panel_x_lf + n, "-")
            stdscr.addstr(self.input_panel_y + 2, self.input_panel_x_lf + n, "-")

        stdscr.addstr(self.input_panel_y + 1, self.input_panel_x_lf, "|")
        stdscr.addstr(self.input_panel_y + 1, self.input_panel_x_ri , "|")

    def words(self, stdscr, words):
        lines = 4
        prev_pos_x = 0
        current_word = True
        for word in words:
            if self.main_panel_x + prev_pos_x + len(word) > self.max_panel_len:
                lines -= 1
                prev_pos_x = 0
            if lines < 2:
                break
            if words[word] == True:
                stdscr.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.color_pair(1))
            elif words[word] == False:
                stdscr.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.color_pair(2))
            elif not current_word:
                stdscr.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word)
            else:
                stdscr.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.A_BOLD)
                current_word = False

            prev_pos_x += len(word + " ")

    def check_first_line(self, words):
        line_len = 0
        prev_pos_x = 0
        past_words = []
        line_complete = False
        for word in words:
            line_len += 1
            if words[word] != None:
                past_words.append(word)
            if self.main_panel_x + prev_pos_x + len(word) > self.max_panel_len and line_len == len(past_words) + 1:
                line_complete = True
                break
            prev_pos_x += len(word + " ")

        if line_complete:
            for wo in past_words: del words[wo]
            return True
        return False
