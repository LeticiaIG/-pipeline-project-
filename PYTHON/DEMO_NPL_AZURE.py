import requests
# pprint is used to format the JSON response
from pprint import pprint
import os

# dotenv
from dotenv import load_dotenv
load_dotenv()
AZURE_KEY = os.getenv("AZURE_KEY")

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.1/"

keyphrase_url = text_analytics_base_url + "keyPhrases"

documents = {"documents" : [
  {"id": "1", "language": "en", "text": "También puedes escribir a: delitosdeodio@madrid.es o acercarte a la calle  Sacramento,2 de Madrid. Al comprobar que se aproximaba la fecha de la prescripción del delito, el juzgado número 2 de Gavà (Barcelona) optó por reabrir el caso en coordinación con la Jefatura Superior de Policía de Cataluña. “Reiniciamos los trámites desde el principio y llegamos a determinar por las redes sociales que el principal sospechoso seguía viviendo en Nueva York”, cuenta uno de los investigadores que reactivó el caso. La reinstrucción del caso coincidió con la detención de R. A. B. en Estados Unidos por falsear su documentación de inmigrante. "},
  {"id": "2", "language": "en", "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},  
  {"id": "3", "language": "es", "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},  
  {"id": "4", "language": "es", "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."}
]}

headers   = {"Ocp-Apim-Subscription-Key": AZURE_KEY}
response  = requests.post(keyphrase_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)