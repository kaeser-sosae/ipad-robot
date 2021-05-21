import serial, time
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

# CONSTANTS
# Home button location = X128 Y300
# Home button pressed X128 Y300 Z56
# Z off screen travel height Z-48
# Arm out of the way = X-226 Y0 Z6
# Shift button = 128,208
# Power button press = -106,348,-102


letter_locations = {
	"a":[(103,208)],
	"b":[(111,270)],
	"c":[(113,244)],
	"d":[(99,236)],
	"e":[(87,232)],
	"f":[(99,250)],
	"g":[(99,264)],
	"h":[(97,278)],
	"i":[(81,302)],
	"j":[(97,292)],
	"k":[(175,306)],
	"l":[(95,318)],
	"m":[(109,298)],
	"n":[(109,284)],
	"o":[(81,314)],
	"p":[(81,328)],
	"q":[(87,202)],
	"r":[(85,246)],
	"s":[(99,222)],
	"t":[(85,260)],
	"u":[(83,288)],
	"v":[(111,256)],
	"w":[(87,218)],
	"x":[(113,228)],
	"y":[(83,274)],
	"z":[(115,214)]
}

def press_letter(letter):
	print('Typing letter ' + letter)

	for tap in letter_locations[letter]:
		screen_tap(tap[0], tap[1])

def get_current_location(axis):
	all_coords = dexarm.get_current_position()
	ret_value = ''
	x = all_coords[0]
	y = all_coords[1]
	z = all_coords[2]
	if axis == "x":
		ret_value = x
	if axis == "y":
		ret_value = y
	if axis == "z":
		ret_value = z
	return ret_value

def go_home():
		print('Going home...')
		dexarm.fast_move_to(-226, 0, 6, 5000)

def press_home_button():
		print('Pressing home button...')
		dexarm.fast_move_to(126, 252, get_current_location('z'), 5000)
		dexarm.fast_move_to(126, 252, -56, 5000)
		dexarm.fast_move_to(126, 252, -48, 5000)


def press_power_button(seconds):
		# Set the Z to -20
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -20, 5000)
		# Move to the XY
		dexarm.fast_move_to(-128, 344, get_current_location('z'), 5000)
		# Plunge the Z into position
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -84, 5000)
		# Increase the X to press the button
		dexarm.fast_move_to(-118, get_current_location('y'), get_current_location('z'), 5000)
		# Hold for as long as we need
		dexarm._send_cmd("G4 S" + str(seconds) + "\n")
		# Reduce X to stop pressing the button
		dexarm.fast_move_to(-128, get_current_location('y'), get_current_location('z'), 5000)
		# Pull out the Z to -20 and move on
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -20, 5000)
		dexarm.go_home()

def screen_tap(x, y):
	#dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -20, 5000)
	dexarm.fast_move_to(x, y, get_current_location('z'), 10000)
	#dexarm.fast_move_to(x, y, -44, 10000)
	dexarm.fast_move_to(x, y, -54, 2000)
	dexarm._send_cmd("G4 P300\n")
	dexarm.fast_move_to(x, y, -44, 2000)
	dexarm._send_cmd("G4 S1\n")

def type_word(word):
	print('Typing word ' + word)
	for char in word[ : : 1]:
		press_letter(char)

# Go home
print('Moving arm to home position...')
dexarm.go_home()

# Get encoder position
home_encoder_position = dexarm.get_encoder_position()

# Press power button for 2 seconds
print('Pressing power button...')
press_power_button(2)

# Wait 15 seconds after button is pressed, then press the home button once
print('Waiting for iPad to boot...')
dexarm._send_cmd("G4 S15\n")

#Press on English
screen_tap(2, 282)

# Press on Australia = 4,252
screen_tap(20,262)

# Pause 4 seconds
dexarm._send_cmd("G4 S5\n")

# Press Set up manually = 72,252
screen_tap(90,280)

# Press on Lindisfarne = 72,252
screen_tap(90,280)

# Type username
type_word("gavin.kennedy")

# Press in password box = -56,252

























# Go home
print('Going back home...')
go_home()

print('Script finished')