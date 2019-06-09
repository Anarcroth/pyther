#!bin/python3
# -*- coding: utf-8 -*-

import curses
import curses.ascii
import time
import sys


class Player(object):
    def __init__(self):
        self.score = 0
        self.errors = 0
        self.accuracy = 0
        self.correct_chars = 0
        self.num_key_presses = 0
        self.pl_str = ''

        self.restart = False
        self.has_input = True

    def input(self, screen, clk, words, word_counter):
        self.pl_str = ''
        self.has_input = True

        while self.has_input:
            try:
                _input = screen.getch(1, 1 + len(self.pl_str))
                if self.is_submit(_input):
                    self.submit(words, word_counter)
                elif self.is_delete(_input):
                    self.delete(screen)
                elif self.is_restart(_input):
                    self.restart(screen)
                elif _input == curses.ascii.ESC:
                    raise KeyboardInterrupt
                else:
                    self.pl_str += chr(_input)
                    self.num_key_presses += 1

            except KeyboardInterrupt:
                clk.set()
                sys.exit()

    def is_submit(self, _input):
        if self.pl_str and _input in [curses.ascii.SP, curses.ascii.NL]:
            return True
        return False

    def submit(self, words, word_counter):
        self.is_correct(words, word_counter)
        self.has_input = False

    def is_delete(self, _input):
        if _input in [curses.ascii.DEL, curses.KEY_BACKSPACE]:
            return True
        return False

    def delete(self, screen):
        if not self.pl_str:
            screen.addstr(1, 1 + len(self.pl_str), '   ')
        else:
            screen.addstr(1, 1 + len(self.pl_str) - 1, '   ')
        self.pl_str = self.pl_str[:-1]

    def is_restart(self, _input):
        if _input == curses.KEY_F5:
            return True
        return False

    def restart(self, screen):
        self.restart = True
        self.has_input = False
        screen.addstr(self.y, self.x, 'Restarting...')
        screen.refresh()
        time.sleep(2)

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
