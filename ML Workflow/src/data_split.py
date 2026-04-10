from sklearn.model_selection import train_test_split
import pandas as pd
import logging

def splitting_data(df:pd.DataFrame, test_size : float, random_state: int):
    if df.empty or "Sleep efficiency" not in df.columns:
        logging.error("Data Frame has no data in it.")
        raise ValueError("No data in the data frame")
    logging.info("Splitting Data in training and testing dataframe")
    x = df.drop('Sleep efficiency', axis=1)
    y = df['Sleep efficiency']

    x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=random_state, test_size=test_size)

    return x_train, x_test, y_train, y_test
    