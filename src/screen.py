#!bin/python3
# -*- coding: utf-8 -*-

import curses
import locale
import sys
import logging

locale.setlocale(locale.LC_ALL, '')

logging.basicConfig(filename="logger",
                    filemode='a',
                    level=logging.INFO)


class Screen(object):
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
        input_y, input_x = self.w_input.getmaxyx()
        self.w_time = curses.newwin(3, 4,
                                    self.main_y,
                                    int(self.main_x) + 13)

        self.time = 1
        self.line_words = ['']

        self.init()

    def init(self):
        curses.noecho()
        curses.curs_set(0)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        self.update(self.main_win)

    def show(self):
        self.update(self.w_input)
        self.update(self.w_words)

    def update(self, win):
        win.erase()
        win.border()
        win.refresh()

    def draw_main_menu(self):
        option = 0
        selection = -1
        while selection < 0:
            selected = [0] * 2
            selected[option] = curses.A_REVERSE

            self.main_win.addstr(int(self.height / 2 - 5),
                                 int(self.width / 2 - 8),
                                 "Welcome to Pyther")
            self.main_win.addstr(int(self.height / 2 - 2),
                                 int(self.width / 2 - 10),
                                 "Start typing (60 sec)", selected[0])
            self.main_win.addstr(int(self.height / 2 + 1),
                                 int(self.width / 2 - 2),
                                 "Exit", selected[1])

            self.main_win.refresh()

            try:
                action = self.main_win.getch()
                if action == curses.KEY_UP:
                    option = (option - 1) % 2
                elif action == curses.KEY_DOWN:
                    option = (option + 1) % 2
                elif action == curses.ascii.NL:
                    selection = option
            except KeyboardInterrupt:
                sys.exit()

        return selection

    def clock(self):
        self.w_time.addstr(1, 1, str(self.time))
        self.w_time.border()
        self.w_time.refresh()

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
            self.main_win.addstr(int(self.height / 2 + 6),
                                 int(self.width / 2 - 7),
                                 "Wrong words:")
            logging.debug("the wrong words are ")
            logging.debug(player.wrong_words)
            prev_word_pos = 0
            for w, plw in player.wrong_words.items():
                self.main_win.addstr(int(self.height / 2 + 7),
                                     int(self.width / 2 - 19 + prev_word_pos),
                                     w + ":" + plw)
                prev_word_pos += len(w) + len(plw) + 2

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
        self.w_words.noutrefresh()

    def check_first_line(self, words):
        if words[self.line_words[-1]] is not None:
            for w in self.line_words:
                del words[w]
            return True
        return False
