#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'tox',
]

setup(
    name='marketeer',
    version='0.1.2',
    description='A trading bot',
    long_description=readme + '\n\n' + history,
    author='Richard King',
    author_email='mail@richardskingdom.net',
    url='https://github.com/graphiclunarkid/marketeer',
    packages=[
        'marketeer',
    ],
    package_dir={'marketeer':
                 'marketeer'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords='marketeer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    cmdclass = {'test': Tox},
)
