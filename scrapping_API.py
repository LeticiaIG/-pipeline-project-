from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import numpy as np
import requests
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import os

# dotenv
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("KEY")

#ESTAS DOS ÚLTIMAS LÍNEAS SE METEN EN UNA FUNCIÓN EN EL main.py

print(key)

# 3 RETRIEVE NEWS FROM URLs 

def get_text_apply(url): 
    print(url)
    try:
        res = requests.get(url)
        # print(type(res))
        soup = BS(res.text, 'html.parser')
        parrafos = '\n'.join([p.get_text().strip() for p in soup.select("p")])
        return parrafos
    except: 
        return None

def DF_get_text_apply(df):
    #df = df.fillna(' ')
    df['noticia'] = df['url'].apply(get_text_apply)
    return df 
#df_3 = DF_get_text_apply(df_2)
#print('ok')
#print(dfn.head())

#4  GET LAT LONG FROM ADDRESS throughout OpenCageGeocode API
'''
def get_gps (adress):
    # 
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(adress)
        return {
            "calle": adress, 
            "latitud" : results[0]['geometry']['lat'], 
            "longitud" : results[0]['geometry']['lng']
        }
    except: 
        return {
            "calle": None, 
            "latitud" : None, 
            "longitud" : None
        }
def returnDic (df):
    direcciones = []
    for calle in df:

        query = get_gps(calle)
        direcciones.append(query)
        if query == {"calle": None, "latitud" : None, "longitud" : None}: 
            print('fallo')
            
    dic = pd.DataFrame(direcciones)        
    return dic
df = returnDic(df.DIRECTION)
'''
# ESTA FUNCIÓN ME DEVUELVE UN DATAFRAME CON: ADDRESS/LAT/LONG , que exporté al csv Coordenadas.csv
    # COMO LA API NO ME HA DEVULETO NADA EN LA ULTIMA EJECUCIÓN DEBIDO AL GRAN NÚMERO DE LLAMADAS QUE HE HECHO

# 5 LEO EL CSV QUE TENÍA GUARDADO CON ELLAS SACADAS:
def ReadDirectionsCoordenadas(file):
    df_entrada = pd.read_csv(file,sep=';', engine='python', encoding='latin1')
    df = df_entrada.copy()
    return df
#df_5 = ReadDirectionsCoordenadas('Coordenadas.csv')
#print(df_5.head())

def CleanDataSetDirections_Coor (df):
    df['VIA_CLASE'] = df.VIA_CLASE.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_PAR'] = df.VIA_PAR.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_NOMBRE'] = df.VIA_NOMBRE.apply(lambda x: x if not pd.isnull(x) else '')
    dfnew = pd.DataFrame(columns=['DIRECTION'])
    dfnew['DIRECTION'] = df['VIA_CLASE'].astype(str) + ' ' + df['VIA_PAR'].astype(str) + ' ' + df['VIA_NOMBRE'].astype(str)
    df = dfnew.drop_duplicates()
    return df
#df_5_clean= CleanDataSetDirections_Coor(df_5)
#print(df_5.head())
#direcciones únicas y limpias

# DF WITH DIRECTION LATITUDE LONGITUDE (DLL)
def MergeDF(df1,df2):
    df = df1[['LATITUD','LONGITUD']]
    df =  pd.merge(df,df2, left_index=True, right_index=True)
    return df
#df_5_DLL = MergeDF(df_5,df_5_clean)
#print(df_5_DLL.head())

'''
# Remove the news whose html doesnt match with "madrid", "street", "avenue"
def returnIndexes(df):
    indexes = []
    for noticia in range(len(df['noticia'])):
        print("procesando doc: " + str(noticia))
        try:
        # Guardo el índice de las filas que han hecho match en el array indexes
            if not (("calle" in df['noticia'][noticia]) or ("avenida" in df['html'][noticia]) or ("plaza" in df['noticia'][noticia])) and ("Madrid" in df['noticia'][noticia]):
                indexes.append(i)
        except:
            pass
    return indexes
indexes = (returnIndexes(df))
print(indexes)

def CleanDataFrame(dataframe,list_index):
    for i in list_index:
        dataframe = dataframe.drop([i])
        return dataframe
df = CleanDataFrame(df,indexes)
df.head(6)
'''

def scrapping_API(df_2):
    df_3 = DF_get_text_apply(df_2)
    df_5 = ReadDirectionsCoordenadas('Coordenadas.csv')
    df_5_clean= CleanDataSetDirections_Coor(df_5)
    df_5_DLL = MergeDF(df_5,df_5_clean)
    return df_5_DLL

if __name__ == "__main__":
    pass
    '''
    from cleaning import cleaning
    df_2 = cleaning
    scrapping_API(df_2)'''