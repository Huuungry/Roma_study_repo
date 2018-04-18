import time
import recognizing_code as aa
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
speak.Speak("Hi there")


print("Как тебя зовут?")
aa.try_to_recognise()

time.sleep(2)

print("A лет сколько?")
aa.try_to_recognise()

time.sleep(2)

