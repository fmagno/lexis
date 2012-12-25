#!/usr/bin/python

import sys
from draw import Screen
from tempo import Tempo
from level import Level
from time import sleep


class Game:
    def __init__(self):
        # Begining:

        # Exit condition initialization
        self.running = True

        # Tempo initialization (Refresh rate)
        self.t = Tempo()
        self.fps = 30
        self.delay = 1.0 / self.fps

        # Tempo initialization (Level words)
        self.t_w = Tempo()

        # Screen initialization
        self.scr = Screen()
        #self.scr.addWord(Word('Score: ', 1, -1, 0))
        #self.scr.addWord(Word('Life: ', 15, -1, 0))

        #self.scr.addWord(Word(name='video', speed=-0.02))
        #self.scr.addWord(Word(name='shot', speed=-0.03, pos_x=15, pos_y=-3))
        #self.scr.addWord(Word(name=':)', speed=-0.05, pos_x=22, pos_y=-3))

        # Dynamics initialization
        #self.dyn = Dynamics()

        # Load levels
        self.lev = Level()
        #self.curr_lev = self.lev.loadLev('levels/debug.wrd')
        self.curr_lev = self.lev.loadLev('levels/rand.lex')

        # Main loop...
        self.mainLoop()

    def main(self):
        # Print current score
        #self.scr.addstr(1, 8, str(self.scr.score))

        # Check input keys
        self.c = self.scr.getch()
        #if self.c != -1:
        if self.c >= 0 and self.c < 128:
            #self.scr.addstr(3, 3, chr(self.c))
            self.key_res = self.scr.addKey(chr(self.c))
            self.runCommand(self.key_res)
            self.scr.flushinp()

    def runCommand(self, comm):
        if comm:
            if comm == 'exit':
                self.running = False
            else:
                self.scr.scoreWord(comm)

    def mainLoop(self):
        while not self.scr.game_over:
            self.t.tick()
            self.main()

           # Level words
            if len(self.curr_lev) > 0:
                print "Entrei!"
                print "ELAPSED:", self.t_w.elapsed()
                print "ETA BEFORE IF:", self.curr_lev[0].eta
                if self.t_w.elapsed() >= self.curr_lev[0].eta:
                    print "name", self.curr_lev[0].name
                    print "yln", self.curr_lev[0].pos_y
                    print "eta", self.curr_lev[0].eta
                    print "life", self.scr.life
                    print "elapsed:", self.t_w.elapsed()
                    self.scr.addWord(self.curr_lev[0])
                    #print "WORDS", self.scr.words[3].name
                    del self.curr_lev[0]
                    print "blowup"
                    print "length:", len(self.curr_lev)
                    self.t_w.reset()
            elif len(self.scr.words) == 0:
                self.scr.game_over = True
                self.scr.init_pair(1, self.scr.COLOR_GREEN, self.scr.COLOR_BLACK)
                self.scr.addstr(11, 15, "Game Over!", self.scr.color_pair(1))
                self.scr.refresh()
                sleep(3)

            print "Before dynPump"
            # Refresh dynamics
            self.scr.dynPump()

            print "Before drawPump"
            # Drawing refresh
            self.scr.drawPump()

            print "Before waitUntil"
            # Keep FPS value stable...
            self.t.waitUntilMultiple(self.delay)


if __name__ == "__main__":
    fd_err = open("error.log", 'w')
    fd_out = open("out.log", 'w')
    original_stderr = sys.stderr
    original_stdout = sys.stdout
    sys.stderr = fd_err
    sys.stdout = fd_out

    c = Game()

    sys.stderr = original_stderr
    sys.stdout = original_stdout
    fd_err.close()
    fd_out.close()
