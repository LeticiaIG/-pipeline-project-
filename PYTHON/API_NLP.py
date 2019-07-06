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

document = "El miedo se apoderó de la calle Fuencarral de Madrid a las ocho"



base = "https://language.googleapis.com"
    
doc = {"type": "PLAIN_TEXT", "content": document}
request_data = {"document": doc, "encodingType": "UTF8"}

analysis_endpoint = "/v1/documents:analyzeSyntax"
analysis_url = base + analysis_endpoint + "?key=" + NLP_API_KEY
    
entities_endpoint = "/v1/documents:analyzeEntities"
entities_url = base + entities_endpoint + "?key=" + NLP_API_KEY


    
    
    # syntax
#res = requests.post(entities_url, data=json.dumps(request_data))
#analysis_results = json.loads(response.text)


res= requests.post(entities_url, data=json.dumps(request_data))
#res = json.loads(response.text)
#entity_matches, _ = generate_entities_structures(entities)
data = res.json()
print(data)







