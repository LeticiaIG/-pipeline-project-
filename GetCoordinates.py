import pandas as pd
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
df = pd.read_csv('Directorio.csv',sep=';', engine='python', encoding='latin1')
print(df.head())
