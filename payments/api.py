import requests
from django.conf import settings
import base64

def get_access_tokens():

    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET

    credentials = f"{consumer_key} : {consumer_secret}"

    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        'Authorization': f"Bearer {encoded_credentials}"
    }

    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, headers=headers)
    return response.json().get("access_token")




