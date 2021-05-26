import serial, time
from pydexarm import Dexarm
import requests
import os

dexarm = Dexarm("/dev/ttyACM0")

main_username = "simp9998"
main_password = ""
serial_number = ""

# Letter locations are defined as x_start, x_finish, y_start, y_finish
letter_locations = {
	"a":[(103,103,208,208)],
	"b":[(111,111,270,270)],
	"c":[(113,113,244,244)],
	"d":[(99,99,236,236)],
	"e":[(87,87,232,232)],
	"f":[(99,99,250,250)],
	"g":[(99,99,264,264)],
	"h":[(97,97,278,278)],
	"i":[(81,81,302,302)],
	"j":[(97,97,292,292)],
	"k":[(96,96,306,306)],
	"l":[(95,95,318,318)],
	"m":[(109,109,298,298)],
	"n":[(109,109,284,284)],
	"o":[(81,81,314,314)],
	"p":[(81,81,328,328)],
	"q":[(87,87,202,202)],
	"r":[(85,85,246,246)],
	"s":[(99,99,222,222)],
	"t":[(85,85,260,260)],
	"u":[(83,83,288,288)],
	"v":[(111,111,256,256)],
	"w":[(87,87,218,218)],
	"x":[(113,113,228,228)],
	"y":[(83,83,274,274)],
	"z":[(115,115,214,214)],
	"A":[(118,118,200,200),(103,103,208,208)],
	"B":[(118,118,200,200),(111,111,270,270)],
	"C":[(118,118,200,200),(113,113,224,244)],
	"D":[(118,118,200,200),(99,99,236,236)],
	"E":[(118,118,200,200),(87,87,232,232)],
	"F":[(118,118,200,200),(99,99,250,250)],
	"G":[(118,118,200,200),(99,99,264,264)],
	"H":[(118,118,200,200),(97,97,278,278)],
	"I":[(118,118,200,200),(81,81,302,302)],
	"J":[(118,118,200,200),(97,97,292,292)],
	"K":[(118,118,200,200),(96,96,306,306)],
	"L":[(118,118,200,200),(95,95,318,318)],
	"M":[(118,118,200,200),(109,109,298,298)],
	"N":[(118,118,200,200),(109,109,284,284)],
	"O":[(118,118,200,200),(81,81,314,314)],
	"P":[(118,118,200,200),(81,81,328,328)],
	"Q":[(118,118,200,200),(87,87,202,202)],
	"R":[(118,118,200,200),(85,85,246,246)],
	"S":[(118,118,200,200),(99,99,222,222)],
	"T":[(118,118,200,200),(85,85,260,260)],
	"U":[(118,118,200,200),(83,83,288,288)],
	"V":[(118,118,200,200),(111,111,256,256)],
	"W":[(118,118,200,200),(87,87,218,218)],
	"X":[(118,118,200,200),(113,113,228,228)],
	"Y":[(118,118,200,200),(83,83,274,274)],
	"Z":[(118,118,200,200),(115,115,214,214)],
	# "1":[(132,200),(90,202),(132,200)],
	# "2":[(132,200),(90,216),(132,200)],
	# "3":[(132,200),(90,230),(132,200)],
	# "4":[(132,200),(88,244),(132,200)],
	# "5":[(132,200),(88,260),(132,200)],
	# "6":[(132,200),(88,274),(132,200)],
	# "7":[(132,200),(86,288),(132,200)],
	# "8":[(132,200),(86,302),(132,200)],
	# "9":[(132,200),(84,316),(132,200)],
	# "0":[(132,200),(84,330),(132,200)],
	"1":[(87,97,202,202)],
	"2":[(87,97,218,218)],
	"3":[(87,97,232,232)],
	"4":[(85,95,246,246)],
	"5":[(85,95,260,260)],
	"6":[(83,93,274,274)],
	"7":[(83,93,288,288)],
	"8":[(81,91,302,302)],
	"9":[(81,91,314,314)],
	"0":[(81,91,328,328)],

	# "@":[(132,132,200,200),(104,104,208,208),(132,132,200,200)],
	# "#":[(132,132,200,200),(102,102,222,222),(132,132,200,200)],
	# "$":[(132,132,200,200),(102,102,236,236),(132,132,200,200)],
	# "&":[(132,132,200,200),(102,102,250,250),(132,132,200,200)],
	# "*":[(132,132,200,200),(100,100,264,264),(132,132,200,200)],
	# "(":[(132,132,200,200),(100,100,278,278),(132,132,200,200)],
	# ")":[(132,132,200,200),(98,98,292,292),(132,132,200,200)],
	# "%":[(132,132,200,200),(116,116,214,214),(132,132,200,200)],
	# "-":[(132,132,200,200),(116,116,230,230),(132,132,200,200)],
	# "+":[(132,132,200,200),(114,114,244,244),(132,132,200,200)],
	# "=":[(132,132,200,200),(114,114,258,258),(132,132,200,200)],

	"@":[(103,113,208,208)],
	"#":[(99,109,222,222)],
	"$":[(99,109,236,236)],
	"&":[(99,109,250,250)],
	"*":[(99,109,264,264)],
	"(":[(97,107,278,278)],
	")":[(97,107,292,292)],
	"%":[(115,125,214,214)],
	"-":[(113,123,228,228)],
	"+":[(113,123,244,244)],
	"=":[(111,121,256,256)],

	",":[(132,132,200,200),(110,110,314,314),(132,132,200,200)],
	".":[(132,132,200,200),(112,112,328,328),(132,132,200,200)],
	"_":[(132,132,200,200),(118,118,200,200),(100,100,250,250),(132,132,200,200)]
}

