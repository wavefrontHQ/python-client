# coding: utf-8

"""
    Wavefront AWS Lambda Wrapper

    <p>This is a Wavefront python wrapper for AWS Lambda python function handler to send metrics directly to wavefront.</p>  # noqa: E501
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wavefront_lambda"
VERSION = "0.9.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pyformance >= 0.4", "requests >= 2.18.4"]

setup(
    name=NAME,
    version=VERSION,
    description="Wavefront Lambda Python Wrapper",
    author_email="",
    url="https://github.com/wavefrontHQ/python-client/tree/master/wavefront_lambda",
    keywords=["Wavefront Pyformance", "Wavefront"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["wavefront_lambda","*.tests"]),
    include_package_data=True,
    long_description="""\
    This is a Wavefront python wrapper for AWS Lambda python function handler to send metrics directly to wavefront.
    """
)
