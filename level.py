#!/usr/bin/python

from word import Word


class Level:
    def __init__(self):
        # List of words
        self.level = []

    def loadLev(self, lev_path):
        fd_lev = open(lev_path)
        for line in fd_lev:
            line = line.strip()
            if line.startswith('#'):
                continue
            else:
                w_name, w_pos_x, w_pos_y, w_speed, w_life_time, w_eta = line.split(',')
                w_name = w_name.strip()
                w_pos_x = w_pos_x.strip()
                w_pos_y = w_pos_y.strip()
                w_speed = w_speed.strip()
                w_life_time = w_life_time.strip()
                w_eta = w_eta.strip()

                self.level.append(Word(w_name, float(w_pos_x), float(w_pos_y), float(w_speed), float(w_life_time), float(w_eta)))
        #print self.level
        return self.level


if __name__ == "__main__":
    l = Level()
    l.loadLev('levels/lev1.lex')
