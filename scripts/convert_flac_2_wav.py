import sys, os
import shutil

import glob

mod_root = "test_audio_files/"
FLAC_HOME_FILES = mod_root+"LibriSpeech/test-clean/"
TRAIN_DATA_HOME =  mod_root+"wav"

def converting_wav_files():
    for path, subdirs, files in os.walk(FLAC_HOME_FILES):
        for name in files:
            if '.flac' in name:
                split_filename=name.split(".flac")
                get_sub_dir=split_filename[0].split('-')
                if not os.path.exists(TRAIN_DATA_HOME+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]):
                    os.makedirs(TRAIN_DATA_HOME+"/"+get_sub_dir[0]+"/"+ get_sub_dir[1])

                # converting data to .wav files
                shutil.copyfile(FLAC_HOME_FILES+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+name,
                TRAIN_DATA_HOME+"/"+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav' ) 

    print('Files converted to WAV sucussfully.....')

if __name__=='__main__':
    converting_wav_files()