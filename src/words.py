#!bin/python3

import random

class Words(object):

    def __init__(self, path = "../word_lists/200.txt"):
        self.path = path
        self._list = None

    def get_words(self):
        self._list = open(self.path).read().split("\n")
        random.shuffle(self._list)
        self._list = { w : None for w in self._list }
