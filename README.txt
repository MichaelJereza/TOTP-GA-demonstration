Michael Jereza

Programming Assignment 2

Dependencies:
	python3
	python3-pip

	These will be installed by the Makefile if not already present.
	
	pyotp
	pyqrcode


Installation:
	First make sure python3 and python3-pip are installed.
	
	Next make sure that the Makefile is executable, because it is a shell script to install pip packages.
	
	Execute the shell script './Makefile'.
	
Running:
	
	Incorrect input will be caught, help information will be printed when invalid arguments are given.

	Here are the three basic use cases:	
	
	'python3 TOTP.py --generate-secret'
		This prints a 16 character Base32 key that can be used for a TOTP secret, and can be used as the parameter for this program.

	'python3 TOTP.py --generate-qr [user-key]' 
		This will print a scannable QR code to the terminal that works with GA.
	
	'python3 TOTP.py --get-otp [user-key]' 
		This will print the valid OTP for this 30 second interval.

