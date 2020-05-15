#!bin/python3
# -*- coding: utf-8 -*-

import sys
import curses
import threading
from words import Words
from screen import Screen
from player import Player


class Pyther(object):

    def __init__(self, file_path):
        self.time = 0
        self.line_words = ['']

    def make_choice(self, stdscr, draw, player):
        choice = draw.main_menu(screen)
        if choice == 0:
            self.init_pyther_screen()
            self.run(draw, player)
        elif choice == 1:
            screen.addstr(int(self.height / 2 - 1),
                          int(self.width / 2 - 3), "TBA")
        elif choice == 2:
            draw.high_scores(screen, self.get_scores("../scores"))
            self.make_choice()
        elif choice == 3:
            sys.exit()

    def input(self, player, _input, pl_str, word_counter):
        if _input != -1:
            if _input == 32: # SPACE
                player.is_correct(words, word_counter, pl_str)
            elif _input == 263: # BACKSPACE
                if len(pl_str) == 0:
                    return
                screen.addstr(y, x + len(pl_str) - 1, ' ')
                pl_str = pl_str[:-1]
                player.num_key_presses += 1
            elif _input == 269: # F5
                pyther.init_pyther_screen(screen)
            elif _input > 0:
                pl_str += chr(_input)
                player.num_key_presses += 1

    def draw_words(self):
        lines = 4
        prev_pos_x = 0
        current_word = True
        current_line = True
        self.line_words = []
        for word in words:
            if main_panel_x + prev_pos_x + len(word) > max_panel_len:
                current_line = False
                lines -= 1
                prev_pos_x = 0
            if current_line and word != None:
                self.line_words.append(word)
            if lines < 2:
                break
            if words[word] == True:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.color_pair(1))
            elif words[word] == False:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.color_pair(2))
            elif not current_word:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word)
            else:
                screen.addstr(main_panel_y - lines, main_panel_x + prev_pos_x + 1, word, curses.A_BOLD)
                current_word = False
            prev_pos_x += len(word + " ")

    def check_first_line(self):
        if words[self.line_words[-1]] != None:
            for w in self.line_words: del words[w]
            return True
        return False

    def run(self, player):
        words = open("./word_lists/200.txt").read().split("\n")
        word_counter = 0

        screen.nodelay(True)
        curses.echo()

    def get_scores(self, file_path):
        with open(file_path) as pl_file:
            data = json.load(pl_file)
            return data[:3]

    def init_clock(self, clk):
        draw.time += 1
        if not clk.is_set():
            threading.Timer(1, self.init_clock, [clk]).start()
        return draw.time

    def get_words_from(self, path):
        words = open(path).read().split("\n")
        random.shuffle(words)
        return { w : None for w in words }

    def run(self):
        player = Player(draw.pl_input_y, draw.pl_input_x)

        draw.time = 0
        word_counter = 0

        pl_str = ''
        type_clock = threading.Event()
        self.init_clock(type_clock)

        while draw.time < 61:
            stdscr.clear()
            stdscr.border()

        while True:
            time.sleep(0.09)
            screen.clear()
            screen.border()

            if self.check_first_line():
                word_counter = 0

            self.drwords()

            _input = screen.getch(pl_input_y, pl_input_x + len(pl_str))
            self.inp(player, _input, pl_str, word_counter)

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


def run():
    player = Player()

    screen.update(screen.main_win)

    curses.echo()

    words.get_words()

    screen.time = 0
    word_counter = 0

    type_clock = threading.Event()
    init_clock(type_clock)

            player.input(screen, type_clock)
            player.is_correct(words, word_counter)
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


def finish(player):
    player.get_final_stats()

    # turn off echo while in menu
    curses.noecho()

    screen.update(screen.main_win)
    screen.score(player)

    main_menu()

def init(stdscr):
    global screen, words

    screen = Screen(stdscr)
    words = Words()

    pyther.make_choice()
    make_choice()
    main_menu()

if __name__ == "__main__":
    curses.wrapper(init)
