#!/usr/bin/env python

"""Automated wrapper code generation for Ygl.h.  This is Ygl.h specific
and is unlikely to ever work with any other headers.  Yes, I did try
the ctypeslib's h2xml -> xml2py route but no luck.
"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2011, Prabhu Ramachandran 
# License: BSD Style.

import ctypes as C
import sys

def constants(fname):
    """Given the header file in fname, generates the constants."""
    header = open(fname)
    print "## Constants"
    for line in header:
        if line.startswith('#define'):
            val = line.split()
            if len(val) > 2:
                print "%s = %s"%(val[1], val[2])

def is_function(line):
    """Returns True if line is a function definition."""
    l = line.strip()
    if l.startswith('extern') and ('(' in l) \
            and (')' in l ) and l.endswith(';'):
                return True
    return False
    
# Conversion of types.
typmap = {'void': 'None', 'Int8': 'C.c_char', 'Uint8': 'C.c_ubyte',
          'Int16': 'C.c_short', 'Uint16': 'C.c_ushort',
          'Int32': 'C.c_int', 'Uint32': 'C.c_uint',
          'Int64': 'C.c_long', 'Uint64': 'C.c_ulong',
          'Float32': 'C.c_float', 'Float64': 'C.c_double',
          'Char8': 'C.c_char', 'Void': 'None',
          'Byte': 'C.c_ubyte', 'RGBvalue': 'C.c_ubyte',
          'Colorindex': 'C.c_ushort', 'Device': 'C.c_ushort',
          'Linestyle': 'C.c_ushort', 'Angle': 'C.c_short', 
          'Scoord': 'C.c_short', 'Screencoord': 'C.c_short',
          'Icoord': 'C.c_int', 'Coord': 'C.c_float',
          'Window': 'C.c_ulong',
          'int': 'C.c_int', 'Matrix': 'C.c_float*16',
          'char': 'C.c_char', 'short': 'C.c_short'}

def _process_arg(arg):
    """Returns a tuple, the first value being the success in
    processing the argument `arg`, the second being the appropriate
    type."""
    if '[' in arg:
        # FIXME
        arg_base = arg[:arg.find('[')]
        return (False, typmap[arg_base])
    elif '...' in arg:
        return (False, arg)
    elif '*' in arg:
        if 'char' in arg or 'const char' in arg or 'Char8' in arg:
            return (True, 'C.c_char_p')
        else:
            arg_base = arg[:arg.find('*')].strip()
            return (True, 'POINTER(%s)'%typmap[arg_base])
    else:
        return (True, typmap[arg])


def process_function(line):
    func, args = line.strip().split('(')
    args = args.replace(')', '')
    args = args.replace(';', '')
    args = [x.strip() for x in args.split(',')]
    func = func.replace('extern', '')
    ret, name = func.split()
    p_args = [_process_arg(x) for x in args]
    valid = [x[0] for x in p_args]
    vals = [x[1] for x in p_args]

    ignore = ['getXdpy', 'getXgc', 'winX']

    if name.replace('*', '') in ignore:
        return

    print "if hasattr(lib, '%s'):"%name
    print "    %s = lib.%s"%(name, name)
    print "    %s.restype = %s"%(name, typmap[ret])
    if False in valid:
        print "    # Unable to wrap function args:"
        print "    # %s"%line
        print
    else:
        if len(vals) == 1 and vals[0] == 'None':
            print
        else:
            argtypes = ', '.join(vals)
            print "    %s.argtypes = [%s]"%(name, argtypes)
            print


def functions(fname):
    """Wrap the functions given the header file."""
    header = open(fname)
    print "## Automatically wrapped functions"
    for line in header:
        if is_function(line):
            process_function(line)


def special_types():
    """Create simple types similar to Ygl for certain types."""
    ignore = ['char', 'void', 'Void', 'int']
    print "## Special types used in Ygl and mappings to ctypes."
    for key in typmap.keys():
        if key not in ignore:
            print "%s = %s"%(key, typmap[key])

def main():
    if len(sys.argv) != 2:
        print "usage: generator.py /path/to/Ygl.h"
        sys.exit(1)
    header = sys.argv[1]
    constants(header)
    special_types()
    functions(header)

if __name__ == '__main__':
    main()

