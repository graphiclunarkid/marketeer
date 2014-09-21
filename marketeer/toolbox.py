# -*- coding: utf-8 -*-

# Copyright (C) 2013 - see the README file for a list of authors
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
#
# The openAnything function was derived from Dive Into Python
# (http://www.diveintopython.net/) which is copyright 2000, 2001, 2002, 2003,
# 2004 Mark Pilgrim (josh@servercobra.com). It is included here under the terms
# of the Python license (http://www.diveintopython.net/appendix/license.html)


def openAnything(source):

    if hasattr(source, "read"):
        return source

    if source == '-':
        import sys
        return sys.stdin

    # try to open with urllib (if source is http, ftp, or file URL)
    import urllib.request
    import urllib.parse
    import urllib.error
    try:
        return urllib.request.urlopen(source)
    except (ValueError, IOError, OSError):
        pass

    # try to open with native open function (if source is pathname)
    try:
        return open(source)
    except (IOError, OSError):
        pass

    # treat source as string
    import io
    return io.StringIO(str(source))


def printGplNoX():

    print("Marketeer Copyright (C) 2013, 2014")
    print("See the README file for a list of authors.")
    print("")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it \
          under certain conditions.")
    print("See the LICENSE file for details.")
    print("")
