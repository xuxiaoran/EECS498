
Backend dependencies:
ffmpeg: "brew install ffmpeg"
gtts: "pip install gTTS"
selenium WebDriver: "sudo easy_install selenium"
jq: "brew install jq"
Chrome Driver: https://chromedriver.storage.googleapis.com/index.html?path=2.37/

How to Run:

1. Check if node.js & npm are installed first, run:

    node -v
    
     npm -v

2. If not installed, run: 

    brew install node

3. After installing node&npm, run:

    npm install electron -g

4. At the project root directory, run:

    electron .
