#module1 goes into data folder like this: data/raw/authornames.txt
#collects the authors names and their urls, and then calls the process data function
#which will map the author name to the name defined in the class
#it then creates a outputfile and stores it in the processed folder

# I implemented LSP because this allows for the author to have its own class definition 
# which is important so that a author doesn't get mapped to the wrong article 

import os
import newspaper

class PrintAuthor:
    def printauthor(self, article_title, article_content):
        raise NotImplementedError("Subclasses must implement printauthor")

class AlizaChasan(PrintAuthor):
    def printauthor(self, article_title, article_content):
        print("Aliza Chasan")
        print(f"Title: {article_title}\n\n{article_content}")

class KateGibson(PrintAuthor):
    def printauthor(self, article_title, article_content):
        print("Kate Gibson")
        print(f"Title: {article_title}\n\n{article_content}")

class EmilyMaeCzachor(PrintAuthor):
    def printauthor(self, article_title, article_content):
        print("Emily Mae Czachor")
        print(f"Title: {article_title}\n\n{article_content}")

class DavidMorgan(PrintAuthor):
    def printauthor(self, article_title, article_content):
        print("David Morgan")
        print(f"Title: {article_title}\n\n{article_content}")

class ElizabethNapolitano(PrintAuthor):
    def printauthor(self, article_title, article_content):
        print("Elizabeth Napolitano")
        print(f"Title: {article_title}\n\n{article_content}")

def process_data(author, url):
    author_function = get_author_function(author)
    article_title, article_content = scrape_article(url)
    if article_title and article_content:
        process_article(author_function, article_title, article_content)
        write_to_processed(author_function.__name__, article_title, article_content)

def scrape_article(url):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        return article.title, article.text
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")
        return None, None

def process_article(author_function, article_title, article_content):
    author_instance = author_function()
    author_instance.printauthor(article_title, article_content)

def get_author_function(author):
    author_functions = {
        "Aliza Chasan": AlizaChasan,
        "Kate Gibson": KateGibson,
        "Emily Mae Czachor": EmilyMaeCzachor,
        "David Morgan": DavidMorgan,
        "Elizabeth Napolitano": ElizabethNapolitano
    }
    return author_functions.get(author, None)

def write_to_processed(author_function_name, article_title, article_content):
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    file_path = os.path.join(processed_dir, f"mod1_output_{author_function_name}.txt")
    with open(file_path, "a") as file:
        file.write(f"Title: {article_title}\n\n{article_content}\n\n")

def main():
    author_urls = {
        "Aliza Chasan": "https://www.cbsnews.com/news/drake-1-15-million-super-bowl-bet-chiefs-to-win/",
        "Kate Gibson": "https://www.cbsnews.com/news/do-super-bowl-halftime-performers-get-paid/",
        "Emily Mae Czachor": "https://www.cbsnews.com/news/who-is-grammys-host-2024-trevor-noah/",
        "David Morgan": "https://www.cbsnews.com/news/2024-sundance-film-festival-more-highlights-01-27-2024/",
        "Elizabeth Napolitano": "https://www.cbsnews.com/news/netflix-wwe-raw-partnership-live-sports-streaming/"
    }
    for author, url in author_urls.items():
        process_data(author, url)

if __name__ == "__main__":
    main()
