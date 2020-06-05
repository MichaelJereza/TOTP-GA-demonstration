#!/usr/bin/env python3

#https://pyotp.readthedocs.io/en/latest/

import sys
import pyotp
import pyqrcode
import time

#=========

def genQR(secret):
    if checkInput(secret):
        url = pyotp.totp.TOTP(secret).provisioning_uri("Programming Assignment 2", issuer_name="Michael Jereza")
        qr = pyqrcode.create(url)
        print(qr.terminal(quiet_zone=1))
        return
    else:
        return

def genSecret():
    print(pyotp.random_base32())
    return

def getOTP(secret):
    if checkInput(secret):
        totp = pyotp.TOTP(secret)
        print(totp.now())
        return
    
    else:
        return

def checkInput(secret):
    # Valid Base32 = A-Z 2-7
    if len(secret) != 16:
        print('\nInput bad length!\n')
        return 0

    for i in secret:
        asc = ord(i)
        if (asc > 64 and asc < 91) or (asc > 49 and asc < 56):
            return 1
        else:
            print('\nNon-base32 input!\n')
            return 0

def printError():
    print('\nProgrammed by Michael Jereza\n\nCommands:\n\n--generate-qr secret\n\tGenerates image of QR for Google Authenticator for a Base32 key\n\n--get-otp secret\n\tGenerates the valid OTP for the next 30 seconds for a Base32 key\n\n--generate-secret\n\tGenerates a valid 16 character Base32 secret key\n')
    return

#==========

def main():
    arguments = len(sys.argv)

    if arguments == 1: 
        return printError()
    if arguments == 3:
        if sys.argv[1] == '--generate-qr' and arguments == 3:
            return genQR(sys.argv[2])
        elif sys.argv[1] == '--get-otp' and arguments == 3:
            return getOTP(sys.argv[2])
    elif sys.argv[1] == '--generate-secret':
        return genSecret()

    return printError()


if __name__ == '__main__':
    main()
