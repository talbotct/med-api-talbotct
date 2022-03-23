import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ttaylor_speech.json'
speechClient = speech.SpeechClient()


#Local Files
def speechToText(audioSource):
    
    if audioSource.endswith('.wav'):
        #Open file
        fileLocal = 'testSpeech1.wav'

        with open(audioSource, 'rb') as file:
            audioData = file.read()

        #Transcribe audio
        audioLocal = speech.RecognitionAudio(content = audioData)

        #Configue media output
        configLocal = speech.RecognitionConfig(
            sample_rate_hertz = 48000,
            enable_automatic_punctuation = True,
            language_code = 'en-US',
            audio_channel_count = 2
            )

        #Transcribe recAudio object
        responseLocal = speechClient.recognize(config = configLocal, audio = audioLocal)

        print(responseLocal)

    else:
        #Cloud Hosted Files
        cloudURL = 'gs://ttaylor-speech-to-text/testSpeech2.wav'
        audioCloud = speech.RecognitionAudio(uri = cloudURL)

        configCloud = speech.RecognitionConfig(
            sample_rate_hertz = 48000,
            enable_automatic_punctuation = True,
            language_code = 'en-US',
            audio_channel_count = 2
        )

        responseCloud = speechClient.recognize(config = configCloud, audio = audioCloud)

        print(responseCloud)

if __name__ == '__main__':
    speechToText('testSpeech1.wav')
