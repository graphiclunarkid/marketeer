#!/usr/bin/python

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod, currency, market):

        self._url = url
        self.setUpdatePeriod(updatePeriod)
        self._currency = currency
        self._market = market
        
        self._offer = 32490
        self._bid = 32410

    def getUrl(self):

        return self._url
    
    def getUpdatePeriod(self):

        return self._updatePeriod

    def setUpdatePeriod(self, updatePeriod):

        u_p = updatePeriod

        if (u_p < 0):
            raise UpdateError('Invalid update period')
        else:
            self._updatePeriod = u_p

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


class CreateError(Error):
    '''Exception thrown by the Monitor() constructor'''
    
    def __init__(self, message):

        self.message = message
        
    def __str__(self):

        return repr(self.message)

class UpdateError(Error):
    '''Exception thrown by the Monitor() constructor'''
    
    def __init__(self, message):

        self.message = message

    def __str__(self):

        return repr(self.message)
