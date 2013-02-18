#!/usr/bin/python

# Copyright 2013 Richard King
#
# This file is part of Marketeer.
#
# Marketeer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Marketeer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Marketeer.  If not, see <http://www.gnu.org/licenses/>.

class MtgoxMonitor():
    '''
    Class to monitor market prices at MtGox
    '''

    def __init__(self, updatePeriod=30):
        self.updatePeriod = updatePeriod

    def _update(self):

        self._bid = 20
        self._offer = 22

    def get_bid(self):

        self._update()
        return self._bid

    bid = property(get_bid)

    def get_offer(self):

        self._update()
        return self._offer

    offer = property(get_offer)

    def get_spread(self):

        self._update()
        return self._offer - self._bid

    spread = property(get_spread)


