#!/usr/bin/env python

from numpy.distutils.core import setup, Extension

setup(
    name='py_interp',
    platforms=['GNU/Linux'],
    version='1.8.2',
    author='Marker Garcia',
    author_email='markel.garcia@ic3.cat',
    description=( 'It is a command line tool for interpolating WRF output files to pressure levels, ' 
                   'as well as computing a series of diagnostics such as low, medium and high cloud cover' ),
    keywords=['climate', 'weather'],
    install_requires=[ 'numpy', 'netCDF4', 'scipy'],
    url='https://github.com/markelg/py_interp',
    packages=['py_interp'],
    license='MIT',
    package_data={'py_interp': [
        'README.md',
    ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 "],
    scripts=['bin/py_interp'], 
    ext_modules = [Extension( 'py_interp_fortran', ['src/py_interp_fortran.F90']),]
)
