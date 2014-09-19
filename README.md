MARKETEER v0.1.2
----------------
A trading-bot project written in python.

SUPPORTED MARKETS
-----------------
Monitoring only: Bullion Vault (http://www.bullionvault.com/)

BACKLOG
-------
[![Stories in Ready](https://badge.waffle.io/graphiclunarkid/marketeer.png?label=ready)](http://waffle.io/graphiclunarkid/marketeer)
[![Build Status](https://travis-ci.org/graphiclunarkid/marketeer.svg?branch=master)](https://travis-ci.org/graphiclunarkid/marketeer)

USAGE
-----
Run bullionvaultmonitor.py to see live data from the Bullion Vault London Gold
GBP market.

The script calls the Bullionvault public API twice, waiting 30s between each
call, and displays the current bid price, offer price, and spread each time.

It can optionally save the price results to an sqlite database.

```
usage: bullionvaultmonitor.py [-h] [-t] [-s SAVE] [-q] [-c CURRENCY]

Monitor BullionVault Exchange

optional arguments:
  -h, --help            show this help message and exit
  -t, --test            Get and display the current price twice (ignores -q)
  -s SAVE, --save SAVE  Save the price to <SAVE>
  -q, --quiet           Do not display the price
  -c CURRENCY, --currency CURRENCY
                        Currency in which to retrieve price
```

COPYRIGHT
---------
Copyright (C) 2013, 2014 Richard King and Adam Spragg

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.

The openAnything function was derived from the Dive Into Python book
(http://www.diveintopython.net/) which is copyright 2000, 2001, 2002, 2003,
2004 Mark Pilgrim (josh@servercobra.com). It is included here under the terms
of the Python license (http://www.diveintopython.net/appendix/license.html)

