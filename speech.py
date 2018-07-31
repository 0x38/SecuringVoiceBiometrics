import io
import os
import wave
import scipy.io.wavfile

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# from google.cloud import storage
import scipy.io.wavfile as wav
# import audiotools
from pydub import AudioSegment
# filepath_wav = 'music.wav'
# filepath_flac = filepath_wav.replace(".wav", ".flac")
# audiotools.open(filepath_wav).convert(filepath_flac, audiotools.FlacAudio, compression_quality)
class SpeechtoText():
    def __init__(self,filepath):
        rate,data = wav.read(filepath)
        print rate
        song = AudioSegment.from_wav(filepath)
        song.export("flacfile.flac",format = "flac")
        self.file_name = "flacfile.flac"
        self.sample_rate_hertz = rate


    def speechtotext(self):
        client = speech.SpeechClient()

        with io.open(self.file_name, 'rb') as audio_file:
            content = audio_file.read()
            print type(content)
            audio = types.RecognitionAudio(content=content)
            print type(audio)
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
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'dynamic.wav')
    obj = SpeechtoText("statictemp.wav")
    print (obj.speechtotext())
