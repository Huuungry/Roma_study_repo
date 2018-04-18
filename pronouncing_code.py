from tempfile import TemporaryFile
import playsound
import time
from gtts import gTTS
import os
from pygame import mixer  # Load the required library


def save_file(input):
    tts = gTTS(text=input, lang='ru', slow=False)

    # f = TemporaryFile()
    # tts.write_to_fp(f)
    # f.close()

    file_name="test"+".mp3"
    tts.save(file_name)
    # playsound.playsound(file_name, False)

    return file_name
def pronounce(file_name):
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    time.sleep(5)
    print(file_name)
    os.system('rm %s' % file_name)

save_file("Юра")
pronounce(save_file("20"))
# time.sleep(5)
#
# pronounce("Привет-привет Юра")

# if __name__ == "__main__":
#     # stuff only to run when not called via 'import' here
#     pronounce()
