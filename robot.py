import serial, time

print('Opening serial connection')
ser = serial.Serial('/dev/ttyACM0', 115200)

speed = 'F4500'

# CONSTANTS
# Home button location = X124 Y254
# Home button pressed X124 Y254 Z56
# Z off screen travel height Z-48
# Arm out of the way = X-226 Y0 Z6
# Button pressed location = X-136 Y326 Z-106 (press down from X-148)





# Functions
def goto(x, y, press):
        if (press == True):
                ser.write(bytes('G00 X' + str(x) + ' Y' + str(y) + ' ' + speed + '\n', 'utf-8'))
                time.sleep(.2)
                ser.write(bytes('G00 Z760 ' + speed + '\n', 'utf-8'))
                time.sleep(.1)
                ser.write(bytes('G00 Z774 ' + speed + '\n', 'utf-8'))
                time.sleep(1)
        else:
                ser.write(bytes('G00 X' + str(x) + ' Y' + str(y) + ' ' + speed + '\n', 'utf-8'))
                time.sleep(1)


def press_letter(letter):
	print('Typing letter ' + letter)
	if (letter == "a"):
		goto(-66,348,True)
	if (letter == "b"):
		goto(-75,285,True)
	if (letter == "c"):
		goto(-75,315,True)
	if (letter == "d"):
		goto(-63,321,True)
	if (letter == "e"):
		goto(-51,327,True)		
	if (letter == "f"):
		goto(-63,306,True)
	if (letter == "g"):
		goto(-63,291,True)
	if (letter == "h"):
		goto(-60,279,True)
	if (letter == "i"):
		goto(-51,258,True)
	# if (letter == "j"):
	# 	goto(-72,261,True)	
	if (letter == "k"):
		goto(-60,252,True)
	if (letter == "l"):
		goto(-60,237,True)
	if (letter == "m"):
		goto(-72,261,True)
	# if (letter == "n"):
	# 	goto(-48,231,True)
	if (letter == "o"):
		goto(-48,243,True)
	if (letter == "p"):
		goto(-48,228,True)
	if (letter == "q"):
		goto(-54,357,True)
	if (letter == "r"):
		goto(-51,312,True)
	if (letter == "s"):
		goto(-63,339,True)
	if (letter == "t"):
		goto(-51,300,True)
	if (letter == "u"):
		goto(-51,270,True)
	# if (letter == "v"):
	# 	goto(-63,339,True)
	if (letter == "w"):
		goto(-54,342,True)
	# if (letter == "x"):
	# 	goto(-63,339,True)
	if (letter == "y"):
		goto(-51,285,True)
	# if (letter == "z"):
	# 	goto(-63,339,True)

	if (letter == "A"):
		goto(-75,354,True)
		goto(-66,348,True)
	if (letter == "B"):
		goto(-75,354,True)
		goto(-75,285,True)
	if (letter == "C"):
		goto(-75,354,True)
		goto(-75,315,True)
	if (letter == "D"):
		goto(-75,354,True)
		goto(-63,321,True)
	if (letter == "E"):
		goto(-75,354,True)
		goto(-51,327,True)	
	if (letter == "F"):
		goto(-75,354,True)
		goto(-63,306,True)
	if (letter == "G"):
		goto(-75,354,True)
		goto(-63,291,True)
	if (letter == "H"):
		goto(-75,354,True)
		goto(-60,279,True)
	if (letter == "I"):
		goto(-75,354,True)
		goto(-51,258,True)
	# if (letter == "J"):
	#	goto(-75,354,True)
	# 	goto(-72,261,True)	
	if (letter == "K"):
		goto(-75,354,True)
		goto(-60,252,True)
	if (letter == "L"):
		goto(-75,354,True)
		goto(-60,237,True)
	if (letter == "M"):
		goto(-75,354,True)
		goto(-72,261,True)
	# if (letter == "N"):
	#	goto(-75,354,True)
	# 	goto(-48,231,True)
	if (letter == "O"):
		goto(-75,354,True)
		goto(-48,243,True)
	if (letter == "P"):
		goto(-75,354,True)
		goto(-48,228,True)
	if (letter == "Q"):
		goto(-75,354,True)
		goto(-54,357,True)
	if (letter == "R"):
		goto(-75,354,True)
		goto(-51,312,True)
	if (letter == "S"):
		goto(-75,354,True)
		goto(-63,339,True)
	if (letter == "T"):
		goto(-75,354,True)
		goto(-51,300,True)
	if (letter == "U"):
		goto(-75,354,True)
		goto(-51,270,True)
	# if (letter == "V"):
	#	goto(-75,354,True)
	# 	goto(-63,339,True)
	if (letter == "W"):
		goto(-75,354,True)
		goto(-54,342,True)
	# if (letter == "X"):
	#	goto(-75,354,True)
	# 	goto(-63,339,True)
	if (letter == "Y"):
		goto(-75,354,True)
		goto(-51,285,True)
	# if (letter == "Z"):
	#	goto(-75,354,True)
	# 	goto(-63,339,True)


	if (letter == "-"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-75,327,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "1"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-51,357,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "2"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-51,342,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "3"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-51,327,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "4"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-51,312,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "9"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-48,246,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)
	if (letter == "8"):
		goto(-90,357,True)
		time.sleep(1)
		goto(-48,258,True)
		time.sleep(1)
		goto(-90,357,True)
		time.sleep(1)

	if (letter == "nums"):
		goto(-90,357,True)
	if (letter == "left_shift"):
		goto(-78,357,True)		

