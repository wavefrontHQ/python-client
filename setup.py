# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "wavefront-api-client"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

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
    &lt;p&gt;Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.&lt;/p&gt;&lt;p&gt;When you make API calls outside the Wavefront UI you must add the header \&quot;Authorization: Bearer &amp;lt;&amp;lt;API-TOKEN&amp;gt;&amp;gt;\&quot; to your HTTP requests.&lt;/p&gt;&lt;p&gt;For legacy versions of the Wavefront API, see the &lt;a href=\&quot;/api-docs/ui/deprecated\&quot;&gt;legacy API documentation&lt;/a&gt;.&lt;/p&gt;
    """
)


