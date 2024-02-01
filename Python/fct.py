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
    col_binary = ["is_canceled", "is_repeated_guest"]

    scaler = StandardScaler()

    df_quant = df.select_dtypes(include=[np.number])
    df_quant = df_quant.drop(col_binary, axis=1)
    df_quant = pd.DataFrame(scaler.fit_transform(df_quant), columns=df_quant.columns)
    df = df.drop(df_quant.columns, axis=1)
    df = pd.concat([df, df_quant], axis=1)
    print(df)

    return df