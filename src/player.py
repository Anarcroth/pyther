#!bin/python3
# -*- coding: utf-8 -*-

import curses
import curses.ascii
import time
import sys
import json
from datetime import datetime


class Player(object):
    def __init__(self, y, x):
        self.score = 0
        self.errors = 0
        self.accuracy = 0
        self.correct_chars = 0
        self.num_key_presses = 0
        self.pl_str = ''

        self.restart = False
        self.has_input = True

        self.y = y
        self.x = x

    def input(self, screen, clk, words, word_counter):
        self.pl_str = ''
        self.has_input = True

        while self.has_input:
            try:
                _input = screen.getch(self.y, self.x + len(self.pl_str))
                self.handle_submit(_input, words, word_counter)
                self.handle_delete(_input, screen)
                self.handle_restart(_input, screen)
                if _input == curses.ascii.ESC:
                    raise KeyboardInterrupt
                else:
                    self.pl_str += chr(_input)
                    self.num_key_presses += 1
            except KeyboardInterrupt:
                clk.set()
                sys.exit()

    def handle_submit(self, _input, words, word_counter):
        if _input in [curses.ascii.SP,
                      curses.ascii.NL,
                      curses.KEY_ENTER]:
            if self.pl_str:
                self.is_correct(words, word_counter)
                self.has_input = False

    def handle_delete(self, _input, screen):
        if _input in [curses.ascii.BS,
                      curses.ascii.DEL,
                      curses.KEY_BACKSPACE]:
            if self.pl_str:
                screen.addstr(self.y,
                              self.x + len(self.pl_str) - 1,
                              '     ')
                self.pl_str = self.pl_str[:-1]
                self.num_key_presses += 1

    def handle_restart(self, _input, screen):
        if _input == curses.KEY_F5:
            self.restart = True
            # Give player a breather before the restart
            screen.addstr(self.y,
                          self.x,
                          'Restarting...')
            screen.refresh()
            time.sleep(2)
            self.has_input = False

    def get_net_wpm(self):
        return (self.num_key_presses / 5 - self.errors)

    def is_correct(self, words, word_counter):
        current_word = list(words.keys())[word_counter]
        if current_word == self.pl_str:
            words[current_word] = True
            self.correct_chars += len(self.pl_str)
        else:
            words[current_word] = False
            self.errors += 1

    def get_final_stats(self):
        if self.num_key_presses > 0:
            self.accuracy = round(self.correct_chars /
                                  self.num_key_presses, 2) * 100
            self.score = round(self.get_net_wpm(), 2)
        else:
            self.accuracy = 0.0
            self.score = 0

    def save_score(self):
        self.get_final_stats()
        data = []
        with open("../scores") as pl_file:
            data = json.load(pl_file)
            data.append({
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "WPM": self.score,
                "Accuracy": self.accuracy
            })

        sorted_data = sorted(data, key=lambda k: k["WPM"], reverse=True)

        with open("../scores", "w") as fi:
            json.dump(sorted_data, fi)
