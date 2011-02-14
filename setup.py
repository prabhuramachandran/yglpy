#!/usr/bin/env python

from distutils.core import setup

setup(name='ygl',
      version='1.0',
      description='A wrapper for the Ygl plotting library.',
      author='Prabhu Ramachandran',
      author_email='prabhu@aero.iitb.ac.in',
      license='BSD',
      long_description=open('README.txt').read(),
      url='http://github.com/prabhuramachandran/yglpy',
      py_modules=['ygl', 'yplot'],
      platforms=['Linux', 'Mac OS-X', 'Unix', 'Solaris'],
      classifiers = [c.strip() for c in """\
        Development Status :: 5 - Production/Stable
        Environment :: X11 Applications
        Intended Audience :: Developers
        Intended Audience :: Science/Research
        License :: OSI Approved :: BSD License
        Operating System :: MacOS :: MacOS X
        Operating System :: POSIX
        Operating System :: Unix
        Programming Language :: Python
        Topic :: Multimedia :: Graphics
        Topic :: Scientific/Engineering :: Visualization
        Topic :: Software Development :: Libraries
        """.splitlines() if len(c.split()) > 0],
     )

