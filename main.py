# We can transcribe audio using assemblyAI

# Steps:
# 1. Upload the file to Assembly AI
# 2. Start the transcription
# 3. Wait for the transcription to finish (keep polling the API)
# 4. Get the transcription (save)

# Call the functions
import sys
from api_communication import *

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)