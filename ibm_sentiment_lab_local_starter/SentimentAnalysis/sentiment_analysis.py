# Task 2 starts here.
# You will implement sentiment_analyzer(text_to_analyse) yourself with the tutor.

import requests, json

def sentiment_analyzer(text_to_analyse):
 url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

 headers = {
    "grpc-metadata-mm-model-id":
    "sentiment_aggregated-bert-workflow_lang_multi_stock"
 }
 myobj = {
    "raw_document": {
      "text": text_to_analyse
    }
 }

 response = requests.post(url, headers = headers, json = myobj)

 if response.status_code == 500:
  return {
    "label": None,
    "score": None
   }
 
 formatted_response = json.loads(response.text) 
 label = formatted_response["documentSentiment"]["label"]
 score = formatted_response["documentSentiment"]["score"]

 clean_dictionary = {
   "label": label,
    "score": score
 }

 return clean_dictionary

