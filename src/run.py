#!bin/python3
# -*- coding: utf-8 -*-

import sys
import curses
import threading
from words import Words
from screen import Screen
from player import Player


def start():
    player = Player()

    screen.update(screen.main_win)
    curses.echo()
    words.get_words()

    screen.time = 0
    word_counter = 0

    type_clock = threading.Event()
    init_clock(type_clock)

    # TODO fix this part so that it outputs words and plays the game
    #player.is_correct(words._list, word_counter)
    #player.input(screen, type_clock, words._list, word_counter)
    #word_counter += 1

    while screen.time < 61:
        screen.update(screen.w_input)
        screen.update(screen.w_words)
        screen.w_input.border()

    while not type_clock.is_set():
        screen.w_words.erase()
        screen.w_words.border()

        if player.restart:
            type_clock.set()
            start()

            player.save_score()
            make_choice(screen)
            type_clock.wait(1)
            type_clock.set()
            draw.main_panel(screen)
            draw.input_panel(screen)

            if screen.check_first_line(words._list):
                word_counter = 0

            player.save_score()
            make_choice()
            make_choice(player)
            draw.standard_words(screen, words._list)
            screen.standard_words(words._list)

            try:
                player.input(screen.w_input, words._list, word_counter)
            except KeyboardInterrupt as kberr:
                break

            word_counter += 1
            curses.doupdate()

        type_clock.set()
        finish(player)


def make_choice():
    choice = screen.draw_main_menu()
    if choice == 0:
        start()
    elif choice == 1:
        sys.exit()


def init_clock(clk):
    screen.time += 1
    screen.clock()
    if screen.time >= 60:
        clk.set()
        return
    if not clk.is_set():
        threading.Timer(1, init_clock, [clk]).start()
    else:
        screen.w_time.clear()
        screen.w_time.refresh()


def finish(player):
    player.get_final_stats()
    curses.noecho()

    screen.update(screen.main_win)
    screen.score(player)

    screen.draw_main_menu()


def init(stdscr):
    global screen, words, time

    time = 0
    screen = Screen(stdscr)
    words = Words()

    make_choice()


if __name__ == "__main__":
    curses.wrapper(init)
