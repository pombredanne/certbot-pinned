#
# This software is placed in the Public Domain
# Written by Philippe Ombredanne for nexB Inc.
#

from setuptools import setup


long_description = """certbot-pinned is a "metapackage" (that contains no code but only dependencies)
that provides a version of cerbot with all its pinned dependencies as they would be installed by certbot-auto"""

setup(
    name = 'certbot-pinned',
    version = '0.17.0',
    author = "Philippe Ombredanne for nexB Inc.",
    author_email = "pom@nexb.com",
    description = "certbot metapackage with pinned dependency versions",
    long_description = long_description,
    license = "Public Domain",
    keywords = "cerbot pip dependencies",
    url='https://github.com/pombredanne/certbot-pinned',
    include_package_data = True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: System Administrators',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    # pinned deps for 0.17.0
    # from https://github.com/certbot/certbot/blob/912d235466669d516427b5db9997bb92705020f1/certbot-auto#L708
    install_requires = [
        'argparse==1.4.0',
        'pycparser==2.14',
        'asn1crypto==0.22.0',
        'cffi==1.10.0',
        'ConfigArgParse==0.10.0',
        'configobj==5.0.6',
        'cryptography==2.0.2',
        'enum34==1.1.2',
        'funcsigs==1.0.2',
        'idna==2.5',
        'ipaddress==1.0.16',
        'linecache2==1.0.0',
        'ordereddict==1.1',
        'packaging==16.8',
        'parsedatetime==2.1',
        'pbr==1.8.1',
        'pyOpenSSL==16.2.0',
        'pyparsing==2.1.8',
        'pyRFC3339==1.0',
        'python-augeas==0.5.0',
        'pytz==2015.7',
        'requests==2.20.0',
        'six==1.10.0',
        'traceback2==1.4.0',
        'unittest2==1.1.0',
        'zope.component==4.2.2',
        'zope.event==4.1.0',
        'zope.interface==4.1.3',
        'mock==2.0.0',
        'letsencrypt==0.7.0',
        'certbot==0.17.0',
        'acme==0.17.0',
        'certbot-apache==0.17.0',
        'certbot-nginx==0.17.0',
    ]
)
