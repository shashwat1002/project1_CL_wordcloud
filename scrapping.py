import requests
from bs4 import BeautifulSoup


def scrap_english_page(url, corpus_file, url_file):
    # assuming that both the files are in append mode
    response = requests.get(url)
    soup_for_land_page = BeautifulSoup(response.content, 'html.parser')
    all_paragraphs = soup_for_land_page.find_all('p')

    for para in all_paragraphs:
        for content in para.contents:
            # each content has a string object
            # check for type
            # if url type, append url to appropriate file
            # take text and append appropriately
            string = content.string
            if string is not None:
                corpus_file.write(string)
            if content.name == 'a':
                # is a url
                url_string = content['href']
                url_file.write(url_string)
                url_file.write("\n")

