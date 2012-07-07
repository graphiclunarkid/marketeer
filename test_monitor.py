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

            self.assertIsNotNone(self.monitor.currency, 'Currency is not set')
            self.assertIsNotNone(self.monitor.market, 'Market is not set')
            self.assertGreater(self.monitor.bid, 0, 'Bid price is zero or negative')
            self.assertGreater(self.monitor.offer, 0, 'Offer price is zero or negative')
            self.assertGreaterEqual(self.monitor.spread, 0, 'Spread is negative')
            self.assertIsNotNone(self.monitor.url, 'URL not set')
            self.assertGreater(self.monitor.updatePeriod, 0, 'Update period is zero or negative')

            self.monitor = self.validMonitors.pop()

    def test_setInvalidMonitorAttributes(self):

        before = self.monitor.updatePeriod

        with self.assertRaises(monitor.UpdateError) as cm:
            self.monitor.setUpdatePeriod(-90)
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid update period')

        after = self.monitor.updatePeriod
        self.assertEqual(before, after, 'Update period shouldn\'t have changed but it did')

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Monitor)
unittest.TextTestRunner(verbosity=2).run(suite)
