import os
import sys
from amazonLogin import getCode
from forwarding_file import send_command

def initialTokenRetrieval():
    os.system("chmod aug+x auth_code.sh")
    os.system("./auth_code.sh")
    getCode()
    os.system("chmod aug+x auth_token.sh")
    os.system("./auth_token.sh")
    removeQuotes()
    os.system("chmod aug+x request.sh")

def refreshToken():
    os.system("chmod aug+x refresh_token.sh")
    os.system("./refresh_token.sh")
    removeQuotes()
    os.system("chmod aug+x request.sh")

def removeQuotes():
    with open('token.txt', 'r') as tokenFile:
        token = tokenFile.read()[1:-2]
    with open('refresh_token.txt', 'r') as refreshTokenFile:
        refresh_token = refreshTokenFile.read()[1:-2]
    with open('token.txt', 'w') as outFile1:
        outFile1.write(token)
    with open('refresh_token.txt', 'w') as outFile2:
        outFile2.write(refresh_token)

if __name__ == '__main__':
    initialTokenRetrieval()