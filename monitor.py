#!/usr/bin/python

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod, currency, market):

        self.url = url
	self.updatePeriod = updatePeriod
        self.setUpdatePeriod(updatePeriod)
        self.currency = currency
        self.market = market
 
        self.offer = 32490
        self.bid = 32410

	self.spread = self.offer - self.bid

    def set_offer(self, value):
	if (value < self._bid):
	    raise UpdateError('Offer price cannot be less than bid price')
	else:
	    self._offer = value
	
    def get_offer(self):
	return _offer

    offer = property(set_offer, get_offer)


    def setUpdatePeriod(self, updatePeriod):

        u_p = updatePeriod

        if (u_p < 0):
            raise UpdateError('Invalid update period')
        else:
            self.updatePeriod = u_p

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
