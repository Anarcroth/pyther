#!bin/python3

import curses

class Player(object):
    def __init__(self):
        self.score = 0
        self.errors = 0
        self.accuracy = 0
        self.correct_chars = 0
        self.num_key_presses = 0
        self.pl_str = ''

    def input(self, stdscr, y, x):
        curses.echo()
        stdscr.nodelay(True)
        self.pl_str = ''

        while True:
            _input = stdscr.getch(y, x + len(self.pl_str))
            if _input == 32: # SPACE
                break
            elif _input == 263: # BACKSPACE
                if len(self.pl_str) == 0:
                    continue
                stdscr.addstr(y, x + len(self.pl_str) - 1, ' ')
                self.pl_str = self.pl_str[:-1]
                self.num_key_presses += 1
            elif _input == 269: # F5
                pyther.init_pyther_screen(stdscr)
            elif _input > 0:
                self.pl_str += chr(_input)
                self.num_key_presses += 1

    def get_net_wpm(self):
        return (self.num_key_presses / 5 - self.errors) / 1

    def is_correct(self, words, word_counter, pl_str):
        current_word = list(words.keys())[word_counter]
        if current_word == pl_str:
            words[current_word] = True
            self.correct_chars += len(pl_str)
        else:
            words[current_word] = False
            self.errors += 1

    def get_final_stats(self):
        self.score = self.get_net_wpm()
        self.accuracy = (self.correct_chars / self.num_key_presses)

    def save_score(self):
        self.get_final_stats()
        player_data = "WPM:" + str(self.score) + "\nAccuracy:" + str(self.accuracy) + "\n\n"
        with open("score", "w") as pl_file:
            pl_file.write(player_data)

import pyther
