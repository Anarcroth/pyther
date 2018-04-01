#!bin/python3
# -*- coding: utf-8 -*-

import curses
import threading
import locale

locale.setlocale(locale.LC_ALL, '')

class Draw(object):

    def __init__(self, screen):
        self.height, self.width = screen.getmaxyx()
        self.main_panel_y, self.main_panel_x = int(self.height / 3), int(self.width / 3)
        self.main_panel_x_ri = int(self.main_panel_x * 2)
        self.input_panel_y = int(self.main_panel_y)
        self.input_panel_x_lf = int(self.main_panel_x + self.main_panel_x / 4)
        self.input_panel_x_ri = int(self.main_panel_x * 2 - self.main_panel_x / 4)
        self.pl_input_y, self.pl_input_x = self.input_panel_y + 1, self.input_panel_x_lf + 1
        self.max_panel_len = self.main_panel_x * 2 - 2

        self.time = 0

        self.line_words = ['']

    def main_menu(self, screen):
        screen.clear();
        screen.border();

        option = 0;
        selection = -1;
        while selection < 0:
            graphics = [0] * 4;
            graphics[option] = curses.A_REVERSE;

            screen.addstr(int(self.height / 2 - 5), int(self.width / 2 - 8), "Welcome to Pyther");
            screen.addstr(int(self.height / 2 - 2), int(self.width / 2 - 6), "Start typing", graphics[0]);
            screen.addstr(int(self.height / 2 - 1), int(self.width / 2 - 3), "Modes", graphics[1]);
            screen.addstr(int(self.height / 2), int(self.width / 2 - 5), "High scores", graphics[2]);
            screen.addstr(int(self.height / 2 + 1), int(self.width / 2 - 2), "Exit", graphics[3]);

            screen.refresh();

            action = screen.getch();
            if action == curses.KEY_UP:
                option = (option - 1) % 4;
            elif action == curses.KEY_DOWN:
                option = (option + 1) % 4;
            elif action == ord("\n"):
                selection = option;

        return selection

    def main_panel(self, screen):
        for n in range(1, self.main_panel_x - 1):
            screen.addstr(self.main_panel_y - 5, self.main_panel_x + n, "─")
            screen.addstr(self.main_panel_y - 1, self.main_panel_x + n, "─")

        screen.addstr(self.main_panel_y - 5, self.main_panel_x, "┌")
        screen.addstr(self.main_panel_y - 1, self.main_panel_x, "└")

        screen.addstr(self.main_panel_y - 5, self.main_panel_x_ri - 1, "┐")
        screen.addstr(self.main_panel_y - 1, self.main_panel_x_ri - 1, "┘")

        screen.addstr(self.main_panel_y - 4, self.main_panel_x, "│")
        screen.addstr(self.main_panel_y - 3, self.main_panel_x, "│")
        screen.addstr(self.main_panel_y - 2, self.main_panel_x, "│")
        screen.addstr(self.main_panel_y - 4, self.main_panel_x_ri - 1, "│")
        screen.addstr(self.main_panel_y - 3, self.main_panel_x_ri - 1, "│")
        screen.addstr(self.main_panel_y - 2, self.main_panel_x_ri - 1, "│")

        # Draw time
        screen.addstr(self.main_panel_y - 3, self.max_panel_len + 5, str(self.time))

    def init_clock(self, screen, clk):
        self.time += 1
        if not clk.is_set():
            threading.Timer(1, self.init_clock, [screen, clk]).start()

    def input_panel(self, screen):
        for n in range(1, self.input_panel_x_ri - self.input_panel_x_lf):
            screen.addstr(self.input_panel_y, self.input_panel_x_lf + n, "─")
            screen.addstr(self.input_panel_y + 2, self.input_panel_x_lf + n, "─")

        screen.addstr(self.input_panel_y, self.input_panel_x_lf, "┌")
        screen.addstr(self.input_panel_y + 2, self.input_panel_x_lf, "└")

        screen.addstr(self.input_panel_y, self.input_panel_x_ri, "┐")
        screen.addstr(self.input_panel_y + 2, self.input_panel_x_ri, "┘")

        screen.addstr(self.input_panel_y + 1, self.input_panel_x_lf, "│")
        screen.addstr(self.input_panel_y + 1, self.input_panel_x_ri , "│")

    def words(self, screen, words):
        lines = 4
        prev_pos_x = 0
        current_word = True
        current_line = True
        self.line_words = []
        for word in words:
            if self.main_panel_x + prev_pos_x + len(word) > self.max_panel_len:
                current_line = False
                lines -= 1
                prev_pos_x = 0
            if current_line and word != None:
                self.line_words.append(word)
            if lines < 2:
                break
            if words[word] == True:
                screen.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.color_pair(1))
            elif words[word] == False:
                screen.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.color_pair(2))
            elif not current_word:
                screen.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word)
            else:
                screen.addstr(self.main_panel_y - lines, self.main_panel_x + prev_pos_x + 1, word, curses.A_BOLD)
                current_word = False

            prev_pos_x += len(word + " ")

    def check_first_line(self, words):
        if words[self.line_words[-1]] != None:
            for w in self.line_words: del words[w]
            return True
        return False
