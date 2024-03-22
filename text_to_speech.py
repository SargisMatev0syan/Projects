#First, you need to install the library using pip:(pip install gtts)

# We import the gTTS class from the gtts module
from gtts import gTTS
import os 

# We define a function text_to_speech that takes the text to be
#  converted as input and saves the speech as an MP3 file.
def text_to_speech(text,filename='output.mp3'):
    tts = gTTS(text=text, lang='en')
    
    tts.save(filename)
    # the code uses os.system to play the generated audio file. 
    # This line is specific to Windows.
    os.system(f'start {filename}')

if __name__ == '__main__':
    text = input('Enter the text you want to convert to speech:--')
    text_to_speech(text)    


#    When you run this code, it will prompt you to enter the text you want to
#  convert to speech. After entering the text, it will generate an MP3 file 
# with the speech and play it using your default media player.



