# Default Imports
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path=path):
    df = pd.read_csv(path, header=0, delimiter=',')

    return df

print read_csv_data_to_df(path)
