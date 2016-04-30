#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

"""
test_bullionvaultmonitor
----------------------------------

Tests for `bullionvaultmonitor` module.
"""


import pytest

import os
from time import sleep

from marketeer import bullionvaultmonitor


class TestData():
    here = os.path.abspath(os.path.dirname(__file__))
    url = here + '/bvdata.xml'
    updatePeriod = 1
    validCurrencies = list(['EUR', 'GBP', 'USD'])
    validMarkets = list(['AUXLN', 'AUXNY', 'AUXZU'])


@pytest.fixture(scope="module")
def testdata():
    return TestData()


def test_monitorAttributes(testdata):

    validMonitors = set()

    for i in testdata.validCurrencies:

        for j in testdata.validMarkets:

            validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(
                testdata.updatePeriod,
                url=testdata.url,
                currency=i,
                market=j))

    monitor = validMonitors.pop()

    while (len(validMonitors) > 0):

        assert monitor.price.exchange == 'BullionVault', 'Wrong exchange'
        assert monitor.price.security == 'XAU', 'Wrong security'
        assert monitor.price.spread is not None, 'Spread wasn\'t calculated'
        assert monitor.price.spread >= 0, 'Spread is negative'
        assert monitor.price.bid is not None, 'Bid price is not set'
        assert monitor.price.offer is not None, 'Offer price is not set'
        assert monitor.price.timestamp is not None, 'Timestamp not set'

        monitor = validMonitors.pop()


def test_monitorRefresh(testdata):

    monitor = bullionvaultmonitor.BullionVaultMonitor(
        testdata.updatePeriod,
        url=testdata.url,
        currency='GBP',
        market='AUXLN')

    bid = monitor.price.bid
    offer = monitor.price.offer
    spread = monitor.price.spread

    assert bid == 33910, 'Bid price was not imported correctly'
    assert offer == 33950, 'Offer price was not imported correctly'
    assert spread == 40, 'Spread was not calculated imported correctly'

    sleep(testdata.updatePeriod / 2)
    monitor.url = testdata.here + '/bvdata2.xml'
    bid2 = monitor.price.bid
    offer2 = monitor.price.offer
    spread2 = monitor.price.spread
    assert bid2 == bid, 'Bid price changed before update was due'
    assert offer2 == offer, 'Offer price changed before update was due'
    assert spread2 == spread, 'Spread changed before update was due'

    sleep(testdata.updatePeriod)
    bid2 = monitor.price.bid
    offer2 = monitor.price.offer
    spread2 = monitor.price.spread

    assert bid2 == 33920, 'Bid price not updated after update was due'
    assert offer2 == offer, 'Offer price changed but wasn\'t supposed to'
    assert spread2 == 30, 'Spread not updated after update was due'
