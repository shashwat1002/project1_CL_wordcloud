import requests
from bs4 import BeautifulSoup

ENGLISH_URL_seed = "https://en.wikipedia.org/wiki/The_Godfather"

def english_scraping_page(url):
    response = request.get(url)
    soup_for_land_page = BeautifulSoup(response.content, 'html.parser')
    all_paragraphs = soup_for_land_page.find_all('p')

    for para in all_paragraphs:
        for content in para.contents:
            # each content has a string object
            # check for type
            # if url type append url to appropriate file
            # take text and append appropriately
            
