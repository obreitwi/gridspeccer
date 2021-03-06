#!/usr/bin/env python

from setuptools import setup, find_packages

version = "0.1.0"

setup(name='Gridspeccer',
      version=version,
      description='Helper scripts to organize multi-figure plots.',
      author='Oliver Breitwieser',
      author_email='oliver.breitwieser@kip.uni-heidelberg.de',
      url='https://github.com/obreitwi/gridspeccer',
      packages=find_packages(include=['gridspeccer', 'gridspeccer.*']),
      entry_points={
          "console_scripts": [
              "gridspeccer = gridspeccer.cli:plot"
          ]},
      package_data={
          "gridspeccer": ["defaults/matplotlibrc", "defaults/tex_matplotlibrc"],
      },
      include_package_data=True,
      license="GNUv3",
      zip_safe=True,
      install_requires=["matplotlib", "scikit-image"],
      )
