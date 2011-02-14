#!/usr/bin/env python

"""
This module provides fairly powerful functionality to plot things
using Ygl and python

Copyright (C) 2000-2011 Prabhu Ramachandran
Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
http://www.aero.iitb.ac.in/~prabhu

License: BSD Style.

"""

import time
from ygl import *
import copy
import sys

AXES_COLOR=WHITE

def check_order (s):
    if s[1] < s[0]:
        t = s[0]
        s[0] = s[1]
        s[1] = t
    if s[3] < s[2]:
        t = s[2]
        s[2] = s[3]
        s[3] = t        
    return s

######################################################################
class MouseZoom(object):
    def __init__ (self, double_buffer=1):
        self.xl, self.xr, self.yl, self.yr = 0.0, 0.0, 0.0, 0.0 
        self.dbuf = double_buffer
        self.mx, self.my, self.mx1, self.my1 = 0, 0, 0, 0
        self._rect = [None, None, None, None]

    def _delete_rect(self):
        del self._rect
        self._rect = [None, None, None, None]

    def _rect_ptr(self, idx):
        return C.cast(self._rect[idx], C.POINTER(C.c_short))

    def rect_read_outline(self, xll, yll, xur, yur):
        self._delete_rect()
        if xll > xur:
            xll, xur = xur, xll
        if yll > yur:
            yll, yur = yur, yll

        self._rect[0] = (Int16*(xur-xll+4)*3)()
        self._rect[1] = (Int16*(yur-yll+4)*3)()
        self._rect[2] = (Int16*(xur-xll+4)*3)()
        self._rect[3] = (Int16*(yur-yll+4)*3)()
        rectread(xll-1, yll-1, xur+1, yll+1, self._rect_ptr(0))
        rectread(xur-1, yll-1, xur+1, yur+1, self._rect_ptr(1))
        rectread(xll-1, yur-1, xur+1, yur+1, self._rect_ptr(2))
        rectread(xll-1, yll-1, xll+1, yur+1, self._rect_ptr(3))
    
    def rect_write_outline(self, xll, yll, xur, yur):
        if xll > xur:
            xll, xur = xur, xll
        if yll > yur:
            yll, yur = yur, yll

        rectwrite (xll-1, yll-1, xur+1, yll+1, self._rect_ptr(0))
        rectwrite (xur-1, yll-1, xur+1, yur+1, self._rect_ptr(1))
        rectwrite (xll-1, yur-1, xur+1, yur+1, self._rect_ptr(2))
        rectwrite (xll-1, yll-1, xll+1, yur+1, self._rect_ptr(3))
        
    def zoom (self, o_plane, zoom, ortho):
        self.xl, self.xr, self.yl, self.yr = o_plane.ortho
        mxold, myold = 0, 0
        mx, my, mx1, my1 = self.mx, self.my, self.mx1, self.my1

        if self.dbuf:
            frontbuffer(1)
        if zoom:
            self.rect_write_outline(mx, my, mx1, my1)
   
        c_mx = Int16()
        qread(byref(c_mx))
        mx = c_mx.value
        qread(byref(c_mx))
        my = c_mx.value
        c_x, c_y = Int32(), Int32() 
        getsize(byref(c_x), byref(c_y))
        xs, ys = c_x.value, c_y.value
        getorigin(byref(c_x), byref(c_y))
        x0, y0 = c_x.value, c_y.value

        mx -= x0
        my -= y0

        if (mx > (xs-2)):
            mx = xs - 2
        elif (mx < 2):
            mx = 1
        
        if (my > (ys-2)):
            my = ys-2
        elif (my < 1):
            my = 1

        xl, xr, yl, yr = self.xl, self.xr, self.yl, self.yr
        xscale = (xr-xl)/float(xs-1)
        yscale = (yr-yl)/float(ys-1)
        x1 = xl + mx*xscale
        y1 = yl + my*yscale
        unqdevice(LEFTMOUSE)
        first = False
        xs -= 2
        ys -= 2
        x2, y2 = 0, 0

        while (getbutton(LEFTMOUSE)):
            mx1 = getvaluator(MOUSEX) - x0
            my1 = getvaluator(MOUSEY) - y0
            if ortho:
                d_mx = mx1-mx; d_my = my1-my

                if ( abs (d_mx) <> abs (d_my)) :
                    if (d_my >0):
                        my1 = my + abs (d_mx)
                    else:
                        my1 = my - abs (d_mx)

            if (mx1 > xs):
                mx1 = xs
            elif (mx1 < 2):
                mx1 = 1

            if (my1 > ys):
                my1 = ys
            elif (my1 < 1):
                my1 = 1

            x2 = xl + mx1*xscale
            y2 = yl + my1*yscale
            
            if not first:       
                color (WHITE)
                self.rect_read_outline (mx,my, mx1, my1)
                rect(x1,y1,x2 ,y2)
                gflush()
                mxold = mx1; myold = my1;
                first = True
            
            if ( (mx1 - mxold) != 0 or (my1-myold) != 0) :
                color (WHITE)
                self.rect_write_outline (mx,my, mxold, myold)
                self.rect_read_outline (mx,my, mx1, my1)
                rect (x1,y1, x2,y2)
                gflush()
                mxold = mx1; myold = my1;
            time.sleep (0.005)

        # End while               
        self.rect_write_outline (mx,my, mxold,myold)
        
        if x1 > x2: 
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
                        
        self.rect_read_outline (mx,my, mx1, my1)

        qdevice (LEFTMOUSE)

        if (x1 != x2 and y1 != y2):
            rect (x1,y1,x2, y2)
            sleep (0)
            if self.dbuf:
                backbuffer (1);
            o_plane.set((x1, x2, y1, y2))
            self.xl, self.xr, self.yl, self.yr = o_plane.ortho
            return 1
        else:
            if self.dbuf:
                backbuffer(1)
            return 0
    
    def set_doublebuffer (self, d=1):
        self.dbuf = d


