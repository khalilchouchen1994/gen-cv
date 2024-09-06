import logging
import requests
import os
import json

import azure.functions as func

# Define subscription key and region
subscription_key = os.getenv("AZURE_SPEECH_API_KEY")
region = os.getenv("AZURE_SPEECH_REGION")

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    # Define token endpoint
    token_endpoint = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/avatar/relay/token/v1"
    print("*************")
    print(token_endpoint)
    print(subscription_key)

    # Make HTTP request with subscription key as header
    response = requests.get(token_endpoint, headers={"Ocp-Apim-Subscription-Key": subscription_key})

    if response.status_code == 200:
        return func.HttpResponse(
            body= json.dumps(response.json()),
            status_code=200,
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(  
            body=json.dumps({"error": f"Request failed with status code {response.status_code}"}),  
            status_code=response.status_code,  
            headers={"Content-Type": "application/json"}  
        )  
