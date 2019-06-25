# coding: utf-8

"""
    Version 3 of CANDY HOUSE’s Sesame API

    We use RESTful API to provide basic manipulation of the Sesame smart lock, including: * Get Sesame lock/unlock status * Get battery status * Lock and unlock Sesame * Sync Sesame status * Get results for lock, unlock, and sync commands   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: sesame@candyhouse.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Version 3 of CANDY HOUSE’s Sesame API",
    author_email="sesame@candyhouse.co",
    url="",
    keywords=["Swagger", "Version 3 of CANDY HOUSE’s Sesame API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    We use RESTful API to provide basic manipulation of the Sesame smart lock, including: * Get Sesame lock/unlock status * Get battery status * Lock and unlock Sesame * Sync Sesame status * Get results for lock, unlock, and sync commands   # noqa: E501
    """
)
