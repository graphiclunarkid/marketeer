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

    def tearDown(self):

        self.validMonitors.clear()
        self.validMonitors = None
        self.monitors = None

    def test_getMonitorAttributes(self):

        self.monitors = self.validMonitors.copy()

        while len(self.monitors) > 0:

            self.monitor = self.monitors.pop()
            test_monitor.Test_Monitor.test_getMonitorAttributes(self)
        
    def test_invalidMonitors(self):

        with self.assertRaises(monitor.InitError) as cm:
            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.invalidCurrency, self.validMarkets[0])
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid currency')

        with self.assertRaises(monitor.InitError) as cm:
            self.monitor = bullionvaultmonitor.BullionVaultMonitor(self.updatePeriod, self.validCurrencies[0], self.invalidMarket)
        exception = cm.exception
        self.assertEqual(exception.message, 'Invalid market')

        
if __name__ == '__main__':
    unittest.main()
