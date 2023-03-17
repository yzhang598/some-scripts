# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# By default, the Whisper API only supports files that are less than 25 MB. 
# If you have an audio file that is longer than that, you will need to break it up into chunks of 25 MB's or less or used a compressed audio format. 
# ================================================
# This script will help convert sound files to text files. You need provide your openAI token and the audio filename.
# Put the audio file in the same directory with the script.
# ================================================

import openai
from os import getcwd, path

def convert_sound_to_text(audio_name):
    audio_path = getcwd() + "/" + audio_name
    audio_file= open(audio_path, "rb")
    name = path.splitext(path.basename(audio_path))[0]
    transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="text")
    return name, transcript

def write_output_to_file(transcript, name='output.txt'):
    file_name = name + ".txt"
    with open(file_name, 'w') as file:
        file.write(transcript)
        print ("Successfully wrote output in file: " + file_name)

def main():
    openai.api_key = input("Please provide an API key: ")
    # For example: audio1.m4a
    audio_name = input("Please provide the audio name: ")
    name, output = convert_sound_to_text(audio_name)
    write_output_to_file(output, name)

if __name__ == '__main__':
    main()