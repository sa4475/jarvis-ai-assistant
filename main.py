import os
import eel
import pyaudio

print("[DEBUG] Imported modules.")

mic = pyaudio.PyAudio()
print("[DEBUG] Initialized pyaudio.")

from engine.features import *
print("[DEBUG] Imported features.")
from engine.command import *
print("[DEBUG] Imported command.")
from engine.auth import recoganize
print("[DEBUG] Imported recoganize.")

def start():
    print("[DEBUG] Entered start() function.")
    eel.init("www")
    print("[DEBUG] eel.init done.")
    playAssistantSound()
    print("[DEBUG] playAssistantSound done.")
    @eel.expose
    def init():
        # subprocess.call([r'device.bat'])  # Bypassed device setup for development without device
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    print("[DEBUG] Before opening browser.")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    print("[DEBUG] After opening browser.")
    eel.start('index.html', mode=None, host='localhost', block=True)
    print("[DEBUG] eel.start done.")

if __name__ == "__main__":
    try:
        print("[DEBUG] Calling start() from __main__.")
        start()
    except Exception as e:
        print(f"Startup error: {e}")