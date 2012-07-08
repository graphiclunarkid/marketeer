import unittest
import monitor
import test_monitor
import bullionvaultmonitor

class Test_BullionVaultMonitor(test_monitor.Test_Monitor):

    def setUp(self):

        self.updatePeriod = 60
        self.validCurrencies = list( ['EUR','GBP','USD'] )
        self.validMarkets = list( ['AUXLN','AUXNY','AUXZU'] )
        self.invalidCurrency = '123'
        self.invalidMarket = '456'
        self.validMonitors = set()

        for i in self.validCurrencies:
            for j in self.validMarkets:
                self.validMonitors.add(bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod,i,j))

        self.monitor = self.validMonitors.pop()

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
