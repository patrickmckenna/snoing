#!/usr/bin/env python
#
# RatRelasePost3, RatReleasePre4, RatReleasePre3, RatReleasePre2
#
# Base classes for the various rat releases, oldest at the bottom
# RAT-2 is first curl and bzip one!
# RAT-3 adds avalanche, xerces and zeromq extra
# RAT-4 slightly changes the geant dependency
#
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import os
import rat

class RatReleasePost3(rat.RatRelease):
    """ Base package installer for rat release 3."""
    def __init__(self, name, system, root_dep, scons_dep, geant_dep, clhep_dep, curl_dep, \
                     bzip_dep, avalanche_dep, zeromq_dep, xercesc_dep, tar_name):
        """ Initlaise, take extra dependencies."""
        super(RatReleasePost3, self).__init__(name, system, root_dep, scons_dep, tar_name)
        self._geant_dep = geant_dep
        self._clhep_dep = clhep_dep
        self._curl_dep = curl_dep
        self._bzip_dep = bzip_dep
        self._avalanche_dep = avalanche_dep
        self._zeromq_dep = zeromq_dep
        self._xercesc_dep = xercesc_dep
    def _get_dependencies(self):
        """ Return the extra dependencies."""
        return [self._geant_dep, self._clhep_dep, self._curl_dep, self._bzip_dep, \
                    self._avalanche_dep, self._zeromq_dep, self._xercesc_dep]
    def _write_env_file(self):
        """ Diff geant env file and no need to patch rat."""
        self._env_file.add_source(self._dependency_paths[self._geant_dep], "bin/geant4")
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._clhep_dep], 
                                                        "lib"))
        self._env_file.add_environment("AVALANCHEROOT", self._dependency_paths[self._avalanche_dep])
        if self._dependency_paths[self._zeromq_dep] is not None: # Conditional Package
            self._env_file.add_environment("ZEROMQROOT", self._dependency_paths[self._zeromq_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._zeromq_dep], 
                                                            "lib"))
        if self._dependency_paths[self._xercesc_dep] is not None: # Conditional Package
            self._env_file.add_environment("XERCESCROOT", self._dependency_paths[self._xercesc_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._xercesc_dep], 
                                                          "lib"))
        self._env_file.append_path(os.path.join(self._dependency_paths[self._clhep_dep], "bin"))
        self._env_file.append_path(os.path.join(self._dependency_paths[self._geant_dep], "bin"))
        self._env_file.append_libraryPath(os.path.join(self._dependency_paths[self._clhep_dep], 
                                                       "lib"))
        self._env_file.append_libraryPath(os.path.join(self._dependency_paths[self._avalanche_dep], 
                                                       "lib/cpp"))
        if self._dependency_paths[self._curl_dep] is not None: # Conditional Package
            self._env_file.append_path(os.path.join(self._dependency_paths[self._curl_dep], "bin"))
        if self._dependency_paths[self._bzip_dep] is not None: # Conditional Package
            self._env_file.add_environment("BZIPROOT", self._dependency_paths[self._bzip_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._bzip_dep], 
                                                          "lib"))

