import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "https://example.com"

# Send a request to the URL and get its HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links in the webpage
links = soup.find_all('a')

# Print out each link
for link in links:
    print(link.get('href'))
