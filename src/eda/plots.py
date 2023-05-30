import seaborn as sns
import matplotlib.pyplot as plt
from math import ceil
import numpy as np


def cat_distribution(data, excluded_cols=None):
    cat_cols = data.select_dtypes(include=object).columns

    if excluded_cols is not None:
        cat_cols = data.select_dtypes(include=object).columns.drop(excluded_cols)

    n_rows = ceil(len(cat_cols) / 2)
    n_cols = 2

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20,5*n_rows))

    for idx, col in enumerate(cat_cols):
        ticks_labels = data[col].value_counts(ascending=False).index
        if len(ticks_labels) > 25:
            ticks_labels = ticks_labels[:25]
        sns.countplot(data, x=col, ax=axes.ravel()[idx], order=ticks_labels)
        axes.ravel()[idx].set_xticklabels(ticks_labels, rotation = 45)
    fig.suptitle('Distribución de variables categóricas\nen orden descendente', fontsize=16, y = 1)
    plt.tight_layout()

def num_distribution(data, excluded_cols=None, ylog=False):
    num_cols = data.select_dtypes(include=np.number).columns

    if excluded_cols is not None:
        num_cols = data.select_dtypes(include=np.number).columns.drop(excluded_cols)

    n_rows = ceil(len(num_cols) / 2)
    n_cols = 2

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20,5*n_rows))

    for idx, col in enumerate(num_cols):
        ax = axes.ravel()[idx]  
        ax.hist(data[col])
        ax.set_xlabel(col)
        ax.set_ylabel('count')
        if ylog:
            ax.set_yscale('log')
    fig.suptitle('Distribución de variables numéricas', fontsize=16, y = 1)
    plt.tight_layout()