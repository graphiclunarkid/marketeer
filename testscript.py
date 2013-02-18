#!/usr/bin/python

# Copyright 2013 Richard King
#
# This file is part of Marketeer.
#
# Marketeer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Marketeer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Marketeer.  If not, see <http://www.gnu.org/licenses/>.

import bullionvaultmonitor
from time import *

def printstuff(mon):
    print "Exchange:", mon.price.exchange
    print "Security:", mon.price.security
    print "Bid:", mon.price.bid, mon.price.currency
    print "Offer:", mon.price.offer, mon.price.currency
    print "Spread:", mon.price.spread, mon.price.currency
    print "Timestamp:", mon.price.timestamp

def main():
    mon = bullionvaultmonitor.BullionVaultMonitor()
    printstuff(mon)
    sleep(mon.updatePeriod + 1)
    printstuff(mon)

if __name__ == "__main__":
    main()
