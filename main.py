from config import *
import os
import scrapping



try:
    os.mkdir("data")
except FileExistsError:
    # do nothing
    pass

current_directory = os.getcwd()
# get the current working directory
data_dir = os.path.join(current_directory, "data")
# data directory

scrapping.create_relevant_data_files(data_dir)
scrapping.generate_data(ENGLISH_URL_SEED, "English", data_dir)
