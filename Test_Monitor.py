import unittest
import Monitor

class Test_Monitor(unittest.TestCase):

    def setUp(self):
        self.monitor = Monitor.Monitor('http://live.bullionvault.com/view_market_xml.do', 60)
    
    def test_getMonitorAttributes(self):

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

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
