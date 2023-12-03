# DVCLive Getting Started

This READ.md showcases the process in which our team took to set up our visualizations and metrics for the titanic model.

## Setting up VSCode

### Downloading VSCode
We must begin by first installing VSCode instead which can be done via the link below
https://code.visualstudio.com/download

### Setting up DVC extenions
Now we must install the following extensions
  1. DVC
  2. DVC extension pack

## Editing Model Script

Now to generate both the plots and metrics json we must edit the script to impliment DVCLive. To do this we will start by creating the necessary directories, initalize dvclive, and load in our parameters.
```
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Initialize dvclive
    live = Live(dir="logs", dvcyaml=False, report=None)
    
   ...
    
    # Load params
    yaml = YAML(typ="safe")
    with open(params_file) as f:
        params = yaml.load(f)
```
Next we must setup a classifer to train the model over several iterations
```
    # Train the model and log metrics over multiple iterations
    rnf_classifier = RandomForestClassifier(n_estimators=params["num_estimators"], n_jobs=-1)
```
Finally we must setup a loop to train the model over a set amount of iterations
```
    # Example: Simulate 10 iterations (epochs)
    for epoch in range(10):

        ...
        
        # Log metrics at each epoch
        live.log_metric("accuracy", acc)
        live.next_step()  # Advance to the next step to simulate time progression
```

## Setting Params

This file dictates the number of estimators we want to use within our model training

## Creating DVC Pipeline

Although there is only one stage within this pipeline, the yaml file serves as an outline of what should be included within a dvc pipeline including your command (script), dependacies, parameters, outputs and plots.

## Updating .gitingore Files

This file makes sure to keep the Github clean by excluding the enviroment used to run the script, the data files themsleves, the classifer (model output) file, and the logs. The reason for this is so you can simple clone the repo and then run the experiments yourself without having to worry about file discrepencies.

## Resolving Possible Problems 

One of the probelms that we ran into was not beign able to get our dvclive to initialize. This was solved by adjusting the pointer to python to the specifc version of python used within the env.
