import pandas as pd
from pprint import pprint
import numpy as np
import requests
from bs4 import BeautifulSoup as BS
import re
import matplotlib.pyplot as plt
from pandas.plotting import table

#6  Búsqueda de cada una de las calles en los párrafos de las noticias:
    #df_5_clean (direcciones únicas y limpias)


#7 Get TYPE of CRIME
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


#8 draw dataframe in the pipeline 
def PlotDFrames(df):
    print(type(df))
    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    table(ax, df.head(10)) 
    plt.savefig('LAT,LONG,DIRECTION.png')

def analysis(df):
    return PlotDFrames(df)
def df_analysis(df_3):
    df_7 = DF_getTypeOfCrime(df_3)
    return df_7

if __name__ == "__main__":
    from cleaning import cleaning
    df_2 = cleaning
    from scrapping_API import scrapping_API
    scrapping_API(df_2)
    df_5_DLL = scrapping_API(df_2)
    analysis(df_5_DLL)
    df_7 = DF_getTypeOfCrime(df_3)

