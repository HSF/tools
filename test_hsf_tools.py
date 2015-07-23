#!/usr/bin/env python

import unittest
from hsf_platform_compatibility import HSFPlatformCompatibility

compatiblePlatforms = (
  ("x86_64-slc6-gcc481-opt","x86_64-slc6-gcc483-dbg"),
  ("x86_64-slc6-gcc481-opt","x86_64-slc6-gcc483-opt"),
  ("x86_64-redhat6-gcc481-opt","x86_64-slc6-gcc481-opt")
)

incompatiblePlatforms = (
  ("x86_64-slc5-gcc481-opt","x86_64-slc6-gcc481-opt"),
  ("x86_64-slc6-gcc481-opt","x86_64-slc6-gcc491-opt")
)


class TestPlatformCompatibility(unittest.TestCase):
  def test_compatibility(self):
      comp = HSFPlatformCompatibility()
      for first, second in compatiblePlatforms:
        self.assertTrue(comp.is_compatible(first, second))
  def test_incompatibility(self):
      comp = HSFPlatformCompatibility()
      for first, second in incompatiblePlatforms:
        self.assertFalse(comp.is_compatible(first, second))

def main():
  unittest.main()


##########################
if __name__ == "__main__":
    main()
