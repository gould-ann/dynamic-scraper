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
    new_json = json.dumps(r.json())
    return new_json


# with open('zip.json') as f:
#     data = json.load(f)
#
# f.close()

# foo = get_nearby_zipcodes("50265", "5")
# bar = json.loads(foo)

# zip codes already get sorted, so call can be made per zip code in bar["zip_codes"]
