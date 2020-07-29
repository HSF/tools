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
from argparse import ArgumentParser

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
        self.failureReason = f"Architectures {arch1} and {arch2} are incompatible"
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
           self.failureReason = f"OS'es {os1} and {os2} are incompatible"
        return isCompatible

    def check_compiler(self, comp1, comp2):
        # assume that major/minor versions are compatible and patch versions do not matter
        # exceptions to be coded up explicitly
        if (comp1[:-1] == comp2[:-1]):
          return True
        self.failureReason = f"Compilers {comp1} and {comp2} are incompatible"
        return False

    def check_buildtype(self, type1, type2):
        # assume general compatibility for now
        return True

    def get_components(self,platform):
        components = platform.split("-")
        if len(components) != 4:
          print(f"Given platform {platform} doesn't follow standard arch-OS-compiler-buildtype schema.")
          sys.exit(1)
        return components

##########################
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print info messages")
    parser.add_argument("platform1", help="First platform for comparison")
    parser.add_argument("platform2", help="Second platform for comparison")

    args = parser.parse_args()
    comp = HSFPlatformCompatibility()
    isCompatible = comp.is_compatible(args.platform1, args.platform2)

    if isCompatible:
      sys.exit(0)
    else:
      if args.verbose:
        print(comp.failureReason)
      sys.exit(1)