class RatReleasePre4(rat.RatRelease):
    """ Base package installer for rat release 3."""
    def __init__(self, name, system, root_dep, scons_dep, geant_dep, clhep_dep, curl_dep, \
                     bzip_dep, avalanche_dep, zeromq_dep, xercesc_dep, tar_name):
        """ Initlaise, take extra dependencies."""
        super(RatReleasePre4, self).__init__(name, system, root_dep, scons_dep, tar_name)
        self._geant_dep = geant_dep
        self._clhep_dep = clhep_dep
        self._curl_dep = curl_dep
        self._bzip_dep = bzip_dep
        self._avalanche_dep = avalanche_dep
        self._zeromq_dep = zeromq_dep
        self._xercesc_dep = xercesc_dep
    def _get_dependencies(self):
        """ Return the extra dependencies."""
        return [self._geant_dep, self._clhep_dep, self._curl_dep, self._bzip_dep, \
                    self._avalanche_dep, self._zeromq_dep, self._xercesc_dep]
    def _write_env_file(self):
        """ Add the extra info to the env file."""
        self._env_file.add_source(self._dependency_paths[self._geant_dep], "env")
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._clhep_dep], 
                                                        "lib"))
        self._env_file.add_environment("AVALANCHEROOT", self._dependency_paths[self._avalanche_dep])
        if self._dependency_paths[self._zeromq_dep] is not None: # Conditional Package
            self._env_file.add_environment("ZEROMQROOT", self._dependency_paths[self._zeromq_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._zeromq_dep],
                                                            "lib"))
        if self._dependency_paths[self._xercesc_dep] is not None: # Conditional Package
            self._env_file.add_environment("XERCESCROOT", self._dependency_paths[self._xercesc_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._xercesc_dep],
                                                            "lib"))
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._avalanche_dep], 
                                                        "lib/cpp"))
        if self._dependency_paths[self._curl_dep] is not None: # Conditional Package
            self._env_file.append_path(os.path.join(self._dependency_paths[self._curl_dep], "bin"))
        if self._dependency_paths[self._bzip_dep] is not None: # Conditional Package
            self._env_file.add_environment("BZIPROOT", self._dependency_paths[self._bzip_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._bzip_dep], 
                                                            "lib"))
            # Must patch the rat config/EXTERNALS file if BZIPROOT is present
            externals_file = open(os.path.join(self.GetInstallPath(), "config/EXTERNAL.scons"), "r")
            text = externals_file.read()
            externals_file.close()
            externals_file = open(os.path.join(self.GetInstallPath(), "config/EXTERNAL.scons"), "w")
            text = text.replace("ext_deps['bz2']['path'] = None", "ext_deps['bz2']['path'] = os.environ['BZIPROOT']")
            externals_file.write(text)
            externals_file.close()

class RatReleasePre3(rat.RatRelease):
    """ Base package installer for rat release 2."""
    def __init__(self, name, system, root_dep, scons_dep, geant_dep, clhep_dep, curl_dep, bzip_dep, tar_name):
        """ Initlaise, take extra dependencies."""
        super(RatReleasePre3, self).__init__(name, system, root_dep, scons_dep, tar_name)
        self._geant_dep = geant_dep
        self._clhep_dep = clhep_dep
        self._curl_dep = curl_dep
        self._bzip_dep = bzip_dep
    def _get_dependencies(self):
        """ Return the extra dependencies."""
        return [self._geant_dep, self._clhep_dep, self._curl_dep, self._bzip_dep]
    def _write_env_file(self):
        """ Add the extra info to the env file."""
        self._env_file.add_source(self._dependency_paths[self._geant_dep], "env")
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._clhep_dep], 
                                                        "lib"))
        if self._dependency_paths[self._curl_dep] is not None: # Conditional Package
            self._env_file.append_path(os.path.join(self._dependency_paths[self._curl_dep], "bin"))
        if self._dependency_paths[self._bzip_dep] is not None: # Conditional Package
            self._env_file.add_environment("BZIPROOT", self._dependency_paths[self._bzip_dep])
            self._env_file.append_library_path(os.path.join(self._dependency_paths[self._bzip_dep], 
                                                            "lib"))
            # Must patch the rat config/EXTERNALS file if BZIPROOT
            externals_file = open(os.path.join(self.GetInstallPath(), "config/EXTERNAL.scons"), "r")
            text = externals_file.read()
            exterbalsFile.close()
            externals_file = open(os.path.join(self.GetInstallPath(), "config/EXTERNAL.scons"), "w")
            text = text.replace("ext_deps['bz2']['path'] = None", "ext_deps['bz2']['path'] = os.environ['BZIPROOT']")
            externals_file.write(text)
            externals_file.close()

class RatReleasePre2(rat.RatRelease):
    """ Base package installer for rat releases 0, 1."""
    def __init__(self, name, system, root_dep, scons_dep, geant_dep, clhep_dep, tar_name):
        """ Initlaise, take extra dependencies."""
        super(RatReleasePre2, self).__init__(name, system, root_dep, scons_dep, tar_name)
        self._geant_dep = geant_dep
        self._clhep_dep = clhep_dep
    def _get_dependencies(self):
        """ Return the extra dependencies."""
        return [self._geant_dep, self._clhep_dep]
    def _write_env_file(self):
        """ Add the extra info to the env file."""
        self._env_file.add_source(self._dependency_paths[self._geant_dep], "env")
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._clhep_dep], 
                                                        "lib"))
