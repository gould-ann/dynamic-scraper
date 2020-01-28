import urllib.parse
from time import sleep

from bs4 import BeautifulSoup
import requests
import re
from requests import Response

# from zipcodes import get_nearby_zipcodes

# for debugging
import os

'''
:returns a list of attributes from website that *look* like links
'''
def init_search(terms: str) -> list:
    url = "https://google.com/search?q=" + urllib.parse.quote(terms)
    # print(url)
    resp = get_website_data(url)
    soup = BeautifulSoup(resp, 'html.parser')
    total = []
    for i in soup.findAll('a'):
        print(i.get('href'))
        total.append(i.get('href'))
    return total
    # write_to_file("output_a.txt", str(total))


'''
returns contents of html data from website
'''
def get_website_data(website: str) -> Response:
    try:
        r = requests.get(website, timeout=2)
        sleep(0.2)
        r.encoding = 'utf-8'
        print(r.status_code, r.url)
        return r.text
    except:
        # TODO: make this better... maybe mock at some point
        r = requests.get("https://gould-ann.github.io/redirect.html")
        return r.text


def write_to_file(filename : str, contents):
    file = open(filename, 'w')
    file.write(contents)
    file.close()


def append_to_file(filename: str, contents):
    file = open(filename, 'a')
    file.write(contents)
    file.write("\n")
    file.close()

'''
Creates list of urls we can click on to ~learn more~
'''
def decode_urls(contents: list) -> list:
    valid_urls = []
    for i in contents:
        if "http" in i:
            # parse url... remove url encoded stuff before
            new_url = re.findall("http.*", i)
            valid_urls.append(new_url[0])
    return valid_urls

'''
IN PROGRESS:
finds details of addresses
'''
def find_attributes(website_text: str, zipcode: str):
    # split content outside of tags
    split_words = re.findall(">(.+?)<", website_text)
    parsed_adr = []
    # mb make list comprehension
    for i in split_words:
        if zipcode in i:
            zip_index = i.index(zipcode)
            try:
                parsed_adr.append(i[zip_index - 100: zip_index])
            except:
                parsed_adr.append(i[zip_index - 40: zip_index])
    return parsed_adr


def main():
    # search and get links
    zipcode = "50265"
    total = init_search(zipcode + " doctors")
    print(total)
    # find good links
    http = decode_urls(total)
    link_text = [get_website_data(i) for i in http]
    # gets text before zipcode (typically adresses)
    link_atr = [find_attributes(i, zipcode) for i in link_text]
    # save to file here
    write_to_file("contents.txt", str(link_atr[0]))
    # TODO: for some reason everything is duplicated here
    for i in link_atr[1:]:
        append_to_file("contents.txt", str(i))






if __name__== "__main__":
    main()