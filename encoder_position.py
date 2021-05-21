import serial, time
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")




while True:
	print(dexarm.get_encoder_position())
	sleep(.1)

