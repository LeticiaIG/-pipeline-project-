# Imports the Google Cloud client library
#from IPython import utils  
#from IPython.core.display import HTML
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
import requests
import os
import json
 # python module containing the definition API_KEY = "your_own_api_key"
#Google Cloud Platform user account to use for invocation. 
#Overrides the default core/account property value for this command invocation.

# dotenv
from dotenv import load_dotenv
load_dotenv()
NLP_API_KEY = os.getenv("NLP_API_KEY")


def Entities_NPL(articulo):
    print(articulo)  #news' body (type:text)

    try:
        articulo = "También puedes escribir a: delitosdeodio@madrid.es o acercarte a la calle  Sacramento,2 de Madrid. Al comprobar que se aproximaba la fecha de la prescripción del delito, el juzgado número 2 de Gavà (Barcelona) optó por reabrir el caso en coordinación con la Jefatura Superior de Policía de Cataluña. “Reiniciamos los trámites desde el principio y llegamos a determinar por las redes sociales que el principal sospechoso seguía viviendo en Nueva York”, cuenta uno de los investigadores que reactivó el caso. La reinstrucción del caso coincidió con la detención de R. A. B. en Estados Unidos por falsear su documentación de inmigrante. "
        doc = {"type": "PLAIN_TEXT", "content": articulo}

            #BASE URL
        base = "https://language.googleapis.com"
        
            #PREPARING REQUEST MESSAGE
        request_data = {"document": doc, "encodingType": "UTF8"}
        print('requesting data..')
        entities_endpoint = "/v1/documents:analyzeEntities"
        entities_url = base + entities_endpoint + "?key=" + NLP_API_KEY

            #API_REQUEST
        res= requests.post(entities_url, data=json.dumps(request_data))
        #res_text = json.loads(res.text)

        print(res)
        data = res.json()
        print(data)

            # Export to .json   #trial for one example response:
        #with open('npl_demo.json', 'w') as outfile:
        #   json.dump(data, outfile)

        # retrieving JSON file with all the analysis:
        return data 
    except:
        return None

#tengo que hacer una función INTERMEDIA que me devuelva las direcciones (ADDRESS)
#si no pudeira hacerlo, que me devuelva las "type": "LOCATION"
# luego esto, lo aplico sobre las filas de la columna artículo del dataFrame

def Entities_NPL_apply(df):
    df['found_address'] = df['articulo'].apply(Entities_NPL)
    return df


'''
# FILTRAR POR:
            # SI NO ADDRESS:    "type": "LOCATION"

            "name": "calle  Sacramento,2",
            "type": "ADDRESS",
            "metadata": {
                "locality": "Madrid",
                "street_name": "Calle del Sacramento",
                "broad_region": "Comunidad de Madrid",
                "narrow_region": "Madrid",
                "street_number": "2",
                "country": "ES"
'''





    # syntax
#res_syntax = requests.post(entities_url, data=json.dumps(request_data))
#analysis_results = json.loadsres_syntax.text)
#analysis_endpoint = "/v1/documents:analyzeSyntax"
#analysis_url = base + analysis_endpoint + "?key=" + NLP_API_KEY













