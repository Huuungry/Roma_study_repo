import time
import recognizing_code as rc
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
speak.Speak("Hi there")


print("Как тебя зовут?")
listen = rc.try_to_recognise()
time.sleep(2)

print("A лет сколько?")
listen
time.sleep(2)

