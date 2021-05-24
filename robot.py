import serial, time
from pydexarm import Dexarm
import requests

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
# Z height for best photo = -12
# Row arm xy press coordinates
	# 1st row = 12, 280
	# 2nd row = 24, 280
	# 3rd row = 38, 280
	# 4th row = 52, 280
	# 5th row = 64, 280
	# 6th row = 76, 280
	# 7th row = 88, 280
# Row image xy coordinates (x1, x2, y1, y2, rotation)
# Arm is at position 62, 300, -12
	# 1st row = 652, 1445, 261, 348, 168
	# 2nd row = 652, 1445, 439, 531, 168
	# 3rd row = 652, 1445, 609, 703, 168
	# 4th row = 652, 1445, 786, 877, 168
	# 5th row = 652, 1445, 962, 1050, 168
	# 6th row = 652, 1445, 1132, 1238, 168
	# 7th row = 652, 1445, 1320, 1440, 168

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
	dexarm.fast_move_to(x, y, -55, 7000)
	#dexarm._send_cmd("G4 P100\n")
	dexarm.fast_move_to(x, y, -35, 7000)

def type_word(word):
	print('Typing word ' + word)
	for char in word[ : : 1]:
		press_letter(char)

def get_ocr_text(dict_coords):

	#print('Taking a picture at x: ' + str(arm_x) + " y:" + str(arm_y))

	#Move camera to good location for taking pictures
	#dexarm.fast_move_to(arm_x, arm_y, -12, 7000)
	
	#Set up the API call
	parameters = {
		"url": "http://10.151.3.184/ocr",
		"json": dict_coords
	}
	
	#Get the response code
	response = requests.get(**parameters)

	data = {}

	#If response is 200, then get the data in JSON and assign to the "data" variable
	if response.status_code == 200:
		try:
			data = response.json()
		except:
			return [""]

	#If response isn't 200, then return blank string
	else:
		# function failed
		return [""]

	# return the list of strings ("data variable")
	return data["strings"]

# Go home
print('Moving arm to home position...')
dexarm.go_home()

# Get encoder position
home_encoder_position = dexarm.get_encoder_position()

# Press power button for 3 seconds
print('Pressing power button...')
press_power_button(3)

# Go to middle of screen and wait 20 seconds to take picture
print('Waiting for iPad to boot...')
dexarm.fast_move_to(0,274,-12, 10000)
dexarm._send_cmd("G4 S20\n")

#If the word English is found, continue, if not, wait 5 seconds
# Move arm to 0,300,-12
dexarm.fast_move_to(0,300,-12, 10000)
print("Looking for the word 'english'")
cont = True
while cont:
	have_i_waited_once = False
	for returned_strings in get_ocr_text({"areas":[{"x1":587,"x2":960,"y1":842,"y2":960,"rotate":180}]}):
		if "English" in returned_strings:
			# Proceed
			cont = False
		# not english	
		else:
			# Press the home button
			dexarm._send_cmd("G4 S5\n")
			if have_i_waited_once == False:
				cont = False
			have_i_waited_once = True


#Press on English
print('Pressing on english')
screen_tap(2, 282)

# Press on Australia = 4,252
print('Pressing on Australia')
screen_tap(22,290)

# Pause 5 seconds
dexarm._send_cmd("G4 S5\n")

# Press Set up manually = 72,252
print('Pressing on Set Up Manually')
screen_tap(90,280)

# Pause 2 seconds
dexarm._send_cmd("G4 S2\n")

# Search for the Lindisfarne Wifi Network
print("Looking for the word 'Lindisfarne'")
# move arm to 62, 300, -12
dexarm.fast_move_to(62,300,-12, 10000)

# Pause 2 seconds
dexarm._send_cmd("G4 S2\n")

cont = True
row_number = 0
x = 1
while cont:
	print('Taking picture and checking for Lindisfarne...')
	for returned_strings in get_ocr_text({"areas":[
		{"x1":652,"x2":1445,"y1":261,"y2":348,"rotate":168},
		{"x1":652,"x2":1445,"y1":439,"y2":531,"rotate":168},
		{"x1":652,"x2":1445,"y1":609,"y2":703,"rotate":168},
		{"x1":652,"x2":1445,"y1":786,"y2":877,"rotate":168},
		{"x1":652,"x2":1445,"y1":962,"y2":1050,"rotate":168},
		{"x1":652,"x2":1445,"y1":1132,"y2":1238,"rotate":168},
		{"x1":652,"x2":1445,"y1":1320,"y2":1440,"rotate":168}
		]}):
		print('Returned string: ' + returned_strings)
		if "Lindisfarne" in returned_strings:
			# Proceed
			cont = False
			row_number = x
			break
		x = x + 1
	time.sleep(.5)

# Go home
print('Moving arm to home position...')
dexarm.go_home()	

# Press the appropriate row
if row_number == 1:
	print('Row number is 1')
	screen_tap(12,280)
if row_number == 2:
	print('Row number is 2')
	screen_tap(24,280)
if row_number == 3:
	print('Row number is 3')
	screen_tap(38,280)
if row_number == 4:
	print('Row number is 4')
	screen_tap(52,280)
if row_number == 5:
	print('Row number is 5')
	screen_tap(64,280)
if row_number == 6:
	print('Row number is 6')
	screen_tap(76,280)
if row_number == 7:
	print('Row number is 7')
	screen_tap(88,280)

# Pause 2 seconds
dexarm._send_cmd("G4 S2\n")

# Type username
type_word("simp9998")

# Pause 1 second
dexarm._send_cmd("G4 S1\n")

# Press in password box = -56,252
screen_tap(-56,252)

# Type password
type_word("El-barto-graffiti")

























# Go home
print('Going back home...')
go_home()

print('Script finished')