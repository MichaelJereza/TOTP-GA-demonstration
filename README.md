This is a Python implementation of a time-based one-time password algorithm. 
The script can generate a scannable QR code, a 16 character Base32 key, and print the current OTP. 
The QR code is compatible with an authenticator app like Google Authenticator.

### Dependencies:
- python3
- python3-pip

These will be installed by the Makefile if not already present:
- pyotp
- pyqrcode


### Installation:
1. First make sure python3 and python3-pip are installed.	
2. Next make sure that the Makefile is executable, because it is a shell script to install pip packages.
3. Execute the shell script './Makefile'.
	
### Running:
Incorrect input will be caught, help information will be printed when invalid arguments are given.

#### Here are the three basic use cases:	
`python3 TOTP.py --generate-secret`

This prints a 16 character Base32 key that can be used for a TOTP secret, and can be used as the parameter for this program.

`python3 TOTP.py --generate-qr [user-key]`

This will print a scannable QR code to the terminal that works with GA.
	
`python3 TOTP.py --get-otp [user-key]`

This will print the valid OTP for this 30 second interval.

