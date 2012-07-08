#!/usr/bin/python

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod, currency, market):

        self.url = url
	self.updatePeriod = updatePeriod
        self.currency = currency
        self.market = market
 
        self.offer = 32490
        self.bid = 32410
	
    def get_spread(self):

        return (self.offer - self.bid)

    spread = property(get_spread)


class MonitorError(Exception):
    '''Exception thrown by the Monitor class'''
    
    def __init__(self, message):

        self.message = message
        
    def __str__(self):

        return repr(self.message)

