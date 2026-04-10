import pandas as pd
import os
import logging

def loading_files(file_path: str):
    """
    This function is used to load the file in a dataframe
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("File must be in .csv or .xlsx format")
        logging.info(f"Data loaded successfully: {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading the file")
        return None