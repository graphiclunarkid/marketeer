import unittest
import BullionVaultMonitor

class Test_BullionVaultMonitorMarkets(unittest.TestCase):

    def setUp(self):
        self.validCurrencies = list( ['EUR','GBP','USD',''] ) # Blank = all
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU',''] ) # Blank = all
        self.monitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.monitors.add(BullionVaultMonitor.BullionVaultMonitor(i,j))
        
    def test_Markets(self):
        while len(self.monitors) > 0:
            try:
                self.monitor = self.monitors.pop()
                self.assertIn(self.monitor.currency, self.validCurrencies, "Invalid currency")
                self.assertIn(self.monitor.market, self.validMarkets, "Invalid market")
            except KeyError, e:
                self.assertEqual(len(self.monitors), 0, e.message)

    def tearDown(self):
        self.monitors = None
        self.currencies = None
        self.markets = None


class Test_BullionVaultMonitorPrices(unittest.TestCase):

    def setUp(self):
        self.monitor = BullionVaultMonitor.BullionVaultMonitor('EUR', 'AUXLN')
    
    def test_Prices(self):
        self.assertGreater(self.monitor.ask, 0, "Ask price is negative")
        self.assertGreater(self.monitor.bid, 0, "Bid price is negative")
        
        self.assertGreaterEqual(self.monitor.ask, self.monitor.bid, "Ask price is >= bid price")
        self.assertGreaterEqual(self.monitor.spread, 0, "Spread is negative")

    def tearDown(self):
        self.monitor.dispose()
        self.monitor = None


if __name__ == '__main__':
    unittest.main()
