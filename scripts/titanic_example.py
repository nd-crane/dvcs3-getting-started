#!/usr/bin/env python3

import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from ruamel.yaml import YAML
from fastai.tabular.all import *
from dvclive import Live

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
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Initialize dvclive
    live = Live(dir="logs", dvcyaml=False, report=None)
    
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
    
    # Train the model and log metrics over multiple iterations
    rnf_classifier = RandomForestClassifier(n_estimators=params["num_estimators"], n_jobs=-1)
    
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
    model_filename = 'rnf_classifier.pkl'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(rnf_classifier, model_file)
    
if __name__ == "__main__":
    main()