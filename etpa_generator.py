import glob
import json
import os.path

from mutagen.mp3 import MP3

if __name__ == "__main__":

    # Source folder path where JSON files are stored
    json_folder_path = "<JSON_FOLDER_PATH>"

    # Folder path for mp3 files
    audio_folder_path = "<AUDIO_FOLDER_PATH>"

    # Destination folder path to store ETPA files
    etpa_folder_path = "<ETPA_FOLDER_PATH>"

    # Iterate through all the JSON files in a folder
    for file in glob.glob(json_folder_path + "\\*.json"):
        # Store transcript text file name
        filename = os.path.splitext(os.path.basename(file))[0]
        # Construct audio file path using JSON file name
        audio = MP3(audio_folder_path + "\\" + filename + ".m4a")

        # Retrieve audio length from audio file
        audio_length = round(audio.info.length, 3)

        # Open JSON file in read mode
        json_file = open(file, 'r', encoding='utf-8')

        # Read data from the JSON file
        data = json_file.read()

        # Close JSON file
        json_file.close()

        # Word list to store data for each word
        json_row_list = data.split("\n")

        # Remove empty last element from the list
        if json_row_list[len(json_row_list) - 1] == "":
            json_row_list = json_row_list[:len(json_row_list) - 1]

        # Stores all the words
        word_list = []

        # Iterate through all the rows in JSON data to generate word list
        for i in range(0, len(json_row_list)):
            # Parse JSON string to dictionary
            json_row_list[i] = json.loads(json_row_list[i])

            # Append word to word list
            word_list.append(json_row_list[i]['value'])

        # Generate sentence from word list
        sentence = " ".join(word_list)

        # Generate ETPA string
        etpa_string = '<xml>' + "\n" + \
                      "\t" + '<creator program="PhraseAnal 1.14" user="MAQUser" />' + "\n" + \
                      "\t" + '<url >' + audio_folder_path + filename + '.aif</url>' + "\n" + \
                      "\t" + '<timings text=\"' + sentence + '\">'

        # Iterate through all the rows in JSON data to generate ETPA string
        for i in range(0, len(json_row_list)):
            # Use audio length as end time for last word
            if i == len(json_row_list) - 1:
                etpa_string = etpa_string + "\n" + "\t\t" + \
                              '<timing id=\"' + str(i) + '\" start=\"' + str(
                    json_row_list[i]['time'] / 1000) + '\" end=\"' + str(
                    audio_length) + '\" startframe=\"0\" framelength=\"0\"' + ' text=\"' \
                              + json_row_list[i]['value'] + '\"/>'

            # Use end time from the "time" key in JSON data
            else:
                etpa_string = etpa_string + "\n" + "\t\t" + \
                              '<timing id=\"' + str(i) + '\" start=\"' + str(
                    json_row_list[i]['time'] / 1000) + '\" end=\"' + str(
                    json_row_list[i + 1][
                        'time'] / 1000) + '\" startframe=\"0\" framelength=\"0\"' + ' text=\"' + \
                              json_row_list[i]['value'] + '\"/>'

        etpa_string = etpa_string + "\n" + "\t" + "</timings>" + "\n" + "</xml>"

        # Open ETPA file in write mode
        etpa_file = open(etpa_folder_path + "\\" + filename +
                         ".etpa", encoding='utf-8', mode='w')
        etpa_file.write(etpa_string)
        etpa_file.close()
