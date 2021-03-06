# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df


import numpy as np
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    runs_df = ipl_df[['match_code', 'runs', 'batsman']]
    runs_df['count'] = 1
    runs_pivot = runs_df.pivot_table('count', aggfunc=np.sum, index='match_code', columns='runs').fillna('NA')
    return runs_pivot

print get_runs_counts_by_match()
