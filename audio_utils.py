from pydub import AudioSegment

SUPPORTED = [
    "wav",
    "mp3",
    "ogg",
    "m4a",
    "flac"
]

def convert_to_wav(input_file):

    ext = input_file.split(".")[-1]

    if ext not in SUPPORTED:
        raise Exception("Unsupported audio format")

    sound = AudioSegment.from_file(input_file)

    output = input_file.replace("." + ext, ".wav")

    sound.export(output, format="wav")

    return output
