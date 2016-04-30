#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

"""
test_price
----------------------------------

Tests for `price` module.
"""

import pytest
from pytest import raises

import os
from time import time

from marketeer import price


@pytest.fixture(scope="function")
def fixture(request):

    def teardown():

        try:
            os.remove('test_price.sqlite')
        except:
            pass
        return

    request.addfinalizer(teardown)


def test_create():

    p = price.Price('dummy', 'dummy', 'GBP', 100, 150)

    assert p.bid == 100, 'Wrong bid'
    assert p.offer == 150, 'Wrong offer'
    assert p.spread == 50, 'Wrong spread'

    # Neither bid nor ask can be 0
    with raises(TypeError):
        price.Price('dummy', 'dummy', 'GBP', 0, 150)

    # Bid must be less than ask
    with raises(TypeError):
        price.Price('dummy', 'dummy', 'GBP', 150, 100)


def test_store(fixture):

    # Supply integer timestamp, as it gets rounded in the database, and
    # we want to check for equality later
    p = price.Price('dummy', 'dummy', 'GBP', 100, 150,
                    data={'name': 'value'},
                    timestamp=int(time()))

    s = price.Store('test_price.sqlite')
    s.save(p)

    # Load data we've just saved
    rows = s.load('dummy', 'dummy', 'GBP')

    assert len(rows) == 1, 'Incorrect number of rows returned'

    p2 = rows[0]
    assert p.exchange == p2.exchange
    assert p.security == p2.security
    assert p.currency == p2.currency
    assert p.bid == p2.bid
    assert p.offer == p2.offer
    assert p.timestamp == p2.timestamp

    # Close and re-open database to confirm data is still there
    s.close()
    s = price.Store('test_price.sqlite')

    rows = s.load('dummy', 'dummy', 'GBP')
    assert len(rows) == 1, 'Incorrect number of rows returned'

    p2 = rows[0]
    assert p.exchange == p2.exchange
    assert p.security == p2.security
    assert p.currency == p2.currency
    assert p.bid == p2.bid
    assert p.offer == p2.offer
    assert p.timestamp == p2.timestamp

    s.close()
