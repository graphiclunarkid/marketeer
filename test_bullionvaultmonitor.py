#!/usr/bin/python

# Copyright 2013 Richard King (mail@richardskingdom.net)
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
import bullionvaultmonitor
from time import sleep

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.updatePeriod = 10
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )

    def test_monitorAttributes(self):

        validMonitors = set()

        for i in self.validCurrencies:

            for j in self.validMarkets:

                validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

        monitor = validMonitors.pop()

        while (len(validMonitors) > 0):

            self.assertIsNotNone(monitor.spread, 'Spread wasn\'t calculated')
            self.assertIsNotNone(monitor.bid, 'Bid price is not set')
            self.assertIsNotNone(monitor.offer, 'Offer price is not set')
            self.assertGreaterEqual(monitor.spread, 0, 'Spread is negative')

            monitor = validMonitors.pop()


    def test_monitorRefresh(self):

        monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,'GBP','AUXLN')
        monitor.url = 'bvdata.xml'

        bid = monitor.bid
        offer = monitor.offer
        spread = monitor.spread
        self.assertEqual(bid, 33910, 'Bid price was not imported correctly')
        self.assertEqual(offer, 33950, 'Offer price was not imported correctly')
        self.assertEqual(spread, 40, 'Spread was not calculated imported correctly')

        sleep(self.updatePeriod / 2)
        monitor.url = 'bvdata2.xml'
        bid2 = monitor.bid
        offer2 = monitor.offer
        spread2 = monitor.spread
        self.assertEqual(bid2, bid, 'Bid price changed before update was due')
        self.assertEqual(offer2, offer, 'Offer price changed before update was due')
        self.assertEqual(spread2, spread, 'Spread changed before update was due')

        sleep(self.updatePeriod)
        bid2 = monitor.bid
        offer2 = monitor.offer
        spread2 = monitor.spread
        self.assertEqual(bid2, 33920, 'Bid price not updated after update was due')
        self.assertEqual(offer2, offer, 'Offer price changed but wasn\'t supposed to')
        self.assertEqual(spread2, 30, 'Spread not updated after update was due')


suite = unittest.TestLoader().loadTestsFromTestCase(Test_BullionVaultMonitor)
unittest.TextTestRunner(verbosity=2).run(suite)
