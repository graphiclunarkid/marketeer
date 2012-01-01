import unittest
import BullionVaultMonitor

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.validCurrencies = list( ['EUR','GBP','USD',''] ) # Blank = all
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU',''] ) # Blank = all
        self.invalidCurrency = '123'
        self.invalidMarket = '456'
        self.validMonitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.validMonitors.add(BullionVaultMonitor.BullionVaultMonitor(i,j))

    def test_validMonitors(self):

        self.monitors = self.validMonitors.copy()

        while len(self.monitors) > 0:
            self.monitor = self.monitors.pop()
            self.assertIn(self.monitor.currency, self.validCurrencies, 'Invalid currency')
            self.assertIn(self.monitor.market, self.validMarkets, 'Invalid market')
            self.assertGreater(self.monitor.offer, 0, 'Offer price is negative')
            self.assertGreater(self.monitor.bid, 0, 'Bid price is negative')
            self.assertGreaterEqual(self.monitor.offer, self.monitor.bid, 'Offer price is >= bid price')
            self.assertGreaterEqual(self.monitor.spread, 0, 'Spread is negative')

    def test_invalidMonitors(self):

        with self.assertRaises(BullionVaultMonitor.InitError) as cm:
            self.monitor = BullionVaultMonitor.BullionVaultMonitor(self.invalidCurrency, self.validMarkets[0])
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid currency')

        with self.assertRaises(BullionVaultMonitor.InitError) as cm:
            self.monitor = BullionVaultMonitor.BullionVaultMonitor(self.validCurrencies[0], self.invalidMarket)
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid market')

    def tearDown(self):

        self.validMonitors.clear()
        self.validMonitors = None
        self.monitors = None

        
if __name__ == '__main__':
    unittest.main()
