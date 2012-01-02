#!/usr/bin/python

import monitor
import toolbox
from xml.dom import minidom

class BullionVaultMonitor(monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, updatePeriod, currency, market):

        self._url = 'bvdata.xml'
        monitor.Monitor.__init__(self, self._url, updatePeriod, currency, market)

        self._validCurrencies = frozenset( ['EUR','GBP','USD'] )
        self._validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU'] )

        if (self._currency not in self._validCurrencies):
            raise monitor.CreateError('Invalid currency')

        if (self._market not in self._validMarkets):
            raise monitor.CreateError('Invalid market')

        self._data = self._update(self._url)

    def _update(self, source):
        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc
