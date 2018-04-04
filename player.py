#!bin/python3

import curses
import re
import time
import sys
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

        self.y = y
        self.x = x

    def input(self, screen, clk):
        self.pl_str = ''

        while True:
            # Control how fast this loop should execute. Do not comment out since it will cause major CPU usage if not present.
            time.sleep(0.05)
            try:
                _input = screen.getch(self.y, self.x + len(self.pl_str))
                if _input == 32: # SPACE
                    break
                elif _input == 263: # BACKSPACE
                    if len(self.pl_str) == 0:
                        continue
                    screen.addstr(self.y, self.x + len(self.pl_str) - 1, ' ')
                    self.pl_str = self.pl_str[:-1]
                    self.num_key_presses += 1
                elif _input == 269: # F5
                    self.restart = True
                    break
                elif _input == 27: # ESC
                    raise KeyboardInterrupt
                elif _input > 0:
                    self.pl_str += chr(_input)
                    self.num_key_presses += 1
            except KeyboardInterrupt:
                clk.set()
                sys.exit()

    def get_net_wpm(self):
        return (self.num_key_presses / 5 - self.errors) / 1

    def is_correct(self, words, word_counter):
        current_word = list(words.keys())[word_counter]
        if current_word == self.pl_str:
            words[current_word] = True
            self.correct_chars += len(self.pl_str)
        else:
            words[current_word] = False
            self.errors += 1

    def get_final_stats(self):
        self.score = self.get_net_wpm()
        if self.num_key_presses > 0:
            self.accuracy = round(self.correct_chars / self.num_key_presses, 2) * 100
        else:
            self.accuracy = 0.0
            self.score = 0

    def save_score(self):
        self.get_final_stats()
        player_data = "Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\nWPM: " + str(self.score) + "\nAccuracy: " + str(self.accuracy) + "%\n\n"
        with open("scores", "a") as pl_file:
            pl_file.write(player_data)

import pyther
