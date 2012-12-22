#!/usr/bin/python
#import curses
from curses import initscr, noecho, curs_set, cbreak, nocbreak, echo, endwin
import curses

WIDTH = 50
HEIGHT = 25


class Screen:
    def __init__(self):
        # Curses initialization
        self.stdscr = initscr()
        #self.stdscr.notimeout(0)
        # Colors
        curses.resize_term(HEIGHT, WIDTH)
        #curses.start_color()
        self.br = str(curses.baudrate())
        noecho()
        cbreak()
        self.stdscr.keypad(0)  # Changed to 0
        self.stdscr.nodelay(1)
        curs_set(0)
        self.stdscr.clear()
        self.stdscr.border(0)

        # stdscr functions made accessible through the Screen object
        self.addstr = self.stdscr.addstr
        self.getch = self.stdscr.getch
        self.flushinp = curses.flushinp

        # List of all words to be drawn
        # words: [[word, x, y, speed], ...]
        self.words = []

        # Buffer of current pressed keys
        self.keys = []

        # Score
        self.score = 0

        # Life
        self.life = 3

        # Game Over
        self.game_over = False

    def __del__(self):
        # Ending...
        nocbreak()
        self.stdscr.keypad(0)
        echo()
        endwin()

    def addWord(self, word):
        """ Adds a word to the list of printable words"""
        self.words.append(word)

    def addKey(self, key):
        if key == '\n':
            ret = ''.join(self.keys)
            self.keys = []
            return ret
        else:
            self.keys.append(key)
            return False

    def remWord(self, name):
        for i, w in enumerate(self.words):
            if w.name == name:
                del self.words[i]
                return

    def scoreWord(self, name):
        for i, w in enumerate(self.words):
            if w.name == name:
                self.score += len(w.name)
                del self.words[i]

    def remLife(self):
        self.life -= 1
        if self.life == 0:
            self.game_over = True

    def drawPump(self):
        # Draw static data
        # Print current score
        self.addstr(1, 1, 'Score: ' + str(self.score))

        # Print current life
        self.addstr(1, 20, 'Life: ' + str(self.life))

        # Draw dynamic data
        for i, w in enumerate(self.words):
            self.addstr(int(round(-w.pos_y)), int(round(w.pos_x)), w.name)

    def dynPump(self):
        for i, w in enumerate(self.words):
            # Dynamics
            # Pos = Pos + Speed*Dt
            self.words[i].pos_y = self.words[i].pos_y + self.words[i].speed

            # Check the edge
            if self.words[i].pos_y < -HEIGHT + 2:
                self.remWord(self.words[i].name)
                self.remLife()

        #for word in self.words:
        #    self.addstr(-word[2], word[1], word[0])
        #self.addstr(20, 20, self.br)

        self.stdscr.refresh()
        self.stdscr.erase()
        self.stdscr.border(0)
