#!bin/python3
# -*- coding: utf-8 -*-

import curses
import locale
import sys

locale.setlocale(locale.LC_ALL, '')


class Screen():
    def __init__(self, screen):
        self.main_win = screen
        self.height, self.width = screen.getmaxyx()

        self.main_y = int(self.height / 3)
        self.main_x = int(self.width / 3)

        self.w_words_maxw = self.main_x * 2 - 2
        self.w_words = curses.newwin(5,                     # height
                                     self.main_x,           # width
                                     self.main_y - 5,       # Y
                                     self.main_x)           # X

        self.w_input = curses.newwin(3,                     # height
                                     int(self.main_x -
                                         self.main_x / 2),  # width
                                     self.main_y,           # Y
                                     int(self.main_x +
                                         self.main_x / 4))  # X

        self.time = 1
        self.line_words = ['']

        self.init()

    def init(self):
        curses.noecho()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        self.update(self.main_win)

    def update(self, win):
        win.clear()
        win.border()
        win.refresh()

    def draw_main_menu(self):
        option = 0
        selection = -1
        while selection < 0:
            selected = [0] * 3
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
            self.main_win.addstr(int(self.height / 2 + 1),
                                 int(self.width / 2 - 2),
                                 "Exit", selected[2])

            self.main_win.refresh()

            try:
                action = self.main_win.getch()
                if action == curses.KEY_UP:
                    option = (option - 1) % 3
                elif action == curses.KEY_DOWN:
                    option = (option + 1) % 3
                elif action == ord("\n"):
                    selection = option
            except KeyboardInterrupt:
                sys.exit()

        return selection

    def clock(self):
        self.main_win.addstr(self.main_y - 3,
                             self.w_words_maxw + 5,
                             str(self.time))

    def score(self, player):
        if player is not None:
            self.main_win.addstr(int(self.height / 2 + 3),
                                 int(self.width / 2 - 3),
                                 "Score")
            self.main_win.addstr(int(self.height / 2 + 4),
                                 int(self.width / 2 - 4),
                                 "WPM: {}".format(player.score))
            self.main_win.addstr(int(self.height / 2 + 5),
                                 int(self.width / 2 - 7),
                                 "Accuracy: {}%".format(player.accuracy))
        self.main_win.refresh()

    def standard_words(self, words):
        lines = 1
        prev_pos_x = 0
        current_word = True
        current_line = True
        self.line_words = []
        for word in words:
            if self.main_x + prev_pos_x + len(word) > self.w_words_maxw:
                current_line = False
                lines += 1
                prev_pos_x = 0
            if current_line is True and word is not None:
                self.line_words.append(word)
            if lines > 3:
                break
            if words[word] is True:
                self.w_words.addstr(lines,
                                    prev_pos_x + 1,
                                    word, curses.color_pair(1))
            elif words[word] is False:
                self.w_words.addstr(lines,
                                    prev_pos_x + 1,
                                    word, curses.color_pair(2))
            elif not current_word:
                self.w_words.addstr(lines,
                                    prev_pos_x + 1,
                                    word)
            else:
                self.w_words.addstr(lines,
                                    prev_pos_x + 1,
                                    word, curses.A_BOLD)
                current_word = False

            prev_pos_x += len(word) + 1
        self.w_words.refresh()

    def check_first_line(self, words):
        if words[self.line_words[-1]] is not None:
            for w in self.line_words:
                del words[w]
            return True
        return False
