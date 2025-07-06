import os
from pipes import quote
import re
import sqlite3
import subprocess
import time
import webbrowser
from playsound import playsound
import eel

import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").lower().strip()
    app_name = query

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + query)
                path = results[0][0]
                print(f"[DEBUG] Attempting to open: {path}")
                try:
                    os.startfile(path)
                except Exception as e:
                    print(f"[ERROR] os.startfile failed for {path}: {e}")
                    speak("Failed to open application.")
            else: 
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if results:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except Exception as e:
                        print(f"Error opening with os.system: {e}")
                        speak("Not found")
        except Exception as e:
            print(f"Error in openCommand: {e}")
            speak("Something went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

# Removed hotword detection using pyaudio and porcupine

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove).strip().lower()

    try:
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
                       ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('Not found in contacts')
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "Message sent successfully to " + name
    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "Calling " + name
    else:
        target_tab = 6
        message = ''
        jarvis_message = "Starting video call with " + name

    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl', 'f')
    for _ in range(1, target_tab):
        pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    speak(jarvis_message)

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    speak(response)
    return response

def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")
    speak("Calling " + name)
    os.system('adb shell am start -a android.intent.action.CALL -d tel:' + mobileNo)

def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("Sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    tapEvents(136, 2220)
    tapEvents(819, 2192)
    adbInput(mobileNo)
    tapEvents(601, 574)
    tapEvents(390, 2270)
    adbInput(message)
    tapEvents(957, 1397)
    speak("Message sent successfully to " + name)
