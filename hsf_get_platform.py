#!/usr/bin/env python
###############################################################################
# (c) Copyright 2015 CERN                                                     #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENCE".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

__author__ = "Benedikt Hegner (CERN)"
__copyright__ = "Copyright (C) 2015 CERN"
__license__ = "GPLv3"
__version__ = "0.1"

import os
import platform
import re
import sys

from optparse import OptionParser

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
            pf = platform.linux_distribution(full_distribution_name=0)[0]
            version = platform.linux_distribution(full_distribution_name=0)[1].split(".")[0]
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
            raise "System %s not supported" %system

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
            versioninfo = os.popen(ccommand).read()
            patt = re.compile('.*Version ([0-9]+)[.].*')
            mobj = patt.match(versioninfo)
            compiler = 'vc' + str(int(mobj.group(1))-6)
        elif ccommand.endswith('clang'):
            versioninfo = os.popen4(ccommand + ' -v')[1].read()
            patt = re.compile('.*version ([0-9]+)[.]([0-9]+)')
            mobj = patt.match(versioninfo)
            compiler = 'clang' + mobj.group(1) + mobj.group(2)
        elif ccommand == 'icc':
            versioninfo = os.popen(ccommand + ' -dumpversion').read()
            patt = re.compile('([0-9]+)\\.([0-9]+)')
            mobj = patt.match(versioninfo)
            compiler = 'icc' + mobj.group(1)
        elif ccommand.endswith('cc'):
            versioninfo = os.popen(ccommand + ' -dumpversion').read()
            patt = re.compile('([0-9]+)\\.([0-9]+)')
            mobj = patt.match(versioninfo)
            compiler = 'gcc' + mobj.group(1) + mobj.group(2)
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
    parser = OptionParser()
    parser.add_option("-a", "--architecture", dest="architecture",
                  help="set architecture", default=None)
    parser.add_option("-b", "--buildtype", dest="buildtype",
                  help="set buildtype", default = None)
    parser.add_option("-c", "--compiler", dest="compiler",
                  help="set compiler", default = None)
    parser.add_option("-s", "--system", dest="os",
                  help="set operating system", default = None)
    parser.add_option("--get", dest="to_get",
                  help="get either of 'os,architecture,compiler'. Otherwise dump the entire platform", default = None)


    (options, args) = parser.parse_args()
    if len(args) != 0:
        print "ERROR: This tool doesn't take any arguments"
        sys.exit(1)
    if options.to_get in ['os','architecture','compiler']:
        print getattr(HSFPlatform, options.to_get)()
    elif options.to_get != None:
        print 'ERROR: Unkown option to get: %s' %options.to_get
        sys.exit(1)
    else:
        print HSFPlatform.full_platform_string(architecture = options.architecture,
                                        compiler     = options.compiler,
                                        os           = options.os,
                                        buildtype    = options.buildtype
        )