def playsound(file):
	os.system("mpg123 " + file)

def get_password(username):

	passwd = ""

	url = "https://credentials.api.lindisfarne.nsw.edu.au/items"

	payload = {
		"username": username
	}

	headers = {
		'Authorization': 'Bearer dfghdjfghjsdlfhgso980sy54890ghysurfhgjshfosiyf97ovsyg4yuoghfsjuhfgjsdfhgsodhfgso9348ygso34hgskoerhgs0e5ygos45hgiushergsy45yhsgtu5hgushrughsoureg',
		'Content-Type': 'application/json'
	}

	response = requests.request("GET", url, headers=headers, json=payload, verify=False)

	response_dict = response.json()

	for entry_id,entry in response_dict.items():
		passwd = entry["password"]
		break

	return passwd

def press_letter(letter):
	for tap in letter_locations[letter]:
		screen_drag(tap[0], tap[1], tap[2], tap[3])

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
		dexarm.fast_move_to(144, 272, get_current_location('z'), 5000)
		dexarm.fast_move_to(144, 272, -56, 5000)
		dexarm.fast_move_to(144, 272, -40, 5000)

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
	# Move above the location
	dexarm.fast_move_to(x, y, get_current_location('z'), 10000)
	# Drop the Z height
	dexarm.fast_move_to(x, y, -53, 10000)
	# Raise the Z height
	dexarm.fast_move_to(x, y, -40, 10000)
	# Tiny pause
	dexarm._send_cmd("G4 P50\n")

def screen_drag(x_start, x_finish, y_start, y_finish):
	# Move above the starting location
	dexarm.fast_move_to(x_start, y_start, get_current_location('z'), 10000)
	# Drop the Z height
	dexarm.fast_move_to(x_start, y_start, -54, 10000)
	# Move to the finish location
	dexarm.fast_move_to(x_finish, y_finish, -54, 10000)
	# Raise the Z height
	dexarm.fast_move_to(x_finish, y_finish, -40, 10000)
	# Tiny pause
	dexarm._send_cmd("G4 P50\n")

def type_word(word):
	print('Typing word ' + word)
	for char in word[ : : 1]:
		press_letter(char)
	dexarm._send_cmd("G4 P50\n")

def get_ocr_text(dict_coords):

	#Set up the API call
	parameters = {
		"url": "http://10.151.3.184/ocr",
		"json": dict_coords
	}
	
	# Play sond
	#playsound("shutter.mp3")

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

def pause(milliseconds):
	dexarm._send_cmd("G4 P" + str(milliseconds) + "\n")

def get_single_string(x1,x2,y1,y2,rotation,is_serial=False):
	if is_serial == True:
		for returned_strings in get_ocr_text({"areas":[{"x1":x1,"x2":x2,"y1":y1,"y2":y2,"rotate":rotation,"whitelist":"0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"}]}):
			if returned_strings != "":
				print('Found string: ' + returned_strings)
				return returned_strings
			else:
				print('Found string: ' + returned_strings)
				return ""
	else:
		for returned_strings in get_ocr_text({"areas":[{"x1":x1,"x2":x2,"y1":y1,"y2":y2,"rotate":rotation}]}):
			if returned_strings != "":
				print('Found string: ' + returned_strings)
				return returned_strings
			else:
				print('Found string: ' + returned_strings)
				return ""

