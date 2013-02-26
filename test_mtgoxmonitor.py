# Copyright (C) 2013 - see the README file for a list of authors.
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
from time import sleep

class Test_MtgoxMonitor(unittest.TestCase):

    def setUp(self):

        self.url = 'mtgdata'
        self.request = ''
        self.updatePeriod = 1

    def test_monitorAttributes(self):

        monitor = mtgoxmonitor.MtgoxMonitor(url = self.url, request = self.request)
        self.assertIsNotNone(monitor.updatePeriod, 'Update period is not set')
        self.assertEqual(monitor.updatePeriod, 30, 'Default update period not set correctly')

        self.assertEqual(monitor.price.exchange, 'MtGox', 'Wrong exchange')
        self.assertEqual(monitor.price.security, 'BTC', 'Wrong security')

        self.assertIsNotNone(monitor.price.spread, 'Spread is not set')
        self.assertGreaterEqual(monitor.price.spread, 0, 'Spread is negative')
        self.assertIsNotNone(monitor.price.bid, 'Bid is not set')
        self.assertIsNotNone(monitor.price.offer, 'Offer is not set')
        self.assertIsNotNone(monitor.price.timestamp, 'Timestamp not set')

    def test_monitorRefresh(self):

        monitor = mtgoxmonitor.MtgoxMonitor(updatePeriod = self.updatePeriod, url = self.url, request = self.request)

        bid = monitor.price.bid
        offer = monitor.price.offer
        spread = monitor.price.spread
        self.assertEqual(bid, 19.5255, 'Bid price was not imported correctly')
        self.assertEqual(offer, 19.54141, 'Offer price was not imported correctly')
        self.assertEqual(spread, 0.01591, 'Spread was not calculated correctly')

