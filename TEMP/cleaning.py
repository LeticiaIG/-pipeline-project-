import pandas as pd

#1  READ AND CLEAN DIRECTORIO.CSV
def ReadDirections(file):
    df_entrada = pd.read_csv(file,sep=';', engine='python', encoding='latin1')
    df = df_entrada.copy()
    return df
#df = ReadDirections('Directorio.csv')
#print('ok')

def CleanDataSetDirections (df):
    df['VIA_CLASE'] = df.VIA_CLASE.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_PAR'] = df.VIA_PAR.apply(lambda x: x if not pd.isnull(x) else '')
    df['VIA_NOMBRE'] = df.VIA_NOMBRE.apply(lambda x: x if not pd.isnull(x) else '')
    dfnew = pd.DataFrame(columns=['DIRECTION'])
    dfnew['DIRECTION'] = df['VIA_CLASE'].astype(str) + ' ' + df['VIA_PAR'].astype(str) + ' ' + df['VIA_NOMBRE'].astype(str)
    df = dfnew.drop_duplicates()
    return df
#df_1 = CleanDataSetDirections(df)
#print('ok')

#2  'CRIME NEWS' DATAFRAME FROM WEB SCRAPPING > CLEAN DATAFRAME

def getDf_fromCSV(file):
    df_copy = pd.read_csv(file, names = ['url','title','html','date'])
    df = df_copy.copy()
    df = df.drop(df.index[0], axis=0) #remove first (descriptions row)
    df = df.applymap(lambda x: x.lstrip())  #everyelement in each Series
    
    df[['day','month','year']] = df.date.str.split(' ', expand=True) #splitting day column into 'day','month','year
    #df[['day','month','year']] = df.date.apply(lambda x: pd.Series(str(x).split("_"))) _ otra forma de hacer lo anterior
    
    df['year'] = df["year"].replace('[a-zA-Z]','',regex =True)
    df['year'] = df["year"].replace('','2019',regex =True)
    
    df['month'] = df["month"].replace('[0-9]','',regex =True)
    
    df['month'] = df['month'].apply(lambda x: x.lower())
    df['month'] = df["month"].replace('ene.','01',regex =True)
    df['month'] = df["month"].replace('feb.','02',regex =True)
    df['month'] = df["month"].replace('mar.','03',regex =True)
    df['month'] = df["month"].replace('abr.','04',regex =True)
    df['month'] = df["month"].replace('abr.','04',regex =True)
    df['month'] = df["month"].replace('may.','05',regex =True)
    df['month'] = df["month"].replace('jun.','05',regex =True)
    df['month'] = df["month"].replace('jul.','06',regex =True)
    df['month'] = df["month"].replace('aug.','08',regex =True)
    df['month'] = df["month"].replace('sep.','09',regex =True)
    df['month'] = df["month"].replace('oct.','10',regex =True)
    df['month'] = df["month"].replace('nov.','11',regex =True)
    df['month'] = df["month"].replace('dic.','12',regex =True)
    
    df['day'] = df['day'].replace('[a-zA-Z]','',regex =True)
    
    df.drop(['date'], axis=1, inplace=True)
    df.sort_values(by=["year",'month', 'day'])
    df.reset_index()
    return df
#df_2 = getDf_fromCSV('crimen.csv')
#print('ok')

#print(df_2)

def cleaning():
    df = ReadDirections('Directorio.csv')
    df_1 = CleanDataSetDirections(df)
    df_2 = getDf_fromCSV('crimen.csv')
    return df_2

if __name__ == "__main__":
    cleaning()