######################################################################
class OrthoPlane(object):
    def __init__ (self, s = [-1.0, 1.0, -1.0, 1.0]):
        self.ortho = check_order (list (s))

    def __add__ (self, o_plane):
        for i in range (0, 4):
            self.ortho[i] = self.ortho[i] + o_plane[i]
        self.ortho = check_order (self.ortho)
        return self

    def __sub__ (self, o_plane):
        for i in range (0, 4):
            self.ortho[i] = self.ortho[i] - o_plane[i]
        self.ortho = check_order (self.ortho)
        return self

    def __getitem__ (self, i):
        return self.ortho[i]

    def set (self, s):
        self.ortho = check_order (list (s))

    def scale (self, xs, ys):
        x1 = (self.ortho[1] + self.ortho[0])*0.5
        y1 = (self.ortho[3] + self.ortho[2])*0.5
        lenx = (self.ortho[1] - self.ortho[0])*0.5*abs (xs)
        leny = (self.ortho[3] - self.ortho[2])*0.5*abs (ys)
        self.ortho = [x1 - lenx, x1 + lenx, y1 - leny, y1 +leny]

    def ortho2 (self):
        apply (ortho2, self.ortho)


######################################################################
class ZoomManager(object):
    def __init__ (self, zoom=None):
        self.NZ = 10
        self.store = []
        if zoom:
            self.store.append (zoom)
            self.def_zoom = zoom
        self.ins_indx = 0
        self.curr = 0

    def set_default_zoom (self, zoom):
        self.def_zoom = zoom
        self.store_zoom (zoom)

    def store_zoom (self, zoom):
        if len (self.store) > self.NZ:
            self.store[self.ins_indx] = zoom
        else:
            self.store.append (zoom)
        self.ins_indx = (self.ins_indx + 1)%self.NZ

    def next (self):
        self.curr = (self.curr + 1)%len (self.store)
        return self.store[self.curr]

    def previous (self):
        if self.curr == 0:
            self.curr = len (self.store) -1
        else:
            self.curr = self.curr -1
        return self.store[self.curr]

    def zoom_default (self):
        return self.def_zoom


