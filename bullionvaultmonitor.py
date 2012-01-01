#!/usr/bin/python

import monitor

class BullionVaultMonitor(monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, updatePeriod, currency, market):

        self._url = 'http://live.bullionvault.com/view_market_xml.do'
        monitor.Monitor.__init__(self, self._url, updatePeriod, currency, market)

        self._validCurrencies = frozenset( ['EUR','GBP','USD'] )
        self._validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU'] )

        if (self._currency not in self._validCurrencies):
            raise monitor.CreateError('Invalid currency')

        if (self._market not in self._validMarkets):
            raise monitor.CreateError('Invalid market')
