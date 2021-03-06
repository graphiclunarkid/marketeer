#!/usr/bin/python3
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

from time import time
from decimal import Decimal
import sqlite3


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

    def __init__(self, exchange, security, currency, bid, offer, exponent='1',
                 data={}, timestamp=time()):

        if not exchange \
                or not security \
                or not currency \
                or not bid \
                or not offer \
                or not timestamp:
            raise TypeError('Invalid arguments')

        if bid >= offer:
            raise TypeError('Bid >= offer')

        self.exchange = exchange
        self.security = security
        self.currency = currency
        self._bid = Decimal(bid)
        self._offer = Decimal(offer)
        self.exponent = Decimal(exponent)
        self.data = data
        self.timestamp = timestamp

    def get_bid(self):

        return (self._bid * self.exponent)

    bid = property(get_bid)

    def get_offer(self):

        return (self._offer * self.exponent)

    offer = property(get_offer)

    def get_spread(self):

        return (self.offer - self.bid)

    spread = property(get_spread)

    def printstate(self):

        print("Exchange:", self.exchange)
        print("Security:", self.security)
        print("Bid:", self.bid, self.currency)
        print("Offer:", self.offer, self.currency)
        print("Spread:", self.spread, self.currency)
        print("Timestamp:", self.timestamp)


class Store():
    '''
    Class to encapsulate a store of prices
    '''

    def __init__(self, fname):
        '''
        Open/create a price store
        '''
        self._fname = fname
        self._store = sqlite3.connect(fname)

        c = self._store.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS price (
                  exchange TEXT NOT NULL,
                  security TEXT NOT NULL,
                  currency TEXT NOT NULL,
                  timestamp INTEGER NOT NULL,
                  bid DECIMAL(18, 6) NOT NULL,
                  offer DECIMAL(18, 6) NOT NULL,
                  PRIMARY KEY (exchange, security, currency, timestamp)
                  )""")

        c.execute("""CREATE TABLE IF NOT EXISTS price_data (
                  exchange TEXT NOT NULL,
                  security TEXT NOT NULL,
                  currency TEXT NOT NULL,
                  timestamp INTEGER NOT NULL,
                  name TEXT NOT NULL,
                  value TEXT NOT NULL,
                  PRIMARY KEY (exchange, security, currency, timestamp, name),
                  FOREIGN KEY (exchange, security, currency, timestamp)
                  REFERENCES price(exchange, security, currency, timestamp)
                  )""")
        return

    def save(self, p):
        '''
        Save a price to a price store
        '''
        c = self._store.cursor()

        c.execute("""INSERT INTO price (
                  exchange, security, currency, timestamp, bid, offer)
                  VALUES (?, ?, ?, ?, ?, ?)""",
                  (p.exchange, p.security, p.currency, int(p.timestamp),
                   str(p.bid), str(p.offer)))

        for n in p.data:
            c.execute("""INSERT INTO price_data (
                      exchange, security, currency, timestamp, name, value)
                      VALUES (?, ?, ?, ?, ?, ?)""",
                      (p.exchange, p.security, p.currency, int(p.timestamp),
                       str(n), str(p.data[n])))

        self._store.commit()

        return

    def load(self, exchange, security, currency):
        '''
        Load a list of prices from a price store
        '''
        c = self._store.cursor()

        c.execute("""SELECT exchange, security, currency, timestamp, bid, offer
                  FROM price
                  WHERE exchange = ?
                  AND security = ?
                  AND currency = ?""",
                  (exchange, security, currency))

        r = []
        for row in c:
            r.append(Price(row[0],
                           row[1],
                           row[2],
                           row[4],
                           row[5],
                           timestamp=row[3]))

        return r

    def close(self):
        '''
        Close a price store
        '''
        self._store.close()
        return
