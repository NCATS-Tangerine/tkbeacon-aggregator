# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.3
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "kba"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.15",
    "six >= 1.10",
    "certifi",
    "python-dateutil",
    "click",
    "progress",
]

setup(
    name=NAME,
    version=VERSION,
    description="Translator Knowledge Beacon Aggregator API",
    author_email="richard@starinformatics.com",
    url="",
    keywords=["Swagger", "Translator Knowledge Beacon Aggregator API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501
    """,
    scripts=['bin/kba_cli.py'],
    entry_points='''
        [console_scripts]
        kba=kba_cli:cli
    ''',
)
