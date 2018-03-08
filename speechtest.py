import io
import os
import wave
import scipy.io.wavfile

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class SpeechtoText():
    def __init__(self,filepath,sample_rate):
        self.file_name = filepath
        self.sample_rate_hertz = sample_rate

    def speechtotext(self):
        client = speech.SpeechClient()

        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = self.sample_rate_hertz,
            language_code='en-US')

        response = client.recognize(config, audio)
        print("Response recieved")
        print (response)
        for result in response.results:
            return ('Transcript: {}'.format(result.alternatives[0].transcript))

if __name__ == "__main__":
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'male.wav')
    obj = SpeechtoText(file_name,8000)
    print (obj.speechtotext())
