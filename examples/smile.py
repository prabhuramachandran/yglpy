#!/usr/bin/python

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2000-2011, Prabhu Ramachandran.
# License: BSD Style.

# --------------------------------------------------------------------
# A python version of the smile.c example from Ygl.  This demonstrates
# some of the python bindings for the Ygl library.  Please note that
# there are a few extra python functions to handle creation, deletion
# and deferencing of some of the pointers used by Ygl.  Also note that
# due to the inability of SWIG to handle arbitrary arguements to a C
# function the defpup() function does not have a python equivalent.  For
# a simple but illustrative example look at the menutest.py example that
# is located in the same directory as this file.  Please also look
# through this example carefully.
# -------  Prabhu Ramachandran <prabhu@aero.iitb.ac.in> -----------

from ygl import *

#initialisation
prefsize(100,100)
w = winopen("SMILE!")

#background
color(BLACK)
clear()

#the face
color(RED)
circfi(50, 50, 40)

#eyes
color(WHITE)
circfi(30, 60, 10)
circfi(70, 60, 10)
color(BLACK)
circfi(30, 60,  5)
circfi(70, 60,  5)

#smile
arci(50, 50, 25, 2000, 3400)

#the gflush() is very important. Try the script without it! :(
#Also note that sleep(0) doesnt flush the pipeline

gflush()

#need ppmtogif (an executable) for this to work.
#gl2ppm("| ppmtogif > normal.gif")

# the wink

sleep(2)
color(RED)
circfi(30, 65, 10)
gflush()

#gl2ppm("| ppmtogif > wink.gif")

sleep(1)

color(WHITE) 
circfi(30, 60, 10)
color(BLACK) 
circfi(30, 60,  5)
gflush()

sleep(2)
gexit()
