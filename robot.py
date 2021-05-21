import serial, time
from pydexarm import Dexarm

dexarm = Dexarm("/dev/ttyACM0")

# CONSTANTS
# Home button location = X126 Y252
# Home button pressed X126 Y252 Z56
# Z off screen travel height Z-48
# Arm out of the way = X-226 Y0 Z6
# Button pressed location = X-136 Y326 Z-106 (press down from X-148)

# def press_letter(letter):
# 	print('Typing letter ' + letter)
# 	if (letter == "a"):
# 		goto(-66,348,True)
# 	if (letter == "b"):
# 		goto(-75,285,True)
# 	if (letter == "c"):
# 		goto(-75,315,True)
# 	if (letter == "d"):
# 		goto(-63,321,True)
# 	if (letter == "e"):
# 		goto(-51,327,True)		
# 	if (letter == "f"):
# 		goto(-63,306,True)
# 	if (letter == "g"):
# 		goto(-63,291,True)
# 	if (letter == "h"):
# 		goto(-60,279,True)
# 	if (letter == "i"):
# 		goto(-51,258,True)
# 	# if (letter == "j"):
# 	# 	goto(-72,261,True)	
# 	if (letter == "k"):
# 		goto(-60,252,True)
# 	if (letter == "l"):
# 		goto(-60,237,True)
# 	if (letter == "m"):
# 		goto(-72,261,True)
# 	# if (letter == "n"):
# 	# 	goto(-48,231,True)
# 	if (letter == "o"):
# 		goto(-48,243,True)
# 	if (letter == "p"):
# 		goto(-48,228,True)
# 	if (letter == "q"):
# 		goto(-54,357,True)
# 	if (letter == "r"):
# 		goto(-51,312,True)
# 	if (letter == "s"):
# 		goto(-63,339,True)
# 	if (letter == "t"):
# 		goto(-51,300,True)
# 	if (letter == "u"):
# 		goto(-51,270,True)
# 	# if (letter == "v"):
# 	# 	goto(-63,339,True)
# 	if (letter == "w"):
# 		goto(-54,342,True)
# 	# if (letter == "x"):
# 	# 	goto(-63,339,True)
# 	if (letter == "y"):
# 		goto(-51,285,True)
# 	# if (letter == "z"):
# 	# 	goto(-63,339,True)

# 	if (letter == "A"):
# 		goto(-75,354,True)
# 		goto(-66,348,True)
# 	if (letter == "B"):
# 		goto(-75,354,True)
# 		goto(-75,285,True)
# 	if (letter == "C"):
# 		goto(-75,354,True)
# 		goto(-75,315,True)
# 	if (letter == "D"):
# 		goto(-75,354,True)
# 		goto(-63,321,True)
# 	if (letter == "E"):
# 		goto(-75,354,True)
# 		goto(-51,327,True)	
# 	if (letter == "F"):
# 		goto(-75,354,True)
# 		goto(-63,306,True)
# 	if (letter == "G"):
# 		goto(-75,354,True)
# 		goto(-63,291,True)
# 	if (letter == "H"):
# 		goto(-75,354,True)
# 		goto(-60,279,True)
# 	if (letter == "I"):
# 		goto(-75,354,True)
# 		goto(-51,258,True)
# 	# if (letter == "J"):
# 	#	goto(-75,354,True)
# 	# 	goto(-72,261,True)	
# 	if (letter == "K"):
# 		goto(-75,354,True)
# 		goto(-60,252,True)
# 	if (letter == "L"):
# 		goto(-75,354,True)
# 		goto(-60,237,True)
# 	if (letter == "M"):
# 		goto(-75,354,True)
# 		goto(-72,261,True)
# 	# if (letter == "N"):
# 	#	goto(-75,354,True)
# 	# 	goto(-48,231,True)
# 	if (letter == "O"):
# 		goto(-75,354,True)
# 		goto(-48,243,True)
# 	if (letter == "P"):
# 		goto(-75,354,True)
# 		goto(-48,228,True)
# 	if (letter == "Q"):
# 		goto(-75,354,True)
# 		goto(-54,357,True)
# 	if (letter == "R"):
# 		goto(-75,354,True)
# 		goto(-51,312,True)
# 	if (letter == "S"):
# 		goto(-75,354,True)
# 		goto(-63,339,True)
# 	if (letter == "T"):
# 		goto(-75,354,True)
# 		goto(-51,300,True)
# 	if (letter == "U"):
# 		goto(-75,354,True)
# 		goto(-51,270,True)
# 	# if (letter == "V"):
# 	#	goto(-75,354,True)
# 	# 	goto(-63,339,True)
# 	if (letter == "W"):
# 		goto(-75,354,True)
# 		goto(-54,342,True)
# 	# if (letter == "X"):
# 	#	goto(-75,354,True)
# 	# 	goto(-63,339,True)
# 	if (letter == "Y"):
# 		goto(-75,354,True)
# 		goto(-51,285,True)
# 	# if (letter == "Z"):
# 	#	goto(-75,354,True)
# 	# 	goto(-63,339,True)


# 	if (letter == "-"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-75,327,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "1"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-51,357,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "2"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-51,342,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "3"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-51,327,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "4"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-51,312,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "9"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-48,246,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)
# 	if (letter == "8"):
# 		goto(-90,357,True)
# 		time.sleep(1)
# 		goto(-48,258,True)
# 		time.sleep(1)
# 		goto(-90,357,True)
# 		time.sleep(1)

# 	if (letter == "nums"):
# 		goto(-90,357,True)
# 	if (letter == "left_shift"):
# 		goto(-78,357,True)		

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
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -20, 5000)
		dexarm.fast_move_to(get_current_location('x'), 326, get_current_location('z'), 5000)
		dexarm.fast_move_to(-148, get_current_location('y'), get_current_location('z'), 5000)
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -106, 5000)
		dexarm.fast_move_to(-136, get_current_location('y'), get_current_location('z'), 5000)
		dexarm._send_cmd("G4 S" + str(seconds) + "\n")
		dexarm.fast_move_to(-148, get_current_location('y'), get_current_location('z'), 5000)
		dexarm.fast_move_to(get_current_location('x'), get_current_location('y'), -20, 5000)

# def type_word(word):
#         print('Typing word ' + word)
#         for char in word[ : : 1]:
#                 press_letter(char)

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
dexarm.fast_move_to(-14, 256, -52, 5000)
dexarm.fast_move_to(-14, 256, -40, 5000)
dexarm._send_cmd("G4 S1\n")

# Go home
print('Going back home...')
go_home()

print('Script finished')