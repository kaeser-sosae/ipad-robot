import serial, time
from pydexarm import Dexarm
import requests
import os
import functions

dexarm = Dexarm("/dev/ttyACM0")






print(functions.add_device_to_static_group("F9GDNCVTQ1GC", "Tier 1 Software That Needs Configuring"))







# Go home
print('Going back home...')
go_home()

print('Script finished')