# Data Engine Getting Started

This repo showcases the TAI Frameworks data engine, presents the tools used, and explains how each adds trust to the machine-learning pipeline.

To demonstrate our practices, we've built upon the [fastai beginner tutorial](https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial) using the [kaggle titanic dataset](https://www.kaggle.com/competitions/titanic).

## Data Engine

![](images/DataEngineDiagram.png)

As you can see at each stage we apply a different technique to securing the machine learning pipeline.

All of this is managed with DVC.  Let's first explore setting up DVC and how to use its powerful capabilities.

## Installation

Python 3.8+ is required to run this repo.

```bash
$ git clone git@github.com:nd-crane/dvcs3-getting-started.git
$ cd dvcs3-getting-started/
```

Let's install the requirements.  In this project we are using a python virtual environment for dependency managaement, but Conda and PDM work as well.

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

As depicted above, source data is stored in S3 Buckets with DVC remote storage.  This is a read only HTTP remote.

```bash
$ dvc remote list
myemote     s3://mytestbucket
```

You should run `dvc pull` to download the data.

```bash
$ dvc pull
```

## Running Experiments

