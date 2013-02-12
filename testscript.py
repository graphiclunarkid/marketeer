#!/usr/bin/python

import bullionvaultmonitor
from time import *


def printstuff(mon):
    print "Bid:", mon.bid
    print "Offer:", mon.offer
    print "Spread:", mon.spread


def main():
    mon = bullionvaultmonitor.BullionVaultMonitor()
    printstuff(mon)
    sleep(mon.updatePeriod + 1)
    printstuff(mon)


if __name__ == "__main__":
    main()
