from fastapi import FastAPI
from app import execute_asr_cap_en

import wave


app = FastAPI()

# Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)

from typing import Annotated

from fastapi import FastAPI, File, Form
    
@app.post("/api/audio-file")
async def upload_file(
    audio_file_path: Annotated[str, Form()],
):
    asr_out=execute_asr_cap_en.calling_asr(audio_file_path,"en_ID")
    return {"out-put-string": asr_out}
