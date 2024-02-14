import os
import newspaper

# Function to scrape article content and title
def scrape_article(url):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        return article.title, article.text
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")
        return None, None

def save_to_file(article_title, article_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Title: {article_title}\n\n")
        file.write(article_content)

def main():
    urls_file = "urls.txt"
    output_folder = "Articles"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(urls_file, 'r') as file:
        urls = file.readlines()

    for idx, url in enumerate(urls):
        url = url.strip()
        if url:
            print(f"Scraping article {idx + 1}/{len(urls)}: {url}")
            article_title, article_content = scrape_article(url)
            if article_title and article_content:
                t_folder = os.path.join(output_folder, f"Article{idx + 1}")
                if not os.path.exists(t_folder):
                    os.makedirs(t_folder)
                filename = os.path.join(t_folder, f"file{idx + 1}.txt")
                save_to_file(article_title, article_content, filename)
                print(f"Article {idx + 1} saved to {filename}")

if __name__ == "__main__":
    main()
