from time import time, sleep


class Tempo:
    def __init__(self):
        self.t0 = time()

    def __str__(self):
        return "Elapsed: " + str(self.elapsed) + \
               "\tTo wait: " + str(self.to_wait) + \
               "\tSummation: " + str(self.elapsed + self.to_wait) + \
               "\tFPS: " + str(1.0 / (self.elapsed + self.to_wait))

    def tick(self):
        self.t0 = time()

    def waitUntilMultiple(self, sec):
        self.elapsed = (time() - self.t0)
        self.to_wait = sec - self.elapsed
        if self.to_wait < 0:
            self.to_wait = 0
        sleep(self.to_wait)

    def reset(self):
        self.t0 = time()

    def elapsed(self):
        return (time() - self.t0)
