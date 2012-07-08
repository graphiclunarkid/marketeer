import unittest
import monitor
import test_monitor
import bullionvaultmonitor

class Test_BullionVaultMonitor(unittest.TestCase):

    def setUp(self):

        self.updatePeriod = 60
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )
        self.invalidCurrency = '123'
        self.invalidMarket = '456'

    def test_monitorAttributes(self):

        validMonitors = set()

        for i in self.validCurrencies:

            for j in self.validMarkets:

                validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

        monitor = validMonitors.pop()

        while (len(validMonitors) > 0):

            monitor.offer = 32500
            monitor.bid = 32450
            self.assertGreaterEqual(monitor.spread, 0, 'Spread is negative')

            monitor = validMonitors.pop()

    def test_invalidMonitors(self):

        with self.assertRaises(monitor.MonitorError) as cm:

            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.invalidCurrency, self.validMarkets[0])

        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid currency')

        with self.assertRaises(monitor.MonitorError) as cm:

            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.validCurrencies[0], self.invalidMarket)

        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid market')


suite = unittest.TestLoader().loadTestsFromTestCase(Test_BullionVaultMonitor)
unittest.TextTestRunner(verbosity=2).run(suite)
