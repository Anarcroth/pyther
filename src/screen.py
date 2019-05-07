#!bin/python3
# -*- coding: utf-8 -*-

import curses
import locale
import sys
import re
import time

locale.setlocale(locale.LC_ALL, '')


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Screen(metaclass=Singleton):
    def __init__(self, screen):
        self.main_win = screen
        self.height, self.width = screen.getmaxyx()

        self.main_panel_y = int(self.height / 3)
        self.main_panel_x = int(self.width / 3)
        self.main_panel_x_ri = int(self.main_panel_x * 2)
        self.input_panel_y = int(self.main_panel_y)
        self.input_panel_x_lf = int(self.main_panel_x +
                                    self.main_panel_x / 4)
        self.input_panel_x_ri = int(self.main_panel_x * 2 -
                                    self.main_panel_x / 4)
        self.pl_input_y = self.input_panel_y + 1
        self.pl_input_x = self.input_panel_x_lf + 1
        self.max_panel_len = self.main_panel_x * 2 - 2

        self.words_win = curses.newwin(5,
                                       self.main_panel_x_ri,
                                       self.main_panel_y,
                                       self.main_panel_x)
        self.input_win = curses.newwin(3,
                                       self.input_panel_x_ri,
                                       self.input_panel_y,
                                       self.input_panel_x_lf)

        self.time = 1

        self.line_words = ['']

        self.init()

    def main_menu(self, player):
        self.draw_main_men()

    def init(self):
        curses.echo()

        self.main_win.clear()
        self.main_win.refresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        self.main_win.clear()
        self.main_win.border()

    def draw_main_men(self):
        option = 0
        selection = -1
        while selection < 0:
            selected = [0] * 4
            selected[option] = curses.A_REVERSE

            self.main_win.addstr(int(self.height / 2 - 5),
                                 int(self.width / 2 - 8),
                                 "Welcome to Pyther")
            self.main_win.addstr(int(self.height / 2 - 2),
                                 int(self.width / 2 - 10),
                                 "Start typing (60 sec)", selected[0])
            self.main_win.addstr(int(self.height / 2 - 1),
                                 int(self.width / 2 - 3),
                                 "Modes", selected[1])
            self.main_win.addstr(int(self.height / 2),
                                 int(self.width / 2 - 5),
                                 "High scores", selected[2])
            self.main_win.addstr(int(self.height / 2 + 1),
                                 int(self.width / 2 - 2),
                                 "Exit", selected[3])

            # self.score(self.main_win, player)

            self.main_win.refresh()
            selection = self.get_menu_input(option)

        return selection

    def get_menu_input(self, option):
        try:
            action = self.main_win.getch()
            if action == curses.KEY_UP:
                option = (option - 1) % 4
            elif action == curses.KEY_DOWN:
                option = (option + 1) % 4
            elif action == ord("\n"):
                return option
        except KeyboardInterrupt:
            sys.exit()

    def standard_words(self, words):
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
            if current_line and word is not None:
                self.line_words.append(word)
            if lines < 2:
                break
            if words[word] is True:
                self.main_win.addstr(self.main_panel_y - lines,
                                     self.main_panel_x + prev_pos_x + 1,
                                     word, curses.color_pair(1))
            elif words[word] is False:
                self.main_win.addstr(self.main_panel_y - lines,
                                     self.main_panel_x + prev_pos_x + 1,
                                     word, curses.color_pair(2))
            elif not current_word:
                self.main_win.addstr(self.main_panel_y - lines,
                                     self.main_panel_x + prev_pos_x + 1,
                                     word)
            else:
                self.main_win.addstr(self.main_panel_y - lines,
                                     self.main_panel_x + prev_pos_x + 1,
                                     word, curses.A_BOLD)
                current_word = False

            prev_pos_x += len(word) + 1

    def check_first_line(self, words):
        if words[self.line_words[-1]] is not None:
            for w in self.line_words:
                del words[w]
            return True
        return False