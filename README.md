# Decision Tree Classifier with Stratified K-Fold Cross-Validation

## Overview
This project implements a Decision Tree Classifier using the `scikit-learn` library in Python. The dataset is loaded from a CSV file, cleaned to remove missing values, and then evaluated using stratified k-fold cross-validation. The classifier is tested with both `gini` and `entropy` criteria to determine its accuracy.

## Requirements
Ensure you have the following dependencies installed before running the script:
- Python 3.x
- pandas
- scikit-learn

You can install the required packages using the following command:
```bash
pip install pandas scikit-learn
```

## Dataset
The script reads data from `test.csv`, which should be structured with:
- Feature columns representing input data.
- A `class` column representing labels for classification.

## Data Source
If you need sample datasets, you can download them from the following sources:
[Source](https://archive.ics.uci.edu/dataset/372/htru2)

## Features
- Reads a dataset from `test.csv`
- Identifies and removes missing values
- Applies stratified k-fold cross-validation (k=5)
- Trains a Decision Tree Classifier with `gini` and `entropy` criteria
- Calculates and prints the accuracy for each fold and overall average accuracy

## Usage
Run the script using Python:
```bash
python script.py
```
Ensure that `test.csv` is present in the working directory.

## Code Explanation
1. **Data Preprocessing**
   - Loads the dataset using pandas.
   - Identifies and removes missing values.
2. **Model Training & Evaluation**
   - Uses `StratifiedKFold` for splitting the dataset.
   - Trains a `DecisionTreeClassifier` with both `gini` and `entropy` criteria.
   - Calculates accuracy for each fold and averages results.

## Output
The script outputs:
- The shape of the original and cleaned dataset.
- Number of missing values.
- Accuracy per fold for both `gini` and `entropy` criteria.
- Final average accuracy across all folds.

## References
R. J. Lyon, B. W. Stappers, S. Cooper, J. M. Brooke, J. D. Knowles, Fifty Years of Pulsar Candidate Selection: From simple filters to a new principled real-time classification approach, MNRAS, 2016.
