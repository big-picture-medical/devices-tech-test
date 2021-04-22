# devices-tech-test
Python technical test for device integration hires

## Overview
This repository is the starting point for Big Picture's Device Tech Test.

We have created a basic DICOM SCP that we would like you to extend to store the data and forward to a DICOMWeb endpoint.

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
Before getting started, should you have any questions regarding any of the tasks please email stuart@bigpicturemedical.com.

### 1. Save the DICOM File
Save the DICOM file locally to a cache directory with a temporary file with a randomly generated name.
* The folder should be configurable via a file that stores properties
* There should be no risk of files for different scans having conflicting names

### 2. Extract metadata and store
From the DICOM file, extract metadata including patient ID, SOP Instance UID along with the saved filename and timestamp. This can be stored in a persistence store of your choosing eg. CSV file, SQLLite etc.

### 3. Upload the DICOM to a DICOMWeb URL
Send the DICOM to a configurable DICOM Web URL. This should follow the standard defined at https://www.dicomstandard.org/dicomweb/store-stow-rs/.
* Note that this may take some time and should be run in a separate thread to the 
* The store should also recorded which DICOM files have been sent, failed etc.
* The temporary DICOM file stored must be deleted once it has been sent.

## What we're looking for
* Maintainable code split into files logically
* Correct usage of appropriate Python libraries
* Tests as documentation
* Git hygiene

## Submission
Once complete, please create a zip file or tarball of your repository with the git history intact. Then please send your solution to stuart@bigpicturemedical.com

