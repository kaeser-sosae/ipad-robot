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
	"a":[(116,216)],
	"b":[(124,278)],
	"c":[(126,252)],
	"d":[(112,244)],
	"e":[(100,240)],
	"f":[(112,258)],
	"g":[(112,272)],
	"h":[(110,286)],
	"i":[(94,310)],
	"j":[(110,300)],
	"k":[(188,314)],
	"l":[(108,326)],
	"m":[(122,306)],
	"n":[(122,292)],
	"o":[(94,322)],
	"p":[(94,336)],
	"q":[(100,210)],
	"r":[(98,254)],
	"s":[(112,230)],
	"t":[(98,268)],
	"u":[(96,296)],
	"v":[(124,264)],
	"w":[(100,226)],
	"x":[(126,236)],
	"y":[(96,282)],
	"z":[(128,222)]
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

def screen_tap(x, y):
	dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -40, 5000)
	dexarm.fast_move_to(x, y, -60, 10000)
	dexarm.fast_move_to(x, y, -72, 3000)
	dexarm.fast_move_to(x, y, -60, 10000)
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
screen_tap(12, 282)

# Press on Australia = 4,252
screen_tap(30,282)

# Pause 4 seconds
dexarm._send_cmd("G4 S5\n")

# Press Set up manually = 72,252
screen_tap(102,280)

# Press on Lindisfarne = 72,252
screen_tap(102,280)

# Type username
type_word("gavin.kennedy")

# Press in password box = -56,252

























# Go home
print('Going back home...')
go_home()

print('Script finished')