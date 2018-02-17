# Nick Shahin
import os
import sys
from gtts import gTTS

def main(command):

    print(command)

    os.system("rm command.mp3")
    os.system("rm command.wav")

    command = "Alexa, " + command
    tts = gTTS(text=command, lang='en')
    tts.save("command.mp3")

    os.system("ffmpeg -i command.mp3 -ar 441000 -ac 2 command.wav")

    # os.system("./request.sh")

if __name__ == "__main__":
    main(sys.argv[1])
