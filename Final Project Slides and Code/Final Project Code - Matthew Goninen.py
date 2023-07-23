#Importing SpeechRecognition, gTTS, playsound, OpenAI, and os Libraries
import speech_recognition as sr
from gtts import gTTS
import playsound
import openai
import os

gptKey = "INPUT YOUR KEY HERE"

name = "JOHN"
admin = "Matthew"

#Defining Function, Printing Text, Calling Voice Function with Input (from String & Variable),
def welcome(text):
        tts = gTTS(text)
        audioFile = 'welcomeAudio.mp3'
        tts.save(audioFile)
        playsound.playsound(audioFile)
        os.remove(audioFile)

print("Welcome to " + name + ". How are you, " + admin + "?")
welcome("Welcome to " + name + ". How are you, " + admin + "?")

#While Loop to Input Questiosn with Microphone and Outputs Questions in Voice with gTTS and playsound
useCompleted = False
while useCompleted == False:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        audioPrompt = r.recognize_google(audio)
        
    print("Generating Response...")

    def generate(input):
      openai.api_key = gptKey
      response = openai.Completion.create(model="text-davinci-003",
                                          prompt=input,
                                          temperature=0,
                                          max_tokens=1000,
                                          top_p=1,
                                          frequency_penalty=0,
                                          presence_penalty=0
    )
      return response.choices[0]['text']

    gptResponse = generate(audioPrompt)
    
    def voiceReply(text):
        tts = gTTS(text)
        audioFile = 'voiceReply.mp3'
        tts.save(audioFile)
        playsound.playsound(audioFile)
        os.remove(audioFile)
    
    print(gptResponse)
    voiceReply(gptResponse)

