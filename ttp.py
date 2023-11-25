from gtts import gTTS
import os 
text =  'This is for testing mp3'
output =  gTTS(text=text, lang='en' , slow = False)
output.save('output.mp3')
os.system('start output.mp3' )
