#!/usr/bin/python

import monitor
import toolbox
from xml.dom import minidom

class BullionVaultMonitor(monitor.Monitor):
    '''Class to monitor market prices at BullionVault'''

    def __init__(self, updatePeriod, currency, market):

        self.url = 'bvdata.xml'
        monitor.Monitor.__init__(self, self.url, updatePeriod, currency, market)
        self.data = self.update(self.url)

    def update(self, source):
        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc



