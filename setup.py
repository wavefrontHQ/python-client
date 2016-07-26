# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "wavefront_client"
VERSION = "1.0.2"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Wavefront Public API",
    author="Wavefront",
    author_email="support@wavefront.com",
    url="https://github.com/wavefrontHQ/python-client",
    keywords=["Wavefront", "Wavefront Public API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
   license="Apache License",
    long_description="""\
    The Wavefront Public APIs are published for customers to use when interacting with Wavefront servers.  They can be used to automate commonly executed operations such as tagging sources automatically. Please note that you will need to supply the X-AUTH-TOKEN header with a valid token.;
    """
)
