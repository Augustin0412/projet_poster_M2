import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler

def filter_occurence_variable(df, variable, threshold_min):
    """
    Filter the dataframe by keeping only the values of the variable that occur more than the threshold
    """
    occurrences = df[variable].value_counts()
    values_to_keep = occurrences[occurrences >= threshold_min].index
    df = df[df[variable].isin(values_to_keep)]

    return df

def standardisation(df):
    """
    Standardize dataframe variables
    """
    # ne pas sélectionner tt les variables binaires car pas de standardisation des variables binaires
    exclude_columns = []
    for col in df.columns:
        if len(df[col].unique()) == 2:
            exclude_columns.append(col)

    columns_to_scale = df.select_dtypes(include=['int64', 'float64']).columns.difference(exclude_columns)

    scaler = StandardScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    df

    return df