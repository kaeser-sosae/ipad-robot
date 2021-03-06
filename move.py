import serial, time, sys
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

print('Current pos = ' + str(dexarm.get_current_position()))
print('Encoder pos = ' + str(dexarm.get_encoder_position()))
print(' ')
dexarm.fast_move_to(x, y, z)
time.sleep(5)
print('Moved to X' + x + ' Y' + y + ' Z' + z)
print(' ')
print('New Current pos = ' + str(dexarm.get_current_position()))
print('New Encoder pos = ' + str(dexarm.get_encoder_position()))

