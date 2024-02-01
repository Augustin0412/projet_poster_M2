import pandas as pd 
import numpy as np

def filter_occurence_variable(df, variable, threshold_min):
    """
    Filter the dataframe by keeping only the values of the variable that occur more than the threshold
    """
    occurrences = df[variable].value_counts()
    values_to_keep = occurrences[occurrences >= threshold_min].index
    df = df[df[variable].isin(values_to_keep)]

    return df