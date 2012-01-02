import unittest
import monitor

class Test_Monitor(unittest.TestCase):

    def setUp(self):
        self.url = 'bvdata.xml'
        self.updatePeriod = 60
        self.validCurrencies = 'GBP'
        self.validMarkets = 'AUXLN'

        self.validMonitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.validMonitors.add(monitor.Monitor(self.url,self.updatePeriod,i,j))

        self.monitor = self.validMonitors.pop()

    def tearDown(self):

        if (len(self.validMonitors) > 0):
            self.validMonitors.clear()

        self.validMonitors = None
        self.monitor = None
        
    def test_getMonitorAttributes(self):

        while (len(self.validMonitors) > 0):

            self.assertIsNotNone(self.monitor.getCurrency(), 'Currency is not set')
            self.assertIsNotNone(self.monitor.getMarket(), 'Market is not set')
            self.assertGreater(self.monitor.getBid(), 0, 'Bid price is zero or negative')
            self.assertGreater(self.monitor.getOffer(), 0, 'Offer price is zero or negative')
            self.assertGreaterEqual(self.monitor.getSpread(), 0, 'Spread is negative')
            self.assertIsNotNone(self.monitor.getUrl(), 'URL not set')
            self.assertGreater(self.monitor.getUpdatePeriod(), 0, 'Update period is zero or negative')

            self.monitor = self.validMonitors.pop()

    def test_setMonitorAttributes(self):

        self.monitor.setUpdatePeriod(90)
        self.assertEqual(self.monitor.getUpdatePeriod(), 90, 'Update period was not set correctly')

    def test_setInvalidMonitorAttributes(self):

        before = self.monitor.getUpdatePeriod()

        with self.assertRaises(monitor.UpdateError) as cm:
            self.monitor.setUpdatePeriod(-90)
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid update period')

        after = self.monitor.getUpdatePeriod()
        self.assertEqual(before, after, 'Update period shouldn\'t have changed but it did')

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Monitor)
unittest.TextTestRunner(verbosity=2).run(suite)
