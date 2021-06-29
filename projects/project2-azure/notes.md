# Azure DataScience Notes
## Module 1 - Overview
## Module 2 - NoCode ML
## Module 3 - Running Experiment and Training Models
### 3.3 
Experiment object called from azure ml python sdk, keeps track of experiment data and metadata in log files - can be run local or cloud

code:

    from azureml.core import Workspace, Experiment
    import pandas as pd
    
    ws = Workspace.from_config()
    experiment = Experiment(workspace, "My-Experiment")
    run = experiment.start_logging(outputs=None, snapshot_directory=".")
    data = pd.read_csv('data.csv')
    row_count = (len(data))
    run.log('observations', row_count)
    run.log_metric("Accuracy", accuracy)
    data.sample(100).to_csv('sample.csv', index=False, header=True)
    run.upload_file(name='outputs/sample.csv',path_or_stream='./sample.csv')
    run.complete()
   

### 3.4
Run script as experiment
run = Run.get_context()
    or
script_config = ScriptRunConfig(source_directory='my_dir',script='script.py')
run = experiment.submit(config=script_config)

### 3.5 
MLFlow - Model Management
### 3.6
Training models
### 3.7
Parameters and hyperparameters and argparse for argument parsing
### 3.8 
register models

## Module 4 - Working with DataStores
### 4.3
Registering and adding Data Stores

Code Samples:

    from azureml.core import Workspace, Datastore
    
    ws = Workspace.from_config()
    
    blob_ds = Datastore.register_azure_blob_container(workspace=ws,
                                                        datastore_name='blob_data'
                                                        container_name='data_container'
                                                        account_name='az_store_acct',
                                                        account_key='12345abscde8...')
                                                        
    ds = Datastore.get(ws, datastore_name='blob_data)
    
    ds.upload(src_dir='/files',target_path='/data/files')
    ds.download(target_path='downloads',prefix='/data')
    
### 4.5
Datasets defined (tabular and file)
### 4.6
Creating and Registering Datasets (tabular and file)
### 4.7
ScriptRunConfig vs Script

    code example
    
### 4.8
Pass dataset as named input (scriptrunconfig and script)

    code example

### 4.9
passing dataset as script argument (scriptrunconfig and script)

    code example
    
### 4.10
pass a dataset as named input (scriptrunconfig and script)

    code example

### 4.11 
Create new version of existing dataset

    code example
    

## Module 5 - Working with Compute
### 5.2 
Environments 
Run Contexts for experiments in a container 
### 5.3
Conda Env
    Create env from specification file
        file in YAML format for conda
    Create env from existing conda env

    code example

Specificying packages

    code example
    
### 5.4
Docker Images env
configure env containers 

    code examples
    
### 5.5
save env to workspace

### 5.6
Compute options
    local
    cluster
    attached - used outside of workspace (e.g. vm, azure databricks, azure HDInsight)

### 5.7 
Cluster

### 5.8 
Databricks

