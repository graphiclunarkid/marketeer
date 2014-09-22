===============================
Marketeer
===============================

.. image:: https://badge.waffle.io/graphiclunarkid/marketeer.png?label=ready
    :target: http://waffle.io/graphiclunarkid/marketeer

.. image:: https://travis-ci.org/graphiclunarkid/marketeer.png?branch=master
    :target: https://travis-ci.org/graphiclunarkid/marketeer

.. image:: https://coveralls.io/repos/graphiclunarkid/marketeer/badge.png?branch=master
    :target: https://coveralls.io/r/graphiclunarkid/marketeer?branch=master

A trading-bot project written in python.

Features
--------
* Display live data from Bullion Vault (http://www.bullionvault.com/)
* Stores market data to an sqlite3 database
* Documentation: https://marketeer.readthedocs.org

::

    Usage: python3 marketeer.bullionvaultmonitor.py [-h] [-t] [-s SAVE] [-q] [-c CURRENCY]

    Monitor BullionVault Exchange

    optional arguments:
      -h, --help            show this help message and exit
      -t, --test            Get and display the current price twice (ignores -q)
      -s SAVE, --save SAVE  Save the price to <SAVE>
      -q, --quiet           Do not display the price
      -c CURRENCY, --currency CURRENCY
                            Currency in which to retrieve price

Copyright (C) 2013, 2014 Richard King and Adam Spragg.
Licensed under the GNU General Public License v3 (or later).
See the file LICENCE for details.
