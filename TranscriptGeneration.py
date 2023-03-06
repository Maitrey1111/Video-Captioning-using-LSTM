import moviepy
import moviepy.editor
import speech_recognition as sr
from os import path
from pydub import AudioSegment
 
clip_name = "vid2"

#Load the Video Clip
video = moviepy.editor.VideoFileClip("./videos/"+ clip_name + ".mp4")
#Extract and export the Audio
video.audio.write_audiofile("./audios/"+ clip_name +"_audio.mp3")

#convert mp3 to wav
audio_file = "./audios/"+ clip_name +"_audio.mp3"
sound = AudioSegment.from_mp3(audio_file)
sound.export("./audios/"+ clip_name +"_audio.wav", format="wav")

#generate transcript
r = sr.Recognizer()
with sr.AudioFile("./audios/"+ clip_name +"_audio.wav") as source:
        audio = r.record(source)  # read the entire audio file                  

text = ""
try:
    text = r.recognize_google(audio)
except Exception as e:
    print("Exception: "+str(e))

print("\nText: \n"+ text)