def get_jamf_username_from_device_serial(serial_number):
	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/mobiledevices/serialnumber/" + serial_number

	payload = ""
	headers = {
		'Accept': 'application/json',
		'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0'
	}

	response = requests.request("GET", url, headers=headers, json=payload)

	if response.status_code == 200:
		#print(response.json()["mobile_device"]["location"]["username"])
		return response.json()["mobile_device"]["location"]["username"]

	else:
		print('API call failed with status code ' + str(response.status_code))
		return ""

def get_student_yearlevel(username):
	
	if username == "simp9998":
		return "6"
	else:

		url = "https://query.lindisfarne.nsw.edu.au/query?id=tass-enrolled-students"

		payload = ""
		headers = {
			'Accept': 'application/json',
			'Authorization': 'Bearer LKJHASDJKLhasdlkjAHSDlKJASHdASdkjHWDPOQHdQKWJdhLWKDjhASdkljHASDlkJASHDLKASJdhLKASdhALSDUHYWQPDWQdqwd8790qwd897q6wd*W&dqwdqwdqwed76d9a8s7dt6asdjhgasda(S8dasdashgdaisdaysgtduasgduygas'
		}

		response = requests.request("GET", url, headers=headers, json=payload, verify=False)

		if response.status_code == 200:
			for student in response.json()["results"]:
				if student["student_cafe_username"] == username:
					return student["year_group"]
		else:
			print('API call failed with status code ' + str(response.status_code))
			#return ""


# Get the password
while main_password == "":
	print('get_password(' + main_username + ') is blank...')
	main_password = get_password(main_username)
	pause(100)

print('Got the password!')

# Go home
print('Moving arm to home position...')
dexarm.go_home()

# Get encoder position
home_encoder_position = dexarm.get_encoder_position()

# Press power button for 3 seconds
print('Pressing power button...')
press_power_button(3)

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
	for returned_strings in get_ocr_text({"areas":[{"x1":587,"x2":960,"y1":842,"y2":960,"rotate":180}]}):
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
				press_home_button()		
				dexarm._send_cmd("G4 S1\n")		
				cont = False
				break
			have_i_waited_once = True

# Press on English
print('Pressing on english')
screen_tap(2, 282)

# Look for the word "Australia"
# Send arm to 48,272,-12
# Crop photo to {"x1": 862, "x2": 1308, "y1": 541, "y2": 710, "rotate": 170}
print("Looking for the word 'Australia'")
dexarm.fast_move_to(48,272,-12, 10000)
while "Australia" not in get_single_string(862,1308,541,710,170):
	pass

# Press on Australia = 4,252
print('Pressing on Australia')
screen_tap(22,290)

# Look for the word "Manually"
# Send arm to 112,298,-12
# Crop photo to {"x1": 895, "x2": 1380, "y1": 683, "y2": 820, "rotate": 159}
print("Looking for the word 'Manually'")
dexarm.fast_move_to(112,298,-12, 10000)
while "Manually" not in get_single_string(895,1380,683,820,159):
	pass

# Press Set up manually = 72,252
print('Pressing on Set Up Manually')
screen_tap(90,280)

# Pause 2 seconds
#dexarm._send_cmd("G4 S2\n")

connected_to_correct_wifi = False

while connected_to_correct_wifi == False:

	# Search for the Lindisfarne Wifi Network
	print("Looking for the word 'Lindisfarne'")
	# move arm to 62, 300, -12
	dexarm.fast_move_to(62,300,-12, 10000)

	# Pause 1 second
	dexarm._send_cmd("G4 S1\n")

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
type_word(main_username)

# Press the Next button
screen_tap(94,342)

# Type password
type_word(main_password)

# Press the join button
# 96,342
screen_tap(96,342)

# Look for the word "lindisfarne"
# Send arm to 0,300,-12
# Crop photo to 710, 1460, 555, 640, 180
print("Looking for the word 'lindisfarne'")
dexarm.fast_move_to(0,300,-12, 10000)
while "lindisfarne" not in get_single_string(710,1460,555,640,180):
	pass

# Press the Trust button
# -40 318
screen_tap(-40,318)

