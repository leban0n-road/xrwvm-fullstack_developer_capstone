# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', "")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',"")

# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    request_url = backend_url + endpoint + "?" + params
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network exception occurred")


# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return {"sentiment": "error"}


# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        return {"status": "error"}
