#!/usr/bin/env python3
###############################################################################
# (c) Copyright 2015-2020 CERN                                                #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENCE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

__author__ = "Benedikt Hegner (CERN)"
__copyright__ = "Copyright (C) 2015-2020 CERN"
__license__ = "GPLv3"
__version__ = "0.2"

import os
import platform
import re
import sys

try:
    import distro
except ImportError:
    print("Failed to import required Python 'distro' module", file=sys.stderr)
    sys.exit(1)

from argparse import ArgumentParser
from subprocess import run, PIPE, STDOUT

class HSFPlatform(object):
    def __init__(self):
        pass

    @staticmethod
    def os():
        """
        Return the Operating System and its major version like
        "macos109", "ubuntu14", ...
        """
        system = platform.system()
        if system == "Linux":
            pf = distro.linux_distribution(full_distribution_name=0)[0]
            version = distro.linux_distribution(full_distribution_name=0)[1].split(".")[0]
            # SLC6 misidentifies itself has RedHat
            if pf == "redhat":
                if "CERN" in platform.linux_distribution()[0]:
                    pf = "slc"
        elif system == "Darwin":
            pf = "macos10"
            version = platform.mac_ver()[0].split(".")[1]
        elif system == "Windows":
            pass
        else:
            raise f"System {system} not supported"

        return (pf+version).lower()

    @staticmethod
    def architecture():
        """
        return architecture as defined by platform.machine()
        """
        return platform.machine()

    @staticmethod
    def compiler():
        """
        Derive the name and version of the compiler from the
        'COMPILER'or 'CC' environment variables
        If these variables are not set, it falls back to reasonable defaults.

        """
        system = platform.system()
        if os.getenv('COMPILER') and not os.getenv("CC"):
            compiler = os.getenv('COMPILER')
        else:
          if os.getenv('CC'):
            ccommand = os.getenv('CC')
          elif system == 'Windows':
            ccommand = 'cl'
          elif system == 'Darwin':
            ccommand = 'clang'
          else:
            ccommand = 'gcc'
        if ccommand == 'cl':
            versioninfo = run((ccommand), stdout=PIPE, stderr=STDOUT).stdout.decode("utf-8")
            patt = re.compile('.*Version ([0-9]+)[.].*')
            mobj = patt.match(versioninfo)
            compiler = 'vc' + str(int(mobj.group(1))-6)
        elif ccommand.endswith('clang'):
            # clang prints version information to stderr
            versioninfo = run((ccommand, '-v'), stdout=PIPE, stderr=STDOUT).stdout.decode("utf-8")
            patt = re.compile('.*version ([0-9]+)[.]([0-9]+)\\.([0-9]+)')
            mobj = patt.match(versioninfo)
            compiler = 'clang' + mobj.group(1) + mobj.group(2)
        elif ccommand == 'icc':
            versioninfo = run((ccommand, '-dumpversion'), stdout=PIPE, stderr=STDOUT).stdout.decode("utf-8")
            patt = re.compile('([0-9]+)\\.([0-9]+)\\.([0-9]+)')
            mobj = patt.match(versioninfo)
            compiler = 'icc' + mobj.group(1)
        elif ccommand.endswith('cc'):
            versioninfo = run((ccommand, '-dumpversion'), stdout=PIPE, stderr=STDOUT).stdout.decode("utf-8")
            patt = re.compile('([0-9]+)\\.([0-9]+)\\.([0-9]+)')
            mobj = patt.match(versioninfo)
            # Some builds of gcc may only return the major version number
            if mobj == None:
                versioninfo = run((ccommand, '-dumpfullversion'), stdout=PIPE, stderr=STDOUT).stdout.decode("utf-8")
                mobj = patt.match(versioninfo)
            compiler = 'gcc' + mobj.group(1) + mobj.group(2) + mobj.group(3)
        else:
            compiler = 'unknown'

        return compiler

    @staticmethod
    def full_platform(architecture = None,
                      os           = None,
                      compiler     = None,
                      buildtype    = None ):
        """
        Return the full platform components
          (arch, os, compiler, buildtype)
        """
        if architecture == None: architecture = HSFPlatform.architecture()
        if compiler     == None: compiler = HSFPlatform.compiler()
        if os           == None: os = HSFPlatform.os()
        if buildtype    == None: buildtype = "all"

        return (architecture, os, compiler, buildtype)

    @staticmethod
    def full_platform_string(architecture = None,
                      os           = None,
                      compiler     = None,
                      buildtype    = None ):
        """
        Return the full platform string consisting of
          arch-os-compiler-buildtype
        """
        return "%s-%s-%s-%s" %HSFPlatform.full_platform(architecture, os, compiler, buildtype)

##########################
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--architecture", dest="architecture",
                        help="set architecture")
    parser.add_argument("-b", "--buildtype", dest="buildtype",
                        help="set buildtype")
    parser.add_argument("-c", "--compiler", dest="compiler",
                        help="set compiler")
    parser.add_argument("-s", "--system", dest="os",
                        help="set operating system")
    parser.add_argument("--get", dest="to_get", choices=("os", "architecture", "compiler"),
                        help='get one of %(choices)s. Otherwise print the entire platform')


    args = parser.parse_args()
    if args.to_get:
        print(getattr(HSFPlatform, args.to_get)())
    else:
        print(HSFPlatform.full_platform_string(architecture = args.architecture,
                                        compiler     = args.compiler,
                                        os           = args.os,
                                        buildtype    = args.buildtype
            )
        )
