import urllib.parse
from time import sleep

from bs4 import BeautifulSoup
import requests
import re
from requests import Response

# for debugging
import os

'''
:returns a list of attributes from website that *look* like links
'''
def init_search(terms: str) -> list:
    url = "https://google.com/search?q=" + urllib.parse.quote(terms)
    print(url)
    resp = get_data(url)
    soup = BeautifulSoup(resp, 'html.parser')
    total = []
    for i in soup.findAll('a'):
        print(i.get('href'))
        total.append(i.get('href'))
    return total
    # write_to_file("output_a.txt", str(total))


def get_data(website: str) -> Response:
    r = requests.get(website)
    sleep(0.2)
    print(r.status_code)
    # print(r.headers)
    return r.text


def write_to_file(filename : str, contents):
    file = open(filename, 'w')
    file.write(contents)
    file.close()

def append_to_file(filename: str, contents):
    file = open(filename, 'a')
    file.write(contents)
    file.write("---------------------------------------------------------------------------------------------------")
    file.close()


def decode_urls(contents: list) -> list:
    valid_urls = []
    for i in contents:
        if "http" in i:
            # parse url... remove url encoded stuff before
            new_url = re.findall("http.*", i)
            valid_urls.append(new_url[0])
    return valid_urls


def main():
    total = init_search("50014 healthcare")
    http = decode_urls(total)
    filename = "results.html"
    os.remove(filename)
    for i in http:
        append_to_file(filename, get_data(i))


if __name__== "__main__":
    main()