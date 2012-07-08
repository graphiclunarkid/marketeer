#!/usr/bin/python

import monitor
import toolbox
from xml.dom import minidom

class BullionVaultMonitor(monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, updatePeriod, currency, market):

        self.url = 'bvdata.xml'
        monitor.Monitor.__init__(self, self.url, updatePeriod, currency, market)

        self.validCurrencies = frozenset( ['EUR','GBP','USD'] )
        self.validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU'] )

        if (self.currency not in self.validCurrencies):
            raise monitor.MonitorError('Invalid currency')

        if (self.market not in self.validMarkets):
            raise monitor.MonitorError('Invalid market')

        self.data = self.update(self.url)

    def update(self, source):
        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc
