.. :changelog:

=======
History
=======

Version 0.1.4 (2016-03-08)
--------------------------
Blow the cobwebs off the project after a year of inactivity

| Doc: Add python3 environment prerequisites to contributing documentation
| Other: Remove python3.3 support since Debian stable no longer ships with it
| Other: Change my email address
| Other: Update copyright years

Version 0.1.3 (2014-11-23)
--------------------------
Tidy-up release, mostly to do with packaging

| Other: Convert branch structure to git-flow
| Other: Port project to Python3
| Bug: Import paths don't always resolve correctly
| Test: Display test-coverage badge in readme
| Test: PEP8 compliance
| Test: Add test coverage to testing regime
| Test: Add TravisCI integration back into project
| Test: Express install and test dependencies in setup.py
| Test: Integrate tox testing with setup.py
| Test: Implement continuous integration
| Packaging: Move git repository down one directory
| Packaging: Delete "old" directory from project
| Packaging: Check how version number gets updated
| Packaging: Figure out fury.io
| Packaging: Switch from distutils to setuptools
| Packaging: Add long_description to setup.py
| Packaging: Package project for redistribution
| Packaging: Update version number in a single location
| Doc: Basic documentation
| Doc: Update contributing instructions

Version 0.1.2 (2014-09-20)
--------------------------
This version restructures the project to use a simpler git-flow process

- Everything lives on the master branch
- Branches are created, merged and then deleted for bug fixes or new features
- Tags are used for releases

This version also packages the project properly

| Bug: rounding error fixed
| Feature: MtGox code removed as exchange is now defunct
| Feature: Prices can now be saved to an sqlite database
| Feature: Added Travis CI
| Test: refactored API tests to use local data files rather than live service

Version 0.1.1 (2013-02-18)
--------------------------
Bug fix release

| Bug: fixed bug if 'spread' is called before 'bid' or 'ask'

Version 0.1.0 (2013-02-12)
--------------------------
| Initial public version of development code

