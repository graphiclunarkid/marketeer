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
import mtgoxmonitor
from time import *

def checkmon(mon):
    mon.price.printstate()
    sleep(mon.updatePeriod + 1)
    mon.price.printstate()

def main():
    checkmon(bullionvaultmonitor.BullionVaultMonitor())
    checkmon(mtgoxmonitor.MtgoxMonitor())

if __name__ == "__main__":
    main()

