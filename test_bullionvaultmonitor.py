import unittest
import monitor
import bullionvaultmonitor

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.updatePeriod = 60
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )

    def test_monitorAttributes(self):

        validMonitors = set()

        for i in self.validCurrencies:

            for j in self.validMarkets:

                validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

        monitor = validMonitors.pop()

        while (len(validMonitors) > 0):

#            monitor.offer = 32500
#            monitor.bid = 32450
            self.assertGreaterEqual(monitor.spread, 0, 'Spread is negative')

            monitor = validMonitors.pop()


suite = unittest.TestLoader().loadTestsFromTestCase(Test_BullionVaultMonitor)
unittest.TextTestRunner(verbosity=2).run(suite)
