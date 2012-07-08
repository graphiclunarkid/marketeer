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
        
    def test_monitorAttributes(self):

        while (len(self.validMonitors) > 0):
            self.assertGreater(self.monitor.bid, 0, 'Bid price is zero or negative')
            self.assertGreater(self.monitor.offer, 0, 'Offer price is zero or negative')
            self.assertGreaterEqual(self.monitor.spread, 0, 'Spread is negative')

            self.monitor = self.validMonitors.pop()


suite = unittest.TestLoader().loadTestsFromTestCase(Test_Monitor)
unittest.TextTestRunner(verbosity=2).run(suite)
