import pyaudio
import wave
import speech_recognition as sr
import nltk

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print('Recording...')
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ('Recording...')
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

r = sr.Recognizer()

with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    audio = r.record(source) # read the entire audio file


# recognize speech using Google Speech Recognition
try:
    speech = r.recognize_google(audio)
    print(speech)

    tokens = nltk.word_tokenize(speech)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged[0:6])

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

