#!/usr/bin/env python

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2000-2011, Prabhu Ramachandran.
# License: BSD Style.

import sys
import ygl
import time
import random

def start():
    w = ygl.winopen('test')
    ygl.ortho2(0, 1.0, 0.0, 1.0)
    ygl.qdevice(ygl.SPACEKEY)
    ygl.qdevice(ygl.REDRAW)
    ygl.qdevice(ygl.WINQUIT)
    ygl.qdevice(ygl.ESCKEY)
    return w

def draw():
    ygl.color(ygl.BLACK)
    ygl.clear()
    ygl.color(ygl.RED)
    ygl.circf(random.random(), random.random(), random.random())
    ygl.gflush()

def compute():
    print "computing ",
    time.sleep(2)
    print "done"

iteration = 0
def show():
    global iteration
    qval = ygl.Int16()
    wait = 1
    ret = 0

    e = ygl.qtest()
    print e
    if e == 0:
        draw()

    while (e != 0) or (iteration == 1):
        e = 0
        event = ygl.qread(ygl.byref(qval))
        val = qval.value
        if event == ygl.REDRAW:
            ygl.reshapeviewport()
            draw()
        elif event == ygl.WINQUIT or event == ygl.ESCKEY:
            iteration = 0
            ygl.gexit()
            ret = 1
            break
        elif event == ygl.SPACEKEY:
            if val == 1:
                if wait:
                    wait = 0
                    iteration = 1
                    print "Press space again to continue. ",
                    sys.stdout.flush()
                else:
                    iteration = 0
                    wait = 1
                    print "Done waiting."
                    
    return ret

def iterate():
    while True:
        compute()
        if show():
            break

if __name__ == '__main__':
    start()
    draw()
    iterate()
