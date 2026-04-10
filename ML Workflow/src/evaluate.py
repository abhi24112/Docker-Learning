import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import logging

def evaluate(model, x_test, y_test):
    """
    This function evaluate the model
    """
    if len(x_test)!=len(y_test):
        raise ValueError(f"Mismatch the number of sample between the x_test {len(x_test)} and y_test {len(y_test)}")
    
    y_pred = model.predict(x_test)

    if y_pred.size == 0:
        logging.info("Error in Making Prediction on Test ")
        raise ValueError("Error in Making prediction for test data")


    logging.info("Calculating Evaluation Matries for")
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    return mse, rmse, r2