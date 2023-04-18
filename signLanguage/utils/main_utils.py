import os.path
import sys
import yaml
import base64
from signLanguage.exception import SignException
from signLanguage.logger import logging

def read_yaml_file(file_path: str) ->dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            logging.info('Reading yaml file')
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SignException(e, sys) from e
    

def write_yaml_file(file_path: str,content: object,replace: bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path, 'w') as file:
            yaml.dump(content,file)
            logging.info('Writing yaml file')

    except Exception as e:
        raise SignException(e, sys) from e
    
def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+ filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64decode(f.read())