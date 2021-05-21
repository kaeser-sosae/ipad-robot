import serial, time
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

# CONSTANTS
# Home button location = X128 Y300
# Home button pressed X128 Y300 Z56
# Z off screen travel height Z-48
# Arm out of the way = X-226 Y0 Z6
# Shift button = 118,200
# Special characters button = 132,200
# Special characters alt button = 118,200
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
	"k":[(96,306)],
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
	"z":[(115,214)],
	"A":[(118,200),(103,208)],
	"B":[(118,200),(111,270)],
	"C":[(118,200),(113,244)],
	"D":[(118,200),(99,236)],
	"E":[(118,200),(87,232)],
	"F":[(118,200),(99,250)],
	"G":[(118,200),(99,264)],
	"H":[(118,200),(97,278)],
	"I":[(118,200),(81,302)],
	"J":[(118,200),(97,292)],
	"K":[(118,200),(96,306)],
	"L":[(118,200),(95,318)],
	"M":[(118,200),(109,298)],
	"N":[(118,200),(109,284)],
	"O":[(118,200),(81,314)],
	"P":[(118,200),(81,328)],
	"Q":[(118,200),(87,202)],
	"R":[(118,200),(85,246)],
	"S":[(118,200),(99,222)],
	"T":[(118,200),(85,260)],
	"U":[(118,200),(83,288)],
	"V":[(118,200),(111,256)],
	"W":[(118,200),(87,218)],
	"X":[(118,200),(113,228)],
	"Y":[(118,200),(83,274)],
	"Z":[(118,200),(115,214)],
	"1":[(132,200),(90,202),(132,200)],
	"2":[(132,200),(90,216),(132,200)],
	"3":[(132,200),(90,230),(132,200)],
	"4":[(132,200),(88,244),(132,200)],
	"5":[(132,200),(88,260),(132,200)],
	"6":[(132,200),(88,274),(132,200)],
	"7":[(132,200),(86,288),(132,200)],
	"8":[(132,200),(86,302),(132,200)],
	"9":[(132,200),(84,316),(132,200)],
	"0":[(132,200),(84,330),(132,200)],
	"@":[(132,200),(104,208),(132,200)],
	"#":[(132,200),(102,222),(132,200)],
	"$":[(132,200),(102,236),(132,200)],
	"&":[(132,200),(102,250),(132,200)],
	"*":[(132,200),(100,264),(132,200)],
	"(":[(132,200),(100,278),(132,200)],
	")":[(132,200),(98,292),(132,200)],
	"%":[(132,200),(116,214),(132,200)],
	"-":[(132,200),(116,230),(132,200)],
	"+":[(132,200),(114,244),(132,200)],
	"=":[(132,200),(114,258),(132,200)],
	",":[(132,200),(110,314),(132,200)],
	".":[(132,200),(112,328),(132,200)],
	"_":[(132,200),(118,200),(100,250),(132,200)]
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
	dexarm.fast_move_to(x, y, get_current_location('z'), 10000)
	dexarm.fast_move_to(x, y, -50, 6000)
	dexarm._send_cmd("G4 P100\n")
	dexarm.fast_move_to(x, y, -35, 6000)

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

# Go to middle of screen and wait
dexarm.fast_move_to(0,274,-44, 10000)

# Wait 15 seconds after button is pressed, then press the home button once
print('Waiting for iPad to boot...')
dexarm._send_cmd("G4 S20\n")

#Press on English
screen_tap(2, 282)

# Press on Australia = 4,252
screen_tap(22,290)

# Pause 2 seconds
dexarm._send_cmd("G4 S2\n")

# Press Set up manually = 72,252
screen_tap(90,280)

# Pause 2 seconds
dexarm._send_cmd("G4 S2\n")

# Press on Lindisfarne = 72,252
screen_tap(90,280)

# Type username
type_word("gavin.kEnnedy_Anthony-gerke&")

# Press in password box = -56,252

























# Go home
print('Going back home...')
go_home()

print('Script finished')