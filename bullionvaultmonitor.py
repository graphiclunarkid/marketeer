#!/usr/bin/python

import monitor

class BullionVaultMonitor(monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, currency, market):

        self._currency = currency
        self._market = market

        self._validCurrencies = frozenset( ['EUR','GBP','USD'] )
        self._validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU'] )

        if self._currency not in self._validCurrencies:
            raise monitor.InitError('Invalid currency')

        if self._market not in self._validMarkets:
            raise monitor.InitError('Invalid market')

        self._offer = 32490
        self._bid = 32410
        self._spread = self._offer - self._bid

    def getCurrency(self):
        return self._currency

    def getMarket(self):
        return self._market

    def getOffer(self):
        return self._offer

    def getBid(self):
        return self._bid
    
    def getSpread(self):
        return self._spread

