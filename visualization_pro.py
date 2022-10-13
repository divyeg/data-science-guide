"""
Visualizer Pro - Python functions for creating different types of visualizations.
"""

__version__ = "0.1.0"

import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, average_precision_score, f1_score, precision_score, recall_score
from sklearn.metrics import roc_auc_score, balanced_accuracy_score, mathews_corrcoef
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.metrics import classification_report

import warnings
warnings.simplefilter(action="ignore")


def classification_model_performance_report(y, y_hat, y_hat_proba):
    """
    Returns Key Model Performance metrics for binary classification problems

    Params Type: pd.Series or numpy.ndarray
    Returns: Print model performance metrics, confusion matrix
    """
    
    cm = confusion_matrix(y, y_hat)
    precision = np.round(precision_score(y,y_hat), 2)
    recall = np.round(recall_score(y,y_hat), 2)
    average_precision = np.round(average_precision_scrore(y, y_hat), 4)
    accuracy = np.round(accuracy_score(y,y_hat), 4)
    balanced_accuracy = np.round(balanced_accuracy(y,y_hat),4)
    mathews_cor = np.round(matthews_corrcoef(y,y_hat), 4)
    f1 = np.round(f1_score(y,y_hat), 4)
    auc = np.round(roc_auc_score(y, y_hat_proba), 4)
    
    print('Precision & Recall: ', (precision, recall) )
    print('Average Precision: ', average_precision)
    print('Accuracy & Balanced Accuracy: ', (accuracy, balanced_accuracy) )
    print('Mathews Correlation Coefficient: ', mathews_cor)
    print('F1 Score: ', f1)
    print('AUC ROC: ', auc)
    
    sns.heatmap(cm, cmap='PuBu', annot=True, fmt='g', annot_kws={'size':20})
    plt.xlabel('predicted', fontsize=18)
    plt.ylabel('actual', fontsize=18)
    plt.title(title, fontsize=18)
    
    plt.show();
    
def plot_categorical_countplots(column_x1, column_x2, column_x3, column_x4, hue, df, figsize=(12,12)):
    """
    Returns 4 categorical countplots

    Params Type: pd.DataFrame, column strings, hue string
    Returns: 4x1 plot
    """
    plt.figure(figsize=figsize)
    
    plt.subplot(411)
    sns.countplot(x = column_x1, hue=hue, data=df)
    
    plt.subplot(412)
    sns.countplot(x = column_x2, hue=hue, data=df)
    
    plt.subplot(413)
    sns.countplot(x = column_x3, hue=hue, data=df)
    
    plt.subplot(414)
    sns.countplot(x = column_x4, hue=hue, data=df)
    
    plt.show();
        
