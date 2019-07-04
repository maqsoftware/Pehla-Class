# Localization of audio files

## Process
There are three key steps in generating localized audio files:

1. **Generate audio files:** Generate audio instructions in local language and English content in local accent using transcripts and Amazon Polly.
2. **Generate JSON files:** Generate JSON files to store timestamps for highlighting text using Amazon Polly.
3. **Generate ETPA files:** Generate ETPA files used by the application for highlighting text using the JSON file.

## Pre-requisites
1. Register for [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/getting-started.html) service and retrieve the access key id, secret access key and region name.
2. Download and install [Python 3](https://www.python.org/downloads/) to run the Python scripts.
3. Install boto3 Python package to request audio and JSON data from Amazon Polly using the following command:  
    `pip install boto3`
4. Install mutagen Python package to retrieve audio metadata using the following command:  
    `pip install mutagen`

## 1. Generate audio files
### Generating audio instructions in local language
1. Audio files in local language need to be generated for all the instructions in [GLEXP-Team-onebillion-Hindi-assets](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets) repository's folders.
2. Generate locale-specific transcripts using English transcripts stored in [assets/transcripts](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/blob/master/assets/transcripts)/MODULE/english folder for audio instructions and store them in assets/transcripts/MODULE/LOCALE folder.  
**Note:** Save the text files using **UTF-16-LE** encoding.
3. Configure the [audio_json_generator.py](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi/blob/master/audio_json_generator.py) script to generate locale-specific audio files as follows:
    * Set the Amazon Polly credentials as follows:
      ```python
      # Initialize Amazon Polly Client
      polly_client = boto3.Session(
          aws_access_key_id="<YOUR_ACCESS_KEY_ID>",
          aws_secret_access_key="<YOUR_SECRET_ACCESS_KEY>",
          region_name="<YOUR_AMAZON_POLLY_REGION>"
      ).client("polly")
      ```
    * Set the transcript folder path where locale-specific transcripts are stored in *transcript_folder_path* variable and the output folder path where locale-specific audio files need to be stored in *output_folder_path* variable as follows:
      ```python
      # Source folder path where transcripts are stored
      transcript_folder_path = "<TRANSCRIPT_FOLDER_PATH>"
      # Destination folder path to store JSON/audio files
      output_folder_path = "<DESTINATION_FOLDER_PATH>"
      ```
    * If you plan to use SSML tags, adjust the speech rate by setting a percentage value in *prosody_rate* variable as follows:
      ```python
      # Adjust the speech rate
      prosody_rate = "80%"
      ```
      **Note:** Refer the supported SSML tags in Amazon Polly [documentation](https://docs.aws.amazon.com/polly/latest/dg/supported-ssml.html).  
    * If you don't plan to use the SSML tags, comment the variables as follows:
      ```python
      # SSML tags for Amazon Polly
      # speak_start_tag = "<speak>\n"
      # speak_end_tag = "</speak>"
      # Adjust the speech rate
      # prosody_rate = "80%"
      # prosody_start_tag = "\n<prosody rate=\"" + prosody_rate + "\">"
      # prosody_end_tag = "</prosody>"
      .
      .
      .
      # Generate text with SSML tags
        # data = speak_start_tag + prosody_start_tag + \
            # data + prosody_end_tag + speak_end_tag
      ```
    * Set the voice id in *synthesize_speech* function to generate locale-specific audios as follows:
      ```python
      # Retrieve JSON response with timestmaps from Amazon Polly
      if (sys.argv[1] == "0"):
          response = polly_client.synthesize_speech(
              VoiceId="<LOCALE_SPECIFIC_VOICE_ID>",
              OutputFormat=output_format,
              TextType="ssml",
              SpeechMarkTypes=['ssml', 'word'],
              Text=data
          )
      # Retrieve audio response from Amazon Polly
      else:
          response = polly_client.synthesize_speech(
              VoiceId="<LOCALE_SPECIFIC_VOICE_ID>",
              OutputFormat=output_format,
              TextType="ssml",
              Text=data
          )
      ```
       **Note:** Refer the supported Voice IDs in Amazon Polly [documentation](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#API_SynthesizeSpeech_RequestSyntax).  
4. Run the *audio_json_generator.py* Python script using the following command:  
    `python audio_json_generator.py 1`  
    **Note:** Argument value "0" generates JSON files and "1" generates audio files.
5. Replace the generated locale-specific audio files in assets/MODULE/local/en_GB folder.

### Generating audios in local English accent
1. Audio files in local English accent need to be generated for the following folders:  
    * [assets/oc-bubblewrap](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-bubblewrap)  
    * [assets/oc-echobox](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-echobox)  
    * [assets/oc-literacy-gen](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-literacy-gen)  
    * [assets/oc-phrases](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-phrases)  
    * [assets/oc-prepr3](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-prepr3)  
    * [assets/oc-reading/books](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-reading/books)  
    * [assets/oc-wordproblems](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/tree/master/assets/oc-wordproblems)  
2. English transcripts for the English content are stored in [assets/transcripts](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/blob/master/assets/transcripts)/MODULE/english folder.
English transcripts for the stories are stored in [assets/transcripts/oc-reading](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi-assets/blob/master/assets/transcripts/oc-reading)/STORY/english folder.
3. Configure the [audio_json_generator.py](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi/blob/master/audio_json_generator.py) script to generate locale-specific English accent audio files as mentioned in [Generating audio instructions in local language](#generating-audio-instructions-in-local-language) section's step 3.
4. Run the *audio_json_generator.py* Python script using the following command:  
    `python audio_json_generator.py 1`  
    **Note:** Argument value "0" generates JSON files and "1" generates audio files.
5. Replace the generated locale-specific English accent audio files in assets/MODULE/local/en_GB and assets/oc-reading/books/STORY/local/en_GB folders.

## 2. Generate JSON files
1. JSON files need to be generated for the modules which contain ETPA files.
2. Configure the [audio_json_generator.py](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi/blob/master/audio_json_generator.py) script to generate JSON files as mentioned in [Generating audio instructions in local language](#generating-audio-instructions-in-local-language) section's step 3.
3. Run the *audio_json_generator.py* Python script using the following command:  
    `python audio_json_generator.py 0`  
    **Note:** Argument value "0" generates JSON files and "1" generates audio files.  

## 3. Generate ETPA files
1. EPTA files will be generated using the JSON files generated in above section.
2. Configure the [etpa_generator.py](https://github.com/maqsoftware/GLEXP-Team-onebillion-Hindi/blob/master/etpa_generator.py) script as follows:
    * Set the JSON folder path where the JSON files generated in previous section are stored in *json_folder_path* variable, audio folder path where the corresponding audio files are stored in *audio_folder_path* variable and ETPA folder path where the ETPA files will be stored in *etpa_folder_path* variable as follows:
      ```python
      # Source folder path where JSON files are stored
      json_folder_path = "<JSON_FOLDER_PATH>"

      # Folder path for mp3 files
      audio_folder_path = "<AUDIO_FOLDER_PATH>"

      # Destination folder path to store ETPA files
      etpa_folder_path = "<ETPA_FOLDER_PATH>"
      ```
3. Run the *etpa_generator.py* Python script using the following command:  
    `python etpa_generator.py`
4. Replace the generated ETPA files in their respective folders.
