import os, sys

def helpText():
	os.system("osascript -e \'tell application \"Messages\" to send \"I am in trouble. Please send help!\" to buddy \"Nick Shahin\"\'")

if __name__ == '__main__':
	helpText()