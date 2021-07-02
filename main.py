from config import *
import os
import scrapping
import nltk
from collections import Counter
import stanza
import plotting
import re
from wordcloud import WordCloud

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
count_all_words = Counter(word_list_english)
plotting.plotter_of_counter("All English Tokens", count_all_words, 15)
english_stopwords = []
try:
    english_stopwords = nltk.corpus.stopwords.words("english")
except LookupError:
    nltk.download('stopwords')
    english_stopwords = nltk.corpus.stopword.words("english")


word_list_without_stopwords_english = []

for word in word_list_english:
    if word.lower() not in english_stopwords and len(word) > 2:
        word_list_without_stopwords_english.append(word.lower())

nltk.download('averaged_perceptron_tagger')
tagged_corpus_english = nltk.pos_tag(word_list_english)
# pos tagger called on the list with stop words

# now stopwords will be removed
clean_tagged_corpus_english = []

for tag_pair in tagged_corpus_english:
    if tag_pair[0].lower() not in english_stopwords and len(tag_pair[0]) > 1:
        clean_tagged_corpus_english.append(tag_pair)

#tagged_corpus_english = clean_tagged_corpus_english
# print(tagged_corpus_english)

# getting list of all pos tags in the corpus
pos_tags = []
for tup in tagged_corpus_english:
    pos_tags.append(tup[1])

count_pos_tags = Counter(pos_tags)
# plot pos tags
plotting.plotter_of_counter("Pos tags plot", count_pos_tags, 15)

counts_of_words = Counter(word_list_without_stopwords_english)
# the list has all words in their lowercase form
plotting.plotter_of_counter("After Removal of stopwords", counts_of_words, 10)
# print(counts_of_words)
cloud_english = WordCloud(max_words=15)
cloud_english.fit_words(counts_of_words)
cloud_english.to_file("english_wordcloud.png")

unique_words = []

for word in counts_of_words:
    unique_words.append(word)

#print(unique_words)

stemmer = nltk.stem.SnowballStemmer('english')
stemmed_words = []

for word in word_list_without_stopwords_english:
    stemmed_words.append(stemmer.stem(word))

# print(stemmed_words)
counts_of_stemmed_words = Counter(stemmed_words)
plotting.plotter_of_counter("Stemmed words", counts_of_stemmed_words, 10)
# print(counts_of_stemmed_words)

nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()

lemmatized_words = []

for word in word_list_without_stopwords_english:
    lemmatized_words.append(lemmatizer.lemmatize(word))

# print(lemmatized_words)

counts_of_lemmatized_words = Counter(lemmatized_words)
plotting.plotter_of_counter("Lemmatized words", counts_of_lemmatized_words, 10)
# HINDI PART BEGINS HERE

print("Will you send corpus input for Hindi? Y/n")
custom_input = input()
corpus_given = False

if custom_input == "Y":
    corpus_given = True

if corpus_given:
    print("Please enter filename to Hindi corpus")
    file_name = input()
    corpus_hindi_path = os.path.join(current_directory, file_name)
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
    scrapping.generate_data(HINDI_URL_SEED, "Hindi", data_dir)
    corpus_hindi_path = os.path.join(data_dir, DATA_FILE_NAMES[4])

corpus_hindi = open(corpus_hindi_path, "r")

corpus_text_hindi = corpus_hindi.read()

# re cleaning of corpus
corpus_text_hindi = re.sub("[A-Z]|[a-z]", "", corpus_text_hindi)

# # inltk setup
# inltk.setup("hi")
#
# hindi_words_list = []
#
# # removing foreign words
# hindi_words_list = inltk.remove_foreign_languages(corpus_text_hindi, "hi")
# # retain all hindi words
# #print(hindi_words_list)
#
# counter_hindi_words = Counter(hindi_words_list)
# plotting.plotter_of_counter("Hindi words", counter_hindi_words, 10)
#
# new_list_hindi_words = []
# # since since the removed words have become <unk>
# # we want to be rid of all <unk>s
#
# for word in hindi_words_list:
#     if word != "<unk>":
#         new_list_hindi_words.append(word)
#
# hindi_words_list = new_list_hindi_words
#
# hindi_words_without_stopwords = []
#
# for word in hindi_words_list:
#     if word.lstrip("▁") not in HINDI_STOP_WORDS and len(word) > 1:
#         hindi_words_without_stopwords.append(word.lstrip("▁"))
#
# # print(hindi_words_without_stopwords)
#
# count_hindi_words_without_stopwords = Counter(hindi_words_without_stopwords)
# plotting.plotter_of_counter("Hindi words without stopwords", count_hindi_words_without_stopwords, 10)

stanza.download('hi')
stanza.download('en')
nlp = stanza.Pipeline(processors = "tokenize,mwt,pos,lemma")
hindi_doc = nlp(corpus_text_hindi)

def get_tokens(doc):
    tokens = []
    for sentence in doc.sentences:
        for word in sentence.words:
            tokens.append(word.text)
    return tokens

list_tokens_hindi = get_tokens(hindi_doc)
token_counter_hindi = Counter(list_tokens_hindi)

plotting.plotter_of_counter("Hindi Tokens", token_counter_hindi, 10)

# gotta clean off stopwords
hindi_tokens_without_stopwords = []

for word in list_tokens_hindi:
    if word.rstrip("।") not in HINDI_STOP_WORDS and len(word) > 2:
        hindi_tokens_without_stopwords.append(word.rstrip("।"))

token_counter_hindi_without_stopwords = Counter(hindi_tokens_without_stopwords)
# print(token_counter_hindi_without_stopwords)
plotting.plotter_of_counter("Hindi tokens without stopwords", token_counter_hindi_without_stopwords, 10)
cloud_hindi = WordCloud(max_words=15, font_path=HINDI_FONT_PATH)
cloud_hindi.fit_words(token_counter_hindi_without_stopwords)
cloud_hindi.to_file("hindi_wordcloud.png")

def extract_pos_stanford_model(doc):
    parsed_text = {'token': [], 'pos_tag': []}
    for sentence in doc.sentences:
        for word in sentence.words:

            parsed_text['token'].append(word.text)
            parsed_text['pos_tag'].append(word.upos)
    return parsed_text

pos_tags_hindi_doc = extract_pos_stanford_model(hindi_doc)
# returns a dictionary
# one attribute has a list of all words
# the other attribute has a list of all corresponding tags
# print(pos_tags_hindi_doc['token'])
counter_pos_hindi = Counter(pos_tags_hindi_doc['pos_tag'])
plotting.plotter_of_counter("POS tags in hindi cor", counter_pos_hindi, 10)

# print(pos_tags_hindi_doc)
def extract_lemmatized_hindi_words(doc):
    lemmatized_list = []
    for sentence in doc.sentences:
        for word in sentence.words:
            lemmatized_list.append(word.lemma)

    return lemmatized_list
lemmatized_hindi_words = extract_lemmatized_hindi_words(hindi_doc)

# print(lemmatized_hindi_words)
lemmatized_hindi_words_count = Counter(lemmatized_hindi_words)
plotting.plotter_of_counter("Lemmatized hindi words", lemmatized_hindi_words_count, 10)

def extract_lemma_ignoring_stopwords(doc):
    return_list = []
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.text.rstrip("।") not in HINDI_STOP_WORDS and len(word.text.rstrip("।")) > 2:
                return_list.append(word.lemma)
    return return_list


lemma_minus_stop_counter = Counter(extract_lemma_ignoring_stopwords(hindi_doc))
plotting.plotter_of_counter("Lemmatization minus stopwords", lemma_minus_stop_counter, 10)
