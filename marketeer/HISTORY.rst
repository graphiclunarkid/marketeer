.. :changelog:

History
-------

0.1.2 (2014-09-20)
---------------------
This version restructures the project to use a simpler git-flow process
 - Everything lives on the master branch
 - Branches are created, merged and then deleted for bug fixes or new features
 - Tags are used for releases

This version also packages the project properly

Bug: rounding error fixed
Feature: MtGox code removed as exchange is now defunct
Feature: Prices can now be saved to an sqlite database
Feature: Added Travis CI
Test: refactored API tests to use local data files rather than live service


Version 0.1.1
-------------
Patch: fixed bug if 'spread' is called before 'bid' or 'ask'

Version 0.1
-----------
Initial public version of development code

