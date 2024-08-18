from fastapi import FastAPI
from app import execute_asr_cap_en

import wave


app = FastAPI()

# Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)

from typing import Annotated

from fastapi import FastAPI, File, Form

mod_root = "test_audio_files/"
TRAIN_DATA_HOME =  mod_root+"tmp/"

@app.post("/api/audio-file")
async def post_media_file(uploaded_file: str):
    """
    Receive File, store to disk & return it
    """
    # Write file to disk. This simulates some business logic that results in a file sotred on disk
    
@app.post("/upload/")
async def upload_file(
    audio_bytes: Annotated[bytes, File()],
    file_name: Annotated[str, Form()],
):
    if len(audio_bytes) == 0:
       return {"Error":"Please send valid data for audio_bytes"}
    if len(file_name) == 0:
       return {"Error":"Please enter value for filename"}
    with wave.open(TRAIN_DATA_HOME+file_name+'.wav', 'wb') as wav_file: 
      wav_file.setnchannels(1) # Mono
      wav_file.setsampwidth(2) # Sample width in bytes
      wav_file.setnframes(78480)
      wav_file.setframerate(16000) # Sample rate
      wav_file.writeframes(audio_bytes)

    asr_out=execute_asr_cap_en.calling_asr(TRAIN_DATA_HOME+file_name+'.wav',"en_ID")
    return {"out-put-string": asr_out}
