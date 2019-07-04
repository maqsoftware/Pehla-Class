import codecs
import glob
import os.path
import sys

import boto3

if __name__ == "__main__":

    # Initialize data based on user input
    if sys.argv[1] == "0":
        # File extension to store JSON data
        output_file_extension = ".json"
        output_format = "json"
    else:
        # File extension to store audio
        output_file_extension = ".m4a"
        output_format = "mp3"

    # Source folder path where transcripts are stored
    transcript_folder_path = "<TRANSCRIPT_FOLDER_PATH>"
    # Destination folder path to store JSON/audio files
    output_folder_path = "<DESTINATION_FOLDER_PATH>"

    # SSML tags for Amazon Polly
    speak_start_tag = "<speak>\n"
    speak_end_tag = "</speak>"
    # Adjust the speech rate
    prosody_rate = "80%"
    prosody_start_tag = "\n<prosody rate=\"" + prosody_rate + "\">"
    prosody_end_tag = "</prosody>"

    # Initialize Amazon Polly Client
    polly_client = boto3.Session(
        aws_access_key_id="<YOUR_ACCESS_KEY_ID>",
        aws_secret_access_key="<YOUR_SECRET_ACCESS_KEY>",
        region_name="<YOUR_AMAZON_POLLY_REGION>"
    ).client("polly")

    # Iterate through all the transcript text files in a folder
    for file in glob.glob(transcript_folder_path + "\\*.txt"):
        # Store transcript text file name
        filename = os.path.splitext(os.path.basename(file))[0]
        # File path to store JSON/audio file
        outputfile = os.path.join(
            output_folder_path,
            filename + output_file_extension
        )

        # Open transcript text file in read mode
        text_file = open(file, 'r', encoding="utf-16-le")

        # Read data from the transcript text file
        data = text_file.read()

        # Close transcript text file
        text_file.close()

        # Read byte data to check whether Byte Order Mark (BOM) character exists
        byte_data = open(file, 'rb').read()

        # Remove BOM character from data if it exists
        if byte_data.startswith(codecs.BOM_UTF16_LE):
            data_list = data.split(' ')
            data_list[0] = data_list[0][1:]
            data = ' '.join(data_list)

        # Generate text with SSML tags
        data = speak_start_tag + prosody_start_tag + \
               data + prosody_end_tag + speak_end_tag

        # Retrieve JSON response with timestmaps from Amazon Polly
        if sys.argv[1] == "0":
            response = polly_client.synthesize_speech(
                VoiceId="Aditi",
                OutputFormat=output_format,
                TextType="ssml",
                SpeechMarkTypes=['ssml', 'word'],
                Text=data
            )
        # Retrieve audio response from Amazon Polly
        else:
            response = polly_client.synthesize_speech(
                VoiceId="Aditi",
                OutputFormat=output_format,
                TextType="ssml",
                Text=data
            )

        # Open JSON/audio file in write byte mode
        json_file = open(outputfile, 'wb')
        # Store the JSON/audio response in a JSON file
        json_file.write(response["AudioStream"].read())
        # Close JSON/audio file
        json_file.close()
