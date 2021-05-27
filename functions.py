import serial, time
from pydexarm import Dexarm
import requests
import os

dexarm = Dexarm("/dev/ttyACM0")

# Letter locations are defined as x_start, x_finish, y_start, y_finish
# For a tap, make the start and finish the same. For a drag, they
# can be different

x_start_offset = 2
x_finish_offset = 2
y_start_offset = 0
y_finish_offset = 0

letter_locations = {
	"a":[(103 + x_start_offset,103 + x_finish_offset,208 + y_start_offset,208 + y_finish_offset)],
	"b":[(111 + x_start_offset,111 + x_finish_offset,270 + y_start_offset,270 + y_finish_offset)],
	"c":[(113 + x_start_offset,113 + x_finish_offset,244 + y_start_offset,244 + y_finish_offset)],
	"d":[(99 + x_start_offset,99 + x_finish_offset,236 + y_start_offset,236 + y_finish_offset)],
	"e":[(87 + x_start_offset,87 + x_finish_offset,232 + y_start_offset,232 + y_finish_offset)],
	"f":[(99 + x_start_offset,99 + x_finish_offset,250 + y_start_offset,250 + y_finish_offset)],
	"g":[(99 + x_start_offset,99 + x_finish_offset,264 + y_start_offset,264 + y_finish_offset)],
	"h":[(97 + x_start_offset,97 + x_finish_offset,278 + y_start_offset,278 + y_finish_offset)],
	"i":[(81 + x_start_offset,81 + x_finish_offset,302 + y_start_offset,302 + y_finish_offset)],
	"j":[(97 + x_start_offset,97 + x_finish_offset,292 + y_start_offset,292 + y_finish_offset)],
	"k":[(96 + x_start_offset,96 + x_finish_offset,306 + y_start_offset,306 + y_finish_offset)],
	"l":[(95 + x_start_offset,95 + x_finish_offset,318 + y_start_offset,318 + y_finish_offset)],
	"m":[(109 + x_start_offset,109 + x_finish_offset,298 + y_start_offset,298 + y_finish_offset)],
	"n":[(109 + x_start_offset,109 + x_finish_offset,284 + y_start_offset,284 + y_finish_offset)],
	"o":[(81 + x_start_offset,81 + x_finish_offset,314 + y_start_offset,314 + y_finish_offset)],
	"p":[(81 + x_start_offset,81 + x_finish_offset,328 + y_start_offset,328 + y_finish_offset)],
	"q":[(87 + x_start_offset,87 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)],
	"r":[(85 + x_start_offset,85 + x_finish_offset,246 + y_start_offset,246 + y_finish_offset)],
	"s":[(99 + x_start_offset,99 + x_finish_offset,222 + y_start_offset,222 + y_finish_offset)],
	"t":[(85 + x_start_offset,85 + x_finish_offset,260 + y_start_offset,260 + y_finish_offset)],
	"u":[(83 + x_start_offset,83 + x_finish_offset,288 + y_start_offset,288 + y_finish_offset)],
	"v":[(111 + x_start_offset,111 + x_finish_offset,256 + y_start_offset,256 + y_finish_offset)],
	"w":[(87 + x_start_offset,87 + x_finish_offset,218 + y_start_offset,218 + y_finish_offset)],
	"x":[(113 + x_start_offset,113 + x_finish_offset,228 + y_start_offset,228 + y_finish_offset)],
	"y":[(83 + x_start_offset,83 + x_finish_offset,274 + y_start_offset,274 + y_finish_offset)],
	"z":[(115 + x_start_offset,115 + x_finish_offset,214 + y_start_offset,214 + y_finish_offset)],
	"A":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(103 + x_start_offset,103 + x_finish_offset,208 + y_start_offset,208 + y_finish_offset)],
	"B":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(111 + x_start_offset,111 + x_finish_offset,270 + y_start_offset,270 + y_finish_offset)],
	"C":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(113 + x_start_offset,113 + x_finish_offset,224 + y_start_offset,244 + y_finish_offset)],
	"D":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(99 + x_start_offset,99 + x_finish_offset,236 + y_start_offset,236 + y_finish_offset)],
	"E":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(87 + x_start_offset,87 + x_finish_offset,232 + y_start_offset,232 + y_finish_offset)],
	"F":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(99 + x_start_offset,99 + x_finish_offset,250 + y_start_offset,250 + y_finish_offset)],
	"G":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(99 + x_start_offset,99 + x_finish_offset,264 + y_start_offset,264 + y_finish_offset)],
	"H":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(97 + x_start_offset,97 + x_finish_offset,278 + y_start_offset,278 + y_finish_offset)],
	"I":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(81 + x_start_offset,81 + x_finish_offset,302 + y_start_offset,302 + y_finish_offset)],
	"J":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(97 + x_start_offset,97 + x_finish_offset,292 + y_start_offset,292 + y_finish_offset)],
	"K":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(96 + x_start_offset,96 + x_finish_offset,306 + y_start_offset,306 + y_finish_offset)],
	"L":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(95 + x_start_offset,95 + x_finish_offset,318 + y_start_offset,318 + y_finish_offset)],
	"M":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(109 + x_start_offset,109 + x_finish_offset,298 + y_start_offset,298 + y_finish_offset)],
	"N":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(109 + x_start_offset,109 + x_finish_offset,284 + y_start_offset,284 + y_finish_offset)],
	"O":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(81 + x_start_offset,81 + x_finish_offset,314 + y_start_offset,314 + y_finish_offset)],
	"P":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(81 + x_start_offset,81 + x_finish_offset,328 + y_start_offset,328 + y_finish_offset)],
	"Q":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(87 + x_start_offset,87 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)],
	"R":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(85 + x_start_offset,85 + x_finish_offset,246 + y_start_offset,246 + y_finish_offset)],
	"S":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(99 + x_start_offset,99 + x_finish_offset,222 + y_start_offset,222 + y_finish_offset)],
	"T":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(85 + x_start_offset,85 + x_finish_offset,260 + y_start_offset,260 + y_finish_offset)],
	"U":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(83 + x_start_offset,83 + x_finish_offset,288 + y_start_offset,288 + y_finish_offset)],
	"V":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(111 + x_start_offset,111 + x_finish_offset,256 + y_start_offset,256 + y_finish_offset)],
	"W":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(87 + x_start_offset,87 + x_finish_offset,218 + y_start_offset,218 + y_finish_offset)],
	"X":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(113 + x_start_offset,113 + x_finish_offset,228 + y_start_offset,228 + y_finish_offset)],
	"Y":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(83 + x_start_offset,83 + x_finish_offset,274 + y_start_offset,274 + y_finish_offset)],
	"Z":[(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(115 + x_start_offset,115 + x_finish_offset,214 + y_start_offset,214 + y_finish_offset)],
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
	"1":[(87 + x_start_offset,97 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)],
	"2":[(87 + x_start_offset,97 + x_finish_offset,218 + y_start_offset,218 + y_finish_offset)],
	"3":[(87 + x_start_offset,97 + x_finish_offset,232 + y_start_offset,232 + y_finish_offset)],
	"4":[(85 + x_start_offset,95 + x_finish_offset,246 + y_start_offset,246 + y_finish_offset)],
	"5":[(85 + x_start_offset,95 + x_finish_offset,260 + y_start_offset,260 + y_finish_offset)],
	"6":[(83 + x_start_offset,93 + x_finish_offset,274 + y_start_offset,274 + y_finish_offset)],
	"7":[(83 + x_start_offset,93 + x_finish_offset,288 + y_start_offset,288 + y_finish_offset)],
	"8":[(81 + x_start_offset,91 + x_finish_offset,302 + y_start_offset,302 + y_finish_offset)],
	"9":[(81 + x_start_offset,91 + x_finish_offset,314 + y_start_offset,314 + y_finish_offset)],
	"0":[(81 + x_start_offset,91 + x_finish_offset,328 + y_start_offset,328 + y_finish_offset)],

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

	"@":[(103 + x_start_offset,113 + x_finish_offset,208 + y_start_offset,208 + y_finish_offset)],
	"#":[(99 + x_start_offset,109 + x_finish_offset,222 + y_start_offset,222 + y_finish_offset)],
	"$":[(99 + x_start_offset,109 + x_finish_offset,236 + y_start_offset,236 + y_finish_offset)],
	"&":[(99 + x_start_offset,109 + x_finish_offset,250 + y_start_offset,250 + y_finish_offset)],
	"*":[(99 + x_start_offset,109 + x_finish_offset,264 + y_start_offset,264 + y_finish_offset)],
	"(":[(97 + x_start_offset,107 + x_finish_offset,278 + y_start_offset,278 + y_finish_offset)],
	")":[(97 + x_start_offset,107 + x_finish_offset,292 + y_start_offset,292 + y_finish_offset)],
	"%":[(115 + x_start_offset,125 + x_finish_offset,214 + y_start_offset,214 + y_finish_offset)],
	"-":[(113 + x_start_offset,129 + x_finish_offset,228 + y_start_offset,228 + y_finish_offset)],
	"+":[(113 + x_start_offset,123 + x_finish_offset,244 + y_start_offset,244 + y_finish_offset)],
	"=":[(111 + x_start_offset,121 + x_finish_offset,256 + y_start_offset,256 + y_finish_offset)],

	",":[(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset),(108 + x_start_offset,108 + x_finish_offset,314 + y_start_offset,314 + y_finish_offset),(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)],
	".":[(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset),(108 + x_start_offset,108 + x_finish_offset,328 + y_start_offset,328 + y_finish_offset),(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)],
	"_":[(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset),(118 + x_start_offset,118 + x_finish_offset,200 + y_start_offset,200 + y_finish_offset),(100 + x_start_offset,100 + x_finish_offset,250 + y_start_offset,250 + y_finish_offset),(130 + x_start_offset,130 + x_finish_offset,202 + y_start_offset,202 + y_finish_offset)]
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

def screen_tap(x, y, z_down=-53, z_up=-40):
	# Move above the location
	dexarm.fast_move_to(x, y, get_current_location('z'), 10000)
	# Drop the Z height
	dexarm.fast_move_to(x, y, z_down, 10000)
	# Raise the Z height
	dexarm.fast_move_to(x, y, z_up, 10000)
	# Tiny pause
	dexarm._send_cmd("G4 P50\n")

def screen_drag(x_start, x_finish, y_start, y_finish, z_down=-55, z_up=-40):
	# Move above the starting location
	dexarm.fast_move_to(x_start, y_start, get_current_location('z'), 10000)
	# Drop the Z height
	dexarm.fast_move_to(x_start, y_start, z_down, 10000)
	# Move to the finish location
	dexarm.fast_move_to(x_finish, y_finish, z_down, 10000)
	# Raise the Z height
	dexarm.fast_move_to(x_finish, y_finish, z_up, 10000)
	# Tiny pause
	dexarm._send_cmd("G4 P50\n")

def type_word(word):
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
	pass

def get_single_string(x1,x2,y1,y2,rotation,is_serial=False):
	if is_serial == True:
		for returned_strings in get_ocr_text({"areas":[{"x1":x1,"x2":x2,"y1":y1,"y2":y2,"rotate":rotation,"whitelist":"0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"}]}):
			if returned_strings != "":
				#print('Found string: ' + returned_strings)
				return returned_strings
			else:
				#print('Found string: ' + returned_strings)
				return ""
	else:
		for returned_strings in get_ocr_text({"areas":[{"x1":x1,"x2":x2,"y1":y1,"y2":y2,"rotate":rotation}]}):
			if returned_strings != "":
				#print('Found string: ' + returned_strings)
				return returned_strings
			else:
				#print('Found string: ' + returned_strings)
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

def does_device_have_app_installed(serial_number, application_name):
	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/mobiledevices/serialnumber/" + serial_number

	payload = ""
	headers = {
		'Accept': 'application/json',
		'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0'
	}

	response = requests.request("GET", url, headers=headers, json=payload)

	if response.status_code == 200:
		for app in response.json()["mobile_device"]["applications"]:
			if app["application_name"] == application_name:
				return True
		return False

	else:
		print('API call failed with status code ' + str(response.status_code))
		return False

def get_jamf_device_id_from_device_serial(serial_number):
	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/mobiledevices/serialnumber/" + serial_number

	payload = ""
	headers = {
		'Accept': 'application/json',
		'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0'
	}

	response = requests.request("GET", url, headers=headers, json=payload)

	if response.status_code == 200:
		return str(response.json()["mobile_device"]["general"]["id"])

	else:
		print('API call failed with status code ' + str(response.status_code))
		return ""

def add_device_to_static_group(serial_number, group_name):

	device_id = get_jamf_device_id_from_device_serial(serial_number)
	
	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/mobiledevicegroups/name/Tier 1 Software That Needs Configuring"

	payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<mobile_device_group>\n\t<name>" + group_name + "</name>\n\t<is_smart>False</is_smart>\n\t<mobile_device_additions>\n\t\t<mobile_device>\n\t\t\t<id>" + device_id + "</id>\n\t\t</mobile_device>\n\t</mobile_device_additions>\n</mobile_device_group>"
	headers = {
		'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0',
		'Content-Type': 'application/json'
	}

	response = requests.request("PUT", url, headers=headers, data=payload)

	if response.status_code == 201:
		print('API call succeeded with status code ' + str(response.status_code))
		return True

	else:
		print('API call failed with status code ' + str(response.status_code))
		return False		

def send_mdm_command(command, serial_number):

	device_id = get_jamf_device_id_from_device_serial(serial_number)

	url = "https://casper.lindisfarne.nsw.edu.au:8443/JSSResource/mobiledevicecommands/command"

	payload = "<mobile_device_command>\n        <general>\n            <command>" + command + "</command>\n        </general>\n        <mobile_devices>\n            <mobile_device>\n                <id>" + device_id + "</id>\n            </mobile_device>\n        </mobile_devices>\n    </mobile_device_command>"
	headers = {
  		'Authorization': 'Basic aWRlbnRpdHk6c3lwaG9uLW1hbnRpbGxhLXN0eW1pZTgtb3V0bGV0',
  		'Content-Type': 'application/xml'
	}

	response = requests.request("POST", url, headers=headers, data=payload)

	if 200 <= response.status_code <= 299:
		print('API call succeeded with status code ' + str(response.status_code))
		return True

	else:
		print('API call failed with status code ' + str(response.status_code))
		return False	
