
from reportlab import *
from pipeline import*
'''
def main():
    df_2 = cleaning() #recibe y limpia los csvs- to dataframe
    df_5_DLL = scrapping_API (df_2) # obtiene noticias basadas en búsqueda a través de webscrapping y latlong de API OpenCageGeocode
    df_7 = DF_getTypeOfCrime(df_3)
    df_8 = analysis (df_5_DLL )
    CreateCanvas()
'''

if __name__ == "__main__":
    exe()
    CreateCanvas()
