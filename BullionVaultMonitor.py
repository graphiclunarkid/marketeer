class BullionVaultMonitor():
    def __init__(self):
        self.currency = "GBP"
        self.market = "AUXZU"
        self.ask = 32490
        self.bid = 32410
        self.spread = self.ask - self.bid
