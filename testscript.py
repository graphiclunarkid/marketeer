#!/bin/python

import bullionvaultmonitor
from time import *


period = 5


def printstuff(mon):
    print "Bid:", mon.bid
    print "Offer:", mon.offer
    print "Spread:", mon.spread


def main():
    mon = bullionvaultmonitor.BullionVaultMonitor(period, "GBP", "AUXLN")
    printstuff(mon)
    sleep(period + 1)
    printstuff(mon)


if __name__ == "__main__":
    main()
