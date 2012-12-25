#!/usr/bin/python
import random


class Lexgen:
    def __init__(self):
        self.fd_words = open('levels/words_list.txt', 'r')
        self.fd_rand = open('levels/rand.lex', 'w')

        random.seed()

        self.num_words = 10

        self.mean = 0.05
        self.stddev = 0.05

        # Generate self.num_words random indexes
        self.words_ind = []
        self.words = []
        self.num_list = range(5449)
        self.ind_list = range(5449)

        for i in range(self.num_words):
            self.rand = random.randint(0, len(self.ind_list) - 1)
            self.index = self.ind_list[self.rand]
            #print "index list:", self.ind_list
            #print "INDEX REM:", self.index
            self.words_ind.append(self.num_list[self.index])
            del self.ind_list[self.rand]

        self.words_ind.sort()
        #print "INDEXES:", self.words_ind

        #print "BLA", self.words_ind
        for i, w in enumerate(self.fd_words):
            if i in self.words_ind:
                self.words.append(w)

        for w in self.words:
            word = w.strip()
            self.pos_x = random.randint(1, 15)
            self.eta = random.randint(0, 3)
            self.speed = -abs(random.gauss(self.mean, self.stddev))
            self.line = "%s, %s, %s, %s, %s, %s" % (word, self.pos_x, '-2', self.speed, '-1', self.eta)
            self.fd_rand.write(self.line + '\n')

if __name__ == '__main__':
    l = Lexgen()
