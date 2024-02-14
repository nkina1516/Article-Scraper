# Article-Scraper

## Overview

Article-Scraper is a Python script that extracts article information from articles and saves 
said info in a folder that you have called "Articles", otherwise it creates a folder for you 
and creates and also stores five folders inside this folder and names them as follows: "Article 1, 
Article 2, etc." which corresponds to the articles present in the urls.txt file. Once this  
happens, the scraper creates a text file for the article and stores the article title, along 
with its content, exluding junk and ads. 

## Installation

To use Article-Scraper, follow these steps:

1. Create a new enviornemt using my requirements.yaml file

Be sure that you are in the location where you stored this file! If you dont know, enter cd to 
the terminal. Once you've done this, say you had it stored on your dekstop inside of your 
cs325 folder, you would enter this follwoing information to the terminal:

cd
cd desktop/cs325
conda env create -n new_env_name -f requirements.yaml

2. Write the command "conda list" into the terminal 
conda list 

3. Check to see that the package newspaper3k is downloaded 

Example of what your output should look like after entering the command into the terminal:
ncurses                   6.4                  h313beb8_0  
newspaper3k               0.2.8                    pypi_0    pypi
nltk                      3.8.1                    pypi_0    pypi
openssl                   3.0.13               h1a28f6b_0  

4. Navigate to the place (location) where you stored the python3articleScraper
Ex: I stored my pyhton3articleScraper in my cs325 folder
Heres what you do:
1. cd 
2. cd desktop/cs325

5. Enter this command to run the script:
- /Users/niatekina/miniconda3/envs/project1/bin/python3 "python3articleScraper.py"

Example of what your output shoud look like:

Scraping article 1/6: 
https://www.cbsnews.com/news/drake-1-15-million-super-bowl-bet-chiefs-to-win/
Article 1 saved to Articles/Article1/file1.txt
Scraping article 2/6: https://www.cbsnews.com/news/do-super-bowl-halftime-performers-get-paid/
Article 2 saved to Articles/Article2/file2.txt
Scraping article 3/6: https://www.cbsnews.com/news/who-is-grammys-host-2024-trevor-noah/
Article 3 saved to Articles/Article3/file3.txt
etc...
