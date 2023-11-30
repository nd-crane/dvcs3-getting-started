---
language:
- en
datasets:
- https://www.kaggle.com/competitions/titanic/data
license:
- http://www.apache.org/licenses/LICENSE-2.0
---

# Model Card for Titanic Neural Net Example 

This model was created using fastai and pytorch frameworks from this [tutorial](https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial). 
It uses the Kaggle Titanic dataset, split into training and testing sets.

## Model Details

### Model Description

This model is a neural network predicting survival of passengers on the Titanic. 

### Model Sources

The model can be found in [this](https://github.com/nd-crane/dvcs3-getting-started/tree/main/nbs) repository, 
and the tutorial can be found [here](https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial).

- **Repository:** https://github.com/nd-crane/dvcs3-getting-started/tree/main
- **Demo:** https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial

## Uses

This model was created as a toy-example for working with DVC. It is not intended to serve a greater purpose. 

## Bias, Risks, and Limitations

The data does not include information on crew members, allocation of resources (e.g. lifeboats) during the disaster, or other interactions among passengers. The model may reinforce biases regarding race or economic class that originally affected survival rates.

## Training Details

### Training Data

https://github.com/nd-crane/dvcs3-getting-started/blob/main/data/README.md

### Training Procedure 

A random forest classifier was used to train the validation set. 

#### Preprocessing

The training data was split so that 20% of the data would be included in a validation set to prevent overfitting. 

### Testing Data, Factors & Metrics

#### Testing Data

https://github.com/nd-crane/dvcs3-getting-started/blob/main/data/README.md

#### Metrics

Prediction accuracy was used to assess the effectiveness of the model on the validation set. 

## Model Card Authors

Maria Murphy
