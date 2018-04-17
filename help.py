import os, sys
import re
import json
from urllib.request import urlopen

def helpText():
	url = 'http://ipinfo.io/json'
	response = urlopen(url)
	data = json.load(response)
	script = "osascript -e \'tell application \"Messages\" to send \"I am in trouble. Please send help! https://www.google.com/maps/search/?api=1&query={0} \" to buddy \"Nick Shahin\"\'".format(data['loc'])
	os.system(script)

if __name__ == '__main__':
	helpText()