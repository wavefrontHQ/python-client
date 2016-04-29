# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "wavefront_client"
VERSION = "1.0.0"



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
    author_email="",
    url="",
    keywords=["Swagger", "Wavefront Public API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;p&gt;The Wavefront Public APIs are published for customers to use when interacting with Wavefront servers.They can be used to automate commonly executed operations (such as tagging sourcesautomatically whenthey come up).&lt;/p&gt;&lt;p&gt;Please note that you&#39;ll need to supply the X-AUTH-TOKEN header with a valid tokenshould you attempt to make the API calls directly outside of this console.&lt;/p&gt;
    """
)


