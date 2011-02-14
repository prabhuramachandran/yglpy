#!/usr/bin/python

# -------------------------------------------------------------------
# This is a simple script that tests the menu functionality that is
# available. have defined a function called addtopup(Int32, Char8*) this
# takes a menu created by newpup() and a standard GL input (note - %M
# doesnt work ) string and adds the menu.  Irrespective of the fact that
# a %F is given in the string or not the function merely calls a dummy
# function that returns the menu value that an entry has.  The standard
# addtopup is hence used only to create sub, subsub menu's and the like.
# In order to use callbacks since one cannot pass python functions to
# the C library one needs to use the returned value of dopup() and then
# call the required callback function.  Please look through this example
# to see what can be done.
# -------- Prabhu Ramachandran <prabhu@aero.iitb.ac.in> ----------

from ygl import *

def do_callback(x):
    "This calls the callbacks for the test menu"
    if x == 1:
	print "do_callback got ", x, " - so do some stuff"
    elif x == 2:
	print "do_callback got ", x, " - so do some stuff"
    elif x == 3:
	print "do_callback got ", x, " - so do some stuff"
    elif x == 4:
	print "do_callback got ", x, " - so do some stuff"
    elif x ==5:
	print "Quitting!"
	gexit()
	return WINQUIT

    elif x == -1:
	print "do_callback got ", x, " - Do nothing - nothing selected"
    else:
	print "do_callback got ", x, " - Submenu works too!"


def draw():
    "This draws some stuff for the demo"
    color(BLACK)
    clear()
    color(BLUE)
    circfi(150,150,75)
	


#initialisation and some drawing
minsize(300, 300)
winopen("Menu")
draw()

# defining new menu's
menu = newpup()
submenu = newpup()
subsubmenu = newpup()

# there is no defpup() :(
# The "Tens" sub menu - note I must define the number that each menu item
# will return right here - this is not too hard. The %F at the end is
# optional and need not be given, the add2pup will still work ok.

addtopup(submenu,"SubMenu!%t|10%x10|20%x20|30%x30%F")

#defining the sub-sub menu!
addtopup(subsubmenu, "SubSub menu!%t|100%x100|200%x200|300%x300")

#adding sub-submenu to submenu
addtopup(submenu,"Hundreds%m", subsubmenu)
#adding the submenu to main menu while defining the main menu
addtopup(menu,"Menu!%t|1|2|Tens%m", submenu)
#adding further menu's to the main menu
addtopup(menu,"4|Exit!")

#disabling the first entry in the submenu
setpup(submenu,1,PUP_GREY)

#some device queing so I can trap the right click on the mouse
qdevice(MENUBUTTON)
qdevice(WINQUIT)


val = Int16()
# this "val" is needed for qread(). I have to create a pointer to
# Int16 and pass this as an arguement to qread() - remember to delete
# this variable.  Int16_p is an added function.

r = 1
dev = 1 

# the interaction loop
while dev != WINQUIT:
    dev = qread(byref(val))
    if dev == MENUBUTTON:
	if val.value == 1: #another added function
	    r = dopup(menu)
	    if do_callback(r) == WINQUIT:
		dev = WINQUIT

    elif dev == REDRAW:
	reshapeviewport()
	draw()	

    elif dev == WINQUIT:
	gexit()

