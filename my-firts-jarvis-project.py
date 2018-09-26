
import wikipedia
import pyttsx
import speech_recognition as sr
import pyaudio
import time
import os
import math
from time import ctime
import numpy as np
import serial
import aiml
import argparse
import sys
import webbrowser
from playsound import playsound
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from array import array



def listen_master():


    r = sr.Recognizer()
    r.energy_threshold = 4000

    def say(text):
        engine = pyttsx.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 2.0)
        engine.say(text)
        engine.runAndWait()


    
   
                                
    #print("A moment of silence, please...")
                                
    with sr.Microphone(device_index = 0,sample_rate = 44100, chunk_size = 512) as source:
        print 'Listening...'
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
            
       
        try:
            message = (r.recognize_google(audio, language = 'id', show_all = False))
            print("You said: " + message)
            #call(["espeak", message])

    
            if (message == 'Open Google'):
                print 'Oke boss'
                say("Oke boss")
                webbrowser.open("https://www.google.com")

        
            if (message == 'my position now'):
                print 'ZOke boss'
                say("Oke boss")
                lokasi = webbrowser.open("https://www.google.com/maps/place/")
                time.sleep(2)

                
            if (message == 'shutdown computer'):
                os.system('shutdown now')
                shutdown()
            

            if (message == 'halo' or message == 'tes' or message == 'tes 123'):
                print 'Haloo boss'
                say("Haloo boss")
                time.sleep(2)


                                
        except:
            #call(['espeak', 'Silahkan ulangi'])
            print 'Please, speak again...'
            time.sleep(1)



if __name__ == '__main__':

    while True:
        listen_master()
    

    

