import pandas as pd
import os
import fastcore
import fastai
from fastai.tabular.all import *
from dvclive import Live
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Setup directpry to store logs 
live = Live("../dvclive_logs") 

# Prep Data
df_test = pd.read_csv('../data/data/test.csv')
df_train = pd.read_csv('../data/data/train.csv')

df_train.isnull().sum().sort_index()/len(df_train)

df_train.dtypes
g_train =df_train.columns.to_series().groupby(df_train.dtypes).groups

cat_names  = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
cont_names = ['PassengerId', 'Pclass', 'SibSp', 'Parch', 'Age', 'Fare']

splits = RandomSplitter(valid_pct=0.2)(range_of(df_train))

# Preprocess Data
to = TabularPandas(df_train, procs=[Categorify, FillMissing, Normalize],
                   cat_names = cat_names,
                   cont_names = cont_names,
                   y_names = 'Survived',
                   splits=splits)

g_train =to.train.xs.columns.to_series().groupby(to.train.xs.dtypes).groups

to.train.xs

# Training
X_train = to.train.xs
X_valid = to.valid.xs

y_train = to.train.ys.values.ravel()
y_valid = to.valid.ys.values.ravel()

rnf_classifier= RandomForestClassifier(n_estimators=100, n_jobs=-1)
rnf_classifier.fit(X_train,y_train)

y_pred = rnf_classifier.predict(X_valid)
acc = accuracy_score(y_pred, y_valid)

# Make sure to log the accuracy in DVCLive
live.log_metric('accuracy', acc)
live.next_step()

# Test Dataset
df_test.dtypes
g_train =df_test.columns.to_series().groupby(df_test.dtypes).groups

cat_names  = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
cont_names = ['PassengerId', 'Pclass', 'SibSp', 'Parch', 'Age', 'Fare']

test = TabularPandas(df_test, procs=[Categorify, FillMissing,Normalize],
                   cat_names = cat_names,
                   cont_names = cont_names,
                   )

X_test= test.train.xs

X_test.dtypes
g_train =X_test.columns.to_series().groupby(X_test.dtypes).groups

X_test= X_test.drop('Fare_na', axis=1)

y_pred=rnf_classifier.predict(X_test)

y_pred= y_pred.astype(int)

output= pd.DataFrame({'PassengerId':df_test.PassengerId, 'Survived': y_pred})
output.to_csv('my_submission_titanic.csv', index=False)