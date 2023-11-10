import pandas as pd
import os
import fastcore
import fastai
from fastai.tabular.all import *
from dvclive import Live
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import sys
import os
from ruamel.yaml import YAML


def prep_data(df, split=0.2):

    cat_names  = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    cont_names = ['PassengerId', 'Pclass', 'SibSp', 'Parch', 'Age', 'Fare']

    splits = RandomSplitter(valid_pct=split)(range_of(df))

    to = TabularPandas(df, procs=[Categorify, FillMissing, Normalize],
                   cat_names = cat_names,
                   cont_names = cont_names,
                   y_names = 'Survived',
                   splits=splits)
    

    X_train = to.train.xs
    X_valid = to.valid.xs

    y_train = to.train.ys.values.ravel()
    y_valid = to.valid.ys.values.ravel()

    return X_train, X_valid, y_train, y_valid



def main():

    live = Live(dir="logs", dvcyaml=False, report=None)
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    train_data_file = os.path.join(script_directory, '..', 'data', 'train.csv')
    test_data_file = os.path.join(script_directory, '..', 'data', 'test.csv')
    params_file = os.path.join(script_directory, '..', 'params.yaml')

    # here's where we can parameterize the script for quick experimentation with DVC
    # this is similar to command line args, but we'll use the DVC technique instead
    
    # load params
    yaml = YAML(typ="safe")
    with open("params.yaml") as f:
        params = yaml.load(f)

    # load data

    df_test = pd.read_csv(test_data_file)
    df_train = pd.read_csv(train_data_file)


    X_train, X_valid, y_train, y_valid = prep_data(df_train, split=0.2)

    rnf_classifier= RandomForestClassifier(n_estimators=params["num_estimators"], n_jobs=-1)
    rnf_classifier.fit(X_train,y_train)

    y_pred = rnf_classifier.predict(X_valid)
    acc = accuracy_score(y_pred, y_valid)

    live.log_metric('accuracy',acc)

    model_filename = 'rnf_classifier.pkl'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(rnf_classifier, model_file)

    live.end()    

if __name__ == "__main__":
    main()