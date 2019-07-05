from google.cloud import texttospeech
from shutil import copyfile
import random
import os
import google.api_core.exceptions as core_exc
import google.auth.exceptions as auth_exc
from sys import exit


def gen_speech(num, **kwargs):
    # Instantiates a client
    try:
        client = texttospeech.TextToSpeechClient()
    except auth_exc.DefaultCredentialsError as e:
        print("Exiting Program. Make sure to set environment variable "
              "GOOGLE_APPLICATION_CREDENTIALS to the path of your google "
              "project json file.\n This is step 5 at "
              "https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries")
        exit(1)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=f'{num}')

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='ja-JP',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type

    def write_response():
        if not response and kwargs["prev_file"]:
            return kwargs["prev_file"]
        elif not response and not kwargs["prev_file"]:
            print("whoops. Should get an error soon")
        else:
            if kwargs["prev_file"]:
                os.remove(kwargs["prev_file"])
            # The response's audio_content is binary.
            with open('output.mp3', 'wb') as out:
                # Write the response to the output file.
                out.write(response.audio_content)

            # unfortunately even with setting block=False on playsound(), playsound
            # keeps a file open (I believe) and doesn't allow me to write to the file
            # as I do down below. Errno 13 Permission denied is thrown. I'm on Win 10.
            # Also, I searched far and wide for an alternative to playsound that can play
            # mp3 files. I was not successful in finding an easy solution. An example of
            # playsound keeping the file open may be that the files don't seem to be officially
            # deleted until after the program finishes running. With ctrl C signal.
            rand_num = random.randint(1, 10000)
            tmp_file = f'tempfile{rand_num}.mp3'
            try:
                with open(tmp_file, 'wb') as tmp:
                    pass
            except PermissionError as e:
                print("Permissions error")
                # just retry. If it errors again just close the program. No big deal
                rand_num = random.randint(1, 10000)
                tmp_file = f'tempfile{rand_num}.mp3'
                with open(tmp_file, 'wb') as tmp:
                    pass

            copyfile("output.mp3", tmp_file)
            return tmp_file

    try:
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.

    except core_exc.InternalServerError as e:
        print(e)
        response = None

    tmp_file = write_response()
    return tmp_file
