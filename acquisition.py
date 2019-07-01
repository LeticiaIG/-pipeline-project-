import pandas as pd

def csv_to_df (file):
    df = pd.read_csv(csv,sep=';', engine='python', encoding='utf-8')
    return df
