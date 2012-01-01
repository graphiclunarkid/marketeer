class BullionVaultMonitor():

    def __init__(self, currency, market):

        self.offer = 32490
        self.bid = 32410
        self.spread = self.offer - self.bid

        self.currency = currency
        self.market = market

        ''' Blank = monitor all markets / currencies '''
        self.validCurrencies = frozenset( ['EUR','GBP','USD',''] )
        self.validMarkets = frozenset( ['AUXLN','AUXNY','AUXZU',''] )

        if self.currency not in self.validCurrencies:
            raise InitError('Invalid currency')

        if self.market not in self.validMarkets:
            raise InitError('Invalid market')


class Error(Exception):
    ''' Base class for exceptions in this module '''
    pass


class InitError(Error):
    ''' Exception thrown by the constructor '''
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