######################################################################
def draw_axes (region, n_div):
    xl = region[0]
    xr = region[1]
    yl = region[2]
    yr = region[3]

    dx = (xr-xl)/float (n_div)
    dy = (yr-yl)/float (n_div)

    lenx = dx*0.25
    leny = dy*0.25

    color (AXES_COLOR)
    move2 (xl,yl+leny*1.5); rdr2 (xr-xl,0.0) # x axis
    move2 (xl+lenx*0.2,yl); rdr2 (0.0,yr-yl) # y axis    

    n = n_div +1
    ychar = yl
    y = yl+leny*1.5
    for i in range (0, n):  # x axis
        x = xl+i*dx
        xchar = x 
        move2 (x,y)
        rdr2 (0.0, leny)
        if i%2 == 0:
            str  = "%1.3e"%x
            cmov2 (xchar,ychar)
            charstr (str)

    xchar = xl+lenx*0.4
    x = xl +lenx*0.2
    for i in range (0, n): # y axis
        y = yl+i*dy
        ychar = y
        move2 (x,y)
        rdr2 (lenx,0.0)        
        if ((i != 0) and (i%2 == 0)):
            str = "%1.3e"%y
            cmov2 (xchar,ychar)
            charstr (str)
    gflush ()


help_msg = """The following keys are recognised by the Window:\n
Zoom and Pan Keys:
^^^^^^^^^^^^^^^^^^
Use the LEFT MOUSE BUTTON and drag the mouse to get a rubberband of
the region you want to zoom to and then click the MIDDLE MOUSE BUTTON
to set the screen to that particular zoom.

'O' or 'o' key - toggle orthographic zoom.

Left, Right, Up and Down arrow keys - pan the screen appropriately.
Equal/Plus key - zoom in.
Minus/Underscore key - zoom out.
Keypad + key - increase pan amount.
Keypad - key - reduce pan amount.
Keypad * key - increase zoom factor.
Keypad / key - reduce zoom factor.

'Z' or 'z' key - gets the next stored zoom view.
'X' or 'x' key - gets the previous stored zoom view.
'S' or 's' key - stores the current view as the default.
'D' or 'd' key - sets the current view to the default zoom.

Miscellaneous Keys:
^^^^^^^^^^^^^^^^^^^
'A' or 'a' key - toggle axes.
Spacebar - returns so the user can perform an iteration.
'5' key - allows the user to perform 5 iterations.
'H' or 'h' key - show this help screen.
F3 function key - Dumps the screen to an image.
Escape - Exit the visualization - WindowManager will return 1.
"""