def go_home():
        #ser.write(bytes('M1112\n', 'utf-8'))
        print('Going home...')
        ser.write(bytes('G00 X-226 Y0 Z6 ' + speed + '\n', 'utf-8'))
        time.sleep(1)

def press_home_button():
        print('Pressing home button...')
        ser.write(bytes('G00 X124 Y254 ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 Z-56 ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 Z-48 ' + speed + '\n', 'utf-8'))
        time.sleep(1)

def press_power_button(seconds):
        print('Pressing power button...')
        ser.write(bytes('G00 Z-20 ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 Y326 X-148 Z-106 ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 X-136 ' + speed + '\n', 'utf-8'))
        time.sleep(seconds)
        ser.write(bytes('G00 X-148 ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 Z-20 ' + speed + '\n', 'utf-8'))

def type_word(word):
        print('Typing word ' + word)
        for char in word[ : : 1]:
                press_letter(char)

def start_siri(x,y):
        ser.write(bytes('G00 X' + str(x) + ' Y' + str(y) + ' ' + speed + '\n', 'utf-8'))
        ser.write(bytes('G00 Z-68 ' + speed + '\n', 'utf-8'))
        time.sleep(5)
        ser.write(bytes('G00 Z-45 ' + speed + '\n', 'utf-8'))
        time.sleep(1)

# Go home
go_home()
time.sleep(1)

# Press power button for 2 seconds
press_power_button(2)
time.sleep(1)

#Press home button twice
press_home_button()
time.sleep(2)
press_home_button()
time.sleep(2)

# Go home
go_home()

# Press on English
#goto(66,303,True)

# Press on Australia
#goto(36,300,True)

# Sleep for 10
#time.sleep(7)

# Press on Set Up Manually
#goto(-87,285,True)

# Sleep for 10
#time.sleep(5)

# Press on Gav's iPhone Network
#goto(42,285,True)

# Type Hotspot password
#type_word("abcd1234")

# Press the join button
#goto(84,246,True)

# Sleep for 10 seconds
#time.sleep(20)

# Press on Next
#goto(99,222,True)

# Sleep for 30 seconds
#time.sleep(30)

# Press on Don't Transfer Data
#goto(3,291,True)

# Press on Next
#goto(99,222,True)

# Sleep 15 seconds
#time.sleep(15)

# Type in the username
#type_word("simp9998")

# Click in the password box
#goto(27,312,True)

# Type the password
#type_word("El-barto-graffiti")

# Press on Next
#goto(99,222,True)

# Sleep 20 seconds
#time.sleep(20)

# Press Continue
#goto(-75,282,True)

# Sleep 5 seconds
#time.sleep(5)

# Press Enable Location Services
#goto(-75,282,True)

# Sleep 5 seconds
#time.sleep(5)

# Press Don't Share
#goto(-87,282,True)

#go_home()

#time.sleep(5)

print('Closing serial connection')
ser.close()
print('Script finished')