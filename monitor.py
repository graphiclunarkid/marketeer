#!/usr/bin/python

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod, currency, market):

        self.url = url
	self._updatePeriod = updatePeriod
        self.currency = currency
        self.market = market
 
        self._offer = 32490
        self.bid = 32410

	self.spread = self._offer - self.bid


    def set_offer(self, value):
	if (value < self.bid):
	    raise UpdateError('Offer price cannot be less than bid price')
	self._offer = value
        self.spread = self._offer - self.bid
	
    def get_offer(self):
	return self._offer

    offer = property(get_offer, set_offer)


    def set_updatePeriod(self, value):
        if (value < 0):
            raise UpdateError('Invalid update period')
        self._updatePeriod = value

    def get_updatePeriod(self):
        return self._updatePeriod

    updatePeriod = property(get_updatePeriod, set_updatePeriod)


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
