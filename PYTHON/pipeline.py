import pandas as pd
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import numpy as np
import requests
from bs4 import BeautifulSoup as BS
import re
import matplotlib.pyplot as plt
from pandas.plotting import table
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
import requests
import os
import json

# dotenv
from dotenv import load_dotenv
load_dotenv()
NLP_API_KEY = os.getenv("NLP_API_KEY")
KEY = os.getenv("NLP_API_KEY")

#  READ AND CLEAN DIRECTORIO.CSV
def ReadDirections(file):
    df_entrada = pd.read_csv(file,sep=';', engine='python', encoding='latin1')
    df = df_entrada.copy()
    return df
#df = ReadDirections('Directorio.csv')
#print(df)

def CleanDataSetDirections (df):
    df['VIA_CLASE'] = df.VIA_CLASE.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_PAR'] = df.VIA_PAR.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_NOMBRE'] = df.VIA_NOMBRE.apply(lambda x: x if not pd.isnull(x) else '')
    dfnew = pd.DataFrame(columns=['DIRECTION'])
    dfnew['DIRECTION'] = df['VIA_CLASE'].astype(str) + ' ' + df['VIA_PAR'].astype(str) + ' ' + df['VIA_NOMBRE'].astype(str)
    df = dfnew.drop_duplicates()
    return df
#df_1 = CleanDataSetDirections(df)

#  'CRIME NEWS' DATAFRAME FROM WEB SCRAPPING > CLEAN DATAFRAME
def getDf_fromCSV(file):
    df_copy = pd.read_csv(file, names = ['url','title','html','date'])
    df = df_copy.copy()
    df = df.drop(df.index[0], axis=0) #remove first (descriptions row)
    df = df.applymap(lambda x: x.lstrip())  #every element in each Series
    
    df[['day','month','year']] = df.date.str.split(' ', expand=True) #splitting day column into 'day','month','year
    #df[['day','month','year']] = df.date.apply(lambda x: pd.Series(str(x).split("_"))) _ otra forma de hacer lo anterior
    
    df['year'] = df["year"].replace('[a-zA-Z]','',regex =True)
    df['year'] = df["year"].replace('','2019',regex =True)
    df['month'] = df["month"].replace('[0-9]','',regex =True)
    df['month'] = df['month'].apply(lambda x: x.lower())
    
    months = ['ene.','feb.','mar.','abr.','may.','jun.','jul.','aug.','sep.','oct.','nov.','dic.']
    for i, month in enumerate(months,1): 
        df["month"].replace(month, str(i))
    
    df['day'] = df['day'].replace('[a-zA-Z]','',regex =True)
    
    df.drop(['date'], axis=1, inplace=True)
    df.sort_values(by=["year",'month', 'day'])
    df.reset_index()
    return df
#df_2 = getDf_fromCSV('crimen.csv')
#print(df_2)

#  RETRIEVE NEWS FROM URLs 
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
    df = df.fillna(' ')
    df['noticia'] = df['url'].apply(get_text_apply)
    return df 
#df_3 = DF_get_text_apply(df_2)
#print('ok')


#  GET LAT LONG FROM ADDRESS throughout OpenCageGeocode API/Google Geocoding
def get_gps (adress):
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
#df = returnDic(df.DIRECTION)

# coordenadas.csv includes [address_lat_long] not to call the API again

# Reading that csv
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
#direcciones únicas y limpias

# DF WITH DIRECTION LATITUDE LONGITUDE (DLL)
def MergeDF(df1,df2):
    df = df1[['LATITUD','LONGITUD']]
    df =  pd.merge(df,df2, left_index=True, right_index=True)
    return df
#df_5_DLL = MergeDF(df_5,df_5_clean)
#print(df_5_DLL.head())


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

#indexes = (returnIndexes(df))
#print(indexes)

def CleanDataFrame(dataframe,list_index):
    for i in list_index:
        dataframe = dataframe.drop([i])
        return dataframe

#df = CleanDataFrame(df,indexes)
#df.head(6)


#  Search for each of the streets in the news paragraphs:
    #df_5_clean (direcciones únicas y limpias)

# Get TYPE of CRIME
def getTypeOfCrime(noticia):
    crimes = ["agresion","pelea", "peleas", "ataque",
              "sexual", "violacion","crimen","matar","asesinato","detenido"]
    try: 
        noticia = noticia.lower()
        for crime in crimes: 
            if crime in noticia: 
                return crime
        else: 
            return ''
    except: 
        return ''

def DF_getTypeOfCrime(df):
    df['Type_crime'] = df['noticia'].apply(getTypeOfCrime)
    return df
# df_7 = DF_getTypeOfCrime(df_3)


# plotting dataframes > png
def PlotDFrames(df):
    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis

    table(ax, df[10:20])  # AJUSTAR EL DATAFRAME !!!

    plt.savefig('LAT,LONG,DIRECTION.png')

def exe():
    df = ReadDirections('../DATA/Directorio.csv')    # recibe y limpia los csvs- to dataframe
    df_1 = CleanDataSetDirections(df)  
    print(df_1)      #  get search-based news through opencracking API and webcrapping API latlong
    df_2 = getDf_fromCSV('../DATA/crimen.csv')       
    df_3 = DF_get_text_apply(df_2)
    df_5 = ReadDirectionsCoordenadas('../OUTPUT/Coordenadas.csv')
    df_5_clean= CleanDataSetDirections_Coor(df_5)
    df_5_DLL = MergeDF(df_5,df_5_clean)
    #df_6 : calles/noticia
    df_7 = DF_getTypeOfCrime(df_3)

if __name__ == "__main__":
    exe()
    #PlotDFrames(df_2)
