# Universal Web Scraper

To make this project, we have used Beautiful Soup Library. Beautiful Soup is a Python library that allows you to parse HTML and XML documents. It is commonly used for web scraping tasks because it makes it easy to navigate and search through the structure of a web page.

Here's a step-by-step guide for building a universal web scraper using Beautiful Soup:

- Install Beautiful Soup: 
First, you need to install the Beautiful Soup library. You can do this using pip, the Python package manager. Open your terminal or command prompt and type the following command:

```
pip install beautifulsoup4

```

- Import the necessary libraries:
Once you have installed Beautiful Soup, you need to import it along with other libraries that will be used in your program. 
Here is an example of how to import the necessary libraries:

```
from bs4 import BeautifulSoup
import requests
import csv

```

- Send an HTTP request to the URL of the webpage you want to access:
In order to scrape a webpage, you need to first send an HTTP request to the URL of the webpage. You can do this using the requests library in Python.
Here is an example:

```
url = 'https://www.example.com'
response = requests.get(url)

```

- Parse the HTML content of the page using Beautiful Soup: 
After sending the HTTP request, you will receive a response object. You can then parse the HTML content of the page using Beautiful Soup.
Here is an example:

```
soup = BeautifulSoup(response.content, 'html.parser')

```

- Extract the information you need: 
Once you have parsed the HTML content of the page using Beautiful Soup, you can extract the information you need. This could be anything from the titles of articles on a news website to the prices of products on an e-commerce website. 
Here is an example of how to extract all of the links on a webpage:

```
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

```

- Store the extracted information: Finally, you can store the extracted information in a file or database. 
 Here is an example of how to store the links in a CSV file:

```
with open('links.csv', 'w') as file:
    writer = csv.writer(file)
    for link in links:
        writer.writerow([link])

```

That's it! With these steps, you can build a universal web scraper using Beautiful Soup. Of course, you may need to modify the code depending on the website you are scraping and the information you are trying to extract.










