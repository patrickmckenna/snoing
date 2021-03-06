#!/usr/bin/env python
#
# LibraryPackage
#
# Deals with packages that must be linked to, e.g. X11
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import systempackage

class LibraryPackage(systempackage.SystemPackage):
    """ For packages that are system wide libraries e.g. X11."""
    def __init__(self, name, system, help_text, library, headers = []):
        """ Initlialise with library and header (optional)."""
        super(LibraryPackage, self).__init__(name, system, help_text)
        self._library = library
        self._headers = headers
    def check_state(self):
        """ Need to test the library linking and inclusion of the header."""
        self._installed = self._system.test_library(self._library, self._headers)
