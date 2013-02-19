#!/usr/bin/python

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

from time import time

class Price():
    '''
    Class to encapsulate market prices

    Properties:
        exchange    -- Exchange where price was found (e.g. "BullionVault")
        security    -- id of the security (currency, stock) priced (e.g. "XAU")
        currency    -- ISO 4217 currency code of price (e.g. "GBP")
        bid         -- Bid price of security (e.g. 33328)
        offer       -- Offer price of security (e.g. 33370)
        spread      -- Difference between #bid and #offer (e.g. 42)
        data        -- Dictionary of extra data provided by Monitor
        timestamp   -- Date/time the price was retrieved/accurate
    '''

    def __init__(self, exchange, security, currency, bid, offer, data=None, timestamp=time()):
        if not exchange \
                or not security \
                or not currency \
                or not bid \
                or not offer \
                or not timestamp:
            raise TypeError('Invalid arguments')

        if bid >= offer:
            raise TypeError('Bid >= offer');

        self.exchange = exchange
        self.security = security
        self.currency = currency
        self.bid = bid
        self.offer = offer
        self.data = data
        self.timestamp = timestamp


    def get_spread(self):

        return (self.offer - self.bid)

    spread = property(get_spread)
