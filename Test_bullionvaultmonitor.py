import unittest
import monitor
import bullionvaultmonitor

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.updatePeriod = 60
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )
        self.invalidCurrency = '123'
        self.invalidMarket = '456'
        self.validMonitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

    def test_getMonitorAttributes(self):

        self.monitors = self.validMonitors.copy()

        while len(self.monitors) > 0:

            self.monitor = self.monitors.pop()

            self.currency = self.monitor.getCurrency()
            self.market = self.monitor.getMarket()
            self.bid = self.monitor.getBid()
            self.offer = self.monitor.getOffer()
            self.spread = self.monitor.getSpread()
            self.url = self.monitor.getUrl()
            self.updatePeriod = self.monitor.getUpdatePeriod()

            self.assertGreater(self.offer, 0, 'Offer price is zero or negative')
            self.assertGreater(self.bid, 0, 'Bid price is zero or negative')
            self.assertGreaterEqual(self.offer, self.bid, 'Offer price is >= bid price')
            self.assertGreaterEqual(self.spread, 0, 'Spread is negative')
            self.assertIsNotNone(self.url, 'URL not set')
            self.assertGreater(self.updatePeriod, 0, 'Update period is zero or negative')
        
    def test_invalidMonitors(self):

        with self.assertRaises(monitor.InitError) as cm:
            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.invalidCurrency, self.validMarkets[0])
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid currency')

        with self.assertRaises(monitor.InitError) as cm:
            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.validCurrencies[0], self.invalidMarket)
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid market')

    def tearDown(self):

        self.validMonitors.clear()
        self.validMonitors = None
        self.monitors = None

        
if __name__ == '__main__':
    unittest.main()
