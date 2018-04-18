import time
from recognizing_code import try_to_recognise
from win32com.client import Dispatch
import pronouncing_code as prc


# speak = Dispatch("SAPI.SpVoice")
# speak.Speak("Hi there")
#
#
# print("Как тебя зовут?")
# try_to_recognise()
# time.sleep(2)
prc.pronounce("10")
prc.pronounce("Тест")

# print("A лет сколько?")
# try_to_recognise()
#
# time.sleep(2)