######################################################################
class Window(object):
    
    """Derive a subclass and do what you want.  Remember to call the
    set_draw_method."""

    def __init__ (self, title="Plot Canvas", bg=BLACK, xsize=400,
                  ysize=400, double_buffer=1):
        minsize (xsize, xsize)
        self.root = winopen (title)
        winconstraints ()
        self.bg = bg
        self.dbuf = double_buffer
        if self.dbuf:
            doublebuffer ()
        else:
            singlebuffer ()
        self.setup_que ()
        self.setup_defaults ()
        self.mz = MouseZoom (self.dbuf)

    def setup_defaults (self):
        self.region = OrthoPlane ([-1.0, 1.0, -1.0, 1.0])
        self.new_region = OrthoPlane ()
        self.z_mgr = ZoomManager (self.region)
        self.changed = 1
        self.axis = 1        
        self.zoom = 0
        self.ortho = 1
        self.ymag=1.0/1.2
        self.xmag=self.ymag
        self.xshr=1.2
        self.yshr=self.xshr
        self.ddx = 1.1
        self.one_ddx = 1.0/self.ddx
        self.ddy = self.ddx
        self.one_ddy = self.one_ddx
        self.dummy = 1
        self.iter = 5
        self.n_axes = 10
        self.img_name = "img"
        self.n_img = 0
        
    def setup_que (self):
        # panning keys
        qdevice (LEFTARROWKEY)
        qdevice (RIGHTARROWKEY) 
        qdevice (UPARROWKEY) 
        qdevice (DOWNARROWKEY)
        # zoom in/out
        qdevice (EQUALKEY)
        qdevice (MINUSKEY)
        qdevice (ZKEY) # next zoom
        qdevice (XKEY) # prev zoom
        qdevice (SKEY)
        qdevice (DKEY)

        # increment/decrement the zoom and pan amounts
        qdevice (PADPLUSKEY)
        qdevice (PADMINUS) 
        qdevice (PADASTERKEY)
        qdevice (PADVIRGULEKEY)
        qdevice (AKEY)
        qdevice (HKEY) # help on keys

        qdevice (OKEY) # toggle orthographic zoom
        qdevice (LEFTMOUSE) # get zoomed region
        qdevice (MIDDLEMOUSE) # zoom to zoomed region
        tie (LEFTMOUSE, MOUSEX, MOUSEY)
        tie (MIDDLEMOUSE, MOUSEX, MOUSEY)
        

    def set_doublebuffer (self, d):
        val = winget ()
        winset (self.root)
        self.dbuf = d
        if self.dbuf:
            doublebuffer ()
            self.mz.set_doublebuffer (self.dbuf)
        else:
            singlebuffer ()
            self.mz.set_doublebuffer (self.dbuf)

        winset (val)

    def set_background_color (self, bg):
        self.bg = bg

    def set_title (self, title):
        wintitle (title)

    def set_num_axes_tick (self, n):
        self.n_axes = n

    def clear (self):
        color (self.bg)
        clear ()

    def get_window_id (self):
        return self.root

    def set_domain (self, s):
        "Argument is a tuple of the form (xl, xr, yl, yr)."        
        self.region.set (s)
        r = self.region
        self.dx = abs (r[1]-r[0])*0.02;
        self.dy = abs (r[3]-r[2])*0.02;
        self.region.ortho2 ()
        self.z_mgr.set_default_zoom (r)

    def set_draw_method (self, fun):
        self.drw = fun

    def set_changed (self, state):
        self.changed = state

    def draw (self):
        self.clear ()
        self.drw ()
        if self.axis:
            draw_axes (self.region, self.n_axes)
        self.changed = 0
        gflush ()
        if self.dbuf:
            swapbuffers ()
        
    def process_que (self, event, val):
        if self.changed:
            self.draw ()        
        if event == LEFTMOUSE:
            if val == 1:
                self.new_region = copy.deepcopy (self.region)
                self.zoom = self.mz.zoom (self.new_region, self.zoom,
                                          self.ortho)
        elif event == MIDDLEMOUSE:
            if val == 1:
                if self.zoom:
                    self.region = copy.deepcopy (self.new_region)
                    self.region.ortho2 ()
                    self.z_mgr.store_zoom (self.region)
                    self.changed = 1
                    self.zoom = 0                        

        elif event == LEFTARROWKEY:
            if val == 1:
                self.region = self.region - (self.dx, self.dx, 0.0, 0.0)
                self.region.ortho2 ()
                self.changed = 1
        elif event == RIGHTARROWKEY:
            if val == 1:
                self.region = self.region + (self.dx, self.dx, 0.0, 0.0)
                self.region.ortho2 ()
                self.changed = 1
        elif event == DOWNARROWKEY:
            if val == 1:
                self.region = self.region -(0.0, 0.0, self.dy, self.dy)
                self.region.ortho2 ()
                self.changed = 1
        elif event == UPARROWKEY:
            if val == 1:
                self.region = self.region + (0.0, 0.0, self.dy, self.dy)
                self.region.ortho2 ()
                self.changed = 1
        elif event == PADPLUSKEY:
            if val == 1:
                self.dx = self.dx*self.ddx
                self.dy = self.dy*self.ddy
        elif event == PADMINUS:
            if val == 1:
                self.dx = self.dx*self.one_ddx
                self.dy = self.dy*self.one_ddy                
        elif event == PADASTERKEY:
            if val == 1:
                self.xmag = self.xmag*self.one_ddx
                self.ymag = self.ymag*self.one_ddx
                self.xshr = self.xshr*self.ddx
                self.yshr = self.yshr*self.ddx
        elif event == PADASTERKEY:
            if val == 1:
                self.xmag = self.xmag*self.ddx
                self.ymag = self.ymag*self.ddx
                self.xshr = self.xshr*self.one_ddx
                self.yshr = self.yshr*self.one_ddx
        elif event == EQUALKEY:
            if val == 1:
                self.region.scale (self.xmag, self.ymag)
                self.region.ortho2 ()
                self.changed = 1
        elif event == MINUSKEY:
            if val == 1:
                self.region.scale (self.xshr, self.yshr)
                self.region.ortho2 ()
                self.changed = 1                    
                
        elif event == OKEY:
            if val == 1:
                if self.ortho:
                    self.ortho = 0
                    print "Toggling to non-orthographic mode."
                else:
                    self.ortho = 1
                    print "Toggling to orthographic mode."

        elif event == HKEY:
            if val == 1:
                    print help_msg,

        elif event == ZKEY: # next zoom
            if val == 1:
                self.region = self.z_mgr.next ()
                self.region.ortho2 ()
                self.changed = 1
                
        elif event == XKEY: # prev zoom
            if val == 1:
                self.region = self.z_mgr.previous ()
                self.region.ortho2 ()
                self.changed = 1
                
        elif event == DKEY: # default zoom
            if val == 1:
                self.region = self.z_mgr.zoom_default ()
                self.region.ortho2 ()
                self.changed = 1
                
        elif event == SKEY: # save as default zoom
            if val == 1:
                print "Stored current view as default zoom."
                self.z_mgr.set_default_zoom (self.region)

        elif event == AKEY:
            if val == 1:
                if self.axis:
                    self.axis = 0
                    print "Turning off axes."
                    self.changed = 1
                else:
                    self.axis = 1
                    if self.dbuf:
                        frontbuffer (1)
                    draw_axes (self.region, 10)
                    print "Turning on axes."
                    if self.dbuf:
                        backbuffer (1)


