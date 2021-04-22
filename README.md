# devices-tech-test
Python technical test for device integration hires

## Overview
This repository is the starting point for Big Picture's Device Tech Test.

We have created a basic DICOM SCP that we would like you to extend to anonymise the data and forward to a DICOMWeb endpoint.

## Setup

### Repo
Start by cloning this repository locally. You will not need to publish your copy on GitHub as we are requesting that you send us a zip or tarball with the git history intact.

### Installation
How you install this exactly on your host is up to you, but we recommend:

1. Install Python 3 and virtualenv locally on your computer
2. Create and activate a virtualenv for this project and run pip install -r requirements.txt
3. run python src/dicom_scp.py
4. Open a new console tab, activate the virtualenv and run python test/test_scu.py
5. You should see output from the dicom_scp.py execution: `INFO:__main__:Store received for patient Healthy Retina - adult
`

## The Tasks

1. Save the dicom file locally to a cache directory with a temporary file with a randomly generated name
2. Extract meta data from the dicom file and store a record of the update including it's full filename and timestamp in a persistence store of your choosing (eg a CSV file, pickle file or even SQLite database)
3. write code to Upload the c-store temporary dicom file to a remote Dicomweb URL
4. Write a worker to interrogate the persistence store and forward unsent dicom files recorded in step 2 to the Dicomweb URL in step 3. Log the worker's progress 
5. Package the above tasks into a standalone application which forwards DICOM files to a remote Dicomweb URL. In the above we will be interested in tha patterns you use and how you structure and encapsulate your code into logically self-contained  classes and methods
