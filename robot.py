import serial, time
from pydexarm import Dexarm
import requests
import os
import functions

dexarm = Dexarm("/dev/ttyACM0")

main_username = "simp9998"
main_password = ""
serial_number = ""

# Get the password
while main_password == "":
	print('get_password(' + main_username + ') is blank...')
	main_password = functions.get_password(main_username)
	functions.pause(100)

print('Got the password!')

# Go home
print('Moving arm to home position...')
dexarm.go_home()

# Get encoder position
home_encoder_position = dexarm.get_encoder_position()

# Press power button for 3 seconds
print('Pressing power button...')
functions.press_power_button(3)

# Go to middle of screen and wait 13 seconds to take picture
print('Waiting for iPad to boot...')
dexarm.fast_move_to(0,274,-12, 10000)
dexarm._send_cmd("G4 S13\n")

# If the word English is found, continue, if not, wait 5 seconds
# Move arm to 0,300,-12
print("Looking for the word 'english'")
dexarm.fast_move_to(0,300,-12, 10000)
cont = True
have_i_waited_once = False
while cont:
	for returned_strings in functions.get_ocr_text({"areas":[{"x1":587,"x2":960,"y1":842,"y2":960,"rotate":180}]}):
		print('Returned strings: ' + returned_strings)
		if "English" in returned_strings:
			print('Found English on screen')
			# Proceed with the script, no need to hit home button
			cont = False
			break
		# Didn't find English in the string
		else:
			print('Did not find English on screen')
			print('have_i_waited_once=' + str(have_i_waited_once))
			# Pause for 5 seconds
			dexarm._send_cmd("G4 S5\n")
			if have_i_waited_once == True:
				print('have_i_waited_once is True! Pressing the home button!')
				# Press the home button, then move on with the script
				functions.press_home_button()		
				dexarm._send_cmd("G4 S1\n")		
				cont = False
				break
			have_i_waited_once = True

# Press on English
print('Pressing on english')
functions.screen_tap(2, 282)

# Look for the word "Australia"
# Send arm to 48,272,-12
# Crop photo to {"x1": 862, "x2": 1308, "y1": 541, "y2": 710, "rotate": 170}
print("Looking for the word 'Australia'")
dexarm.fast_move_to(48,272,-12, 10000)
while "Australia" not in functions.get_single_string(862,1308,541,710,170):
	pass

# Press on Australia = 4,252
print('Pressing on Australia')
functions.screen_tap(22,290)

# Look for the word "Manually"
# Send arm to 112,298,-12
# Crop photo to {"x1": 895, "x2": 1380, "y1": 683, "y2": 820, "rotate": 159}
print("Looking for the word 'Manually'")
dexarm.fast_move_to(112,298,-12, 10000)
while "Manually" not in functions.get_single_string(895,1380,683,820,159):
	pass

# Press Set up manually = 72,252
print('Pressing on Set Up Manually')
functions.screen_tap(90,280)

# Pause 2 seconds
#dexarm._send_cmd("G4 S2\n")

connected_to_correct_wifi = False

