import unittest
import monitor

class Test_Monitor(unittest.TestCase):

    def setUp(self):
        self.url = 'http://live.bullionvault.com/view_market_xml.do'
        self.updatePeriod = 60
        self.currency = 'GBP'
        self.market = 'AUXLN'
        self.monitor = monitor.Monitor(self.url,self.updatePeriod,self.currency,self.market)

    def tearDown(self):
        self.monitor = None

    def suite():
        return unittest.TestLoader().loadTestsFromTestCase(Test_Monitor)
    
    def test_getMonitorAttributes(self):
        self.assertIsNotNone(self.monitor.getCurrency(), 'Currency is not set')
        self.assertIsNotNone(self.monitor.getMarket(), 'Market is not set')
        self.assertGreater(self.monitor.getBid(), 0, 'Bid price is zero or negative')
        self.assertGreater(self.monitor.getOffer(), 0, 'Offer price is zero or negative')
        self.assertGreaterEqual(self.monitor.getSpread(), 0, 'Spread is negative')
        self.assertIsNotNone(self.monitor.getUrl(), 'URL not set')
        self.assertGreater(self.monitor.getUpdatePeriod(), 0, 'Update period is zero or negative')

if __name__ == '__main__':
    unittest.main()
