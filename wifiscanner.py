#!/usr/bin/python

import iwlist

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



content = iwlist.scan(interface='wlp2s0')
cells = iwlist.parse(content)
print 'ssid', 'level', 'mac', 'freq'
for cell in cells:
    ssid = cell['essid']
    level = cell['signal_level']
    mac = cell['mac']
    freq = cell['frequency']
    if ssid in ['ServientBackup', 'ServientRadio']:
        print ssid, color.BOLD + level + color.END, mac, freq