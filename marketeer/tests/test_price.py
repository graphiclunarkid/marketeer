#!/usr/bin/python3

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
import os
from time import time

from .. import price


class Test_Price(unittest.TestCase):

    def test_create(self):

        p = price.Price('dummy', 'dummy', 'GBP', 100, 150)

        self.assertEqual(p.bid, 100, 'Wrong bid')
        self.assertEqual(p.offer, 150, 'Wrong offer')
        self.assertEqual(p.spread, 50, 'Wrong spread')

        self.assertRaises(TypeError, price.Price, 'dummy', 'dummy', 'GBP', 0, 150)
        self.assertRaises(TypeError, price.Price, 'dummy', 'dummy', 'GBP', 150, 100)


    def test_store(self):
        # Supply integer timestamp, as it gets rounded in the database, and
        # we want to check for equality later
        p = price.Price('dummy', 'dummy', 'GBP', 100, 150, data={ 'name': 'value' }, timestamp=int(time()))

        s = price.Store('test_price.sqlite')
        s.save(p)

        # Load data we've just saved
        all = s.load('dummy', 'dummy', 'GBP')
        self.assertEqual(len(all), 1, 'Incorrect number of rows returned')

        p2 = all[0]
        self.assertEqual(p.exchange, p2.exchange)
        self.assertEqual(p.security, p2.security)
        self.assertEqual(p.currency, p2.currency)
        self.assertEqual(p.bid, p2.bid)
        self.assertEqual(p.offer, p2.offer)
        self.assertEqual(p.timestamp, p2.timestamp)

        s.close()

        # Close and re-open database to confirm data is still there
        s = price.Store('test_price.sqlite')

        all = s.load('dummy', 'dummy', 'GBP')
        self.assertEqual(len(all), 1, 'Incorrect number of rows returned')

        p2 = all[0]
        self.assertEqual(p.exchange, p2.exchange)
        self.assertEqual(p.security, p2.security)
        self.assertEqual(p.currency, p2.currency)
        self.assertEqual(p.bid, p2.bid)
        self.assertEqual(p.offer, p2.offer)
        self.assertEqual(p.timestamp, p2.timestamp)

        s.close()


    def tearDown(self):
        try:
            # TODO: Why does this fail?
            os.remove('test_price.sqlite')
        except:
            pass
        return
