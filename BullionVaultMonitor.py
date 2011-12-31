class BullionVaultMonitor():
    def __init__(self, currency, market):
        self.currency = currency
        self.market = market
        self.ask = 32490
        self.bid = 32410
        self.spread = self.ask - self.bid

    def dispose(self):
        pass
