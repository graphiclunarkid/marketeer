#!/usr/bin/python

import toolbox
from time import time
from xml.dom import minidom

class Monitor:
    '''Generic market-price monitor class'''

    def __init__(self, url, updatePeriod):

        self.url = url
	self.updatePeriod = updatePeriod
        self.offer = None
        self.bid = None
        self.timestamp = time()
        self.data = self._refreshData()	

    def get_spread(self):

        return (self.offer - self.bid)

    spread = property(get_spread)


    def _refreshData(self):

        sock = toolbox.openAnything(self.url)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc


    def get_data(self):

        '''Extremely dubious time-check: needs sorting!'''
        if (time() - self.timestamp) > 60:

            self.data = self._refreshData()

        return self.data

    data = property(get_data)


class MonitorError(Exception):
    '''Exception thrown by the Monitor class'''
    
    def __init__(self, message):

        self.message = message
        
    def __str__(self):

        return repr(self.message)

