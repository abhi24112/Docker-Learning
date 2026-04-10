import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import LabelEncoder, StandardScaler

# we are using xgboost regressor which handles null values automatically

def dropping_unwanted_cols(df:pd.DataFrame):
    """Remove unwanted columns (ID, Bedtime, Wakeup time) from the DataFrame."""
    logging.info("Dropping the unwanted column from the data")
    df = df.drop(['ID','Bedtime','Wakeup time'], axis=1)
    return df

def removing_outliers(df:pd.DataFrame) -> pd.DataFrame:
    """Remove outliers from numeric columns using the Interquartile Range (IQR) method."""
    df_filterd = df.copy()

    for col in df_filterd.select_dtypes(['int', 'float']).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        IQR = q3 - q1

        lower_bound = q1 - 1.5 * IQR
        upper_bound = q3 + 1.5 * IQR

        filtered_rows = (df_filterd[col] < upper_bound) & (df_filterd[col] > lower_bound)

        df_filterd = df_filterd[filtered_rows]

    return df_filterd


def encoding(df:pd.DataFrame):
    """Encode categorical columns to numeric values using Label Encoding."""
    categorical_col = df.select_dtypes(include=['object', 'string', 'category']).columns.tolist()

    if not categorical_col:
        logging.warning("No Categorical columns found in the data")
        return df

    try:
        le = LabelEncoder()
        
        for col in categorical_col:
            logging.info(f"Encodding columns: {col}")
            df[col] = le.fit_transform(df[col])
        
        logging.info("Label Encoding completed Successfully")
        return df
    except Exception as e:
        logging.info("Error in Label Encoding")
        raise ValueError("Error occured in LabelEncoding")
    

def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """Scale numeric features to have mean=0 and std=1 using StandardScaler."""
    
    scaler = StandardScaler()
    
    cols_to_scale = df.columns[df.columns != 'Sleep efficiency']
    
    df_scaled = df.copy()
    df_scaled[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    return df_scaled
