import unittest
import bullionvaultmonitor
from time import sleep

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.updatePeriod = 10
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )

    def test_monitorAttributes(self):

        validMonitors = set()

        for i in self.validCurrencies:

            for j in self.validMarkets:

                validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

        monitor = validMonitors.pop()

        while (len(validMonitors) > 0):

            self.assertIsNotNone(monitor.bid, 'Bid price is not set')
            self.assertIsNotNone(monitor.offer, 'Offer price is not set')
            self.assertGreaterEqual(monitor.spread, 0, 'Spread is negative')

            monitor = validMonitors.pop()


    def test_monitorRefresh(self):

        monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,'GBP','AUXLN')
        monitor.url = 'bvdata.xml'

        bid = monitor.bid
        offer = monitor.offer
        spread = monitor.spread
        self.assertEqual(bid, 33910, 'Bid price was not imported correctly')
        self.assertEqual(offer, 33950, 'Offer price was not imported correctly')
        self.assertEqual(spread, 40, 'Spread was not calculated imported correctly')

        monitor.url = 'bvdata2.xml'
        bid2 = monitor.bid
        offer2 = monitor.offer
        spread2 = monitor.spread
        self.assertEqual(bid2, bid, 'Bid price changed before update was due')
        self.assertEqual(offer2, offer, 'Offer price changed before update was due')
        self.assertEqual(spread2, spread, 'Spread changed before update was due')

        sleep(self.updatePeriod)
        bid2 = monitor.bid
        offer2 = monitor.offer
        spread2 = monitor.spread
        self.assertEqual(bid2, 33920, 'Bid price not updated after update was due')
        self.assertEqual(offer2, offer, 'Offer price changed but wasn\'t supposed to')
        self.assertEqual(spread2, 30, 'Spread not updated after update was due')


suite = unittest.TestLoader().loadTestsFromTestCase(Test_BullionVaultMonitor)
unittest.TextTestRunner(verbosity=2).run(suite)
