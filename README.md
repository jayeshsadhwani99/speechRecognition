# Speech Recognition

This project is made to transcribe the results of an audio to a text file using
[AssemblyAI]('https://www.assemblyai.com/')

## Steps

We can transcribe audio using assemblyAI

> These are basically just functions written in main.py

Steps:

1.  Upload the file to Assembly AI

2.  Start the transcription

3.  Wait for the transcription to finish (keep polling the API)

4.  Get the transcription (save)

## To run

1. Add a file

   `api_secrets.py`

   with the data as

   ```
   API_KEY_ASSEMBLYAI= "YOUR-API-KEY"
   ```

2. Install the requirements (only 1 - requests)

   `pip install -r requirements.txt`

   NOTE: I don't think there is a need for a venv here
   since we only have the requests and it's pretty standard and you can have it installed globally

3. Run

   `python3 main.py audio_file_name`
