# Capstone project
## Installation
Run
`pip install -r requirements.txt`
to intall libraries used in the project.

## Notebooks
 - Capstone-Proposal.ipynb - is the notebook where capstone proposal is written.
 - Base_Line.ipynb - logistic regression and random guess applied to the data set.
 - Data_Exploration.ipynb - data exploration and visualizatin notebook
 - Data_Merging.ipynb - merging of all files into single file data set
 - isolation_forest_outliers.npy - isolation forest applied to data set to detect possible outliers
 - Lightgbm.ipynb - Lightgbm algorithm application

## How to run and get results
### Data_Exploration.ipynb
Use to analyze data, see visulizations, anomalies, etc.

### Base_Line.ipynb
To build base line it's needed to extract features first, for that there is Feature_Extraction.ipynb, it pre-process data using basics techniques and save tran and test joblibs. After that it's possible to build base line.

### isolation_forest_outliers.npy
This is optional step to find outliers using isolation forest algorithm.

### Data_Merging.ipynb
Run this notebook to merge files into single train and test csv's. This step is neccessary to run Lightgbm notebook.

### Lightgbm.ipynb
Run this notebook to train and get results using Lightgbm algorithm. It saves submission for kaggle at the end.

## Data set
Data set is hosted on kaggle platform. To download it follow this [link](https://www.kaggle.com/c/home-credit-default-risk/data) and accept 'Terms and Conditions' of the project and use download button or [kaggle command line tool](https://github.com/Kaggle/kaggle-api) to download files:  
`kaggle competitions download -c home-credit-default-risk`


## Submission
`kaggle competitions submit -c home-credit-default-risk -f submission.csv -m "Message"`

