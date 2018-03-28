#!bin/python3

import curses

class Player(object):
    def __init__(self):
        self.errors = 0
        self.correct_words = 0
        self.num_key_presses = 0
        self.pl_str = ''

    def input(self, stdscr, y, x):
        curses.echo()

        self.pl_str = ''
        while True:
            _input = stdscr.getch(y, x + len(self.pl_str))
            if _input == 32: # SPACE
                break
            elif _input == 263: # BACKSPACE
                stdscr.addstr(y, x + len(self.pl_str) - 1, ' ')
                self.pl_str = self.pl_str[:-1]
                self.num_key_presses += 1
            elif _input == 269: # F5
                init_pyther(stdscr)
            elif _input > 0:
                self.pl_str += chr(_input)
                self.num_key_presses += 1

    def get_net_wpm():
        return (self.correcrt_words / 5 + self.errors) / time

    def is_correct(self, words, word_counter):
        current_word = list(words.keys())[word_counter]
        if current_word == self.pl_str:
            words[self.pl_str] = True
            self.correct_words += 1
        else:
            words[current_word] = False
            self.errors += 1
