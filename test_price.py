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
import price

class Test_Price(unittest.TestCase):

    def test_create(self):

        p = price.Price('dummy', 'dummy', 'GBP', 100, 150)

        self.assertEqual(p.bid, 100, 'Wrong bid')
        self.assertEqual(p.offer, 150, 'Wrong offer')
        self.assertEqual(p.spread, 50, 'Wrong spread')

        self.assertRaises(TypeError, price.Price, 'dummy', 'dummy', 'GBP', 0, 150)
        self.assertRaises(TypeError, price.Price, 'dummy', 'dummy', 'GBP', 150, 100)


    def test_store(self):

        p = price.Price('dummy', 'dummy', 'GBP', 100, 150)
        s = price.Store('test-price.sqlite')

        s.save(p)
        self.assertEqual(s.load('dummy', 'dummy', 'GBP'), [p], 'Store save/load failed')

