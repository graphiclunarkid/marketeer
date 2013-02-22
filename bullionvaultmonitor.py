#!/usr/bin/python

# Copyright (C) 2013 Richard King, Adam Spragg
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
from xml.dom import minidom

class BullionVaultMonitor():
    '''
    Class to monitor market prices at BullionVault
    '''

    def __init__(self, \
	             updatePeriod=30,\
				 url="http://live.bullionvault.com/view_market_xml.do",\
				 currency="GBP",\
				 market="AUXLN"):

        self.updatePeriod = updatePeriod
        self.url = url
        self.currency = currency
        self.market = market
        self._data = None
        self._timestamp = time()

    def _update(self):
        '''
        Function extract prices in the selected currency, from the selected market, into variables

        Assumes one pitch per market/currency combination in the file.
        Also assumes one buy and one sell price per pitch!
        '''

        now = time()

        if ((now - self._timestamp) > self.updatePeriod) or self._data == None:

            sock = toolbox.openAnything(self.url)
            xmldoc = minidom.parse(sock).documentElement
            sock.close()
            self._data = xmldoc
            self._timestamp = now

        for pitch in self._data.getElementsByTagName('pitch'):

            if pitch.getAttribute('securityId') == self.market and \
                pitch.getAttribute('considerationCurrency') == self.currency:

                for p in pitch.getElementsByTagName('price'):

                    if p.getAttribute('actionIndicator') == 'B':

                        bid = int(p.getAttribute('limit'))

                    elif p.getAttribute('actionIndicator') == 'S':

                        offer = int(p.getAttribute('limit'))

                    else:

                        raise MonitorError('No prices were found')

        self._price = price.Price('BullionVault', 'XAU', self.currency,
                bid, offer, { 'url': self.url }, now)

    def get_price(self):

        self._update()
        return self._price

    price = property(get_price)


class MonitorError(Exception):
    '''Exception thrown by the BullionVaultMonitor class'''

    def __init__(self, message):

        self.message = message

    def __str__(self):

        return repr(self.message)


def _test(mon):
    mon.price.printstate()
    sleep(mon.updatePeriod + 1)
    mon.price.printstate()

def main():
    _test(BullionVaultMonitor())

if __name__ == "__main__":
    main()