while connected_to_correct_wifi == False:

	# Search for the Lindisfarne Wifi Network
	print("Looking for the word 'Lindisfarne'")
	# move arm to 70, 280, -12
	dexarm.fast_move_to(70,280,-12, 10000)

	# Pause 1 second
	dexarm._send_cmd("G4 S1\n")

	cont = True
	row_number = 0
	x = 1
	while cont:
		print('Taking picture and checking for Lindisfarne...')
		for returned_strings in get_ocr_text({"areas":[
			{"x1":868,"x2":1729,"y1":183,"y2":303,"rotate":166}, # 183,303
			{"x1":868,"x2":1729,"y1":371,"y2":488,"rotate":166}, # 371,488
			{"x1":868,"x2":1729,"y1":539,"y2":662,"rotate":166}, # 539,662
			{"x1":868,"x2":1729,"y1":715,"y2":840,"rotate":166}, # 715,840
			{"x1":868,"x2":1729,"y1":889,"y2":1010,"rotate":166}, # 889,1010
			{"x1":868,"x2":1729,"y1":1066,"y2":1191,"rotate":166}, # 1066,1191
			{"x1":868,"x2":1729,"y1":1244,"y2":1360,"rotate":166} # 868,1729,1244,1360

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

	# Check that we pressed the correct wifi network
	# If the word lindisfarne is not found, press the back button
	# Move arm to -68,348,-12
	print('Checking that we pressed the right Wifi network')
	dexarm.fast_move_to(-68,348,-12, 10000)
	
	# Pause 4 seconds
	dexarm._send_cmd("G4 S4\n")

	print("Looking for the word 'Lindisfarne'")
	cont = True
	while cont:
		for returned_strings in get_ocr_text({"areas":[{"x1":110,"x2":900,"y1":560,"y2":650,"rotate":191}]}):
		#for returned_strings in get_ocr_text({"areas":[{"x1":587,"x2":960,"y1":842,"y2":960,"rotate":180}]}):
			print('Returned strings: ' + returned_strings)
			if "Lindisfarne" not in returned_strings:
				screen_tap(-66,230)
				# Pause 2 seconds
				dexarm._send_cmd("G4 S2\n")
				# Proceed
				cont = False
			else:
				cont = False
				connected_to_correct_wifi = True

# Type username
functions.type_word(main_username)

# Press the Next button
functions.screen_tap(94,342)

# Type password
functions.type_word(main_password)

# Press the join button
# 96,342
functions.screen_tap(96,342)

# Look for the word "lindisfarne"
# Send arm to 0,300,-12
# Crop photo to 710, 1460, 555, 640, 180
print("Looking for the word 'lindisfarne'")
dexarm.fast_move_to(0,300,-12, 10000)
while "lindisfarne" not in functions.get_single_string(710,1460,555,640,180):
	pass

# Press the Trust button
# -40 318
functions.screen_tap(-40,318)

# Look for the word "Transfer"
# Send arm to 74,300,-12
# Crop photo to 541, 1200, 720, 811, 166
print("Looking for the word 'Transfer'")
dexarm.fast_move_to(74,300,-12, 10000)
while "Transfer" not in functions.get_single_string(541,1200,720,811,166):
	pass

# Press on the Don't Transfer option
functions.screen_tap(54,300)

# Look for the word "Next"
# Send arm to -52,364,-12
# Crop photo to {"x1": 934, "x2": 1130, "y1": 715, "y2": 804, "rotate": 188}
print("Looking for the word 'Next'")
dexarm.fast_move_to(-52,364,-12, 10000)
while "Next" not in functions.get_single_string(934,1130,715,804,188):
	pass

# Press Next
print('Pressing next')
functions.screen_tap(-52,326)

# Type username
functions.type_word(main_username)

# Press the return key
functions.screen_tap(96,344)

# Type password
functions.type_word(main_password)

# Press Next
functions.screen_tap(-82,326)


# Look for the word "password"
# Send arm to 42,312,-12
# Crop photo to {"x1": 408, "x2": 1640, "y1": 872, "y2": 1016, "rotate": 172}
print("Looking for the word 'password'")
dexarm.fast_move_to(42,312,-12, 10000)
while "password" not in functions.get_single_string(408,1640,872,1016,172):
	pass

# Press don't have apple ID
# 44,274
functions.screen_tap(44,274)
functions.pause(1000)

# Press setup later in settings
# 4,274
functions.screen_tap(4,274)
functions.pause(1000)

# Press Don't use
# 36, 286
functions.screen_tap(36,286)
functions.pause(1000)

# Press continue
# 78,286
functions.screen_tap(78,286)
functions.pause(1000)

# Press enable location services
# 78,286
functions.screen_tap(78,286)
functions.pause(1000)

# Press Don't share
# 90,276
functions.screen_tap(90,276)
functions.pause(1000)

# Press the settings button
# 44,238
functions.screen_tap(44,238)

# Press about
# -68,290
functions.screen_tap(-68,290)

functions.pause(2000)

# Get the serial number
# Send arm to -12,376,-12
# Crop photo to 730, 1163, 510, 590, 181
print("Looking for the serial number")
dexarm.fast_move_to(-12,376,-12, 10000)
x = 1

# OCR the serial number, and match the usernames by
# making an API call to Jamf Pro Mobile Devices. If
# we find a match, continue with the script.
x = 0
while True:
	serial_number = functions.get_single_string(730,1163,510,590,181,True)
	if x > 2:
		if serial_number == "":
			print('I think the screen is off, pressing the home button twice')
			functions.press_home_button()
			functions.press_home_button()
			print('Moving the arm back into position')
			dexarm.fast_move_to(-12,376,-12, 10000)
	print('Matching serial ' + serial_number + ' to username ' + main_username)
	serial_username = functions.get_jamf_username_from_device_serial(serial_number)
	if serial_username == main_username:
		print('Found a match!')
		break
	else:
		print("Does not match! '" + serial_username + "' does not equal '" + main_username + "'")
	functions.pause(1000)
	x = x + 1

# If we get to here, I am satified that we
# have the correct serial number for the iPad

# Add the iPad to the static group
while functions.add_device_to_static_group(serial_number, "Tier 1 Software That Needs Configuring") == False:
	print('Adding to group failed, trying again')
print('Added to the group')

# Press the home button
functions.press_home_button()

# Turn on Siri
dexarm.fast_move_to(144, 272, functions.get_current_location('z'), 5000)
dexarm.fast_move_to(144, 272, -56, 5000)
functions.pause(1000)
dexarm.fast_move_to(144, 272, -40, 5000)
# Tap on Use Siri
functions.screen_tap(104,272)
# Tap on Voice 2
functions.screen_tap(-4,270)
# Press on Next
functions.screen_tap(-82,332)
# Tap on Not Now
functions.screen_tap(118,272)
# Press the home button
functions.press_home_button()
# Press settings
functions.screen_tap(44,238)
# Press Display and Brightness
functions.screen_tap(94,226)
# Press auto lock
functions.screen_tap(34,298)
# Press Never
functions.screen_tap(-32,298)
# Press Display and brightness
functions.screen_tap(-86,274)
# Press the brightness slider
functions.screen_tap(0,334)
functions.screen_tap(0,334)
functions.screen_tap(0,334)
# Press the home button
functions.press_home_button()

# Wait for the Vivi app to be installed
while functions.does_device_have_app_installed(serial_number, "Vivi") == False:
	print('Vivi not found. Waiting...')
	functions.pause(1000)
	pass

# Drag down the home screen
functions.screen_drag(44,64,300,300)

# Search for the Vivi App
functions.type_word("vivi")

# Press go button
functions.screen_tap(96,344)

functions.pause(1000)

# type word lindis
functions.type_word("lindis")

# Tap the lindisfarne button
functions.screen_tap(-38,278)

# Tap the login button
functions.screen_tap(-30,278)

# Type username
functions.type_word(main_username)

# Tap in the password box
functions.screen_tap(-62,244)
functions.screen_tap(-62,244)
functions.screen_tap(-62,244)

# Type password
functions.type_word(main_password)

# Press the return key
functions.screen_tap(96,344)

if int(functions.get_student_yearlevel(main_username)) > 4:
	# Press Mahers Lane button
	functions.screen_tap(-36,266)
else:
	# Press Sunshine Avenue button
	functions.screen_tap(-24,266)

# Press home button
functions.press_home_button()














# Go home
print('Going back home...')
go_home()

print('Script finished')