#!/usr/bin/python

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod):
        self._url = url
        self._updatePeriod = updatePeriod

        self._currency = 'EUR'
        self._market = 'AUXLN'
        self._offer = 32490
        self._bid = 32410

    def getUrl(self):
        return self._url
    
    def getUpdatePeriod(self):
        return self._updatePeriod

    def getCurrency(self):
        return self._currency

    def getMarket(self):
        return self._market

    def getOffer(self):
        return self._offer

    def getBid(self):
        return self._bid
    
    def getSpread(self):
        return self._offer - self._bid

    
class Error(Exception):
    '''Base class for exceptions in the Monitor module'''
    pass


class InitError(Error):
    '''Exception thrown by the Monitor() constructor'''
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


