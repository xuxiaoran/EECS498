import os, sys

def helpText():
	os.system("osascript -e \'tell application \"Messages\" to send \"I am in trouble. Please send help!\" to buddy \"Jose Contreras\"\'")

if __name__ == '__main__':
	helpText()