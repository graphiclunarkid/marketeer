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

import unittest
import mtgoxmonitor

class Test_MtgoxMonitor(unittest.TestCase):

    def test_monitorAttributes(self):

        monitor = mtgoxmonitor.MtgoxMonitor()
        self.assertIsNotNone(monitor.updatePeriod, 'Update period is not set')
        self.assertEqual(monitor.updatePeriod, 30, 'Default update period not set correctly')

        self.assertIsNotNone(monitor.spread, 'Spread is not set')
        self.assertGreaterEqual(monitor.spread, 0, 'Spread is negative')
        self.assertIsNotNone(monitor.bid, 'Bid is not set')
        self.assertIsNotNone(monitor.offer, 'Offer is not set')

