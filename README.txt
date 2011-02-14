Python wrapper for Ygl
=======================

Ygl_, developed by Fred Hucht, emulates a significant subset of SGI's
`IRIS GL`_ on X11.  IRIS GL was a precursor to OpenGL. Ygl is an easy to
use library.  This package provides a ctypes-based, Python wrapper for
Ygl_.  It also provides a convenient and rather simple plotting
interface. 

It is perhaps a lot more convenient to use OpenGL via PyOpenGL_,
however, I am providing this wrapper for legacy support for applications
that have used Ygl.  I used to provide a SWIG_ based wrapper but a
ctypes based wrapper is a lot easier to build and install.
 

.. _Ygl: <http://WWW.thp.Uni-Duisburg.DE/Ygl/ReadMe.html>
.. _`IRIS GL`: http://en.wikipedia.org/wiki/IRIS_GL
.. _PyOpenGL: http://pyopengl.sf.net
.. _SWIG: http://www.swig.org


Installation
-------------

You will require to have Ygl installed.  Under Debian/Ubuntu, this is
easily done by installing libygl4 like so::

    $ sudo apt-get install libygl4

If you are not on Debian or Ubuntu you would need to install Ygl from
the sources downloadable from the Ygl_ webpage.

To install the wrapper you should be able to simply do::

   $ easy_install ygl


Examples
---------

There are a few sample examples in the examples directory of the source
package.  These should show you how to use both the ``ygl`` module and the
``yplot`` module.  A simple example of how to use ``yplot`` is in
``examples/plot.py``. 


