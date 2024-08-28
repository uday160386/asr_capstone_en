from pydantic import BaseModel

class VoiceData(BaseModel):
    audio_file_path: str
    lang_id: str