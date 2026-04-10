import pandas as pd
import logging
import os

def reading_files(data_dir:str = "data/")-> str:
    valid_data = ['csv', 'xlsx']
    files=[]
    for i in os.listdir(data_dir):
        if i.split(".")[-1] in valid_data:
            files.append(i)
    if not files:
        logging.info("File are not founded in location")
        raise FileNotFoundError("No file csv or xlsx file in the directory")

    if len(files) > 1:
        logging.info("Multiple files are present in the location")
        raise ValueError("Multiple csv or xlsx file in directory")
    return os.path.join(data_dir, files[0])