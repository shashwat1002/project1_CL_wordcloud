import os
import scrapping
import nltk.tokenize

try:
    os.mkdir("data")
except FileExistsError:
    # do nothing
    pass

DATA_FILE_NAMES = ["english_corpus.txt", "english_corpus_cleaned.txt", "url_file_english.txt", "visited_urls_english.txt"]
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



# scrapping.scrap_english_page(ENGLISH_URL_SEED, english_corpus_file, english_url_file)


def tokenize_sentence_and_words(text, language):
    word_tokens = []
    sentence_tokens = []
    if language == "English":
        word_tokens = nltk.tokenize.word_tokenize(text)
        sentence_tokens = nltk.tokenize.sent_tokenize(text)

    return word_tokens, sentence_tokens

def read_urls_files_to_memory(url_file_path, visited_url_file_path):
    url_file = open(url_file_path, "r")
    url_list = []
    visited_urls = []

    for url in url_file:
        url_list.append(url.rstrip("\n"))

    url_file.close()

    visited_url_file = open(visited_url_file_path, "rb")
    for url in visited_url_file:

        visited_urls.append(url.rstrip("\n"))

    visited_url_file.close()

    return url_list, visited_urls

def crawl_begin(sentence_limit, corpus_file_path, url_file_path, visited_urls_file_path, language):

    # takes everything from the data files
    grand_url_list, visited_urls_list = read_urls_files_to_memory(url_file_path, visited_urls_file_path)

    corpus_file = open(corpus_file_path, "r")
    grand_corpus_text = corpus_file.read()
    corpus_file.close()

    corpus_file = open(corpus_file_path, "a")

    url_file = open(url_file_path, "a")
    visited_urls_file = open(visited_urls_file_path, "a")


    visited_urls = set()
    visited_urls.update(visited_urls_list)
    total_sentences = 0
    all_sentence_list = nltk.tokenize.sent_tokenize(grand_corpus_text)
    all_words_list = nltk.tokenize.word_tokenize(grand_corpus_text)
    for url in grand_url_list:
        if url in visited_urls:
            continue
        new_text, cur_url_list = scrapping.scrap_english_page(url, corpus_file, url_file)
        current_words_list, current_sentence_list = tokenize_sentence_and_words(new_text, language)
        num_sentences = len(current_sentence_list)
        total_sentences += num_sentences
        grand_corpus_text += new_text
        all_sentence_list += current_sentence_list
        all_words_list += current_words_list

        if total_sentences >= sentence_limit:
            break
        visited_urls.add(url)
        grand_url_list += cur_url_list

    file_index_for_visited_urls = 0
    # index in the data files list
    # all the visited urls will be stored in a relevant file



    while len(visited_urls) > 0:
        url = visited_urls.pop()
        visited_urls_file.write(url)

    visited_urls_file.close()
    corpus_file.close()
    url_file.close()

    return grand_corpus_text, all_sentence_list, all_words_list

def generate_data(seed_url, language):

    visited_url_file_index = 0
    corpus_path_index = 0
    url_file_index = 0
    if language == "English":
        visited_url_file_index = 3
        corpus_path_index = 0
        url_file_index = 2

    corpus_path = os.path.join(data_dir, DATA_FILE_NAMES[corpus_path_index])

    url_file_path = os.path.join(data_dir, DATA_FILE_NAMES[url_file_index])

    visited_url_file_path = os.path.join(data_dir, DATA_FILE_NAMES[visited_url_file_index])

    url_file = open(url_file_path, "a")
    url_file.write(seed_url)
    url_file.write('\n')
    url_file.close()
    # url_file is in append mode, so even if it has some urls, we don't care
    ## in the event that this is starting after some data has already been collected
    # all this will do is repeat seed but we'll have visited it already so that won't be an issue
    # however if the file is empty then this is essential

    corpus, sentences_list, words_list = crawl_begin(10000, corpus_path, url_file_path, visited_url_file_path, language)


    return corpus, sentences_list, words_list

generate_data(ENGLISH_URL_SEED, "English")
