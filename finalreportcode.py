
import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('test.csv')
print('Original dataset shape: ',df.shape)
print('Data Missing rows/columns: ',df[df.isnull().any(axis = 1)].shape)
print('\nTotal null values are: ',df.isnull().sum().sum()) 

cleaned_df= df.dropna()
print('\nCleaned dataset shape: ',cleaned_df.shape)
print('Cleaned dataset Missing rows/columns: ',cleaned_df[cleaned_df.isnull().any(axis = 1)].shape)

X = cleaned_df.drop(['class'], axis = 1).values
y = cleaned_df['class'].values

skf = StratifiedKFold(n_splits=5)
criterion = ['gini', 'entropy']
final_gini_accuracy = 0 
final_entropy_accuracy = 0


for i, (train_index, test_index) in enumerate (skf.split(X,y)):
    print('Fold: ',i)
    X_train = X[train_index]
    X_test = X[test_index]
    y_train = y[train_index]
    y_test = y[test_index]
    max_depth = 10*X_train.shape[1]
    for criteria in criterion:
        print('Criterion: ',criteria)
        dt = DecisionTreeClassifier(criterion=criteria,max_depth=max_depth,random_state = 0)
        dt.fit(X_train, y_train)
        y_tested = dt.predict(X_test)
        
        accuracy = accuracy_score(y_test,y_tested)
        print('Accuracy: %.3f' % (accuracy * 100))
        if criteria == 'gini':
            final_gini_accuracy += accuracy
        else:
            final_entropy_accuracy += accuracy
print('\n\n')
print('final_gini_accuracy: %.3f'%(final_gini_accuracy*100/5))
print('final_entropy_accuracy: %.3f'%(final_entropy_accuracy*100/5))