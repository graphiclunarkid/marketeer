#!/usr/bin/python

import toolbox
from time import time
from xml.dom import minidom

class BullionVaultMonitor():
    '''
    Class to monitor market prices at BullionVault
    '''

    def __init__(self, updatePeriod, currency, market):

#        self.url = 'http://live.bullionvault.com/view_market_xml.do'
        self.url = 'bvdata.xml'
	self.updatePeriod = updatePeriod
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

        if ((time() - self._timestamp) > self.updatePeriod) or \
        self._data == None:

            sock = toolbox.openAnything(self.url)
            xmldoc = minidom.parse(sock).documentElement
            sock.close()
            self._data = xmldoc
            self._timestamp = time()

        for pitch in self._data.getElementsByTagName('pitch'):

            if pitch.getAttribute('securityId') == self.market and \
               pitch.getAttribute('considerationCurrency') == self.currency:

                for price in pitch.getElementsByTagName('price'):

                    if price.getAttribute('actionIndicator') == 'B':

                        self._bid = int(price.getAttribute('limit'))

                    elif price.getAttribute('actionIndicator') == 'S':

                        self._offer = int(price.getAttribute('limit'))

                    else:

                        raise MonitorError('No prices were found')

    def get_offer(self):

        self._update()
        return self._offer

    offer = property(get_offer)


    def get_bid(self):

        self._update()
        return self._bid

    bid = property(get_bid)


    def get_spread(self):

        return (self._offer - self._bid)

    spread = property(get_spread)


class MonitorError(Exception):
    '''Exception thrown by the Monitor class'''
    
    def __init__(self, message):

        self.message = message
        
    def __str__(self):

        return repr(self.message)

