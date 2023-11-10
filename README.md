# Data Engine Getting Started

This repo showcases the TAI Frameworks data engine, presents the tools used, and explains how each adds trust to the machine-learning pipeline.

To demonstrate our practices, we've built upon the [fastai beginner tutorial](https://www.kaggle.com/code/hitesh1724/titanic-1-fastai-beginner-tutorial) using the [kaggle titanic dataset](https://www.kaggle.com/competitions/titanic).

## Data Engine

![](images/DataEngineDiagram.png)

As you can see at each stage we apply a different technique to securing the machine learning pipeline.

All of this is managed with DVC.  Let's first explore setting up DVC and how to use its powerful capabilities.

## DVC Client

Here's how to configure a DVC workflow with AWS's S3 buckets.  This configuration is specific to localstack, but can be applied to any S3 instance.

For more information on the server side configuration, please view the `server-side` branch.

### Getting Started

### Initalizing DVC

To initialize a DVC project inside a Git project run:

```bash
dvc init
```

DVC requires an underlying Git project to properly track data.  If the current directory is not part of a git repository either clone an existing repository or run `git init` prior to initializing DVC.

### Adding S3 Buckets

DVC supports Amazon S3 buckets for remote storage (in addition to many other options).  To add a remote bucket run:

```bash
dvc remote add -d myremote s3://<bucket>/key
```

With the localstack configuration there will be no key.  Since the localstack endpoint is different from a typical AWS bucket, we need to specify it in the DVC config file.  The `endpointurl` parameter can be modified with the following command:

```bash
dvc remote modify myremore endpointurl http://<domain>:<port>
```

These commands will modify the `.dvc/config` file.  All settings can be written to that file with the appropriate `.ini` format.

With S3 buckets set up data can be pushed with:

```bash
dvc add <file>
dvc push
```


### Further Information

For more information please refer to the (DVC Docs)[https://dvc.org/doc/user-guide/data-management/remote-storage/amazon-s3]