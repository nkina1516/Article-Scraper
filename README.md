# Article-Scraper

## Overview

Article-Scraper is a Python script that extracts article information from articles and saves 
said information in a folder called "Articles". If this folder doesn't exist it creates it and 
stores five subfolders named "Article 1, Article 2, Article 3, and so on, corresponding to the 
article present in the `url.txt` file." Once the scraping process is complete, the script generates 
text files for each article containing the article title and content, excluding irrelevant information 
such as junk and ads. 

## Installation

To use Article-Scraper, follow these steps:

1. Create a new enviornemt using my `requirements.yaml` file

Be sure that you are in the location where you stored this yaml file! 

If you dont know, enter cd into the terminal. Once you've done this, say you had it stored on your dekstop inside of your 
cs325 folder, you would enter this following information to the terminal:

```
cd
cd desktop/cs325
conda env create -n new_env_name -f requirements.yaml

```
2. Activate the enviornament:

Notice how I am activating the one that got created in step 1

```
conda activate new_env_name 

```

2. Enter the command "conda list" to the terminal:
 
```
conda list

```

3. Check to see that the package newspaper3k is downloaded 

Example of what your output should look like after entering the command from step 2:

```
ncurses                   6.4                  h313beb8_0  
newspaper3k               0.2.8                    pypi_0    pypi
nltk                      3.8.1                    pypi_0    pypi
openssl                   3.0.13               h1a28f6b_0  

```
If it is not downloaded, enter the following to the terminal:

```
pip install newspaper3k

```

### Run the script

4. Navigate to the place (location) where you stored `python3articleScraper.py`
Ex: I stored my `pyhton3articleScraper.py` in my cs325 folder

You'd enter this to the terminal:

```
cd 
cd desktop/cs325

```
5. Enter this command to run the script:

```
/Users/niatekina/miniconda3/envs/project1/bin/python3 "python3articleScraper.py"

```

Example of what your output shoud look like:

```

Scraping article 1/6: 
https://www.cbsnews.com/news/drake-1-15-million-super-bowl-bet-chiefs-to-win/
Article 1 saved to Articles/Article1/file1.txt
Scraping article 2/6: https://www.cbsnews.com/news/do-super-bowl-halftime-performers-get-paid/
Article 2 saved to Articles/Article2/file2.txt
Scraping article 3/6: https://www.cbsnews.com/news/who-is-grammys-host-2024-trevor-noah/
Article 3 saved to Articles/Article3/file3.txt

```

