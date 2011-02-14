#!/usr/bin/env python

"""Simple example of multiple plot windows with yplot and ygl."""


from ygl import *
from yplot import Window, WindowManager
import math


######################################################################
class Graph(object):

    """A simple test class that creates a trivial simulation."""
    
    def __init__ (self, mul, fg=WHITE):
        self.mul = mul
        self.count = 1
        self.fg = fg

    def next (self):
        self.count = self.count + 1

    def draw (self):
        import math
        color (self.fg)
        x = 0.0
        y = math.sin (self.mul*self.count + x)
        factor = math.pi*0.02
        move2 (x, y)
        for i in range (0, 100):
            x = i*factor
            y = math.sin (self.mul*self.count + x)
            draw2 (x, y)


######################################################################
def main ():
    wm = WindowManager ()
    w1 = Window (title="test1")
    wm.add_window (w1)
    w1.set_domain ((0.0, 7.0, -3.5, 3.5))
    g1 = Graph (0.1)
    w1.set_draw_method (g1.draw)
    w2 = Window (title="test another window.")
    wm.add_window (w2)
    w2.set_domain ((0.0, 7.0, -3.5, 3.5))
    g2 = Graph (0.5, RED)
    w2.set_draw_method (g2.draw)
    ret = 0
    while not ret:
        ret = wm.show ()
        g1.next ()
        g2.next ()

if __name__ == "__main__":
    main ()
