import requests
from bs4 import BeautifulSoup
import csv 

# 1. The URL of the website we want to scrape
url = "http://quotes.toscrape.com"

# 2. Ask the website for its data
response= requests.get(url)

# 3. Use BeautifulSoup to turn that data into something Python can search
soup = BeautifulSoup(response.text, 'html.parser')

# 4. Find all the "quote" boxes on the page
quotes = soup.find_all('div', class_='quote')

# 5. Loop through each box and pull out the text and the author
with open('my_quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["quote", "Author"]) # These are your column headers

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text

        # This saves it to the file instead of just printing it
        writer.writerow([text, author])
        print(f"Saved quote by {author}")

    print("--- FINISHED! Check your folder for my_quotes.csv ---")