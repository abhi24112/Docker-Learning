from sklearn.metrics import r2_score
import pandas as pd
import joblib as jb
import os
import logging

def check_dump(model_name: str,run_name: str, model, x_test:pd.DataFrame, y_test:pd.Series):
    """
    Check model R2 score and save if threshold is met.
    """
    logging.info("Checking the r2_score of the model")
    y_pred = model.predict(x_test)
    acc = r2_score(y_test, y_pred)
    acc = acc * 100
    logging.info(f"The R2 score of the Regression Model is {acc:.4f}")
    
    if acc >= 30:
        logging.info("Saving the Model in the Directory")
        model_dir = r"C:\Users\Abhishek\Desktop\Docker Learning\ML Workflow\models"
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, f"{run_name}_{model_name}.jbl")
        
        # Ensure the model is being saved properly
        jb.dump(model, model_path)
        
        print(f"✅ Model Successfully Saved at {model_path}")
        return True
    else:
        logging.error(f"Model R2 is {acc:.4f}%, below 30% threshold. Not saving {model_name}")
        return False     