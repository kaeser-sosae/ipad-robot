import serial, time, sys
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

print('Current pos = ' + str(dexarm.get_current_position()))
print('Encoder pos = ' + str(dexarm.get_encoder_position()))
print(' ')
dexarm.go_home()
time.sleep(10)
print('New Current pos = ' + str(dexarm.get_current_position()))
print('New Encoder pos = ' + str(dexarm.get_encoder_position()))

