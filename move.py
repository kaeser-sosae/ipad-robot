import serial, time, sys
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

x = sys.argv[0]
y = sys.argv[1]
z = sys.argv[2]

print('Current pos = ' + str(dexarm.get_current_position()))
print('Encoder pos = ' + str(dexarm.get_encoder_position()))
print(' ')
print('Moved to X' + x + ' Y' + y + ' Z' + z)
print(' ')
print('New Current pos = ' + str(dexarm.get_current_position()))
print('New Encoder pos = ' + str(dexarm.get_encoder_position()))

