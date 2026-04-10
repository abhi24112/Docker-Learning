import mlflow
import mlflow.sklearn
import numpy as np
import logging
import os


from src.data_ingestion import reading_files
from src.data_loader import loading_files
from src.data_split import splitting_data
from src.data_preprocessing import dropping_unwanted_cols, removing_outliers, scale_features, encoding, save_scaler
from src.utils import load_config
from src.evaluate import evaluate
from src.model_training import model_training
from  src.model_saving import check_dump


# Import all config data
mlflow_config, data_split_config, xgboost_config, gradient_boosting_config = load_config()

# Create logs directory if it doesn't exist
log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(log_dir, "tracking.log"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Setting mlflow experiment
mlflow.set_tracking_uri(mlflow_config['tracking_uri'])
experiment = mlflow.get_experiment_by_name(mlflow_config['experiment_name'])

if experiment is None:
    logging.info(f"Experiment {experiment} doesn't exists in the mlflow")
    experiment_id = mlflow.create_experiment(mlflow_config["experiment_name"])
else: 
    logging.info(f"Experiment {experiment} already exists in the mlflow")
    experiment_id = experiment.experiment_id

mlflow.set_experiment(experiment_id=experiment_id)

def main():
    logging.info("Mlflow Pipeline execution is started......")
    try:
        # finding dataset on data directory
        file_path = reading_files(data_dir=r"C:\\Users\\Abhishek\\Desktop\\Docker Learning\\ML Workflow\\data")
        logging.info(f"Data file found at: {file_path}")

        # Loading data in df
        df = loading_files(file_path=file_path)
        logging.info(f"Data is import in df Dataframe successfully.")

        # preprocessing of df
        logging.info(f"Preprocesing and feature scaling running....")
        df = dropping_unwanted_cols(df)
        df = removing_outliers(df)
        df = encoding(df)
        df, scaler = scale_features(df)
        save_scaler(scaler)  # Save the scaler for later use in predictions
        logging.info(f"Preprocesing and feature scaling has been done successfully")

        # Splitting data in training and testing
        x_train, x_test, y_train, y_test = splitting_data(
            df=df, 
            test_size=data_split_config['test_size'], 
            random_state=data_split_config['random_state']
        )
        logging.info(f"Splitting of data in train and test is executed successfully")

        # model training
        models_config = {
            "xgboost": xgboost_config,
            "gradient_boosting": gradient_boosting_config
        }

        for model_name, config in models_config.items():
            if config['model_status']:
                with mlflow.start_run(run_name=f"{mlflow_config['run_name']}_{model_name}"):
                    logging.info(f"====================================={model_name}============================================")
                    model = model_training(
                        model_name=model_name, 
                        params=config['params'], 
                        model_status=config['model_status'], 
                        x_train=x_train, 
                        y_train=y_train
                    )
                    logging.info(f"{model_name} trained successfully.")

                    # Evaluting metrics
                    mse, rmse, r2 = evaluate(
                        model=model,
                        x_test=x_test,
                        y_test=y_test
                    )
                    
                    # Save model
                    saved = check_dump(
                        model_name=model_name,
                        run_name=mlflow_config['run_name'], 
                        model=model, 
                        x_test=x_test, 
                        y_test=y_test
                    )
                    if saved:
                        logging.info(f"{mlflow_config['run_name']}_{model_name} dumped successfully.")

                    #log model
                    input_example = np.array(x_test.iloc[:1])
                    mlflow.sklearn.log_model(
                        model,
                        artifact_path="model",
                        input_example=input_example
                    )
                    logging.info(f"{model_name} logged successfully in mlflow.")

                    # Log parameters and metrics
                    mlflow.log_params(config['params'])
                    mlflow.log_metrics({
                        "mse": mse,
                        "rmse": rmse,
                        "r2": r2
                    })
                    logging.info(f"{model_name} parameters and metrics logged successfully in mlflow.")

                    print(f"{model_name} MSE:", mse)
                    print(f"{model_name} RMSE:", rmse)
                    print(f"{model_name} R2:", r2)

        logging.info("🎉 Pipeline Execution Completed Successfully!")

    except Exception as e:
        logging.error(f"Error Occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()