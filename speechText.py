import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ttaylor_speech.json'
speechClient = speech.SpeechClient()

def speechToText(audioSource):

    if audioSource.startswith(b'gs:'):
        #Cloud Hosted Files
        #cloudURL = 'gs://ttaylor-speech-to-text/testSpeech2.wav'
        rawAudio = speech.RecognitionAudio(uri = audioSource)
    else:
        #Local Files
        #Open file
        with open(audioSource, 'rb') as file:
            audioData = file.read()
        #Transcribe audio
        rawAudio = speech.RecognitionAudio(content = audioData)


    #Configue media output
    configRec = speech.RecognitionConfig(
        sample_rate_hertz = 48000,
        enable_automatic_punctuation = True,
        language_code = 'en-US',
        audio_channel_count = 2
        )

    #Transcribe recAudio object
    respon = speechClient.recognize(config = configRec, audio = rawAudio)

    print(respon)

#if __name__ == '__main__':
    #speechToText('gs://ttaylor-speech-to-text/testSpeech2.wav')
    #speechToText('testSpeech1.wav')
