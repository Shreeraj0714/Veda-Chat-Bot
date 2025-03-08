import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import time
import wikipedia
import pywhatkit as pwk
import smtplib, ssl
import userPass

 


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
        # recognize speech using ShreeAI Speech Recognition
        try:
            content = r.recognize_google(audio,language='en-IN')
            print("Veda Speech Recognition thinks you said : " + content)
        except Exception as e:
            print("Please try again...")
            
        return content
    
def main_process():
    while True:
        request = command().lower()
        if"hello" in request:
            speak("Hello, How can I help you?")
            
        elif"hi" in request:
            speak("Hello, How can I help you?")
            
        elif"how are you veda" in request:
            speak("I'm doing great, thank you! How can I assist you today?")
            
        elif"how are you" in request:
            speak("I'm doing great, thank you! How can I assist you today?")
            
        elif"how r u" in request:
            speak("I'm doing great, thank you! How can I assist you today?")
            
        elif"what is veda" in request:
            print("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
            speak("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
                        
        elif"why your name is veda" in request:
            print("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
            speak("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
           
        elif"Vada stands for" in request:
            print("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
            speak("Veda stands for Virtual Assistant for Daily Activities. The name 'Veda' is inspired by 'Ved,' an ancient Indian tradition of engaging in meaningful dialogue and discussions. Just as Vade encourages knowledge sharing, Vada the chatbot is designed by Shree,raj, to offer intelligent, insightful, and helpful assistance to make your daily activities easier.")
                        
        elif "play song" in request:
            speak("playing song")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://open.spotify.com/track/52itZ0w0CydihB2JCZEIft?si=cb09e7e830a94f11")
            elif song == 2:
                webbrowser.open("https://open.spotify.com/track/1tPPINau3vBP8Q89JTn0ER?si=14a1fcf5fb114395")
            elif song == 3:
                webbrowser.open("https://youtu.be/AGsn2ycFRqI")
                
        elif"ok bye" in request:
            speak("bye, have a good day")
            
        elif"bye" in request:
            speak("bye, have a nice day")
        
        elif "current time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
            
        elif "time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
            
        elif "today's date" in request:
            now_time = datetime.datetime.now().strftime("%d %m %y")
            speak("Todays date is " + str(now_time))
            
        elif "date" in request:
            now_time = datetime.datetime.now().strftime("%d %m %y")
            speak("Todays date is " + str(now_time))
            
        elif "date today" in request:
            now_time = datetime.datetime.now().strftime("%d %m %y")
            speak("Todays date is " + str(now_time))
        
        elif "new task" in request:
            task = request.replace("new task","")
            task = task.strip()
            if task != "":
                speak("Adding new task " + task)
                with open("todo.txt","a") as file:
                    file.write(task + "\n")
                  
        elif "my task today" in request:
            with open("todo.txt","r") as file:
                speak("Work u have to do is " + file.read())
                
        elif "show task" in request:
            with open("todo.txt","r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's Work",
                message = tasks    
            )
            
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's Work",
                message = tasks    
            )
            
        elif "delete task" in request:
            task_to_delete = request.replace("delete task", "").strip()
            with open("todo.txt", "r") as file:
                tasks = file.readlines()
            with open("todo.txt", "w") as file:
                for task in tasks:
                    if task.strip() != task_to_delete:
                        file.write(task)
            speak(f"Deleted task: {task_to_delete}")
            
        
        elif "take screenshot" in request:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{timestamp}.png"
            screenshot.save(filename)
            speak(f"Screenshot taken and saved ")
            
            
        elif "open" in request:
            query = request.replace("open","")
            pyautogui.press("win")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            
        elif"search wikipedia" in request:
            request = request.replace("veda","")
            request = request.replace("search wikipedia","")
            print("Searching Wikipedia...")
            result = wikipedia.summary(request,sentences=2)
            speak(result)
            
        elif"search google" in request:
            request = request.replace("veda","")
            request = request.replace("search google","")
            print("Searching google...")
            webbrowser.open("http://www.google.com/search?q=" + request)
            
        elif"send whatsapp" in request:
            pwk.sendwhatmsg("+918369926907","Hi i am veda how are u",21,47)
            
        elif"send email" in request:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("jadhavshreeraj2020@gmail.com",userPass.email_password)
            message = """
            This is messgage from VEDA
            
            Thanks from shree
            
            """
            s.sendmail("jadhavshreeraj14@outlook.com","jadhavshreeraj2020@gmail.com",message)
            s.quit()
            speak("Email sent successfully")
            
         
         
        
        
        
main_process()
        
    