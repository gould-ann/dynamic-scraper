import urllib.parse
from time import sleep

from bs4 import BeautifulSoup
import requests


def search_save(terms: str):
    url = "https://google.com/search?q=" + urllib.parse.quote(terms)
    print(url)
    r = requests.get(url)
    sleep(1)
    print(r.status_code)
    print(r.headers)
    write_to_file("output.html", r.text)


def write_to_file(filename : str, contents: str):
    file = open(filename, 'w')
    file.write(contents)
    file.close()

def begin_parse():
    pass
    # soup = BeautifulSoup(html_doc, '')
    # foo = soup.findAll('a')
    # print(foo)

search_save("50014 healthcare")