# Look for the word "Transfer"
# Send arm to 74,300,-12
# Crop photo to 541, 1200, 720, 811, 166
print("Looking for the word 'Transfer'")
dexarm.fast_move_to(74,300,-12, 10000)
while "Transfer" not in get_single_string(541,1200,720,811,166):
	pass

# Press on the Don't Transfer option
screen_tap(54,300)

# Look for the word "Next"
# Send arm to -52,364,-12
# Crop photo to {"x1": 934, "x2": 1130, "y1": 715, "y2": 804, "rotate": 188}
print("Looking for the word 'Next'")
dexarm.fast_move_to(-52,364,-12, 10000)
while "Next" not in get_single_string(934,1130,715,804,188):
	pass

# Press Next
print('Pressing next')
screen_tap(-52,326)

# Type username
type_word(main_username)

# Press the return key
screen_tap(96,344)

# Type password
type_word(main_password)

# Press Next
screen_tap(-82,326)


# Look for the word "password"
# Send arm to 42,312,-12
# Crop photo to {"x1": 408, "x2": 1640, "y1": 872, "y2": 1016, "rotate": 172}
print("Looking for the word 'password'")
dexarm.fast_move_to(42,312,-12, 10000)
while "password" not in get_single_string(408,1640,872,1016,172):
	pass

# Press don't have apple ID
# 44,274
screen_tap(44,274)
pause(1000)

# Press setup later in settings
# 4,274
screen_tap(4,274)
pause(1000)

# Press Don't use
# 36, 286
screen_tap(36,286)
pause(1000)

# Press continue
# 78,286
screen_tap(78,286)
pause(1000)

# Press enable location services
# 78,286
screen_tap(78,286)
pause(1000)

# Press Don't share
# 90,276
screen_tap(90,276)
pause(1000)

# Press the settings button
# 44,238
screen_tap(44,238)

# Press about
# -68,290
screen_tap(-68,290)

pause(2000)

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
	serial_number = get_single_string(730,1163,510,590,181,True)
	if x > 2:
		if serial_number == "":
			print('I think the screen is off, pressing the home button twice')
			press_home_button()
			press_home_button()
			print('Moving the arm back into position')
			dexarm.fast_move_to(-12,376,-12, 10000)
	print('Matching serial ' + serial_number + ' to username ' + main_username)
	serial_username = get_jamf_username_from_device_serial(serial_number)
	if serial_username == main_username:
		print('Found a match!')
		break
	else:
		print("Does not match! '" + serial_username + "' does not equal '" + main_username + "'")
	pause(1000)
	x = x + 1

# If we get to here, I am satified that we
# have the correct serial number for the iPad

# Press the home button
press_home_button()

# Turn on Siri
dexarm.fast_move_to(144, 272, get_current_location('z'), 5000)
dexarm.fast_move_to(144, 272, -56, 5000)
pause(1000)
dexarm.fast_move_to(144, 272, -40, 5000)
# Tap on Use Siri
screen_tap(104,272)
# Tap on Voice 2
screen_tap(-4,270)
# Press on Next
screen_tap(-82,332)
# Tap on Not Now
screen_tap(118,272)
# Press the home button
press_home_button()
# Press settings
screen_tap(44,238)
# Press Display and Brightness
screen_tap(94,226)
# Press auto lock
screen_tap(34,298)
# Press Never
screen_tap(-32,298)
# Press Display and brightness
screen_tap(-86,274)
# Press the brightness slider
screen_tap(0,334)
screen_tap(0,334)
screen_tap(0,334)
# Press the home button
press_home_button()

pause(2000)

# Drag down the home screen
screen_drag(44,64,300,300)

# Search for the Vivi App
type_word("vivi")

# Press go button
screen_tap(96,344)

pause(1000)

# type word lindis
type_word("lindis")

# Tap the lindisfarne button
screen_tap(-38,278)

# Tap the login button
screen_tap(-30,278)

# Type username
type_word(main_username)

# Press the return key
screen_tap(96,344)

# Type password
type_word(main_password)

# Press the return key
screen_tap(96,344)

if int(get_student_yearlevel(main_username)) > 4:
	# Press Mahers Lane button
	screen_tap(-36,266)
else:
	# Press Sunshine Avenue button
	screen_tap(-24,266)

# Press home button
press_home_button()














# Go home
print('Going back home...')
go_home()

print('Script finished')