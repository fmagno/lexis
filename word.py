#!/usr/bin/python


class Word:
    def __init__(self,
                 name='noname',
                 pos_x=5,
                 pos_y=-5,
                 speed=-1,
                 life_time=-1,
                 eta=0):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.life_time = life_time  # -1: forever (can only be killed by a 'hit' or 'crash')
        self.eta = eta

    def __str__(self):
        return "N:%s, X:%f, Y:%f, S:%f, L:%f, E:%f" % (self.name, self.pos_x, self.pos_y, self.speed, self.life_time, self.eta)
        #return "OLA"

# Debugging purposes
if __name__ == '__main__':
    w = Word()
    l = [Word(), Word()]
    print l[0]
