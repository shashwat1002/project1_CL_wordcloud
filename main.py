from config import *
import os
import scrapping
import nltk
from collections import Counter

current_directory = os.getcwd()
corpus_english_path = ""

print("Will you send corpus input for English or should I scrape data? Y/n")
custom_input = input()
corpus_given = False

if custom_input == "Y":
    corpus_given = True

if corpus_given:
    print("Please enter filename to English corpus")
    file_name = input()
    corpus_english_path = os.path.join(current_directory, file_name)
else:
    #scrape data
    try:
        os.mkdir("data")
    except FileExistsError:
        # do nothing
        pass


    # get the current working directory
    data_dir = os.path.join(current_directory, "data")
    # data directory

    scrapping.create_relevant_data_files(data_dir)
    scrapping.generate_data(ENGLISH_URL_SEED, "English", data_dir)
    corpus_english_path = os.path.join(current_directory, DATA_FILE_NAMES[0])

corpus_english = open(corpus_english_path, "r")

corpus_text_english = corpus_english.read()


word_list_english = nltk.tokenize.word_tokenize(corpus_text_english)
english_stopwords = []
try:
    english_stopwords = nltk.corpus.stopwords.words("english")
except LookupError:
    nltk.download('stopwords')
    english_stopwords = nltk.corpus.stopword.words("english")


word_list_without_stopwords_english = []

for word in word_list_english:
    if word.lower() not in english_stopwords:
        word_list_without_stopwords_english.append(word.lower())

nltk.download('averaged_perceptron_tagger')
tagged_corpus_english = nltk.pos_tag(word_list_english)
# pos tagger called on the list with stop ords

# now stopwords will be removed
clean_tagged_corpus_english = []

for tag_pair in tagged_corpus_english:
    if tag_pair[0].lower() not in english_stopwords:
        clean_tagged_corpus_english.append(tag_pair)

#tagged_corpus_english = clean_tagged_corpus_english
# print(tagged_corpus_english)

counts_of_words = Counter(word_list_without_stopwords_english)
# the list has all words in their lowercase form

# print(counts_of_words)

