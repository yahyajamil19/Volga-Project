import azure.cognitiveservices.speech as speechsdk

speech_key = "YOUR_AZURE_SPEECH_KEY"
service_region = "eastus"

def transcribe_audio(audio_file):

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key,
        region=service_region
    )

    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    result = speech_recognizer.recognize_once()

    return {
        "language": "en-US",
        "text": result.text,
        "segments": [
            {
                "start": 0,
                "end": 0,
                "text": result.text
            }
        ]
    }
