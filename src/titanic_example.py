#!/usr/bin/env python3

# This is a simple example of a machine learning model training script.
# It trains a Random Forest Classifier on the Titanic dataset and logs
# the accuracy metric over multiple iterations (epochs) using dvclive.

# The script is based on the following tutorial:
# https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial

# And uses the Kaggle Titanic dataset:
# https://www.kaggle.com/c/titanic/data

# Authors: Peter Ainsworth and Conner Rauguth

# Import standard libraries
import os
from pathlib import Path

# Import third-party libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from ruamel.yaml import YAML
from fastai.tabular.all import *
from dvclive import Live

# Prepare data for training
def prep_data(df, split=0.2):
    cat_names = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    cont_names = ['PassengerId', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    splits = RandomSplitter(valid_pct=split)(range_of(df))
    to = TabularPandas(df, procs=[Categorify, FillMissing, Normalize],
                       cat_names=cat_names,
                       cont_names=cont_names,
                       y_names='Survived',
                       splits=splits)
    X_train = to.train.xs
    X_valid = to.valid.xs
    y_train = to.train.ys.values.ravel()
    y_valid = to.valid.ys.values.ravel()
    return X_train, X_valid, y_train, y_valid

def main():
    # Create results directory if it doesn't exist
    results_dir = Path('results')    
    results_dir.mkdir(exist_ok=True)

    # Initialize dvclive
    live = Live(dir=results_dir, dvcyaml=False, report=None)
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    train_data_file = os.path.join(script_directory, '..', 'data', 'train.csv')
    params_file = os.path.join(script_directory, '..', 'params.yaml')
    
    # Load params
    yaml = YAML(typ="safe")
    with open(params_file) as f:
        params = yaml.load(f)
    
    # Load data
    df_train = pd.read_csv(train_data_file)
    X_train, X_valid, y_train, y_valid = prep_data(df_train, split=0.2)

    # set the params
    train_params = {
        "n_estimators": params["num_estimators"],
        "max_depth": params["max_depth"],
    }
    
    # Train the model and log metrics over multiple iterations
    rnf_classifier = RandomForestClassifier(**train_params)
    
    # Example: Simulate 10 iterations (epochs)
    for epoch in range(10):
        # You can add more sophisticated training logic here if needed
        rnf_classifier.fit(X_train, y_train)
        
        # Predict and calculate accuracy
        y_pred = rnf_classifier.predict(X_valid)
        acc = accuracy_score(y_pred, y_valid)
        
        # Log metrics at each epoch
        live.log_metric("accuracy", acc)
        live.next_step()  # Advance to the next step to simulate time progression

    # Save the model after training
    models_dir = Path('model')
    models_dir.mkdir(exist_ok=True)
    model_filename = 'rnf_classifier.pkl'

    with open((models_dir / model_filename).absolute(), 'wb') as model_file:
        pickle.dump(rnf_classifier, model_file)
    
if __name__ == "__main__":
    main()