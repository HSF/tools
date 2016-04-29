# HSFTEMPLATE

Please add some lines describing the project!

## Building the project

    mkdir build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX=<installdir> [-DHSFTEMPLATE_BUILD_DOCS=ON] <path to sources>
    make -j<number of cores on your machine>
    make install

The `HSFTEMPLATE_BUILD_DOCS` variable is optional, and should be passed if you wish to
build the Doxygen based API documentation. Please note that this requires an existing
installation of [Doxygen](http://www.doxygen.org/index.html). If CMake cannot locate
Doxygen, its install location should be added into `CMAKE_PREFIX_PATH`. 
For further details please have a look at [the CMake tutorial](http://www.cmake.org/cmake-tutorial/).

## Building the documentation

The documentation of the project is based on doxygen. To build the documentation,
the project must have been configured with `HSFTEMPLATE_BUILD_DOCS` enabled, as
described earlier. It can then be built and installed:

    make doc
    make install

By default, this installs the documentation into `<installdir>/share/doc/HSFTEMPLATE/doxygen`.

## Creating a package with CPack

A cpack based package can be created by invoking

    make package

## Running the tests

To run the tests of the project, first build it and then invoke

    make test

## Inclusion into other projects

If you want to build your own project against HSFTEMPLATE, CMake may be the best option for you. Just add its location to `CMAKE_PREFIX_PATH` and call `find_package(HSFTEMPLATE)` within your CMakeLists.txt.
