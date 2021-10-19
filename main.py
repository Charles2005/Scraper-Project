from bs4 import BeautifulSoup
import requests
import os
import functions


"""
Functions: 
- main function 
    - make request
    - Use beautifulSoup 
    - Store Cleaned data 
    - Read the data 
    - Remove the data 

"""


def main(url, dir):
    functions.create_directory(dir)
    result = requests.get(url)
    result_text = result.text
    soup = BeautifulSoup(result_text, "html.parser")
    print(soup.find_all("h1", {"class": 'entry-header'}))