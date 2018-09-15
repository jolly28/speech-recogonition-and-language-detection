import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator


def lang_detect(data):
    translator = Translator()
    l=translator.detect(data)
    return l.lang
 
def speak(audioString):
    print(audioString)
    l=lang_detect(audioString)
    tts = gTTS(text=audioString, lang=l)
    tts.save("audio.mp3")
    os.system("audio.mp3")
    
def translate_to_eng(data):
    translator = Translator()
    t=translator.translate(data,dest='en')
    return t.text

def translate_to_detect_lang(data,l):
    translator = Translator()
    t=translator.translate(data,dest=l)
    return t.text

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        l=lang_detect(data)
        data = r.recognize_google(audio,language=l)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def jarvis(data):
    
    l=lang_detect(data)
    print('language detected:',l)
    dataeng=translate_to_eng(data)
    print(dataeng)

r=recordAudio()
jarvis(r)
