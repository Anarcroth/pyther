#!bin/python3
# -*- coding: utf-8 -*-

import sys
import curses
import threading
from words import Words
from screen import Screen
from player import Player


class Pyther(object):

    def run(self, screen, words):
        player = Player()

        screen.update(screen.main_win)
        curses.echo()
        words.get_words()

        screen.time = 0
        word_counter = 0

        type_clock = threading.Event()
        self.init_clock(type_clock)

        player.is_correct(words._list, word_counter)
        player.input(screen, type_clock, words._list, word_counter)
        word_counter += 1

        while screen.time < 61:
            screen.update(screen.w_input)
            screen.update(screen.w_words)
            screen.w_input.border()

        while not type_clock.is_set():
            screen.w_words.erase()
            screen.w_words.border()

            if player.restart:
                type_clock.set()
                run()

            player.save_score()
            self.make_choice(screen)
            type_clock.wait(1)
            type_clock.set()
            draw.main_panel(screen)
            draw.input_panel(screen)

            if screen.check_first_line(words._list):
                word_counter = 0

            player.save_score()
            self.make_choice()
            self.make_choice(player)
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
