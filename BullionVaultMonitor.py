#!/usr/bin/python

import Monitor

class BullionVaultMonitor(Monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, currency, market):

        self._currency = currency
        self._market = market

        self._validCurrencies = frozenset( ['EUR','GBP','USD'] )
        self._validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU'] )

        if self._currency not in self._validCurrencies:
            raise InitError('Invalid currency')

        if self._market not in self._validMarkets:
            raise InitError('Invalid market')

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


class Error(Exception):
    '''Base class for exceptions in the BullionVaultMonitor module'''
    pass


class InitError(Error):
    '''Exception thrown by the BullionVaultMonitor constructor'''
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


