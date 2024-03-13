#module2 goes into data folder like this: data/raw/publishdate.txt
#collects the publish date, and then calls the process data function
#which will map the process date to the title of the article
#it then creates a outputfile and stores it in the processed folder

import os

class PrintDate:
    def print_date(self, article_title, publish_date):
        raise NotImplementedError("Subclasses must implement print_date")

class ArticleDate(PrintDate):
    def print_date(self, article_title, publish_date):
        print(f"Title: {article_title}\nPublish Date: {publish_date}\n")
        write_to_processed(article_title, publish_date)

def process_data():
    publish_dates = read_publish_dates()
    if not publish_dates:
        print("No publish dates found.")
        return

    articles = [
        "Drake's $1.15 million Super Bowl bet on Chiefs to win",
        "Do Super Bowl halftime performers get paid?",
        "Who is the Grammys host for 2024? Trevor Noah to emcee",
        "2024 Sundance Film Festival: More highlights",
        "Netflix and WWE announce partnership for live sports streaming"
    ]
    if len(articles) != len(publish_dates):
        print("Mismatch between number of articles and publish dates.")
        return

    article_date_printer = ArticleDate()

    for article, publish_date in zip(articles, publish_dates):
        article_date_printer.print_date(article, publish_date)

def read_publish_dates():
    file_path = os.path.join("data", "raw", "publishdate.txt")
    try:
        with open(file_path, "r") as file:
            publish_dates = [line.strip() for line in file if line.strip()]
        return publish_dates
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def write_to_processed(article_title, publish_date):
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    file_path = os.path.join(processed_dir, "mod2_output.txt")
    with open(file_path, "a") as file:
        file.write(f"Title: {article_title}\nPublish Date: {publish_date}\n\n")

def main():
    process_data()

if __name__ == "__main__":
    main()
