import os
import scrapping

try:
    os.mkdir("data")
except FileExistsError:
    # do nothing
    pass

DATA_FILE_NAMES = ["english_corpus.txt", "english_corpus_cleaned.txt", "url_file_english.txt"]
ENGLISH_URL_SEED = "https://en.wikipedia.org/wiki/The_Godfather"

current_directory = os.getcwd()
# get the current working directory
data_dir = os.path.join(current_directory, "data")
# data directory


def create_relevant_data_files():
    # the program will create a file for each stage

    for file_name in DATA_FILE_NAMES:
        file_path = os.path.join(data_dir, file_name)
        try:
            os.mknod(file_path)
        except FileExistsError:
            pass


create_relevant_data_files()

english_corpus_path = os.path.join(data_dir, DATA_FILE_NAMES[0])
english_corpus_file = open(english_corpus_path, "a")
english_url_file_path = os.path.join(data_dir, DATA_FILE_NAMES[2])
english_url_file = open(english_url_file_path, 'a')

scrapping.scrap_english_page(ENGLISH_URL_SEED, english_corpus_file, english_url_file)



