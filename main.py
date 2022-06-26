# We can transcribe audio using assemblyAI

# Steps:
# 1. Upload the file to Assembly AI
# 2. Start the transcription
# 3. Wait for the transcription to finish (keep polling the API)
# 4. Get the transcription (save)

from email.mime import audio
import requests
import sys
from api_secrets import API_KEY_ASSEMBLYAI


# Step 1
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcription_endpoint = "https://api.assemblyai.com/v2/transcript"
filename = sys.argv[1]

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))

print(response.json())

audio_url = response.json()['upload_url']

# Step 2
json = { "audio_url": audio_url }
headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}
response = requests.post(transcription_endpoint, json=json, headers=headers)
print(response.json())