# win32wifi - Windows Native Wifi Api Python library.
# Copyright (C) 2016 - Shaked Gitelman
#
# Forked from: PyWiWi - <https://github.com/6e726d/PyWiWi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Andres Blanco     (6e726d)    <6e726d@gmail.com>
# Author: Shaked Gitelman   (almondg)   <shaked.dev@gmail.com>
#

import sys

sys.path.append('../')

from win32wifi.Win32Wifi import  getWirelessInterfaces, getWirelessNetworkBssList
#from win32wifi import getWirelessNetworkBssList

if __name__ == "__main__":
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        print(iface)
        guid = iface.guid
        bsss = getWirelessNetworkBssList(iface)
        print()
        for bss in bsss:
            print(bss)
            print("-" * 20)
        print()
