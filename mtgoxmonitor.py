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

import toolbox
import price
from time import time, sleep
import json

class MtgoxMonitor():
    '''
    Class to monitor market prices at MtGox

    https://en.bitcoin.it/wiki/MtGox/API/HTTP/v1
    '''

    def __init__(self,\
                 updatePeriod=30,\
                 url = 'https://mtgox.com/api/1/',\
                 security = 'BTC',\
                 currency = 'GBP',\
                 request = '/ticker'):

        self.updatePeriod = updatePeriod
        self.url = url + security + currency + request
        self.currency = currency
        self._data = None
        self._timestamp = time()


    def _update(self):
        '''
        Update price data from MtGox
        '''

        now = time()

        if (now - self._timestamp) <= self.updatePeriod and self._data != None:
            return

        sock = toolbox.openAnything(self.url)
        self._data = json.load(sock)
        sock.close()
        self._timestamp = now

        self._price = price.Price('MtGox', 'BTC', self.currency,
                float(self._data['return']['buy']['value']),
                float(self._data['return']['sell']['value']),
                { 'url': self.url },
                now)


    def get_price(self):

        self._update()
        return self._price

    price = property(get_price)


def _test(mon):
    mon.price.printstate()
    sleep(mon.updatePeriod + 1)
    mon.price.printstate()


def main():
    _test(MtgoxMonitor())


if __name__ == "__main__":
    main()

