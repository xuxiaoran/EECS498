# Nick Shahin
import os
import sys
from gtts import gTTS
from amazonLogin import getCode

def tokenRetrieval():
    # Make ssh request to amazon voice services
    os.system("chmod aug+x auth_code.sh")
    os.system("./auth_code.sh")

    getCode()

    os.system("chmod aug+x auth_token.sh")
    os.system("./auth_token.sh")

    with open('token.txt', 'r') as tokenFile:
        token = tokenFile.read()[1:-1]

    with open('refresh_token.txt', 'r') as refreshTokenFile:
        refresh_token = refreshTokenFile.read()[1:-1]

    with open('token.txt', 'w') as outFile1:
        outFile1.write(token)

    with open('refresh_token.txt', 'w') as outFile2:
        outFile2.write(refresh_token)

    os.system("chmod aug+x request.sh")

def send_command(command):

    # Remove old audio files
    os.system("rm command.mp3")
    os.system("rm command.wav")

    # Send command to google text to speech services, save as mp3
    command = "Alexa, " + command
    tts = gTTS(text=command, lang='en')
    tts.save("command.mp3")

    # Convert command.mp3 to command.wav
    os.system("ffmpeg -i command.mp3 -ar 16000 -ac 1 -acodec pcm_s16le command.wav")

    os.system("./request.sh")

    response_file = open("response.txt", 'r')
    response_text = response_file.read()
    response_file.close() 

    pos = response_text.find("ID3")
    response_text = response_text[pos:]

    spoken_response = open("response_audio.txt", 'w')
    spoken_response.write(response_text)
    spoken_response.close()

    os.system("mv response_audio.txt response_audio.mp3")
    os.system("afplay response_audio.mp3")
