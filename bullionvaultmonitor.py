#!/usr/bin/python

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

import toolbox
import price

from time import time, sleep
from xml.dom import minidom
import argparse
import locale


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

        self._price = price.Price(exchange='BullionVault',\
                                  security='XAU',\
                                  currency=self.currency,\
                                  bid=bid,\
                                  offer=offer,\
                                  data={ 'url': self.url },\
                                  timestamp=now)

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


def main():
    locale.setlocale(locale.LC_ALL, '')

    cur = locale.localeconv()['int_curr_symbol'][:3] or 'GBP'

    parser = argparse.ArgumentParser(description='Monitor BullionVault Exchange')
    parser.add_argument('-t', '--test', action='store_true',
            help='Get and display the current price twice (ignores -q)')
    parser.add_argument('-s', '--save',
            help='Save the price to <SAVE>')
    parser.add_argument('-q', '--quiet', action='store_true',
            help='Do not display the price')
    parser.add_argument('-c', '--currency',
            default=cur,
            help='Currency in which to retrieve price')

    args = parser.parse_args()

    mon = BullionVaultMonitor(currency=args.currency)

    if args.test:
        mon.price.printstate()
        sleep(mon.updatePeriod + 1)
        mon.price.printstate()
        return

    if args.save:
        store = price.Store(args.save)
        store.save(mon.price)
        store.close()

    if not args.quiet:
        mon.price.printstate()


if __name__ == "__main__":
    main()

