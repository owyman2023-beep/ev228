import pandas as pd

def process_data(file, variable1, variable2):
    df_cos = pd.read_csv(file)
    season_variable = df_cos[variable1]
    time_variable = df_cos[variable2]
    return season_variable, time_variable
