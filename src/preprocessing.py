import pandas as pd

def clean_data(df):
    """
    Clean a dataset by removing duplicate rows.
    """

    df = df.drop_duplicates()

    return df
