# project1_CL_wordcloud
Software to build a wordcloud in English and/or hindi 



## Installation

It is recommended that you use a virtual environment to set up the project.

It can be set up  like so:

`python3 -m venv env`

It recommended that the name be `env` because an `env` folder has been added to the gitignore

To activate the virtual environement:

`source env/bin/activate`

now you can `pip install -r requirements.txt`

__Warning: the virtual environment may occupy something to the tune of 2 GB after this__

Note:

The project uses `nltk` and `stanza` both of which download machine translation models in your home directory appropriately. 

The prompt, when you run the program, will let you know where they are being installed.



## Running and usage

Just run the `main.py` and pay attention to the prompts:

For each language you'll be asked to either provide a corpus or have the software get corpus.

__To provide corpus__:

just write the name of the corpus file when prompted (make sure the file is in the current directory)

__To have the program generate corpus:__

- the program has code to generate a corpus from wikipedia.
- It starts with a seed url and scraps the page and collectes urls on that page and continues to do so in a breadth first fashion.
- The scrapping will work reasonably well for any wikipedia article
- The seed urls for hindi and english are decided through global properties found in `config.py`. `ENGLISH_URL_SEED` and `HINDI_URL_SEED` respectively.
- In this mode the program will make a `data` folder and put the corpus and discovered urls in different files under that directory.







## The code

### The basic Structure

The code is divided into three modules and a confid modules:

- `main.py` is the file that has to be run for the software. It asks for input from the user as to whether data must be collected or will be provided or not. All the subroutines on the data (like the different tokenization programs and lemmatizer programs etc.) are called inside the `main.py` itself
- `scrapping.py` has all the suboutines required for scrapping data off wikipedia (hindi or english). If the user wants the software to collect data as well then the subroutines in `scrapping.py` are called.
- `plotting.py` has suboutines required to make graphs 
- `config.py` has useful global variables



#### config.py

The `config.py` has global variables and settings that can be tweaked before running the program

#### scrapping.py

The scrapping algorithm works on a simple principle. 

It starts with a seed url, pulls the content off that page and gathers the urls found on that page.

It then proceeds to visit the urls collected and does the same thing in a breadth first fashion

This is done till the corpus has rough 10k+ sentences.



__Note: When the software's data scrapper is used, it will make a `data` directory and write everything to files there.__



#### plotting.py

Has a method that takes a `Counter` object and makes a frequency plot



#### main.py

this is the main file of the program. This is the program driver and calls the methods in the other files appropriately. 

It asks for input from the user as to whether a corpus has to be generated or will it be provided and then runs analysis on the corpus. 

for both the languages seperately. 

note: for now there is no way to ask the program to do it's work for only one of the languages.