######################################################################
class WindowManager(object):

    """Manages all the Windows and allows que handling for multiple
    windows.  Derive a class to do something different."""
    
    def __init__ (self):
        self.win = {}
        ginit ()
        self.q_val = Int16()
        self.setup_que ()
        self.dummy = 1
        self.iter = 5
        self.img_name = "img"
        self.n_img = 0
        self.curr_win = None

    def setup_que (self):
        qdevice (REDRAW)
        qdevice (INPUTCHANGE)
        qdevice (WINQUIT)
        qdevice (ESCKEY)
        qdevice (SPACEKEY)
        qdevice (RETKEY)
        qdevice (F3KEY) # saves screen to png image.        

    def add_window (self, w):
        id = w.get_window_id ()
        self.win[id] = w
        self.curr_win = w
        winset (id)
        
    def remove_window (self, win):
        id = win.get_window_id ()
        del self.win[win.get_window_id ()]
        if winget () == id:
            # possible problems here?
            self.curr_win = None

    def set_num_iterations (self, iter):
        self.iter = iter

    def draw_all (self):
        val = winget ()
        for key in self.win.keys ():
            winset (key)
            self.win[key].draw ()

        winset (val)

    def show (self):
        ret_val = 0
        q_val = self.q_val
        self.draw_all ()

        if self.dummy > 1:
            self.dummy = self.dummy -1
        else:
            self.dummy = 1

        while (self.dummy == 1):
            event = qread (byref(q_val))
            val= q_val.value
            if event == REDRAW:
                self.curr_win = self.win[val]
                winset (val)
                reshapeviewport ()
                if self.curr_win:
                    self.curr_win.draw ()
                    
            elif event == INPUTCHANGE:                
                if val:
                    self.curr_win = self.win[val]
                    winset (val)
                    
            elif event == RETKEY:
                if val == 1:
                    self.dummy = self.dummy + self.iter

            elif event == SPACEKEY:
                if val == 1:
                    self.dummy = 0

            elif event == F3KEY:
                if val == 1:
                    f = "%s%d.png"%(self.img_name, self.n_img)
                    print "Saving screen ..."
                    sys.stdout.flush ()
                    gl2ppm ("|convert - %s"%f)
                    self.n_img = self.n_img + 1
                    print "Screen saved to", f

            elif (event == ESCKEY) or (event == WINQUIT):
                if val == 1:
                    self.dummy = 0
                    ret_val = 1
                    gexit ()
                    break

            elif self.curr_win:
                self.curr_win.process_que (event, val)
        return ret_val 


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
