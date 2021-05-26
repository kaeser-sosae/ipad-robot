import serial, time
from pydexarm import Dexarm
import requests
import os

dexarm = Dexarm("/dev/ttyACM0")

main_username = "simp9998"
main_password = ""

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
		dexarm.fast_move_to(144, 272, -58, 5000)
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

def get_jamf_username_from_serial(serial_number):
	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/computers/serialnumber/" + serial_number

	payload = ""
	headers = {
	  'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	print(data)

get_jamf_username_from_serial(FVFDVGT7Q6L4)