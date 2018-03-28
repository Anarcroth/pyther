#!bin/python3
# -*- coding: utf-8 -*-

import sys,os
import curses
import random
import time
import threading
from _draw import Draw
from _player import Player

def make_choice(stdscr, draw):
    choice = draw.main_menu(stdscr)
    if choice == 0:
        init_pyther(stdscr, draw)
    elif choice == 1:
        # TODO show different modes
        return;
    elif choice == 2:
        # TODO shows high scores
        return;
    elif choice == 3:
        sys.exit();

def init(stdscr):
    draw = Draw(stdscr)
    make_choice(stdscr, draw)

def get_words_from(_file):
    words = open(_file).read().split("\n")
    random.shuffle(words)
    return { w : None for w in words }


def incr_clock(stdscr, clk, draw):
    draw.clock(stdscr)
    draw.time += 1
    if not clk.is_set():
        threading.Timer(1, incr_clock, [stdscr, clk, draw]).start()

def run_pyther(stdscr, draw):
    word_counter = 0
    randomized_words = get_words_from("./word_lists/200.txt")

    player = Player()
    while draw.time < 61:
        stdscr.clear()
        stdscr.border()

        draw.main_panel(stdscr)
        draw.input_panel(stdscr)
        draw.clock(stdscr)

        if draw.check_first_line(randomized_words):
            word_counter = 0

        draw.words(stdscr, randomized_words)

        player.input(stdscr, draw.pl_input_y, draw.pl_input_x)
        player.is_correct(randomized_words, word_counter)
        word_counter += 1

        stdscr.refresh()

def init_pyther(stdscr, draw):

    stdscr.clear()
    stdscr.refresh()

    stdscr.nodelay(True)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    type_clock = threading.Event()
    incr_clock(stdscr, type_clock, draw)

    run_pyther(stdscr, draw)

    type_clock.set()

    stdscr.clear()
    stdscr.refresh()

    make_choice(stdscr, draw)

if __name__ == "__main__":
    curses.wrapper(init)
