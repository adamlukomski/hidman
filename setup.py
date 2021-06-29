from setuptools import setup
import setuptools

import hidman

setup(name='hidman',
      version=hidman.__version__,
      description=hidman.__description__,
      url='http://github.com/s4hri/hidman',
      author=hidman.__authors__,
      author_email=hidman.__emails__,
      license=hidman.__license__,
      install_requires=hidman.__requirements__,
      packages=setuptools.find_packages(),
      zip_safe=False)
