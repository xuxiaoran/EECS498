# Nick Shahin
import os
import sys
from gtts import gTTS

def main(command):

    # Remove old audio files
    os.system("rm command.mp3")
    os.system("rm command.wav")

    # Send command to google text to speech services, save as mp3
    command = "Alexa, " + command
    tts = gTTS(text=command, lang='en')
    tts.save("command.mp3")

    # Convert command.mp3 to command.wav
    os.system("ffmpeg -i command.mp3 -ar 441000 -ac 2 command.wav")

    # Make ssh request to amazon voice services
    # os.system("./request.sh")

if __name__ == "__main__":
    main("What time is it")
