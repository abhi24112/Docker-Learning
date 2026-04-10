from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
import logging
import pandas as pd


MODEL_MAP = {
    "xgboost": XGBRegressor,
    "gradient_boosting": GradientBoostingRegressor
}

def model_training(model_name: str, params: dict, model_status: bool, x_train: pd.DataFrame, y_train: pd.DataFrame):
    logging.info(f"Creating {model_name} Model")

    if model_name in MODEL_MAP and model_status:
        model = MODEL_MAP[model_name]
        model = model(**params)
        model.fit(x_train, y_train)
        logging.info(f"{model_name} trained successfully.")
        return model
    
    else:
        logging.error(f"{model_name} doesn't exist.")
        raise KeyError(f"{model_name} doesn't exists")

