#!/usr/bin/python

import monitor
import toolbox
from xml.dom import minidom

class BullionVaultMonitor(monitor.Monitor):
    '''
    Class to monitor market prices at BullionVault
    '''

    def __init__(self, updatePeriod, currency, market):

        self.url = 'bvdata.xml'
        self.currency = currency
        self.market = market
        monitor.Monitor.__init__(self, self.url, updatePeriod)
        self.update(self.url)


    def update(self, source):
        '''
        Function to pull the latest prices from BullionVault and extract them into variables
        
        Assumes one pitch per market/currency combination in the file.
        Also assumes one buy and one sell price per pitch!
        '''

        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()

        for pitch in xmldoc.getElementsByTagName('pitch'):

            if pitch.getAttribute('securityId') == self.market and \
               pitch.getAttribute('considerationCurrency') == self.currency:

                for price in pitch.getElementsByTagName('price'):

                    if price.getAttribute('actionIndicator') == 'B':

                        self.bid = int(price.getAttribute('limit'))

                    elif price.getAttribute('actionIndicator') == 'S':

                        self.offer = int(price.getAttribute('limit'))

                    else:

                        raise MonitorError('No prices were found')

