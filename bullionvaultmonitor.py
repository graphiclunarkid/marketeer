#!/usr/bin/python

import monitor

class BullionVaultMonitor(monitor.Monitor):
    '''
    Class to monitor market prices at BullionVault
    '''

    def __init__(self, updatePeriod, currency, market):

#        self.url = 'http://live.bullionvault.com/view_market_xml.do'
        self.url = 'bvdata.xml'
        self.currency = currency
        self.market = market
        monitor.Monitor.__init__(self, self.url, updatePeriod)
        self.update()


    def update(self):
        '''
        Function extract prices in the selected currency, from the selected market, into variables
        
        Assumes one pitch per market/currency combination in the file.
        Also assumes one buy and one sell price per pitch!
        '''

        for pitch in self.data.getElementsByTagName('pitch'):

            if pitch.getAttribute('securityId') == self.market and \
               pitch.getAttribute('considerationCurrency') == self.currency:

                for price in pitch.getElementsByTagName('price'):

                    if price.getAttribute('actionIndicator') == 'B':

                        self.bid = int(price.getAttribute('limit'))

                    elif price.getAttribute('actionIndicator') == 'S':

                        self.offer = int(price.getAttribute('limit'))

                    else:

                        raise MonitorError('No prices were found')

