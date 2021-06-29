import requests
from bs4 import BeautifulSoup
import urllib.parse


def scrap_english_page(url, corpus_file, url_file):
    # assuming that both the files are in append mode
    response = requests.get(url)
    soup_for_land_page = BeautifulSoup(response.content, 'html.parser')
    all_paragraphs = soup_for_land_page.find_all('p')
    parsed_url = urllib.parse.urlparse(url)
    output_text = ""
    url_list = [] # to store the list of urls discovered on this page
    for para in all_paragraphs:
        for content in para.contents:
            # each content has a string object
            # check for type
            # if url type, append url to appropriate file
            # take text and append appropriately
            is_reference = False
            if content.name == "sup":
                # references in wikipedia are sup
                try:
                    classes = content['class']
                    is_reference = "reference" in classes
                except KeyError:
                    # in case sup doesn't have a class, we don't care
                    pass
            string = content.string
            if string is not None and not is_reference:
                # if it's a reference then we don't want to write the text
                output_text += string
                corpus_file.write(string)
            if content.name == 'a':
                # has a url
                # note that this includes the references urls
                try:
                    url_string = content['href']
                except KeyError:
                    # BECAUSE FOR SOME FUCKED UP REASON THERE IS AN A TAG WITHOUT URL
                    continue

                current_url_parsed = urllib.parse.urlparse(url_string)
                if current_url_parsed.netloc == '':
                    # if netloc is empty then that means the url is relative
                    # thus we need to make it an absolute url
                    url_string = "{}://{}/{}".format(parsed_url.scheme, parsed_url.netloc, url_string)
                    # basically we're adding the relative part after the base domain
                url_list.append(url_string)
                url_file.write(url_string)
                url_file.write("\n")
    return output_text, url_list
