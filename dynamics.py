#!/usr/bin/python

#from wdraw import WIDTH, HEIGHT


class Dynamics:
    def __init__(self):
        pass

    def pump(self, words):
        for i, w in enumerate(words):
            # word = word * speed
            words[i].pos_y = words[i].pos_y + words[i].speed
