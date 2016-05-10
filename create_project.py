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

import datetime, os, shutil, sys
from os.path import join, split, dirname, abspath

class ProjectCreator(object):

    def __init__(self,projectname, author, target_dir,license,
                 verbose=True, subpackage_name="package"):
        self.location = dirname(abspath(__file__))
        self.template_dir = join(self.location,"project_template")
        self.license_dir  = join(self.location,"project_licenses")
        self.licenses = [f.rstrip(".txt") for f in
                         os.listdir(self.license_dir)
                         if f.endswith(".txt")]
        self.year = datetime.datetime.now().year
        self.name = projectname
        self.target_dir = target_dir
        self.author = author
        self.verbose = verbose
        self.subpackage_name = subpackage_name
        self.license = license
        if self.license not in self.licenses:
            self.report("ERROR: license %s unknown" %license)
            self.print_licenses()
            sys.exit(1)
        if os.path.exists(self.target_dir):
            self.report("ERROR: %s already exists." %self.target_dir)
            sys.exit(1)

    def print_licenses(self):
        """Print available licenses"""
        self.report("The following licenses are available:")
        for license in self.licenses:
            self.report(" "*3+license)

    def create(self):
        """ Create the new project"""
        shutil.copytree(self.template_dir,self.target_dir)
        self.add_license()
        self.replace_templates()

    def add_license(self):
        """ Add license file and replace year and author"""
        shutil.copy(join(self.license_dir,self.license+".txt"),
                    join(self.target_dir,"LICENSE"))
        shutil.copy(join(self.license_dir,self.license+".notice"),
                    join(self.target_dir,"NOTICE"))

        replacements = {"YEAR": str(self.year),
                        "AUTHOR" : self.author}

        self.replace_in_file(join(self.target_dir,"NOTICE"), replacements)

    def report(self, message):
        """print messages to screen depending on verbosity level"""
        if self.verbose == True:
            print message

    @staticmethod
    def replace_in_file(filename, replacements):
        """replace file contents according to given dictionary"""
        with open(filename,'r') as f:
            newlines = []
            for line in f.readlines():
                for key, value in replacements.iteritems():
                    line = line.replace(key, value)
                newlines.append(line.replace(key, value))
        with open(filename, 'w') as f:
            for line in newlines:
                f.write(line)

    def replace_templates(self):
        """Replace the strings in the project template by the user defined values"""
        # add C++ style comment to the copyright notice
        copyrightnotice = ""
        for line in open(join(self.target_dir,"NOTICE")).readlines():
            copyrightnotice += "// %s\n"%line

        replacements = {"COPYRIGHTNOTICE" : copyrightnotice,
                        "PROJECTTEMPLATE"     : self.name,
                        "AUTHOR"          : self.author,
                        "HSFSUBPACKAGE"   : self.subpackage_name
        }
        for subdir, dirs, files in os.walk(self.target_dir):
            for file in files:
                self.replace_in_file(join(subdir, file),replacements)
        os.rename(join(self.target_dir,"cmake/PROJECTTEMPLATECPack.cmake"),join(self.target_dir,"cmake/%sCPack.cmake" %self.name))
        os.rename(join(self.target_dir,"cmake/PROJECTTEMPLATEConfig.cmake.in"),join(self.target_dir,"cmake/%sConfig.cmake.in" %self.name))
        os.rename(join(self.target_dir,"cmake/PROJECTTEMPLATECreateConfig.cmake"),join(self.target_dir,"cmake/%sCreateConfig.cmake" %self.name))
        os.rename(join(self.target_dir,"cmake/PROJECTTEMPLATEDoxygen.cmake"),join(self.target_dir,"cmake/%sDoxygen.cmake" %self.name))
        os.rename(join(self.target_dir,"PROJECTTEMPLATEVersion.h"),join(self.target_dir,"%sVersion.h" %self.name))
        os.rename(join(self.target_dir,"package/include/example"),join(self.target_dir,"package/include/%s" %self.name))
        os.rename(join(self.target_dir,"package"),join(self.target_dir,"%s" %self.subpackage_name))
    def print_summary(self):
        """Print summary and help message"""
        summary  = "Finished creating project '%s'\n" %self.name
        summary += "  directory: %s\n" % self.target_dir
        summary += "  author   : %s\n" % self.author
        summary += "  license  : %s\n" % self.license
        summary += "  package  : %s\n" %self.subpackage_name

        howto  = "To build and install it, please do:\n"
        howto += "  cd %s\n  mkdir build\n  cd build\n" %self.target_dir
        howto += "  cmake -DCMAKE_INSTALL_PREFIX=../install ../\n"
        howto += "  make\n  make install\n"
        howto += "To build the doxygen documentation:\n"
        howto += "  make doc\n"
        howto += "To run the unit tests:\n"
        howto += "  make test\n"
        howto += "To trigger the package creation with CPack:\n"
        howto += "  make package\n"
        howto += "\nPlease do not forget to add a project description to README.md !"

        self.report(summary)
        self.report(howto)


##########################
if __name__ == "__main__":

    from optparse import OptionParser

    usage = "usage: %prog [options] <project name> <author> <target dir> <license>"
    parser = OptionParser(usage)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="Don't write a report to screen")
    parser.add_option("-p", "--package",
                      action="store", dest="subpackage_name", default="package",
                      help="Name of the created example-subpackage")

    (options, args) = parser.parse_args()
    if len(args) != 4:
        parser.error("Incorrect number of arguments.")

    creator = ProjectCreator(*args,verbose=options.verbose,subpackage_name=options.subpackage_name)
    creator.create()
    creator.print_summary()
