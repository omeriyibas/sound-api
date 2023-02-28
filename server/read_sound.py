import wave

import pyaudio
from playsound import playsound
import speech_recognition as sr

recognizer = sr.Recognizer()

def read_sound():
    # playsound("sound.wav")
    try:
        with sr.AudioFile("sound.wav") as source:
            # recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            text=recognizer.recognize_google(audio,language="tr-TR")
    except:
        text=""

    return text


    # print(text)

    # chunk = 1024
    #
    # # Open the soaudio/sound file
    # af = wave.open("sound.wav", 'rb')
    #
    # # Create an interface to PortAudio
    # pa = pyaudio.PyAudio()
    #
    # # Open a .Stream object to write the WAV file
    # # 'output = True' indicates that the
    # # sound will be played rather than
    # # recorded and opposite can be used for recording
    # stream = pa.open(format=pa.get_format_from_width(af.getsampwidth()),
    #                  channels=af.getnchannels(),
    #                  rate=af.getframerate(),
    #                  output=True)
    #
    # # Read data in chunks
    # rd_data = af.readframes(chunk)
    #
    # # Play the sound by writing the audio
    # # data to the Stream using while loop
    # while rd_data != '':
    #     stream.write(rd_data)
    #     rd_data = af.readframes(chunk)
    #
    # # Close and terminate the stream
    # stream.stop_stream()
    # stream.close()
    # pa.terminate()
