=====
Usage
=====

To use marketeer on the command line::

    python3 marketeer.bullionvaultmonitor.py [-h] [-t] [-s SAVE] [-q] [-c CURRENCY]

    Monitor BullionVault Exchange

    optional arguments:
      -h, --help            show this help message and exit
      -t, --test            Get and display the current price twice (ignores -q)
      -s SAVE, --save SAVE  Save the price to <SAVE>
      -q, --quiet           Do not display the price
      -c CURRENCY, --currency CURRENCY
                            Currency in which to retrieve price

To use marketeer in a project::

    import marketeer
