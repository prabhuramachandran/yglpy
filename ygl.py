"""
ctypes based wrapper for Ygl.  You will require to have libYgl.so
installed.  On Ubuntu/Debian systems this can be done by::

 $ sudo apt-get install libygl4

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2011, Prabhu Ramachandran.
# License: BSD Style.
    

import ctypes as C
from ctypes import byref, pointer, cast
from ctypes.util import find_library

lname = find_library('Ygl')
if lname is None:
    msg = '''Cannot seem to find libYgl.so, have you installed it.
On Ubuntu/Debian you should be able to install it using the command:
    sudo apt-get install libygl4
'''
    raise ImportError(msg)

# Load the library.
lib = C.cdll.LoadLibrary(lname)

######################################################################
# Constants
######################################################################

# Colors
BLACK = 0
WHITE = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
RED = 7

# For queue
NULLDEV = 0
BREAKKEY = 1
SETUPKEY = 2
LEFTCTRLKEY = 3
CAPSLOCKKEY = 4
RIGHTSHIFTKEY = 5
LEFTSHIFTKEY = 6
ESCKEY = 7
ONEKEY = 8
TABKEY = 9
QKEY = 10
AKEY = 11
SKEY = 12
NOSCRLKEY = 13
TWOKEY = 14
THREEKEY = 15
WKEY = 16
EKEY = 17
DKEY = 18
FKEY = 19
ZKEY = 20
XKEY = 21
FOURKEY = 22
FIVEKEY = 23
RKEY = 24
TKEY = 25
GKEY = 26
HKEY = 27
CKEY = 28
VKEY = 29
SIXKEY = 30
SEVENKEY = 31
YKEY = 32
UKEY = 33
JKEY = 34
KKEY = 35
BKEY = 36
NKEY = 37
EIGHTKEY = 38
NINEKEY = 39
IKEY = 40
OKEY = 41
LKEY = 42
SEMICOLONKEY = 43
MKEY = 44
COMMAKEY = 45
ZEROKEY = 46
MINUSKEY = 47
PKEY = 48
LEFTBRACKETKEY = 49
QUOTEKEY = 50
RETKEY = 51
PERIODKEY = 52
VIRGULEKEY = 53
EQUALKEY = 54
ACCENTGRAVEKEY = 55
RIGHTBRACKETKEY = 56
BACKSLASHKEY = 57
PAD1 = 58
PAD0 = 59
LINEFEEDKEY = 60
BACKSPACEKEY = 61
DELKEY = 62
PAD4 = 63
PAD2 = 64
PAD3 = 65
PADPERIOD = 66
PAD7 = 67
PAD8 = 68
PAD5 = 69
PAD6 = 70
PADPF2 = 71
PADPF1 = 72
LEFTARROWKEY = 73
DOWNARROWKEY = 74
PAD9 = 75
PADMINUS = 76
PADCOMMA = 77
PADPF4 = 78
PADPF3 = 79
RIGHTARROWKEY = 80
UPARROWKEY = 81
PADENTER = 82
SPACEKEY = 83
LEFTALTKEY = 143
RIGHTALTKEY = 144
RIGHTCTRLKEY = 145
F1KEY = 146
F2KEY = 147
F3KEY = 148
F4KEY = 149
F5KEY = 150
F6KEY = 151
F7KEY = 152
F8KEY = 153
F9KEY = 154
F10KEY = 155
F11KEY = 156
F12KEY = 157
PRINTSCREENKEY = 158
SCROLLLOCKKEY = 159
PAUSEKEY = 160
INSERTKEY = 161
HOMEKEY = 162
PAGEUPKEY = 163
ENDKEY = 164
PAGEDOWNKEY = 165
NUMLOCKKEY = 166
PADVIRGULEKEY = 167
PADASTERKEY = 168
PADPLUSKEY = 169
MOUSE1 = 101
MOUSE2 = 102
MOUSE3 = 103
LEFTMOUSE = 103
MIDDLEMOUSE = 102
RIGHTMOUSE = 101
MENUBUTTON = 101

WHEELUP = 200
WHEELDOWN = 201
MOUSEX = 266
MOUSEY = 267
ANYKEY = 512
KEYBD = 513
TIMER0 = 515
TIMER1 = 516
TIMER2 = 517
TIMER3 = 518
REDRAW = 528
INPUTCHANGE = 534
WINCLOSE = 537
WINFREEZE = 539
WINTHAW = 540
WINQUIT = 542
DEPTHCHANGE = 543

MAXYGLDEVICE = 544

# For readsource
SRC_AUTO = 0
SRC_FRONT = 1
SRC_BACK = 2

# For getdisplaymode
DMRGB = 0L
DMSINGLE = 1L
DMDOUBLE = 2L
DMRGBDOUBLE = 5L

# For getgdesc
GD_XPMAX = 1L
GD_YPMAX = 2L

# for setpup
PUP_NONE = 0
PUP_GREY = 1

# For logicop
LO_ZERO = 0x0
LO_AND = 0x1
LO_ANDR = 0x2
LO_SRC = 0x3
LO_ANDI = 0x4
LO_DST = 0x5
LO_XOR = 0x6
LO_OR = 0x7
LO_NOR = 0x8
LO_XNOR = 0x9
LO_NDST = 0xa
LO_ORR = 0xb
LO_NSRC = 0xc
LO_ORI = 0xd
LO_NAND = 0xe
LO_ONE = 0xf
LO_MIN = 0x10
LO_MAX = 0x11
LO_AVG = 0x12
LO_DMS = 0x13
LO_SMD = 0x14
LO_SUM = 0x15

# For mmode
MSINGLE = 0
MPROJECTION = 1
MVIEWING = 2

# For blendfunction
BF_ZERO = 0
BF_ONE = 1
BF_SC = 2
BF_MSC = 3
BF_SA = 4
BF_MSA = 5
BF_DA = 6
BF_MDA = 7
BF_DC = 8
BF_MDC = 9
BF_MIN_SA_MDA = 10


# For zfunction
ZF_NEVER = 0
ZF_LESS = 1
ZF_EQUAL = 2
ZF_LEQUAL = 3
ZF_GREATER = 4
ZF_NOTEQUAL = 5
ZF_GEQUAL = 6
ZF_ALWAYS = 7

# For lmdef; Material properties
DEFMATERIAL = 0
EMISSION = 1
AMBIENT = 2
DIFFUSE = 3
SPECULAR = 4
SHININESS = 5
COLORINDEXES = 6
ALPHA = 7

# LIGHT properties
DEFLIGHT = 100
LCOLOR = 101
POSITION = 102
SPOTDIRECTION = 103
SPOTLIGHT = 104

# LIGHTINGMODEL properties
DEFLMODEL = 200
LOCALVIEWER = 201
ATTENUATION = 202
ATTENUATION2 = 203
TWOSIDE = 204

# TARGET constants
MATERIAL = 1000
BACKMATERIAL = 1001
LIGHT0 = 1100
LIGHT1 = 1101
LIGHT2 = 1102
LIGHT3 = 1103
LIGHT4 = 1104
LIGHT5 = 1105
LIGHT6 = 1106
LIGHT7 = 1107
LMODEL = 1200

# For lmcolor modes
LMC_COLOR = 0
LMC_EMISSION = 1
LMC_AMBIENT = 2
LMC_DIFFUSE = 3
LMC_SPECULAR = 4
LMC_AD = 5
LMC_NULL = 6

# For lmdef constants
LMNULL = 0.0

# For shademodel
FLAT = 0
GOURAUD = 1

######################################################################
## Special types used in Ygl and mappings to ctypes.
######################################################################
Angle = C.c_short
Matrix = C.c_float*16
Window = C.c_ulong
Uint16 = C.c_ushort
Uint32 = C.c_uint
Float32 = C.c_float
Int32 = C.c_int
Int16 = C.c_short
Uint8 = C.c_ubyte
Device = C.c_ushort
Byte = C.c_ubyte
Int8 = C.c_char
Uint64 = C.c_ulong
Colorindex = C.c_ushort
Float64 = C.c_double
Coord = C.c_float
Int64 = C.c_long
Screencoord = C.c_short
Scoord = C.c_short
Char8 = C.c_char
short = C.c_short
Icoord = C.c_int
RGBvalue = C.c_ubyte
Linestyle = C.c_ushort

######################################################################
# Simple wrappers for functions
######################################################################

sleep = lib.sleep
sleep.restype = C.c_uint
sleep.argtypes = [C.c_uint]

## Automatically wrapped functions
if hasattr(lib, 'clear'):
    clear = lib.clear
    clear.restype = None

if hasattr(lib, 'pnt2'):
    pnt2 = lib.pnt2
    pnt2.restype = None
    pnt2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'pnt2i'):
    pnt2i = lib.pnt2i
    pnt2i.restype = None
    pnt2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'pnt2s'):
    pnt2s = lib.pnt2s
    pnt2s.restype = None
    pnt2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'move2'):
    move2 = lib.move2
    move2.restype = None
    move2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'move2i'):
    move2i = lib.move2i
    move2i.restype = None
    move2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'move2s'):
    move2s = lib.move2s
    move2s.restype = None
    move2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'rmv2'):
    rmv2 = lib.rmv2
    rmv2.restype = None
    rmv2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'rmv2i'):
    rmv2i = lib.rmv2i
    rmv2i.restype = None
    rmv2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'rmv2s'):
    rmv2s = lib.rmv2s
    rmv2s.restype = None
    rmv2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'draw2'):
    draw2 = lib.draw2
    draw2.restype = None
    draw2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'draw2i'):
    draw2i = lib.draw2i
    draw2i.restype = None
    draw2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'draw2s'):
    draw2s = lib.draw2s
    draw2s.restype = None
    draw2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'rdr2'):
    rdr2 = lib.rdr2
    rdr2.restype = None
    rdr2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'rdr2i'):
    rdr2i = lib.rdr2i
    rdr2i.restype = None
    rdr2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'rdr2s'):
    rdr2s = lib.rdr2s
    rdr2s.restype = None
    rdr2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'arc'):
    arc = lib.arc
    arc.restype = None
    arc.argtypes = [C.c_float, C.c_float, C.c_float, C.c_short, C.c_short]

if hasattr(lib, 'arci'):
    arci = lib.arci
    arci.restype = None
    arci.argtypes = [C.c_int, C.c_int, C.c_int, C.c_short, C.c_short]

if hasattr(lib, 'arcs'):
    arcs = lib.arcs
    arcs.restype = None
    arcs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'arcf'):
    arcf = lib.arcf
    arcf.restype = None
    arcf.argtypes = [C.c_float, C.c_float, C.c_float, C.c_short, C.c_short]

if hasattr(lib, 'arcfi'):
    arcfi = lib.arcfi
    arcfi.restype = None
    arcfi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_short, C.c_short]

if hasattr(lib, 'arcfs'):
    arcfs = lib.arcfs
    arcfs.restype = None
    arcfs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'circ'):
    circ = lib.circ
    circ.restype = None
    circ.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'circi'):
    circi = lib.circi
    circi.restype = None
    circi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'circs'):
    circs = lib.circs
    circs.restype = None
    circs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'circf'):
    circf = lib.circf
    circf.restype = None
    circf.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'circfi'):
    circfi = lib.circfi
    circfi.restype = None
    circfi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'circfs'):
    circfs = lib.circfs
    circfs.restype = None
    circfs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rect'):
    rect = lib.rect
    rect.restype = None
    rect.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'recti'):
    recti = lib.recti
    recti.restype = None
    recti.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rects'):
    rects = lib.rects
    rects.restype = None
    rects.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rectf'):
    rectf = lib.rectf
    rectf.restype = None
    rectf.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'rectfi'):
    rectfi = lib.rectfi
    rectfi.restype = None
    rectfi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rectfs'):
    rectfs = lib.rectfs
    rectfs.restype = None
    rectfs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'sbox'):
    sbox = lib.sbox
    sbox.restype = None
    sbox.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'sboxi'):
    sboxi = lib.sboxi
    sboxi.restype = None
    sboxi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'sboxs'):
    sboxs = lib.sboxs
    sboxs.restype = None
    sboxs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'sboxf'):
    sboxf = lib.sboxf
    sboxf.restype = None
    sboxf.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'sboxfi'):
    sboxfi = lib.sboxfi
    sboxfi.restype = None
    sboxfi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'sboxfs'):
    sboxfs = lib.sboxfs
    sboxfs.restype = None
    sboxfs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'concave'):
    concave = lib.concave
    concave.restype = None
    concave.argtypes = [C.c_int]

if hasattr(lib, 'pmv2'):
    pmv2 = lib.pmv2
    pmv2.restype = None
    pmv2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'pmv2i'):
    pmv2i = lib.pmv2i
    pmv2i.restype = None
    pmv2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'pmv2s'):
    pmv2s = lib.pmv2s
    pmv2s.restype = None
    pmv2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'rpmv2'):
    rpmv2 = lib.rpmv2
    rpmv2.restype = None
    rpmv2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'rpmv2i'):
    rpmv2i = lib.rpmv2i
    rpmv2i.restype = None
    rpmv2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'rpmv2s'):
    rpmv2s = lib.rpmv2s
    rpmv2s.restype = None
    rpmv2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'pdr2'):
    pdr2 = lib.pdr2
    pdr2.restype = None
    pdr2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'pdr2i'):
    pdr2i = lib.pdr2i
    pdr2i.restype = None
    pdr2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'pdr2s'):
    pdr2s = lib.pdr2s
    pdr2s.restype = None
    pdr2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'rpdr2'):
    rpdr2 = lib.rpdr2
    rpdr2.restype = None
    rpdr2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'rpdr2i'):
    rpdr2i = lib.rpdr2i
    rpdr2i.restype = None
    rpdr2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'rpdr2s'):
    rpdr2s = lib.rpdr2s
    rpdr2s.restype = None
    rpdr2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'pclos'):
    pclos = lib.pclos
    pclos.restype = None

if hasattr(lib, 'poly2'):
    poly2 = lib.poly2
    poly2.restype = None
    # Unable to wrap function args:
    #   extern void  poly2 		( Int32,  Coord[][2] );


if hasattr(lib, 'poly2i'):
    poly2i = lib.poly2i
    poly2i.restype = None
    # Unable to wrap function args:
    #   extern void  poly2i		( Int32, Icoord[][2] );


if hasattr(lib, 'poly2s'):
    poly2s = lib.poly2s
    poly2s.restype = None
    # Unable to wrap function args:
    #   extern void  poly2s		( Int32, Scoord[][2] );


if hasattr(lib, 'polf2'):
    polf2 = lib.polf2
    polf2.restype = None
    # Unable to wrap function args:
    #   extern void  polf2 		( Int32,  Coord[][2] );


if hasattr(lib, 'polf2i'):
    polf2i = lib.polf2i
    polf2i.restype = None
    # Unable to wrap function args:
    #   extern void  polf2i		( Int32, Icoord[][2] );


if hasattr(lib, 'polf2s'):
    polf2s = lib.polf2s
    polf2s.restype = None
    # Unable to wrap function args:
    #   extern void  polf2s		( Int32, Scoord[][2] );


if hasattr(lib, 'bgnpoint'):
    bgnpoint = lib.bgnpoint
    bgnpoint.restype = None

if hasattr(lib, 'bgnline'):
    bgnline = lib.bgnline
    bgnline.restype = None

if hasattr(lib, 'bgnclosedline'):
    bgnclosedline = lib.bgnclosedline
    bgnclosedline.restype = None

if hasattr(lib, 'bgnpolygon'):
    bgnpolygon = lib.bgnpolygon
    bgnpolygon.restype = None

if hasattr(lib, 'bgntmesh'):
    bgntmesh = lib.bgntmesh
    bgntmesh.restype = None

if hasattr(lib, 'endpoint'):
    endpoint = lib.endpoint
    endpoint.restype = None

if hasattr(lib, 'endline'):
    endline = lib.endline
    endline.restype = None

if hasattr(lib, 'endclosedline'):
    endclosedline = lib.endclosedline
    endclosedline.restype = None

if hasattr(lib, 'endpolygon'):
    endpolygon = lib.endpolygon
    endpolygon.restype = None

if hasattr(lib, 'endtmesh'):
    endtmesh = lib.endtmesh
    endtmesh.restype = None

if hasattr(lib, 'v2s'):
    v2s = lib.v2s
    v2s.restype = None
    # Unable to wrap function args:
    #   extern void  v2s		( Int16[2] );


if hasattr(lib, 'v2i'):
    v2i = lib.v2i
    v2i.restype = None
    # Unable to wrap function args:
    #   extern void  v2i		( Int32[2] );


if hasattr(lib, 'v2f'):
    v2f = lib.v2f
    v2f.restype = None
    # Unable to wrap function args:
    #   extern void  v2f		( Float32[2] );


if hasattr(lib, 'v2d'):
    v2d = lib.v2d
    v2d.restype = None
    # Unable to wrap function args:
    #   extern void  v2d		( Float64[2] );


if hasattr(lib, 'cmov2'):
    cmov2 = lib.cmov2
    cmov2.restype = None
    cmov2.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'cmov2i'):
    cmov2i = lib.cmov2i
    cmov2i.restype = None
    cmov2i.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'cmov2s'):
    cmov2s = lib.cmov2s
    cmov2s.restype = None
    cmov2s.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'getcpos'):
    getcpos = lib.getcpos
    getcpos.restype = None
    getcpos.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'arcx'):
    arcx = lib.arcx
    arcx.restype = None
    arcx.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float, C.c_short, C.c_short]

if hasattr(lib, 'arcxi'):
    arcxi = lib.arcxi
    arcxi.restype = None
    arcxi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_short, C.c_short]

if hasattr(lib, 'arcxs'):
    arcxs = lib.arcxs
    arcxs.restype = None
    arcxs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'arcxf'):
    arcxf = lib.arcxf
    arcxf.restype = None
    arcxf.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float, C.c_short, C.c_short]

if hasattr(lib, 'arcxfi'):
    arcxfi = lib.arcxfi
    arcxfi.restype = None
    arcxfi.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_short, C.c_short]

if hasattr(lib, 'arcxfs'):
    arcxfs = lib.arcxfs
    arcxfs.restype = None
    arcxfs.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'tie'):
    tie = lib.tie
    tie.restype = None
    tie.argtypes = [C.c_ushort, C.c_ushort, C.c_ushort]

if hasattr(lib, 'noise'):
    noise = lib.noise
    noise.restype = None
    noise.argtypes = [C.c_ushort, C.c_short]

if hasattr(lib, 'isqueued'):
    isqueued = lib.isqueued
    isqueued.restype = C.c_int
    isqueued.argtypes = [C.c_short]

if hasattr(lib, 'qdevice'):
    qdevice = lib.qdevice
    qdevice.restype = None
    qdevice.argtypes = [C.c_ushort]

if hasattr(lib, 'unqdevice'):
    unqdevice = lib.unqdevice
    unqdevice.restype = None
    unqdevice.argtypes = [C.c_ushort]

if hasattr(lib, 'qreset'):
    qreset = lib.qreset
    qreset.restype = None

if hasattr(lib, 'qtest'):
    qtest = lib.qtest
    qtest.restype = C.c_int

if hasattr(lib, 'qread'):
    qread = lib.qread
    qread.restype = C.c_int
    qread.argtypes = [C.POINTER(C.c_short)]

if hasattr(lib, 'qenter'):
    qenter = lib.qenter
    qenter.restype = None
    qenter.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'pick'):
    pick = lib.pick
    pick.restype = None
    pick.argtypes = [C.POINTER(C.c_short), C.c_int]

if hasattr(lib, 'endpick'):
    endpick = lib.endpick
    endpick.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 endpick 		( Int16[] );


if hasattr(lib, 'picksize'):
    picksize = lib.picksize
    picksize.restype = None
    picksize.argtypes = [C.c_short, C.c_short]

if hasattr(lib, 'initnames'):
    initnames = lib.initnames
    initnames.restype = None

if hasattr(lib, 'loadname'):
    loadname = lib.loadname
    loadname.restype = None
    loadname.argtypes = [C.c_short]

if hasattr(lib, 'pushname'):
    pushname = lib.pushname
    pushname.restype = None
    pushname.argtypes = [C.c_short]

if hasattr(lib, 'popname'):
    popname = lib.popname
    popname.restype = None

if hasattr(lib, 'singlebuffer'):
    singlebuffer = lib.singlebuffer
    singlebuffer.restype = None

if hasattr(lib, 'doublebuffer'):
    doublebuffer = lib.doublebuffer
    doublebuffer.restype = None

if hasattr(lib, 'swapbuffers'):
    swapbuffers = lib.swapbuffers
    swapbuffers.restype = None

if hasattr(lib, 'frontbuffer'):
    frontbuffer = lib.frontbuffer
    frontbuffer.restype = None
    frontbuffer.argtypes = [C.c_int]

if hasattr(lib, 'backbuffer'):
    backbuffer = lib.backbuffer
    backbuffer.restype = None
    backbuffer.argtypes = [C.c_int]

if hasattr(lib, 'gflush'):
    gflush = lib.gflush
    gflush.restype = None

if hasattr(lib, 'gsync'):
    gsync = lib.gsync
    gsync.restype = None

if hasattr(lib, 'getXwid'):
    getXwid = lib.getXwid
    getXwid.restype = C.c_ulong

if hasattr(lib, 'getXdid'):
    getXdid = lib.getXdid
    getXdid.restype = C.c_ulong

if hasattr(lib, 'wintitle'):
    wintitle = lib.wintitle
    wintitle.restype = None
    wintitle.argtypes = [C.c_char_p]

if hasattr(lib, 'winset'):
    winset = lib.winset
    winset.restype = None
    winset.argtypes = [C.c_int]

if hasattr(lib, 'winget'):
    winget = lib.winget
    winget.restype = C.c_int

if hasattr(lib, 'getplanes'):
    getplanes = lib.getplanes
    getplanes.restype = C.c_int

if hasattr(lib, 'getvaluator'):
    getvaluator = lib.getvaluator
    getvaluator.restype = C.c_int
    getvaluator.argtypes = [C.c_ushort]

if hasattr(lib, 'getbutton'):
    getbutton = lib.getbutton
    getbutton.restype = C.c_int
    getbutton.argtypes = [C.c_ushort]

if hasattr(lib, 'gversion'):
    gversion = lib.gversion
    gversion.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 gversion		( Char8[12] );


if hasattr(lib, 'ortho2'):
    ortho2 = lib.ortho2
    ortho2.restype = None
    ortho2.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'viewport'):
    viewport = lib.viewport
    viewport.restype = None
    viewport.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'getviewport'):
    getviewport = lib.getviewport
    getviewport.restype = None
    getviewport.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'reshapeviewport'):
    reshapeviewport = lib.reshapeviewport
    reshapeviewport.restype = None

if hasattr(lib, 'pushviewport'):
    pushviewport = lib.pushviewport
    pushviewport.restype = None

if hasattr(lib, 'popviewport'):
    popviewport = lib.popviewport
    popviewport.restype = None

if hasattr(lib, 'winpop'):
    winpop = lib.winpop
    winpop.restype = None

if hasattr(lib, 'winpush'):
    winpush = lib.winpush
    winpush.restype = None

if hasattr(lib, 'windepth'):
    windepth = lib.windepth
    windepth.restype = C.c_int
    windepth.argtypes = [C.c_int]

if hasattr(lib, 'linewidth'):
    linewidth = lib.linewidth
    linewidth.restype = None
    linewidth.argtypes = [C.c_short]

if hasattr(lib, 'getlwidth'):
    getlwidth = lib.getlwidth
    getlwidth.restype = C.c_int

if hasattr(lib, 'deflinestyle'):
    deflinestyle = lib.deflinestyle
    deflinestyle.restype = None
    deflinestyle.argtypes = [C.c_int, C.c_ushort]

if hasattr(lib, 'setlinestyle'):
    setlinestyle = lib.setlinestyle
    setlinestyle.restype = None
    setlinestyle.argtypes = [C.c_int]

if hasattr(lib, 'getlstyle'):
    getlstyle = lib.getlstyle
    getlstyle.restype = C.c_int

if hasattr(lib, 'lsrepeat'):
    lsrepeat = lib.lsrepeat
    lsrepeat.restype = None
    lsrepeat.argtypes = [C.c_int]

if hasattr(lib, 'getlsrepeat'):
    getlsrepeat = lib.getlsrepeat
    getlsrepeat.restype = C.c_int

if hasattr(lib, 'getdisplaymode'):
    getdisplaymode = lib.getdisplaymode
    getdisplaymode.restype = C.c_int

if hasattr(lib, 'setbell'):
    setbell = lib.setbell
    setbell.restype = None
    setbell.argtypes = [C.c_char]

if hasattr(lib, 'ringbell'):
    ringbell = lib.ringbell
    ringbell.restype = None

if hasattr(lib, 'getgdesc'):
    getgdesc = lib.getgdesc
    getgdesc.restype = C.c_int
    getgdesc.argtypes = [C.c_int]

if hasattr(lib, 'foreground'):
    foreground = lib.foreground
    foreground.restype = None

if hasattr(lib, 'logicop'):
    logicop = lib.logicop
    logicop.restype = None
    logicop.argtypes = [C.c_int]

if hasattr(lib, 'getmatrix'):
    getmatrix = lib.getmatrix
    getmatrix.restype = None
    getmatrix.argtypes = [C.c_float*16]

if hasattr(lib, 'loadXfont'):
    loadXfont = lib.loadXfont
    loadXfont.restype = None
    loadXfont.argtypes = [C.c_int, C.c_char_p]

if hasattr(lib, 'font'):
    font = lib.font
    font.restype = None
    font.argtypes = [C.c_short]

if hasattr(lib, 'getfont'):
    getfont = lib.getfont
    getfont.restype = C.c_int

if hasattr(lib, 'getfontencoding'):
    getfontencoding = lib.getfontencoding
    getfontencoding.restype = None
    getfontencoding.argtypes = [C.c_char_p]

if hasattr(lib, 'getheight'):
    getheight = lib.getheight
    getheight.restype = C.c_int

if hasattr(lib, 'getdescender'):
    getdescender = lib.getdescender
    getdescender.restype = C.c_int

if hasattr(lib, 'strwidth'):
    strwidth = lib.strwidth
    strwidth.restype = C.c_int
    strwidth.argtypes = [C.c_char_p]

if hasattr(lib, 'charstr'):
    charstr = lib.charstr
    charstr.restype = None
    charstr.argtypes = [C.c_char_p]

if hasattr(lib, 'mapcolor'):
    mapcolor = lib.mapcolor
    mapcolor.restype = None
    mapcolor.argtypes = [C.c_ushort, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'RGBcolor'):
    RGBcolor = lib.RGBcolor
    RGBcolor.restype = None
    RGBcolor.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'cpack'):
    cpack = lib.cpack
    cpack.restype = None
    cpack.argtypes = [C.c_uint]

if hasattr(lib, 'c3s'):
    c3s = lib.c3s
    c3s.restype = None
    # Unable to wrap function args:
    #   extern void  c3s		( Int16[3] );


if hasattr(lib, 'c3i'):
    c3i = lib.c3i
    c3i.restype = None
    # Unable to wrap function args:
    #   extern void  c3i		( Int32[3] );


if hasattr(lib, 'c3f'):
    c3f = lib.c3f
    c3f.restype = None
    # Unable to wrap function args:
    #   extern void  c3f		( Float32[3] );


if hasattr(lib, 'getcolor'):
    getcolor = lib.getcolor
    getcolor.restype = C.c_int

if hasattr(lib, 'getmcolor'):
    getmcolor = lib.getmcolor
    getmcolor.restype = None
    getmcolor.argtypes = [C.c_ushort, C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'getmcolors'):
    getmcolors = lib.getmcolors
    getmcolors.restype = None
    getmcolors.argtypes = [C.c_ushort, C.c_ushort, C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'gRGBcolor'):
    gRGBcolor = lib.gRGBcolor
    gRGBcolor.restype = None
    gRGBcolor.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'color'):
    color = lib.color
    color.restype = None
    color.argtypes = [C.c_ushort]

if hasattr(lib, 'readsource'):
    readsource = lib.readsource
    readsource.restype = None
    readsource.argtypes = [C.c_int]

if hasattr(lib, 'rectzoom'):
    rectzoom = lib.rectzoom
    rectzoom.restype = None
    rectzoom.argtypes = [C.c_float, C.c_float]

if hasattr(lib, 'crectread'):
    crectread = lib.crectread
    crectread.restype = C.c_int
    crectread.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_ubyte)]

if hasattr(lib, 'rectread'):
    rectread = lib.rectread
    rectread.restype = C.c_int
    rectread.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_short)]

if hasattr(lib, 'lrectread'):
    lrectread = lib.lrectread
    lrectread.restype = C.c_int
    lrectread.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_int)]

if hasattr(lib, 'crectwrite'):
    crectwrite = lib.crectwrite
    crectwrite.restype = None
    crectwrite.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_ubyte)]

if hasattr(lib, 'rectwrite'):
    rectwrite = lib.rectwrite
    rectwrite.restype = None
    rectwrite.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_short)]

if hasattr(lib, 'lrectwrite'):
    lrectwrite = lib.lrectwrite
    lrectwrite.restype = None
    lrectwrite.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.POINTER(C.c_int)]

if hasattr(lib, 'rectcopy'):
    rectcopy = lib.rectcopy
    rectcopy.restype = None
    rectcopy.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'readpixels'):
    readpixels = lib.readpixels
    readpixels.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 readpixels	( Int16, Colorindex[] );


if hasattr(lib, 'writepixels'):
    writepixels = lib.writepixels
    writepixels.restype = None
    # Unable to wrap function args:
    #   extern void  writepixels	( Int16, Colorindex[] );


if hasattr(lib, 'readRGB'):
    readRGB = lib.readRGB
    readRGB.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 readRGB		( Int16, RGBvalue[], RGBvalue[], RGBvalue[] );


if hasattr(lib, 'writeRGB'):
    writeRGB = lib.writeRGB
    writeRGB.restype = None
    # Unable to wrap function args:
    #   extern void  writeRGB		( Int16, RGBvalue[], RGBvalue[], RGBvalue[] );


if hasattr(lib, 'blendfunction'):
    blendfunction = lib.blendfunction
    blendfunction.restype = None
    blendfunction.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'addtopup'):
    addtopup = lib.addtopup
    addtopup.restype = None
    # Unable to wrap function args:
    #   extern void  addtopup		( Int32, Char8 *, ... );


if hasattr(lib, 'defpup'):
    defpup = lib.defpup
    defpup.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 defpup		( Char8 *, ... );


if hasattr(lib, 'dopup'):
    dopup = lib.dopup
    dopup.restype = C.c_int
    dopup.argtypes = [C.c_int]

if hasattr(lib, 'freepup'):
    freepup = lib.freepup
    freepup.restype = None
    freepup.argtypes = [C.c_int]

if hasattr(lib, 'newpup'):
    newpup = lib.newpup
    newpup.restype = C.c_int

if hasattr(lib, 'setpup'):
    setpup = lib.setpup
    setpup.restype = None
    setpup.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'minsize'):
    minsize = lib.minsize
    minsize.restype = None
    minsize.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'maxsize'):
    maxsize = lib.maxsize
    maxsize.restype = None
    maxsize.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'prefsize'):
    prefsize = lib.prefsize
    prefsize.restype = None
    prefsize.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'prefposition'):
    prefposition = lib.prefposition
    prefposition.restype = None
    prefposition.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'stepunit'):
    stepunit = lib.stepunit
    stepunit.restype = None
    stepunit.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'keepaspect'):
    keepaspect = lib.keepaspect
    keepaspect.restype = None
    keepaspect.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'noport'):
    noport = lib.noport
    noport.restype = None

if hasattr(lib, 'noborder'):
    noborder = lib.noborder
    noborder.restype = None

if hasattr(lib, 'ginit'):
    ginit = lib.ginit
    ginit.restype = None

if hasattr(lib, 'winconstraints'):
    winconstraints = lib.winconstraints
    winconstraints.restype = None

if hasattr(lib, 'winopen'):
    winopen = lib.winopen
    winopen.restype = C.c_int
    winopen.argtypes = [C.c_char_p]

if hasattr(lib, 'swinopen'):
    swinopen = lib.swinopen
    swinopen.restype = C.c_int
    swinopen.argtypes = [C.c_int]

if hasattr(lib, 'winposition'):
    winposition = lib.winposition
    winposition.restype = None
    winposition.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'winmove'):
    winmove = lib.winmove
    winmove.restype = None
    winmove.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'getsize'):
    getsize = lib.getsize
    getsize.restype = None
    getsize.argtypes = [C.POINTER(C.c_int), C.POINTER(C.c_int)]

if hasattr(lib, 'getorigin'):
    getorigin = lib.getorigin
    getorigin.restype = None
    getorigin.argtypes = [C.POINTER(C.c_int), C.POINTER(C.c_int)]

if hasattr(lib, 'RGBmode'):
    RGBmode = lib.RGBmode
    RGBmode.restype = None

if hasattr(lib, 'cmode'):
    cmode = lib.cmode
    cmode.restype = None

if hasattr(lib, 'gconfig'):
    gconfig = lib.gconfig
    gconfig.restype = None

if hasattr(lib, 'winclose'):
    winclose = lib.winclose
    winclose.restype = None
    winclose.argtypes = [C.c_int]

if hasattr(lib, 'gexit'):
    gexit = lib.gexit
    gexit.restype = None

if hasattr(lib, 'gl2ppm'):
    gl2ppm = lib.gl2ppm
    gl2ppm.restype = C.c_int
    gl2ppm.argtypes = [C.c_char_p]

if hasattr(lib, 'cmov'):
    cmov = lib.cmov
    cmov.restype = None
    cmov.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'cmovi'):
    cmovi = lib.cmovi
    cmovi.restype = None
    cmovi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'cmovs'):
    cmovs = lib.cmovs
    cmovs.restype = None
    cmovs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'pnt'):
    pnt = lib.pnt
    pnt.restype = None
    pnt.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'pnti'):
    pnti = lib.pnti
    pnti.restype = None
    pnti.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'pnts'):
    pnts = lib.pnts
    pnts.restype = None
    pnts.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'move'):
    move = lib.move
    move.restype = None
    move.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'movei'):
    movei = lib.movei
    movei.restype = None
    movei.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'moves'):
    moves = lib.moves
    moves.restype = None
    moves.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rmv'):
    rmv = lib.rmv
    rmv.restype = None
    rmv.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'rmvi'):
    rmvi = lib.rmvi
    rmvi.restype = None
    rmvi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rmvs'):
    rmvs = lib.rmvs
    rmvs.restype = None
    rmvs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'draw'):
    draw = lib.draw
    draw.restype = None
    draw.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'drawi'):
    drawi = lib.drawi
    drawi.restype = None
    drawi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'draws'):
    draws = lib.draws
    draws.restype = None
    draws.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rdr'):
    rdr = lib.rdr
    rdr.restype = None
    rdr.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'rdri'):
    rdri = lib.rdri
    rdri.restype = None
    rdri.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rdrs'):
    rdrs = lib.rdrs
    rdrs.restype = None
    rdrs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'pmv'):
    pmv = lib.pmv
    pmv.restype = None
    pmv.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'pmvi'):
    pmvi = lib.pmvi
    pmvi.restype = None
    pmvi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'pmvs'):
    pmvs = lib.pmvs
    pmvs.restype = None
    pmvs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rpmv'):
    rpmv = lib.rpmv
    rpmv.restype = None
    rpmv.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'rpmvi'):
    rpmvi = lib.rpmvi
    rpmvi.restype = None
    rpmvi.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rpmvs'):
    rpmvs = lib.rpmvs
    rpmvs.restype = None
    rpmvs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'pdr'):
    pdr = lib.pdr
    pdr.restype = None
    pdr.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'pdri'):
    pdri = lib.pdri
    pdri.restype = None
    pdri.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'pdrs'):
    pdrs = lib.pdrs
    pdrs.restype = None
    pdrs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rpdr'):
    rpdr = lib.rpdr
    rpdr.restype = None
    rpdr.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'rpdri'):
    rpdri = lib.rpdri
    rpdri.restype = None
    rpdri.argtypes = [C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'rpdrs'):
    rpdrs = lib.rpdrs
    rpdrs.restype = None
    rpdrs.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'polf'):
    polf = lib.polf
    polf.restype = None
    # Unable to wrap function args:
    #   extern void  polf 		( Int32, Coord[][3] );


if hasattr(lib, 'polfi'):
    polfi = lib.polfi
    polfi.restype = None
    # Unable to wrap function args:
    #   extern void  polfi 		( Int32, Icoord[][3] );


if hasattr(lib, 'polfs'):
    polfs = lib.polfs
    polfs.restype = None
    # Unable to wrap function args:
    #   extern void  polfs 		( Int32, Scoord[][3] );


if hasattr(lib, 'v3s'):
    v3s = lib.v3s
    v3s.restype = None
    # Unable to wrap function args:
    #   extern void  v3s 		( Int16[3] );


if hasattr(lib, 'v3i'):
    v3i = lib.v3i
    v3i.restype = None
    # Unable to wrap function args:
    #   extern void  v3i 		( Int32[3] );


if hasattr(lib, 'v3f'):
    v3f = lib.v3f
    v3f.restype = None
    # Unable to wrap function args:
    #   extern void  v3f 		( Float32[3] );


if hasattr(lib, 'v3d'):
    v3d = lib.v3d
    v3d.restype = None
    # Unable to wrap function args:
    #   extern void  v3d 		( Float64[3] );


if hasattr(lib, 'v4s'):
    v4s = lib.v4s
    v4s.restype = None
    # Unable to wrap function args:
    #   extern void  v4s 		( Int16[4] );


if hasattr(lib, 'v4i'):
    v4i = lib.v4i
    v4i.restype = None
    # Unable to wrap function args:
    #   extern void  v4i 		( Int32[4] );


if hasattr(lib, 'v4f'):
    v4f = lib.v4f
    v4f.restype = None
    # Unable to wrap function args:
    #   extern void  v4f 		( Float32[4] );


if hasattr(lib, 'v4d'):
    v4d = lib.v4d
    v4d.restype = None
    # Unable to wrap function args:
    #   extern void  v4d 		( Float64[4] );


if hasattr(lib, 'swaptmesh'):
    swaptmesh = lib.swaptmesh
    swaptmesh.restype = None

if hasattr(lib, 'ortho'):
    ortho = lib.ortho
    ortho.restype = None
    ortho.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'lookat'):
    lookat = lib.lookat
    lookat.restype = None
    lookat.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float, C.c_float, C.c_float, C.c_short]

if hasattr(lib, 'window'):
    window = lib.window
    window.restype = None
    window.argtypes = [C.c_float, C.c_float, C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'perspective'):
    perspective = lib.perspective
    perspective.restype = None
    perspective.argtypes = [C.c_short, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'polarview'):
    polarview = lib.polarview
    polarview.restype = None
    polarview.argtypes = [C.c_float, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'rot'):
    rot = lib.rot
    rot.restype = None
    rot.argtypes = [C.c_float, C.c_char]

if hasattr(lib, 'rotate'):
    rotate = lib.rotate
    rotate.restype = None
    rotate.argtypes = [C.c_short, C.c_char]

if hasattr(lib, 'scale'):
    scale = lib.scale
    scale.restype = None
    scale.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'translate'):
    translate = lib.translate
    translate.restype = None
    translate.argtypes = [C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'loadmatrix'):
    loadmatrix = lib.loadmatrix
    loadmatrix.restype = None
    loadmatrix.argtypes = [C.c_float*16]

if hasattr(lib, 'multmatrix'):
    multmatrix = lib.multmatrix
    multmatrix.restype = None
    multmatrix.argtypes = [C.c_float*16]

if hasattr(lib, 'pushmatrix'):
    pushmatrix = lib.pushmatrix
    pushmatrix.restype = None

if hasattr(lib, 'popmatrix'):
    popmatrix = lib.popmatrix
    popmatrix.restype = None

if hasattr(lib, 'shademodel'):
    shademodel = lib.shademodel
    shademodel.restype = None
    shademodel.argtypes = [C.c_int]

if hasattr(lib, 'c4f'):
    c4f = lib.c4f
    c4f.restype = None
    # Unable to wrap function args:
    #   extern void  c4f 		( Float32[4] );


if hasattr(lib, 'c4i'):
    c4i = lib.c4i
    c4i.restype = None
    # Unable to wrap function args:
    #   extern void  c4i 		( Int32[4] );


if hasattr(lib, 'c4s'):
    c4s = lib.c4s
    c4s.restype = None
    # Unable to wrap function args:
    #   extern void  c4s 		( Int16[4] );


if hasattr(lib, 'n3f'):
    n3f = lib.n3f
    n3f.restype = None
    # Unable to wrap function args:
    #   extern void  n3f 		( Float32[3] );


if hasattr(lib, 'normal'):
    normal = lib.normal
    normal.restype = None
    # Unable to wrap function args:
    #   extern void  normal 		( Coord[3] );


if hasattr(lib, 'backface'):
    backface = lib.backface
    backface.restype = None
    backface.argtypes = [C.c_int]

if hasattr(lib, 'frontface'):
    frontface = lib.frontface
    frontface.restype = None
    frontface.argtypes = [C.c_int]

if hasattr(lib, 'getmmode'):
    getmmode = lib.getmmode
    getmmode.restype = C.c_int

if hasattr(lib, 'mmode'):
    mmode = lib.mmode
    mmode.restype = None
    mmode.argtypes = [C.c_short]

if hasattr(lib, 'zbuffer'):
    zbuffer = lib.zbuffer
    zbuffer.restype = None
    zbuffer.argtypes = [C.c_int]

if hasattr(lib, 'zclear'):
    zclear = lib.zclear
    zclear.restype = None

if hasattr(lib, 'zdraw'):
    zdraw = lib.zdraw
    zdraw.restype = None
    zdraw.argtypes = [C.c_int]

if hasattr(lib, 'zfunction'):
    zfunction = lib.zfunction
    zfunction.restype = None
    zfunction.argtypes = [C.c_int]

if hasattr(lib, 'czclear'):
    czclear = lib.czclear
    czclear.restype = None
    czclear.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'depthcue'):
    depthcue = lib.depthcue
    depthcue.restype = None
    depthcue.argtypes = [C.c_int]

if hasattr(lib, 'lRGBrange'):
    lRGBrange = lib.lRGBrange
    lRGBrange.restype = None
    lRGBrange.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_int, C.c_int]

if hasattr(lib, 'lsetdepth'):
    lsetdepth = lib.lsetdepth
    lsetdepth.restype = None
    lsetdepth.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'lshaderange'):
    lshaderange = lib.lshaderange
    lshaderange.restype = None
    lshaderange.argtypes = [C.c_ushort, C.c_ushort, C.c_int, C.c_int]

if hasattr(lib, 'genobj'):
    genobj = lib.genobj
    genobj.restype = C.c_int

if hasattr(lib, 'isobj'):
    isobj = lib.isobj
    isobj.restype = C.c_int
    isobj.argtypes = [C.c_int]

if hasattr(lib, 'makeobj'):
    makeobj = lib.makeobj
    makeobj.restype = None
    makeobj.argtypes = [C.c_int]

if hasattr(lib, 'getopenobj'):
    getopenobj = lib.getopenobj
    getopenobj.restype = C.c_int

if hasattr(lib, 'closeobj'):
    closeobj = lib.closeobj
    closeobj.restype = None

if hasattr(lib, 'callobj'):
    callobj = lib.callobj
    callobj.restype = None
    callobj.argtypes = [C.c_int]

if hasattr(lib, 'delobj'):
    delobj = lib.delobj
    delobj.restype = None
    delobj.argtypes = [C.c_int]

if hasattr(lib, 'lmbind'):
    lmbind = lib.lmbind
    lmbind.restype = None
    lmbind.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'lmcolor'):
    lmcolor = lib.lmcolor
    lmcolor.restype = None
    lmcolor.argtypes = [C.c_int]

if hasattr(lib, 'lmdef'):
    lmdef = lib.lmdef
    lmdef.restype = None
    # Unable to wrap function args:
    #   extern void  lmdef 		( Int16, Int16, Int16, Float32[] );


if hasattr(lib, 'RGBwritemask'):
    RGBwritemask = lib.RGBwritemask
    RGBwritemask.restype = None
    RGBwritemask.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'drawmode'):
    drawmode = lib.drawmode
    drawmode.restype = None
    drawmode.argtypes = [C.c_int]

if hasattr(lib, 'iconsize'):
    iconsize = lib.iconsize
    iconsize.restype = None
    iconsize.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'overlay'):
    overlay = lib.overlay
    overlay.restype = None
    overlay.argtypes = [C.c_int]

if hasattr(lib, 'pushattributes'):
    pushattributes = lib.pushattributes
    pushattributes.restype = None

if hasattr(lib, 'popattributes'):
    popattributes = lib.popattributes
    popattributes.restype = None

if hasattr(lib, 'fullscrn'):
    fullscrn = lib.fullscrn
    fullscrn.restype = None

if hasattr(lib, 'endfullscrn'):
    endfullscrn = lib.endfullscrn
    endfullscrn.restype = None

if hasattr(lib, 'scrmask'):
    scrmask = lib.scrmask
    scrmask.restype = None
    scrmask.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'attachcursor'):
    attachcursor = lib.attachcursor
    attachcursor.restype = None
    attachcursor.argtypes = [C.c_ushort, C.c_ushort]

if hasattr(lib, 'bbox2'):
    bbox2 = lib.bbox2
    bbox2.restype = None
    bbox2.argtypes = [C.c_short, C.c_short, C.c_float, C.c_float, C.c_float, C.c_float]

if hasattr(lib, 'bbox2i'):
    bbox2i = lib.bbox2i
    bbox2i.restype = None
    bbox2i.argtypes = [C.c_short, C.c_short, C.c_int, C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'bbox2s'):
    bbox2s = lib.bbox2s
    bbox2s.restype = None
    bbox2s.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'bgnsurface'):
    bgnsurface = lib.bgnsurface
    bgnsurface.restype = None

if hasattr(lib, 'bgntrim'):
    bgntrim = lib.bgntrim
    bgntrim.restype = None

if hasattr(lib, 'blankscreen'):
    blankscreen = lib.blankscreen
    blankscreen.restype = None
    blankscreen.argtypes = [C.c_int]

if hasattr(lib, 'blanktime'):
    blanktime = lib.blanktime
    blanktime.restype = None
    blanktime.argtypes = [C.c_int]

if hasattr(lib, 'blink'):
    blink = lib.blink
    blink.restype = None
    blink.argtypes = [C.c_short, C.c_ushort, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'blkqread'):
    blkqread = lib.blkqread
    blkqread.restype = C.c_int
    blkqread.argtypes = [C.POINTER(C.c_short), C.c_short]

if hasattr(lib, 'chunksize'):
    chunksize = lib.chunksize
    chunksize.restype = None
    chunksize.argtypes = [C.c_int]

if hasattr(lib, 'clkoff'):
    clkoff = lib.clkoff
    clkoff.restype = None

if hasattr(lib, 'clkon'):
    clkon = lib.clkon
    clkon.restype = None

if hasattr(lib, 'colorf'):
    colorf = lib.colorf
    colorf.restype = None
    colorf.argtypes = [C.c_float]

if hasattr(lib, 'compactify'):
    compactify = lib.compactify
    compactify.restype = None
    compactify.argtypes = [C.c_int]

if hasattr(lib, 'crv'):
    crv = lib.crv
    crv.restype = None
    # Unable to wrap function args:
    #   extern void crv ( Coord[4][3] );


if hasattr(lib, 'crvn'):
    crvn = lib.crvn
    crvn.restype = None
    # Unable to wrap function args:
    #   extern void crvn ( Int32, Coord[][3] );


if hasattr(lib, 'curorigin'):
    curorigin = lib.curorigin
    curorigin.restype = None
    curorigin.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'cursoff'):
    cursoff = lib.cursoff
    cursoff.restype = None

if hasattr(lib, 'curson'):
    curson = lib.curson
    curson.restype = None

if hasattr(lib, 'curstype'):
    curstype = lib.curstype
    curstype.restype = None
    curstype.argtypes = [C.c_int]

if hasattr(lib, 'curvebasis'):
    curvebasis = lib.curvebasis
    curvebasis.restype = None
    curvebasis.argtypes = [C.c_short]

if hasattr(lib, 'curveit'):
    curveit = lib.curveit
    curveit.restype = None
    curveit.argtypes = [C.c_short]

if hasattr(lib, 'curveprecision'):
    curveprecision = lib.curveprecision
    curveprecision.restype = None
    curveprecision.argtypes = [C.c_short]

if hasattr(lib, 'cyclemap'):
    cyclemap = lib.cyclemap
    cyclemap.restype = None
    cyclemap.argtypes = [C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'defbasis'):
    defbasis = lib.defbasis
    defbasis.restype = None
    defbasis.argtypes = [C.c_int, C.c_float*16]

if hasattr(lib, 'defcursor'):
    defcursor = lib.defcursor
    defcursor.restype = None
    defcursor.argtypes = [C.c_short, C.POINTER(C.c_ushort)]

if hasattr(lib, 'defpattern'):
    defpattern = lib.defpattern
    defpattern.restype = None
    defpattern.argtypes = [C.c_short, C.c_short, C.POINTER(C.c_short)]

if hasattr(lib, 'deltag'):
    deltag = lib.deltag
    deltag.restype = None
    deltag.argtypes = [C.c_int]

if hasattr(lib, 'editobj'):
    editobj = lib.editobj
    editobj.restype = None
    editobj.argtypes = [C.c_int]

if hasattr(lib, 'endselect'):
    endselect = lib.endselect
    endselect.restype = C.c_int
    # Unable to wrap function args:
    #   extern Int32 endselect ( Int16[] );


if hasattr(lib, 'endsurface'):
    endsurface = lib.endsurface
    endsurface.restype = None

if hasattr(lib, 'endtrim'):
    endtrim = lib.endtrim
    endtrim.restype = None

if hasattr(lib, 'finish'):
    finish = lib.finish
    finish.restype = None

if hasattr(lib, 'fudge'):
    fudge = lib.fudge
    fudge.restype = None
    fudge.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'gRGBmask'):
    gRGBmask = lib.gRGBmask
    gRGBmask.restype = None
    gRGBmask.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'gammaramp'):
    gammaramp = lib.gammaramp
    gammaramp.restype = None
    # Unable to wrap function args:
    #   extern void gammaramp ( Int16[256], Int16[256], Int16[256] );


if hasattr(lib, 'gbegin'):
    gbegin = lib.gbegin
    gbegin.restype = None

if hasattr(lib, 'gentag'):
    gentag = lib.gentag
    gentag.restype = C.c_int

if hasattr(lib, 'getbackface'):
    getbackface = lib.getbackface
    getbackface.restype = C.c_int

if hasattr(lib, 'getbuffer'):
    getbuffer = lib.getbuffer
    getbuffer.restype = C.c_int

if hasattr(lib, 'getcmmode'):
    getcmmode = lib.getcmmode
    getcmmode.restype = C.c_int

if hasattr(lib, 'getcursor'):
    getcursor = lib.getcursor
    getcursor.restype = None
    getcursor.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_ushort), C.POINTER(C.c_ushort), C.POINTER(C.c_int)]

if hasattr(lib, 'getdcm'):
    getdcm = lib.getdcm
    getdcm.restype = C.c_int

if hasattr(lib, 'getdev'):
    getdev = lib.getdev
    getdev.restype = None
    # Unable to wrap function args:
    #   extern void getdev ( Int32, Device[], short[] );


if hasattr(lib, 'getdrawmode'):
    getdrawmode = lib.getdrawmode
    getdrawmode.restype = C.c_int

if hasattr(lib, 'getgpos'):
    getgpos = lib.getgpos
    getgpos.restype = None
    getgpos.argtypes = [C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float)]

if hasattr(lib, 'getmap'):
    getmap = lib.getmap
    getmap.restype = C.c_int

if hasattr(lib, 'getnurbsproperty'):
    getnurbsproperty = lib.getnurbsproperty
    getnurbsproperty.restype = None
    getnurbsproperty.argtypes = [C.c_int, C.POINTER(C.c_float)]

if hasattr(lib, 'getpattern'):
    getpattern = lib.getpattern
    getpattern.restype = C.c_int

if hasattr(lib, 'getscrmask'):
    getscrmask = lib.getscrmask
    getscrmask.restype = None
    getscrmask.argtypes = [C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'getshade'):
    getshade = lib.getshade
    getshade.restype = C.c_int

if hasattr(lib, 'getsm'):
    getsm = lib.getsm
    getsm.restype = C.c_int

if hasattr(lib, 'getwritemask'):
    getwritemask = lib.getwritemask
    getwritemask.restype = C.c_int

if hasattr(lib, 'getzbuffer'):
    getzbuffer = lib.getzbuffer
    getzbuffer.restype = C.c_int

if hasattr(lib, 'greset'):
    greset = lib.greset
    greset.restype = None

if hasattr(lib, 'gselect'):
    gselect = lib.gselect
    gselect.restype = None
    gselect.argtypes = [C.POINTER(C.c_short), C.c_int]

if hasattr(lib, 'icontitle'):
    icontitle = lib.icontitle
    icontitle.restype = None
    icontitle.argtypes = [C.c_char_p]

if hasattr(lib, 'imakebackground'):
    imakebackground = lib.imakebackground
    imakebackground.restype = None

if hasattr(lib, 'istag'):
    istag = lib.istag
    istag.restype = C.c_int
    istag.argtypes = [C.c_int]

if hasattr(lib, 'lampoff'):
    lampoff = lib.lampoff
    lampoff.restype = None
    lampoff.argtypes = [C.c_char]

if hasattr(lib, 'lampon'):
    lampon = lib.lampon
    lampon.restype = None
    lampon.argtypes = [C.c_char]

if hasattr(lib, 'lgetdepth'):
    lgetdepth = lib.lgetdepth
    lgetdepth.restype = None
    lgetdepth.argtypes = [C.POINTER(C.c_int), C.POINTER(C.c_int)]

if hasattr(lib, 'linesmooth'):
    linesmooth = lib.linesmooth
    linesmooth.restype = None
    linesmooth.argtypes = [C.c_int]

if hasattr(lib, 'maketag'):
    maketag = lib.maketag
    maketag.restype = None
    maketag.argtypes = [C.c_int]

if hasattr(lib, 'mapcolors'):
    mapcolors = lib.mapcolors
    mapcolors.restype = None
    mapcolors.argtypes = [C.c_ushort, C.c_ushort, C.POINTER(C.c_short), C.POINTER(C.c_short), C.POINTER(C.c_short)]

if hasattr(lib, 'mapw'):
    mapw = lib.mapw
    mapw.restype = None
    mapw.argtypes = [C.c_int, C.c_short, C.c_short, C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float)]

if hasattr(lib, 'mapw2'):
    mapw2 = lib.mapw2
    mapw2.restype = None
    mapw2.argtypes = [C.c_int, C.c_short, C.c_short, C.POINTER(C.c_float), C.POINTER(C.c_float)]

if hasattr(lib, 'multimap'):
    multimap = lib.multimap
    multimap.restype = None

if hasattr(lib, 'nurbscurve'):
    nurbscurve = lib.nurbscurve
    nurbscurve.restype = None
    nurbscurve.argtypes = [C.c_int, C.POINTER(C.c_double), C.c_int, C.POINTER(C.c_double), C.c_int, C.c_int]

if hasattr(lib, 'nurbssurface'):
    nurbssurface = lib.nurbssurface
    nurbssurface.restype = None
    nurbssurface.argtypes = [C.c_int, C.POINTER(C.c_double), C.c_int, C.POINTER(C.c_double), C.c_int, C.c_int, C.POINTER(C.c_double), C.c_int, C.c_int, C.c_int]

if hasattr(lib, 'objdelete'):
    objdelete = lib.objdelete
    objdelete.restype = None
    objdelete.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'objinsert'):
    objinsert = lib.objinsert
    objinsert.restype = None
    objinsert.argtypes = [C.c_int]

if hasattr(lib, 'objreplace'):
    objreplace = lib.objreplace
    objreplace.restype = None
    objreplace.argtypes = [C.c_int]

if hasattr(lib, 'onemap'):
    onemap = lib.onemap
    onemap.restype = None

if hasattr(lib, 'patch'):
    patch = lib.patch
    patch.restype = None
    patch.argtypes = [C.c_float*16, C.c_float*16, C.c_float*16]

if hasattr(lib, 'patchbasis'):
    patchbasis = lib.patchbasis
    patchbasis.restype = None
    patchbasis.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'patchcurves'):
    patchcurves = lib.patchcurves
    patchcurves.restype = None
    patchcurves.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'patchprecision'):
    patchprecision = lib.patchprecision
    patchprecision.restype = None
    patchprecision.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'pixmode'):
    pixmode = lib.pixmode
    pixmode.restype = None
    pixmode.argtypes = [C.c_int, C.c_int]

if hasattr(lib, 'pntsmooth'):
    pntsmooth = lib.pntsmooth
    pntsmooth.restype = None
    pntsmooth.argtypes = [C.c_int]

if hasattr(lib, 'poly'):
    poly = lib.poly
    poly.restype = None
    # Unable to wrap function args:
    #   extern void poly 		( Int32, Coord[][3] );


if hasattr(lib, 'polyi'):
    polyi = lib.polyi
    polyi.restype = None
    # Unable to wrap function args:
    #   extern void polyi 		( Int32, Icoord[][3] );


if hasattr(lib, 'polys'):
    polys = lib.polys
    polys.restype = None
    # Unable to wrap function args:
    #   extern void polys 		( Int32, Scoord[][3] );


if hasattr(lib, 'polygonlist'):
    polygonlist = lib.polygonlist
    polygonlist.restype = None
    polygonlist.argtypes = [C.c_int, C.c_int, C.POINTER(None)]

if hasattr(lib, 'polylinelist'):
    polylinelist = lib.polylinelist
    polylinelist.restype = None
    polylinelist.argtypes = [C.c_int, C.c_int, C.POINTER(None)]

if hasattr(lib, 'pwlcurve'):
    pwlcurve = lib.pwlcurve
    pwlcurve.restype = None
    pwlcurve.argtypes = [C.c_int, C.POINTER(C.c_double), C.c_int, C.c_int]

if hasattr(lib, 'rcrv'):
    rcrv = lib.rcrv
    rcrv.restype = None
    # Unable to wrap function args:
    #   extern void rcrv ( Coord[4][4] );


if hasattr(lib, 'rcrvn'):
    rcrvn = lib.rcrvn
    rcrvn.restype = None
    # Unable to wrap function args:
    #   extern void rcrvn ( Int32, Coord[4][4] );


if hasattr(lib, 'rpatch'):
    rpatch = lib.rpatch
    rpatch.restype = None
    rpatch.argtypes = [C.c_float*16, C.c_float*16, C.c_float*16, C.c_float*16]

if hasattr(lib, 'screenspace'):
    screenspace = lib.screenspace
    screenspace.restype = None

if hasattr(lib, 'set_dither'):
    set_dither = lib.set_dither
    set_dither.restype = None
    set_dither.argtypes = [C.c_int]

if hasattr(lib, 'setcursor'):
    setcursor = lib.setcursor
    setcursor.restype = None
    setcursor.argtypes = [C.c_short, C.c_ushort, C.c_ushort]

if hasattr(lib, 'setdblights'):
    setdblights = lib.setdblights
    setdblights.restype = None
    setdblights.argtypes = [C.c_int]

if hasattr(lib, 'setmap'):
    setmap = lib.setmap
    setmap.restype = None
    setmap.argtypes = [C.c_short]

if hasattr(lib, 'setnurbsproperty'):
    setnurbsproperty = lib.setnurbsproperty
    setnurbsproperty.restype = None
    setnurbsproperty.argtypes = [C.c_int, C.c_float]

if hasattr(lib, 'setpattern'):
    setpattern = lib.setpattern
    setpattern.restype = None
    setpattern.argtypes = [C.c_short]

if hasattr(lib, 'setvaluator'):
    setvaluator = lib.setvaluator
    setvaluator.restype = None
    setvaluator.argtypes = [C.c_ushort, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'splf'):
    splf = lib.splf
    splf.restype = None
    # Unable to wrap function args:
    #   extern void splf ( Int32, Coord[][3], Colorindex[] );


if hasattr(lib, 'splf2'):
    splf2 = lib.splf2
    splf2.restype = None
    # Unable to wrap function args:
    #   extern void splf2 ( Int32, Coord[][2], Colorindex[] );


if hasattr(lib, 'splf2i'):
    splf2i = lib.splf2i
    splf2i.restype = None
    # Unable to wrap function args:
    #   extern void splf2i ( Int32, Icoord[][2], Colorindex[] );


if hasattr(lib, 'splf2s'):
    splf2s = lib.splf2s
    splf2s.restype = None
    # Unable to wrap function args:
    #   extern void splf2s ( Int32, Scoord[][2], Colorindex[] );


if hasattr(lib, 'splfi'):
    splfi = lib.splfi
    splfi.restype = None
    # Unable to wrap function args:
    #   extern void splfi ( Int32, Icoord[][3], Colorindex[] );


if hasattr(lib, 'splfs'):
    splfs = lib.splfs
    splfs.restype = None
    # Unable to wrap function args:
    #   extern void splfs ( Int32, Scoord[][3], Colorindex[] );


if hasattr(lib, 'subpixel'):
    subpixel = lib.subpixel
    subpixel.restype = None
    subpixel.argtypes = [C.c_int]

if hasattr(lib, 'swapinterval'):
    swapinterval = lib.swapinterval
    swapinterval.restype = None
    swapinterval.argtypes = [C.c_short]

if hasattr(lib, 'textport'):
    textport = lib.textport
    textport.restype = None
    textport.argtypes = [C.c_short, C.c_short, C.c_short, C.c_short]

if hasattr(lib, 'tpoff'):
    tpoff = lib.tpoff
    tpoff.restype = None

if hasattr(lib, 'tpon'):
    tpon = lib.tpon
    tpon.restype = None

if hasattr(lib, 'underlay'):
    underlay = lib.underlay
    underlay.restype = None
    underlay.argtypes = [C.c_int]

if hasattr(lib, 'wmpack'):
    wmpack = lib.wmpack
    wmpack.restype = None
    wmpack.argtypes = [C.c_uint]

if hasattr(lib, 'writemask'):
    writemask = lib.writemask
    writemask.restype = None
    writemask.argtypes = [C.c_ushort]

if hasattr(lib, 'zsource'):
    zsource = lib.zsource
    zsource.restype = None
    zsource.argtypes = [C.c_int]

if hasattr(lib, 'zwritemask'):
    zwritemask = lib.zwritemask
    zwritemask.restype = None
    zwritemask.argtypes = [C.c_int]

