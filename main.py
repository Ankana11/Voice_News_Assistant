"""News assistant project by using requests and json ,pyttsx3 and datetime module"""
import pyttsx3
import requests
import json
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")

if __name__== '__main__':
    WishMe()
    speak("Hi I am your news assistant. here is our todays news ")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=e57231eade29412a843937296b240cb2"
    news= requests.get(url).text
    news=json.loads(news)
    arts=news['articles']
    for articles in arts:
        speak(articles['title'])
        speak('moving to the next page..')
speak('thank you so much for listening')
