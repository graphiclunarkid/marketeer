import unittest
import BullionVaultMonitor

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = BullionVaultMonitor.BullionVaultMonitor()
        self.currencies = set( ['EUR','GBP','USD',''] ) # Blank = all
        self.markets = set( ['AUXLN','AUXNY','AUXZU',''] ) # Blank = all
        
    def test_Prices(self):
        self.assertGreater(self.monitor.ask, 0, "Ask price is negative")
        self.assertGreater(self.monitor.bid, 0, "Bid price is negative")
        
        self.assertGreaterEqual(self.monitor.ask, self.monitor.bid, "Ask price is >= bid price")
        self.assertGreaterEqual(self.monitor.spread, 0, "Spread is negative")

    def test_Markets(self):
        self.assertIn(self.monitor.currency, self.currencies, "Invalid currency")
        self.assertIn(self.monitor.market, self.markets, "Invalid market")


if __name__ == '__main__':
    unittest.main()
