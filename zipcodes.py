import requests
import json

'''
FOR GETTING API KEY FROM ENVIRONMENT VARIABLES
USES API FROM https://www.zipcodeapi.com/API
'''
import os
from dotenv import load_dotenv
load_dotenv()
zipcode_auth_key = os.getenv("ZIPCODE_AUTH_KEY")


def get_nearby_zipcodes(zipcode: str, distance: str) -> json:
    r = requests.get(" https://www.zipcodeapi.com/rest/" + zipcode_auth_key +  "/radius.json/" + zipcode + "/" + distance
                 + " /mi ")
    return r.json()
    # print(r.json())

print(get_nearby_zipcodes("50014", "10"))