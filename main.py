# We can transcribe audio using assemblyAI

# Steps:
# 1. Upload the file to Assembly AI
# 2. Start the transcription
# 3. Wait for the transcription to finish (keep polling the API)
# 4. Get the transcription (save)

import requests
import sys
from api_secrets import API_KEY_ASSEMBLYAI


# Step 1
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcription_endpoint = "https://api.assemblyai.com/v2/transcript"
filename = sys.argv[1]
headers = {'authorization': API_KEY_ASSEMBLYAI, "content-type": "application/json"}

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = response.json()['upload_url']
    return audio_url

# Step 2
def transcribe(audio_url):
    json = { "audio_url": audio_url }
    response = requests.post(transcription_endpoint, json=json, headers=headers)
    job_id = response.json()['id']
    return job_id

# Step 3
def poll(job_id):
    polling_endpoint = transcription_endpoint + "/" + job_id
    response = requests.get(polling_endpoint, headers=headers)
    return response.json()

def transcription_result_url(audio_url):
    job_id = transcribe(audio_url)
    while True:
        response = poll(job_id)
        if response['status'] == 'completed':
            return response, None
        elif response['status'] == 'error':
            return response, response["error"]

# Step 4
def save_transcript(audio_url):
    data, error = transcription_result_url(audio_url)
    if data:
        text_filename = filename + ".txt"
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print("Transcription saved to " + text_filename)
    elif error:
        print("Error: " + error)

# Call the functions
audio_url = upload(filename)
save_transcript(audio_url)