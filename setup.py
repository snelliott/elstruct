""" install elstruct
"""
from distutils.core import setup


setup(name="elstruct",
      version="0.2.13",
      packages=["elstruct",
                "elstruct.writer",
                "elstruct.reader",
                "elstruct.writer._psi4",
                "elstruct.reader._psi4",
                "elstruct.writer._gaussian09",
                "elstruct.reader._gaussian09",
                "elstruct.writer._molpro",
                "elstruct.reader._molpro"],
      package_dir={'elstruct': 'elstruct'},
      package_data={'elstruct': [
          'writer/_psi4/templates/*.mako',
          'writer/_gaussian09/templates/*.mako',
          'writer/_molpro/templates/*.mako',
      ]})
