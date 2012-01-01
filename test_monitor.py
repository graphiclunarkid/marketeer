import unittest
import monitor

class Test_Monitor(unittest.TestCase):

    def setUp(self):
        self.url = 'http://live.bullionvault.com/view_market_xml.do'
        self.updatePeriod = 60
        self.validCurrencies = 'GBP'
        self.validMarkets = 'AUXLN'

        self.validMonitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.validMonitors.add(monitor.Monitor(self.url,self.updatePeriod,i,j))

    def tearDown(self):

        if len(self.validMonitors) > 0:
            self.validMonitors.clear()

        self.validMonitors = None
        self.monitor = None
        
    def test_getMonitorAttributes(self):

        while len(self.validMonitors) > 0:

            self.monitor = self.validMonitors.pop()

            self.assertIsNotNone(self.monitor.getCurrency(), 'Currency is not set')
            self.assertIsNotNone(self.monitor.getMarket(), 'Market is not set')
            self.assertGreater(self.monitor.getBid(), 0, 'Bid price is zero or negative')
            self.assertGreater(self.monitor.getOffer(), 0, 'Offer price is zero or negative')
            self.assertGreaterEqual(self.monitor.getSpread(), 0, 'Spread is negative')
            self.assertIsNotNone(self.monitor.getUrl(), 'URL not set')
            self.assertGreater(self.monitor.getUpdatePeriod(), 0, 'Update period is zero or negative')

#    def test_setMonitorAttributes(self):
#
#        self.monitor = self.validmonitors.pop()
#        self.monitor.setUpdatePeriod(90)
#        self.assertEqual(self.monitor.getUpdatePeriod, 90, 'Update period was not set correctly')

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Monitor)
unittest.TextTestRunner(verbosity=2).run(suite)
