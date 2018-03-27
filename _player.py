#!bin/python3

import curses
import _type

class Player(object):
    def __init__(self):
        self.errors = 0
        self.correct_words = 0
        self.num_key_presses = 0

    def _input(self, stdscr, y, x):
        curses.echo()
        str_in = ''
        while True:
            _input = stdscr.getch(y, x + len(str_in))
            if _input == 32: # SPACE
                break
            elif _input == 263: # BACKSPACE
                stdscr.addstr(y, x + len(str_in) - 1, ' ')
                str_in = str_in[:-1]
                self.num_key_presses += 1
            elif _input == 269: # F5
                init_pyther(stdscr)
            else:
                str_in += chr(_input)
                self.num_key_presses += 1

                return str_in

    def _get_net_wpm():
        return (self.correcrt_words / 5 + self.errors) #/ time
