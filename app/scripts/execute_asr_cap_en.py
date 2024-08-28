
import speech_recognition as sr
import traceback

r = sr.Recognizer()

out_file_path="result_out.txt"

def calling_asr(wav_file,lid):
    AUDIO_FILE=wav_file
    text="cant read wav file"
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language=lid)
        record_text("\t"+text)
        return text
    except Exception:
        traceback.print_exc()
        record_text(" "+"Error in segement"+" ")
        return text
    
    #file.close()

def record_text(asr_out):
     with open(out_file_path, 'a') as file:
        file.write("{}\n".format(asr_out))
   
