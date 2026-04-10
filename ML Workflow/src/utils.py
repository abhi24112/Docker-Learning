import yaml

def load_config(path="./config/config.yaml"):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
        mlflow_config = config['mlflow']
        data_split_config = config['data']
        xgboost_config = config['model']['xgboost']
        gradient_boosting_config = config['model']['gradient_boosting']
        return mlflow_config, data_split_config,xgboost_config, gradient_boosting_config