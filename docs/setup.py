
import pathlib

from setuptools import setup

from pyutmodel import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
LICENSE = (HERE / 'LICENSE').read_text()

setup(
    name="pyutmodel",
    version=__version__,
    author='Humberto A. Sanchez II',
    author_email='Humberto.A.Sanchez.II@gmail.com',
    maintainer='Humberto A. Sanchez II',
    maintainer_email='humberto.a.sanchez.ii@gmail.com',
    description='External Pyut Data Model',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasii2011/pyutmodel",
    packages=[
        'pyutmodel',
    ],
    package_data={
        'pyutmodel': ['py.typed'],
    },
    install_requires=['codeallybasic==0.5.2', 'Deprecated==1.2.14'],
)
