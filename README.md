# Capstone project
## Notebooks
 - Capstone-Proposal.ipynb - is the notebook where capstone proposal is written.
 - Base_Line.ipynb - logistic regression and random guess applied to the data set.
 - Data_Exploration.ipynb - data exploration and visualizatin notebook
 - Data_Merging.ipynb - merging of all files into single file data set
 - isolation_forest_outliers.npy - isolation forest applied to data set to detect possible outliers
 - Lightgbm.ipynb - Lightgbm algorithm application

## Data set
Data set is hosted on kaggle platform. To download it follow this [link](https://www.kaggle.com/c/home-credit-default-risk/data) and accept 'Terms and Conditions' of the project and use download button or [kaggle command line tool](https://github.com/Kaggle/kaggle-api) to download files:  
`kaggle competitions download -c home-credit-default-risk`


## Submission
`kaggle competitions submit -c home-credit-default-risk -f submission.csv -m "Message"`

