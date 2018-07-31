import io
import os
import wave
import scipy.io.wavfile

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import storage
import scipy.io.wavfile as wav
# import audiotools
from pydub import AudioSegment
import re
# filepath_wav = 'music.wav'
# filepath_flac = filepath_wav.replace(".wav", ".flac")
# audiotools.open(filepath_wav).convert(filepath_flac, audiotools.FlacAudio, compression_quality)
class SpeechtoText():
    def __init__(self,filepath,sample_rate):
        rate,data = wav.read(filepath)
        song = AudioSegment.from_wav(filepath)
        song.export("flacfile.flac",format = "flac")
        self.file_name = "flacfile.flac"
        self.sample_rate_hertz = 44100


    def speechtotext(self):
        client = speech.SpeechClient()

        with io.open(self.file_name, 'rb') as audio_file:
            content = audio_file.read()
            # print type(content)
            audio = types.RecognitionAudio(content=content)
            # print type(audio)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz = self.sample_rate_hertz,
            language_code='en-US')

        response = client.recognize(config, audio)
        print("Response recieved")
        print (response)
        for result in response.results:
            return ('Transcript: {}'.format(result.alternatives[0].transcript))

if __name__ == "__main__":
    obj = SpeechtoText("statictemp.wav",44100)
    string = obj.speechtotext()
    # string = "the time is 5:05 a.m. the time is 5 a.m. the time is 12 p.m. the time is 1:01 a.m."
    print re.findall(r'(\d{1,2}:?\d{1,2}\ [aApP]\.[mM]\.)', string)
    # re.findall(r'(\d{1,2}:?\d{1,2})', string)
# \d{1,2}(?:(?:am|pm)|(?::\d{1,2})(?:am|pm)?)
