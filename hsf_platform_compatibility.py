#!/usr/bin/env python

__author__ = "Benedikt Hegner (CERN)"
__copyright__ = "Copyright (C) 2015 CERN"
__license__ = "GPLv3"
__version__ = "0.1"

import os
import platform
import re
import sys
from optparse import OptionParser

os_compatibility = (("redhat6","slc6"),)

class HSFPlatformCompatibility(object):
    def __init__(self):
        pass
        self.failureReason = None

    def is_compatible(self, platform, other):
        components1 = self.get_components(platform)
        components2 = self.get_components(other)
        is_compatible = self.check_architecture(components1[0], components2[0])
        if is_compatible:
          is_compatible = self.check_os(components1[1], components2[1])
        if is_compatible:
          is_compatible = self.check_compiler(components1[2], components2[2])
        if is_compatible:
          is_compatible = self.check_buildtype(components1[3], components2[3])
        return is_compatible

    def check_architecture(self, arch1, arch2):
        if (arch1 == arch2):
          return True
        self.failureReason = "Architectures %s and %s are incompatible" %(arch1, arch2)
        return False

    def check_os(self, os1, os2):
        isCompatible = False
        if os1 == os2:
          return True
        for set in os_compatibility:
          if os1 in set:
            if os2 in set:
              isCompatible = True
        if not isCompatible:
           self.failureReason = "OS'es %s and %s are incompatible" %(os1, os2)
        return isCompatible

    def check_compiler(self, comp1, comp2):
        # assume that major/minor versions are compatible and patch versions do not matter
        # exceptions to be coded up explicitly
        if (comp1[:-1] == comp2[:-1]):
          return True
        self.failureReason = "Compilers %s and %s are incompatible" %(comp1, comp2)
        return False

    def check_buildtype(self, type1, type2):
        # assume general compatibility for now
        return True

    def get_components(self,platform):
        components = platform.split("-")
        if len(components) != 4:
          print "Given platform '%s' doesn't follow standard arch-OS-compiler-buildtype schema." %platform
          sys.exit(1)
        return components

##########################
if __name__ == "__main__":
    usage = "usage: %prog [options] platform1 platform2"
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print info messages")

    (options, args) = parser.parse_args()
    if len(args) != 2:
      parser.print_help()
      sys.exit(1)
    comp = HSFPlatformCompatibility()
    isCompatible = comp.is_compatible(args[0],args[1])

    if isCompatible:
      sys.exit(0)
    else:
      if options.verbose:
        print comp.failureReason
      sys.exit(1)
