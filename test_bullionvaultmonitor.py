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
import bullionvaultmonitor
from time import sleep

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.url = 'bvdata.xml'
        self.updatePeriod = 10
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )

    def test_monitorAttributes(self):

        validMonitors = set()

        for i in self.validCurrencies:

            for j in self.validMarkets:

                validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,url = self.url,currency=i,market=j))

        monitor = validMonitors.pop()

        while (len(validMonitors) > 0):

            self.assertEqual(monitor.price.exchange, 'BullionVault', 'Wrong exchange')
            self.assertEqual(monitor.price.security, 'XAU', 'Wrong security')
            self.assertIsNotNone(monitor.price.spread, 'Spread wasn\'t calculated')
            self.assertGreaterEqual(monitor.price.spread, 0, 'Spread is negative')
            self.assertIsNotNone(monitor.price.bid, 'Bid price is not set')
            self.assertIsNotNone(monitor.price.offer, 'Offer price is not set')
            self.assertIsNotNone(monitor.price.timestamp, 'Timestamp not set')
            monitor = validMonitors.pop()


    def test_monitorRefresh(self):

        monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,url = self.url,currency='GBP',market='AUXLN')

        bid = monitor.price.bid
        offer = monitor.price.offer
        spread = monitor.price.spread
        self.assertEqual(bid, 33910, 'Bid price was not imported correctly')
        self.assertEqual(offer, 33950, 'Offer price was not imported correctly')
        self.assertEqual(spread, 40, 'Spread was not calculated imported correctly')

        sleep(self.updatePeriod / 2)
        monitor.url = 'bvdata2.xml'
        bid2 = monitor.price.bid
        offer2 = monitor.price.offer
        spread2 = monitor.price.spread
        self.assertEqual(bid2, bid, 'Bid price changed before update was due')
        self.assertEqual(offer2, offer, 'Offer price changed before update was due')
        self.assertEqual(spread2, spread, 'Spread changed before update was due')

        sleep(self.updatePeriod)
        bid2 = monitor.price.bid
        offer2 = monitor.price.offer
        spread2 = monitor.price.spread
        self.assertEqual(bid2, 33920, 'Bid price not updated after update was due')
        self.assertEqual(offer2, offer, 'Offer price changed but wasn\'t supposed to')
        self.assertEqual(spread2, 30, 'Spread not updated after update was due')


