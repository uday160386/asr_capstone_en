from fastapi import FastAPI

from random import randrange
from models.SoundConversion import VoiceData

import scripts.execute_asr_cap_en as execute_asr_cap_en
from scripts import download_from_blob
import os.path

TEMP_AUDIO_FILES =  "test_audio_files/temp/"

app = FastAPI()

# Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)
    
@app.post("/api/audio-file")
async def upload_file(payload: VoiceData):
    rand_audio_number = randrange(100000)
    filePath = TEMP_AUDIO_FILES+payload.audio_file_path+'_'+str(rand_audio_number)
    
    status = download_from_blob.download_blog_file_content_to_wav(payload.audio_file_path,filePath+'.wav')

    asr_out=execute_asr_cap_en.calling_asr(filePath+'.wav', payload.lang_id)
    os.remove(filePath+'.wav')
    return {"out-put-string": asr_out}

